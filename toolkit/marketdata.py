"""Public market-data fetchers: Yahoo Finance (spot, VIX, history) and NSE
(live option chain, with the end-of-day F&O bhavcopy as a fallback).

NSE rate-limits and sometimes blocks cloud IPs. Every fetcher returns None on
failure instead of raising, and the caller falls back to the next source.
Don't poll NSE more often than every ~3 minutes.
"""
import io
import math
import time
import zipfile
from datetime import date, datetime, timedelta

import pandas as pd
import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")

# NSE trading holidays on weekdays (verify each year at nseindia.com -> Holidays).
HOLIDAYS = {
    date(2026, 10, 2), date(2026, 10, 20), date(2026, 11, 10),
    date(2026, 11, 24), date(2026, 12, 25),
}


def log(msg):
    print(f"[data] {msg}", flush=True)


def is_trading_day(d):
    return d.weekday() < 5 and d not in HOLIDAYS


def prev_trading_day(d):
    d -= timedelta(days=1)
    while not is_trading_day(d):
        d -= timedelta(days=1)
    return d


def trading_days_between(a, b):
    """Trading days strictly between dates a and b."""
    n, d = 0, a + timedelta(days=1)
    while d < b:
        n += is_trading_day(d)
        d += timedelta(days=1)
    return n


def nifty_weekly_expiries(start, n=6):
    """NIFTY weeklies expire on Tuesday, moved to the previous trading day on a holiday."""
    out, d = [], start
    while len(out) < n:
        if d.weekday() == 1:
            e = d if is_trading_day(d) else prev_trading_day(d)
            if e >= start:
                out.append(e)
        d += timedelta(days=1)
    return out


# ---------------------------------------------------------------- Yahoo

def yahoo_history(symbol, rng="1y"):
    """Daily OHLC DataFrame (index = date) plus meta dict, or (None, None)."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    for host in ("query1", "query2"):
        try:
            r = requests.get(url.replace("query1", host), params={"range": rng, "interval": "1d"},
                             headers={"User-Agent": UA}, timeout=20)
            r.raise_for_status()
            res = r.json()["chart"]["result"][0]
            q = res["indicators"]["quote"][0]
            idx = pd.to_datetime(res["timestamp"], unit="s", utc=True).tz_convert("Asia/Kolkata").date
            df = pd.DataFrame({k: q[k] for k in ("open", "high", "low", "close")}, index=idx).dropna()
            df = df[~df.index.duplicated(keep="last")]
            return df, res["meta"]
        except Exception as e:
            log(f"Yahoo {symbol} via {host} failed: {e}")
    return None, None


# ---------------------------------------------------------------- NSE

class NSE:
    BASE = "https://www.nseindia.com"

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": UA, "Accept": "application/json, text/plain, */*",
                               "Accept-Language": "en-US,en;q=0.9",
                               "Referer": self.BASE + "/option-chain"})
        self.ok = False
        for path in ("/", "/option-chain"):
            try:
                self.s.get(self.BASE + path, timeout=20,
                           headers={"Accept": "text/html,application/xhtml+xml"})
                self.ok = True
            except Exception as e:
                log(f"NSE handshake {path} failed: {e}")
            time.sleep(1)

    def get(self, path, **params):
        for attempt in range(3):
            try:
                r = self.s.get(self.BASE + path, params=params, timeout=20)
                if r.status_code == 200 and r.text.strip() not in ("", "{}"):
                    return r.json()
                log(f"NSE {path} -> HTTP {r.status_code}, {len(r.text)} bytes")
            except Exception as e:
                log(f"NSE {path} failed: {e}")
            time.sleep(2 * (attempt + 1))
        return None

    def expiries(self, symbol="NIFTY"):
        j = self.get("/api/option-chain-contract-info", symbol=symbol)
        if j and j.get("expiryDates"):
            return [datetime.strptime(x, "%d-%b-%Y").date() for x in j["expiryDates"]]
        return None

    def chain(self, expiry, symbol="NIFTY"):
        """Live chain for one expiry -> (DataFrame, underlying) or (None, None)."""
        exp_s = expiry.strftime("%d-%b-%Y")
        j = self.get("/api/option-chain-v3", type="Indices", symbol=symbol, expiry=exp_s)
        if not (j and j.get("records", {}).get("data")):
            j = self.get("/api/option-chain-indices", symbol=symbol)   # legacy endpoint
        if not (j and j.get("records", {}).get("data")):
            return None, None
        rows = []
        for d in j["records"]["data"]:
            e = d.get("expiryDate") or d.get("expiryDates")
            if e and e != exp_s:
                continue
            for opt in ("CE", "PE"):
                leg = d.get(opt)
                if not leg:
                    continue
                rows.append(dict(strike=int(d["strikePrice"]), type=opt,
                                 bid=float(leg.get("bidprice") or leg.get("bidPrice") or 0),
                                 ask=float(leg.get("askPrice") or leg.get("askprice") or 0),
                                 ltp=float(leg.get("lastPrice") or 0),
                                 oi=float(leg.get("openInterest") or 0)))
        return (pd.DataFrame(rows) if rows else None), j["records"].get("underlyingValue")

    def india_vix(self):
        j = self.get("/api/allIndices")
        for d in (j or {}).get("data", []):
            if d.get("index") == "INDIA VIX":
                return float(d["last"])
        return None


def bhavcopy_chain(expiry, symbol="NIFTY", lookback=7):
    """End-of-day NIFTY options from the NSE F&O bhavcopy archive.
    Returns (DataFrame, underlying close, trade date) or (None, None, None)."""
    d = date.today() if is_trading_day(date.today()) else prev_trading_day(date.today())
    for _ in range(lookback):
        url = ("https://nsearchives.nseindia.com/content/fo/"
               f"BhavCopy_NSE_FO_0_0_0_{d:%Y%m%d}_F_0000.csv.zip")
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
            r.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                df = pd.read_csv(z.open(z.namelist()[0]))
            df = df[(df["TckrSymb"] == symbol) & (df["FinInstrmTp"] == "IDO")]
            df = df[pd.to_datetime(df["XpryDt"]).dt.date == expiry]
        except Exception as e:
            log(f"bhavcopy {d} unavailable: {e}")
            d = prev_trading_day(d)
            continue
        if df.empty:
            log(f"bhavcopy {d}: no {symbol} rows for {expiry}")
            d = prev_trading_day(d)
            continue
        out = pd.DataFrame(dict(strike=df["StrkPric"].astype(float).astype(int), type=df["OptnTp"],
                                bid=0.0, ask=0.0, ltp=df["ClsPric"].astype(float),
                                oi=df["OpnIntrst"].astype(float)))
        return out, float(df["UndrlygPric"].iloc[0]), d
    return None, None, None


def is_nan(x):
    return x is None or (isinstance(x, float) and math.isnan(x))
