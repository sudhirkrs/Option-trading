"""Automated daily trade card for defined-risk NIFTY option selling.

Fetches everything itself from public sources:
  spot, India VIX, 1-year history -> Yahoo Finance (^NSEI, ^INDIAVIX)
  option chain                    -> NSE live API, else NSE F&O bhavcopy (EOD),
                                     else Black-Scholes model on VIX
  expiries                        -> NSE, else computed (Tuesday, holiday-adjusted)
  events                          -> events.csv in this folder (edit it)

Then applies the playbook rules (regime gates, event gate, gap filter,
credit/width, cost gate, 2% risk sizing) and prints a TRADE / NO TRADE card
in Markdown.

  python3 auto.py --capital 500000 [--expiry 2026-10-06] [--report-dir ../reports]
"""
import argparse
import csv
import math
import os
import sys
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import pandas as pd

import marketdata as md
from optlib import bs_greeks, expected_move, implied_vol, prob_itm, prob_touch
from planner import Pricer, R, spread, metrics

IST = ZoneInfo("Asia/Kolkata")
LOT = 65
HERE = os.path.dirname(os.path.abspath(__file__))
DISCLAIMER = ("Estimates for analysis. Verify lot size, expiry, margin and charges "
              "against the exchange and your broker before trading. Not investment advice.")


# ------------------------------------------------------------------ inputs

def load_events(path=os.path.join(HERE, "events.csv")):
    ev = []
    if os.path.exists(path):
        with open(path) as f:
            for row in csv.DictReader(f):
                try:
                    ev.append((date.fromisoformat(row["date"].strip()), row["event"].strip()))
                except (KeyError, ValueError):
                    pass
    return ev


def regime(nifty, vix, spot, vix_now, today):
    """IVP, trend, realised vol and VIX direction. Any input may be None."""
    out = dict(ivp=None, trend="UNKNOWN", rv20=None, d20=None, d50=None,
               vix_rising=None, vix_calming=None, gap=None, vix_5d_high=None)
    if vix is not None and len(vix) > 30:
        closes = vix["close"]
        hist = closes[closes.index < today].iloc[-251:]
        out["ivp"] = (hist < vix_now).mean() * 100
        last5 = hist.iloc[-5:]
        out["vix_5d_high"] = last5.max()
        falls = (hist.diff().iloc[-2:] < 0).sum() + (vix_now < hist.iloc[-1])
        out["vix_rising"] = vix_now >= last5.max() or vix_now > hist.iloc[-5] * 1.10
        out["vix_calming"] = vix_now < last5.max() and falls >= 2
    if nifty is not None and len(nifty) > 60:
        c = nifty["close"].copy()
        c = c[c.index < today]
        prev_close = c.iloc[-1]
        c.loc[today] = spot
        d20, d50 = c.rolling(20).mean(), c.rolling(50).mean()
        slope = d20.iloc[-1] - d20.iloc[-6]
        if spot > d20.iloc[-1] > d50.iloc[-1] and slope > 0:
            out["trend"] = "UP"
        elif spot < d20.iloc[-1] < d50.iloc[-1] and slope < 0:
            out["trend"] = "DOWN"
        else:
            out["trend"] = "RANGE"
        out.update(d20=d20.iloc[-1], d50=d50.iloc[-1],
                   rv20=c.pct_change().iloc[-20:].std() * math.sqrt(252) * 100)
        if today in nifty.index:
            out["gap"] = (nifty.loc[today, "open"] / prev_close - 1) * 100
    return out


# ------------------------------------------------------------------ chain

def build_pricer(spot, vix_now, T, chain_df, mode, eod=None):
    """Return (Pricer, atm_iv, quote_meta). eod = (underlying, T_eod) for bhavcopy."""
    chain, iv_map, meta = {}, {}, {}
    if chain_df is not None:
        for r in chain_df.itertuples():
            key = (int(r.strike), r.type)
            meta[key] = dict(bid=r.bid, ask=r.ask, oi=r.oi, ltp=r.ltp)
            if mode == "LIVE" and r.bid > 0 and r.ask >= r.bid:
                chain[key] = (r.bid + r.ask) / 2
            elif mode == "EOD" and r.ltp > 0:
                v = implied_vol(r.ltp, eod[0], key[0], eod[1], R, key[1])
                if not math.isnan(v):
                    iv_map[key] = v
    atm_iv = vix_now / 100
    probe = Pricer(spot, atm_iv, T, chain, iv_map)
    atm = round(spot / 50) * 50
    ivs = [probe.iv(atm, o) for o in ("CE", "PE") if (atm, o) in chain or (atm, o) in iv_map]
    ivs = [v for v in ivs if not math.isnan(v)]
    if ivs:
        atm_iv = sum(ivs) / len(ivs)
    return Pricer(spot, atm_iv, T, chain, iv_map), atm_iv, meta


def leg_row(p, K, opt, tag, meta):
    iv = p.iv(K, opt)
    q = meta.get((K, opt), {})
    bidask = f"{q['bid']:.2f}/{q['ask']:.2f}" if q.get("ask") else "-"
    oi = f"{q['oi']:,.0f}" if q.get("oi") else "-"
    return (f"| {tag} | {K} {opt} | {p.price(K, opt):.2f} | {bidask} | {iv*100:.1f}% | "
            f"{p.delta(K, opt):+.2f} | {(1-prob_itm(p.S, K, p.T, R, iv, opt))*100:.0f}% | "
            f"{prob_touch(p.S, K, p.T, R, iv)*100:.0f}% | {oi} |")


def liquidity_ok(sides, meta, mode):
    if mode != "LIVE":
        return True, "not checked (no live bid/ask)"
    bad = []
    for s in sides:
        for K in (s["short"], s["long"]):
            q = meta.get((K, s["opt"]))
            if not q or q["ask"] <= 0 or q["bid"] <= 0:
                bad.append(f"{K}{s['opt']} no two-sided quote")
                continue
            mid = (q["bid"] + q["ask"]) / 2
            if (q["ask"] - q["bid"]) > max(0.10 * mid, 0.5):
                bad.append(f"{K}{s['opt']} spread {q['ask']-q['bid']:.2f} on mid {mid:.2f}")
    return (not bad), ("OK" if not bad else "; ".join(bad))


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capital", type=float, default=500000)
    ap.add_argument("--risk-pct", type=float, default=2.0)
    ap.add_argument("--expiry", default="", help="YYYY-MM-DD; blank = nearest valid weekly")
    ap.add_argument("--directional-delta", type=float, default=0.28)
    ap.add_argument("--neutral-delta", type=float, default=0.22)
    ap.add_argument("--widths", default="100,150")
    ap.add_argument("--min-credit-ratio", type=float, default=0.25)
    ap.add_argument("--max-gap", type=float, default=0.7, help="skip if gap against the trade > this %%")
    ap.add_argument("--report-dir", default="")
    a = ap.parse_args()

    now = datetime.now(IST)
    today = now.date()
    widths = [int(w) for w in a.widths.split(",")]
    risk = a.risk_pct / 100
    L = []   # markdown lines

    # ---- spot / VIX / history
    nifty, nmeta = md.yahoo_history("%5ENSEI")
    vix, vmeta = md.yahoo_history("%5EINDIAVIX")
    spot = nmeta.get("regularMarketPrice") if nmeta else None
    vix_now = vmeta.get("regularMarketPrice") if vmeta else None
    src_spot = "Yahoo" if spot else None

    nse = md.NSE()
    if not vix_now:
        vix_now = nse.india_vix()
    expiries = nse.expiries()
    src_exp = "NSE" if expiries else "computed (Tuesday, holiday-adjusted)"
    if not expiries:
        expiries = md.nifty_weekly_expiries(today)

    if a.expiry:
        expiry = date.fromisoformat(a.expiry)
    else:
        expiry = next(e for e in sorted(expiries) if md.trading_days_between(today, e) >= 2)

    chain_df, underlying = nse.chain(expiry)
    mode, eod = ("LIVE", None) if chain_df is not None else (None, None)
    chain_note = "NSE live option chain" if mode else ""
    if mode is None:
        chain_df, und, tdate = md.bhavcopy_chain(expiry)
        if chain_df is not None:
            mode = "EOD"
            t_eod = (datetime.combine(expiry, datetime.min.time()) - datetime.combine(tdate, datetime.min.time())).days / 365
            eod = (und, max(t_eod, 1 / 365))
            chain_note = f"NSE bhavcopy of {tdate} (end-of-day IVs, re-priced at today's spot)"
    if mode is None:
        mode, chain_note = "MODEL", "Black-Scholes model on India VIX (no chain reachable)"
    if not spot and underlying:
        spot, src_spot = float(underlying), "NSE"

    L.append(f"# NIFTY trade card: {now:%a %d %b %Y, %H:%M} IST")
    if not md.is_trading_day(today):
        L.append("\n**Market holiday / weekend: no trade today.**")
    if not spot or not vix_now:
        L.append("\n**NO TRADE: could not fetch NIFTY spot or India VIX from any source.**")
        return emit(L, a, now)

    T = (datetime.combine(expiry, datetime.min.time()).replace(hour=15, minute=30, tzinfo=IST) - now).total_seconds() / 86400 / 365
    p, atm_iv, meta = build_pricer(spot, vix_now, T, chain_df, mode, eod)
    em = expected_move(spot, atm_iv, T)
    rg = regime(nifty, vix, spot, vix_now, today)
    exit_day = md.prev_trading_day(expiry)
    events = [(d, e) for d, e in load_events() if today <= d <= expiry]

    # ---- data section
    L.append("\n## Data")
    L.append(f"| Item | Value | Source |\n|---|---|---|")
    L.append(f"| NIFTY spot | {spot:,.2f} | {src_spot} |")
    L.append(f"| India VIX | {vix_now:.2f} | {'Yahoo' if vmeta else 'NSE'} |")
    L.append(f"| Expiry | {expiry:%a %d %b %Y} ({T*365:.1f} calendar days) | {src_exp} |")
    L.append(f"| Option prices | {mode} | {chain_note} |")
    L.append(f"| ATM IV (this expiry) | {atm_iv*100:.1f}% | {'chain' if mode != 'MODEL' else 'VIX proxy'} |")
    L.append(f"| 1-SD expected move | ±{em:,.0f} → {spot-em:,.0f} – {spot+em:,.0f} | |")

    # ---- regime
    L.append("\n## Regime")
    fmt = lambda x, f: "n/a" if x is None else format(x, f)
    L.append(f"* IV percentile (1y): **{fmt(rg['ivp'], '.0f')}**")
    L.append(f"* Trend: **{rg['trend']}**  (20-DMA {fmt(rg['d20'], ',.0f')}, 50-DMA {fmt(rg['d50'], ',.0f')})")
    L.append(f"* 20-day realised vol {fmt(rg['rv20'], '.1f')}% vs implied {atm_iv*100:.1f}%"
             + (f" → premium {atm_iv*100 - rg['rv20']:+.1f} vol pts" if rg['rv20'] else ""))
    L.append(f"* VIX {'RISING' if rg['vix_rising'] else 'calming' if rg['vix_calming'] else 'flat/mixed' if rg['vix_rising'] is not None else 'n/a'}"
             f" (5-day high {fmt(rg['vix_5d_high'], '.2f')})")
    L.append(f"* Today's opening gap: {fmt(rg['gap'], '+.2f')}{'%' if rg['gap'] is not None else ''}")
    L.append(f"* Events up to expiry: {', '.join(f'{d:%d %b} {e}' for d, e in events) or 'none listed'}")

    # ---- decide structure
    reasons, structure = [], None
    if not md.is_trading_day(today):
        reasons.append("market closed today")
    if rg["ivp"] is not None and rg["ivp"] < 30:
        reasons.append(f"IVP {rg['ivp']:.0f} < 30: premium too thin")
    blocking = [(d, e) for d, e in events if d <= exit_day]
    if blocking:
        reasons.append("event before exit: " + ", ".join(f"{d:%d %b} {e}" for d, e in blocking))
    t = rg["trend"]
    if t == "DOWN":
        structure = "BEAR CALL SPREAD"
        if rg["gap"] is not None and rg["gap"] > a.max_gap:
            reasons.append(f"gap up {rg['gap']:+.2f}% against a bear call")
    elif t == "UP":
        structure = "BULL PUT SPREAD"
        if rg["vix_rising"]:
            reasons.append("uptrend but VIX rising: no put selling")
        if rg["gap"] is not None and rg["gap"] < -a.max_gap:
            reasons.append(f"gap down {rg['gap']:+.2f}% against a bull put")
    elif t == "RANGE":
        structure = "IRON CONDOR"
        if not rg["vix_calming"]:
            reasons.append("range-bound but VIX not calming: condor waits")
    else:
        reasons.append("trend unknown (no price history)")

    cands = {
        "BEAR CALL SPREAD": [spread(p, "CE", a.directional_delta, widths)],
        "BULL PUT SPREAD": [spread(p, "PE", a.directional_delta, widths)],
        "IRON CONDOR": [spread(p, "PE", a.neutral_delta, widths), spread(p, "CE", a.neutral_delta, widths)],
    }

    def card(name, sides):
        m = metrics(p, sides, LOT, a.capital, risk)
        out = [f"\n### {name}", "| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |",
               "|---|---|---|---|---|---|---|---|---|"]
        for s in sides:
            out.append(leg_row(p, s["long"], s["opt"], "BUY (hedge, first)", meta))
            out.append(leg_row(p, s["short"], s["opt"], "SELL", meta))
        ratios = [s["ratio"] for s in sides]
        liq_ok, liq = liquidity_ok(sides, meta, mode)
        checks = [
            (min(ratios) >= a.min_credit_ratio,
             "credit/width " + ", ".join(f"{s['opt']} {s['credit']:.1f}/{s['width']} = {s['ratio']:.2f}" for s in sides)
             + f" (need ≥ {a.min_credit_ratio})"),
            (all(abs(p.delta(s["short"], s["opt"])) <= 0.30 for s in sides), "short delta ≤ 0.30"),
            (m["cost_ok"], f"cost ₹{m['cost']:,.0f} = {m['cost']/m['gross']*100:.1f}% of credit (net ≥ 4× cost)"),
            (liq_ok, f"liquidity: {liq}"),
            (m["lots"] >= 1, f"size: {m['lots']} lot(s) within {a.risk_pct:.0f}% risk (₹{a.capital*risk:,.0f})"),
        ]
        out += [f"* {'✅' if ok else '❌'} {txt}" for ok, txt in checks]
        c = m["credit"]
        out.append(f"* Credit {c:.2f} pts = ₹{m['gross']:,.0f}/lot · max loss ₹{m['max_loss']:,.0f}/lot · "
                   f"margin ~₹{m['margin']:,.0f}/lot · net at 50% target ₹{m['net_target']:,.0f}/lot")
        out.append(f"* Exits: **take profit** when spread ≤ {c*0.5:.2f} · **stop** when spread ≥ {c*3:.2f} "
                   f"(loss = 2× credit) · **time exit** {exit_day:%a %d %b} 15:00 IST")
        return out, all(ok for ok, _ in checks), m

    body, passed, m = card(structure, cands[structure]) if structure else ([], False, None)
    if structure and not passed:
        reasons.append(f"{structure} failed a gate (see ❌ below)")

    L.append("\n## Verdict")
    if not reasons:
        L.append(f"**TRADE: {structure}, {m['lots']} lot(s)** "
                 + ("(prices are live)" if mode == "LIVE" else
                    "(**confirm live**: place only if the live credit/width is ≥ "
                    f"{a.min_credit_ratio})"))
        L.append("Order: buy the hedge leg first, then sell the short leg, both as limit orders at mid.")
    else:
        L.append("**NO TRADE today.**")
        L += [f"* {r}" for r in reasons]
    L += body
    L.append("\n<details><summary>Other structures (for reference only)</summary>\n")
    for name, sides in cands.items():
        if name != structure:
            L += card(name, sides)[0]
    L.append("\n</details>")
    L.append(f"\n_{DISCLAIMER}_")
    return emit(L, a, now)


def emit(L, a, now):
    text = "\n".join(L)
    print(text)
    if a.report_dir:
        os.makedirs(a.report_dir, exist_ok=True)
        with open(os.path.join(a.report_dir, f"{now:%Y-%m-%d_%H%M}.md"), "w") as f:
            f.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
