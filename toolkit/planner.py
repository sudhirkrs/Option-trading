"""Defined-risk option-selling planner for NIFTY (or any cash-settled index).

Builds bear call spreads, bull put spreads and iron condors, picks strikes by
delta, and runs the width, cost and 1-SD gates plus position sizing.

Model mode (no chain): premiums come from Black-Scholes on a skewed surface
anchored on India VIX. Use it for planning only, then re-check with real quotes.

Chain mode (--chain file.csv with columns: strike,type,bid,ask[,oi]):
premiums are bid/ask mids from your broker, and IV is re-solved from them.

Example:
  python3 planner.py --spot 22600 --vix 14.5 --entry "2026-09-30 10:00" \
      --expiry 2026-10-06 --capital 500000
"""
import argparse
import csv
import math
from datetime import datetime

from optlib import (bs_greeks, bs_price, expected_move, implied_vol,
                    prob_itm, prob_touch, skewed_iv, payoff_at_expiry)
from costs import round_trip, estimate_margin, leg_cost

R = 0.065          # INR risk-free proxy (T-bill); small effect on weeklies
STEP = 50          # NIFTY strike interval
DISCLAIMER = ("Estimates for analysis. Verify lot size, expiry, margin and charges "
              "against the exchange and your broker before trading. Not investment advice.")


class Pricer:
    def __init__(self, spot, atm_iv, T, chain=None):
        self.S, self.atm, self.T, self.chain = spot, atm_iv, T, chain or {}

    def iv(self, K, opt):
        quote = self.chain.get((K, opt))
        if quote:
            v = implied_vol(quote, self.S, K, self.T, R, opt)
            if not math.isnan(v):
                return v
        return skewed_iv(self.atm, self.S, K)

    def price(self, K, opt):
        quote = self.chain.get((K, opt))
        if quote:
            return quote
        return bs_price(self.S, K, self.T, R, self.iv(K, opt), opt)

    def delta(self, K, opt):
        return bs_greeks(self.S, K, self.T, R, self.iv(K, opt), opt)["delta"]

    def strike_for_delta(self, target, opt):
        """OTM strike whose |delta| is closest to target without exceeding it."""
        atm = round(self.S / STEP) * STEP
        sign = 1 if opt == "CE" else -1
        K = atm
        for _ in range(200):
            if abs(self.delta(K, opt)) <= target:
                return K
            K += sign * STEP
        return K


def load_chain(path):
    chain = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            bid, ask = float(row["bid"]), float(row["ask"])
            if bid > 0 and ask > 0 and ask >= bid:
                chain[(int(float(row["strike"])), row["type"].upper())] = (bid + ask) / 2
    return chain


def spread(p, opt, short_delta, widths):
    """Pick the short strike by delta, then the width with the best credit/width."""
    Ks = p.strike_for_delta(short_delta, opt)
    best = None
    for w in widths:
        Kl = Ks + w if opt == "CE" else Ks - w
        credit = p.price(Ks, opt) - p.price(Kl, opt)
        ratio = credit / w
        cand = dict(opt=opt, short=Ks, long=Kl, width=w, credit=credit, ratio=ratio)
        if best is None or ratio > best["ratio"]:
            best = cand
    return best


def leg_stats(p, K, opt):
    iv = p.iv(K, opt)
    return dict(K=K, opt=opt, iv=iv, prem=p.price(K, opt), delta=p.delta(K, opt),
                p_otm=1 - prob_itm(p.S, K, p.T, R, iv, opt),
                p_touch=prob_touch(p.S, K, p.T, R, iv))


def evaluate(name, p, sides, lot, capital, risk_pct, em):
    legs, credit, width = [], 0.0, 0.0
    for s in sides:
        legs += [(s["opt"], s["short"], -1, p.price(s["short"], s["opt"])),
                 (s["opt"], s["long"], +1, p.price(s["long"], s["opt"]))]
        credit += s["credit"]
        width = max(width, s["width"])
    max_loss_pts = width - credit                      # only one side can lose at expiry
    cost = round_trip(legs, lot, exit_frac=0.5)
    cost_expiry = sum(leg_cost(pr, lot, q, q < 0) for (_, _, q, pr) in legs)
    gross = credit * lot
    max_loss = max_loss_pts * lot + cost_expiry
    margin = estimate_margin(legs, p.S, lot, hedged=True, max_loss=max_loss_pts * lot)
    lots_risk = int((capital * risk_pct) // max_loss) if max_loss > 0 else 0
    lots_margin = int((capital * 0.5) // margin)
    lots = max(0, min(lots_risk, lots_margin))

    out = [f"\n=== {name} ==="]
    out.append(f"{'leg':<12}{'IV%':>6}{'prem':>8}{'delta':>8}{'P(OTM)':>8}{'P(touch)':>9}{'dist':>8}")
    for s in sides:
        for K, tag in ((s["short"], "SELL"), (s["long"], "BUY")):
            st = leg_stats(p, K, s["opt"])
            out.append(f"{tag} {K}{s['opt']:<3}{st['iv']*100:>6.1f}{st['prem']:>8.1f}"
                       f"{st['delta']:>8.2f}{st['p_otm']*100:>7.0f}%{st['p_touch']*100:>8.0f}%"
                       f"{K - p.S:>+8.0f}")
    flags = []
    for s in sides:
        inside = abs(s["short"] - p.S) < em
        flags.append(f"{s['opt']} short {s['short']} is {abs(s['short']-p.S)/em:.2f} SD away"
                     + ("  <-- INSIDE 1 SD" if inside else ""))
        verdict = "GOOD" if s["ratio"] >= 0.33 else "OK" if s["ratio"] >= 0.25 else \
            "WEAK" if s["ratio"] >= 0.20 else "REJECT"
        flags.append(f"{s['opt']} spread {s['width']} wide: credit {s['credit']:.1f} "
                     f"-> credit/width {s['ratio']:.2f} [{verdict}]")
    out += ["  " + f for f in flags]
    net_at_target = gross * 0.5 - cost
    cost_ok = gross - cost >= 4 * cost
    out.append(f"  Gross credit/lot  Rs{gross:,.0f}   round-trip cost (exit at 50%) Rs{cost:,.0f}"
               f" = {cost/gross*100:.1f}% of credit  [{'PASS' if cost_ok else 'FAIL'} 4x cost gate]")
    out.append(f"  Net profit at 50% target/lot  Rs{net_at_target:,.0f}")
    out.append(f"  Max loss/lot  Rs{max_loss:,.0f}   est. margin/lot Rs{margin:,.0f}   "
               f"return on margin at target {net_at_target/margin*100:.1f}%")
    if len(sides) == 1:
        s = sides[0]
        be = s["short"] + s["credit"] if s["opt"] == "CE" else s["short"] - s["credit"]
        out.append(f"  Breakeven at expiry {be:,.0f}")
    else:
        pe = [s for s in sides if s["opt"] == "PE"][0]
        ce = [s for s in sides if s["opt"] == "CE"][0]
        out.append(f"  Breakevens at expiry {pe['short'] - credit:,.0f} / {ce['short'] + credit:,.0f}")
    out.append(f"  Stop (loss = 2x credit) -> exit when position is down Rs{gross*2:,.0f}/lot "
               f"(spread value ~{credit*3:.1f} pts)")
    out.append(f"  Sizing @ capital Rs{capital:,.0f}, {risk_pct*100:.1f}% risk: "
               f"{lots} lot(s)  [risk cap {lots_risk}, margin cap {lots_margin}]  "
               f"worst case Rs{lots*max_loss:,.0f}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spot", type=float, required=True)
    ap.add_argument("--vix", type=float, help="India VIX (used as ATM IV proxy)")
    ap.add_argument("--atm-iv", type=float, help="ATM IV in %% from the chain (overrides VIX)")
    ap.add_argument("--entry", required=True, help='"YYYY-MM-DD HH:MM" IST')
    ap.add_argument("--expiry", required=True, help="YYYY-MM-DD (expires 15:30 IST)")
    ap.add_argument("--lot", type=int, default=65)
    ap.add_argument("--capital", type=float, default=500000)
    ap.add_argument("--risk-pct", type=float, default=2.0, help="%% of capital at risk per trade")
    ap.add_argument("--neutral-delta", type=float, default=0.15)
    ap.add_argument("--directional-delta", type=float, default=0.20)
    ap.add_argument("--widths", default="100,150,200,250,300")
    ap.add_argument("--chain", help="CSV with strike,type,bid,ask")
    a = ap.parse_args()

    iv = (a.atm_iv or a.vix) / 100.0
    t0 = datetime.strptime(a.entry, "%Y-%m-%d %H:%M")
    t1 = datetime.strptime(a.expiry + " 15:30", "%Y-%m-%d %H:%M")
    days = (t1 - t0).total_seconds() / 86400
    T = days / 365.0
    chain = load_chain(a.chain) if a.chain else None
    p = Pricer(a.spot, iv, T, chain)
    em = expected_move(a.spot, iv, T)
    widths = [int(w) for w in a.widths.split(",")]

    print(f"Spot {a.spot:,.0f}  ATM IV {iv*100:.1f}%  calendar days to expiry {days:.2f}  "
          f"mode={'CHAIN' if chain else 'MODEL (verify against live quotes)'}")
    print(f"1-SD expected move +/-{em:,.0f} pts  -> range {a.spot-em:,.0f} - {a.spot+em:,.0f}")

    bc = spread(p, "CE", a.directional_delta, widths)
    bp = spread(p, "PE", a.directional_delta, widths)
    ic_c = spread(p, "CE", a.neutral_delta, widths)
    ic_p = spread(p, "PE", a.neutral_delta, widths)
    rp = a.risk_pct / 100
    print(evaluate(f"BEAR CALL SPREAD (short ~{a.directional_delta:.2f} delta)", p, [bc], a.lot, a.capital, rp, em))
    print(evaluate(f"BULL PUT SPREAD (short ~{a.directional_delta:.2f} delta)", p, [bp], a.lot, a.capital, rp, em))
    print(evaluate(f"IRON CONDOR (shorts ~{a.neutral_delta:.2f} delta)", p, [ic_p, ic_c], a.lot, a.capital, rp, em))
    print("\n" + DISCLAIMER)


if __name__ == "__main__":
    main()
