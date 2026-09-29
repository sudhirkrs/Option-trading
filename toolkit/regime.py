"""Regime read from daily CSVs: India VIX percentile (IVP) and NIFTY trend.

Download (free):
  India VIX history : nseindia.com -> Reports -> Historical VIX   (1 year, CSV)
  NIFTY 50 history  : niftyindices.com -> Historical Data         (CSV)

Usage:
  python3 regime.py --vix-csv vix.csv --nifty-csv nifty.csv

Only a date column and a close column are needed; common NSE header names
("Close", "Close ", "CLOSE", "Close Price") are detected automatically.
"""
import argparse
import pandas as pd


def _close_series(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    date_col = next(c for c in df.columns if c.lower() in ("date", "index date", "timestamp"))
    close_col = next(c for c in df.columns if c.lower().startswith("close"))
    s = pd.Series(pd.to_numeric(df[close_col].astype(str).str.replace(",", ""), errors="coerce").values,
                  index=pd.to_datetime(df[date_col], dayfirst=True, errors="coerce"))
    return s.dropna().sort_index()


def ivp(vix, window=252):
    last = vix.iloc[-window:]
    today = last.iloc[-1]
    return (last.iloc[:-1] < today).mean() * 100, today, last.min(), last.max()


def trend(nifty):
    px = nifty.iloc[-1]
    d20, d50 = nifty.rolling(20).mean(), nifty.rolling(50).mean()
    slope = d20.iloc[-1] - d20.iloc[-6]
    if px > d20.iloc[-1] > d50.iloc[-1] and slope > 0:
        state = "UP"
    elif px < d20.iloc[-1] < d50.iloc[-1] and slope < 0:
        state = "DOWN"
    else:
        state = "RANGE / TRANSITION"
    rv = nifty.pct_change().iloc[-20:].std() * (252 ** 0.5) * 100
    return state, px, d20.iloc[-1], d50.iloc[-1], slope, rv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vix-csv")
    ap.add_argument("--nifty-csv")
    a = ap.parse_args()
    if a.vix_csv:
        p, today, lo, hi = ivp(_close_series(a.vix_csv))
        gate = "NO-TRADE / defined-risk only" if p < 30 else "spreads / condors" if p < 60 else "premium is rich"
        print(f"India VIX {today:.2f}  1y range {lo:.2f}-{hi:.2f}  IVP {p:.0f}  -> {gate}")
    if a.nifty_csv:
        state, px, d20, d50, slope, rv = trend(_close_series(a.nifty_csv))
        print(f"NIFTY {px:,.0f}  20DMA {d20:,.0f}  50DMA {d50:,.0f}  20DMA 5-day slope {slope:+.0f}  "
              f"trend {state}  20-day realised vol {rv:.1f}%")
        if a.vix_csv:
            _, today, _, _ = ivp(_close_series(a.vix_csv))
            print(f"Implied - realised = {today - rv:+.1f} vol pts "
                  f"({'sellers are being paid' if today - rv > 2 else 'thin or no premium for risk'})")


if __name__ == "__main__":
    main()
