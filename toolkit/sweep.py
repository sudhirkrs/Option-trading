"""Credit/width vs short-strike delta for credit spreads and iron flies.
Usage: python3 sweep.py SPOT ATM_IV_PCT CALENDAR_DAYS"""
import sys
from planner import Pricer, R
from optlib import prob_itm, prob_touch
from costs import round_trip

S, iv, days = float(sys.argv[1]), float(sys.argv[2]) / 100, float(sys.argv[3])
p = Pricer(S, iv, days / 365)
lot = 65
print(f"{'side':<5}{'short':>7}{'delta':>7}{'width':>6}{'credit':>8}{'c/w':>6}{'P(max loss)':>12}{'cost drag/lot*':>17}")
for opt in ("CE", "PE"):
    for d in (0.35, 0.30, 0.25, 0.20, 0.15):
        Ks = p.strike_for_delta(d, opt)
        for w in (100, 150, 200):
            Kl = Ks + w if opt == "CE" else Ks - w
            c = p.price(Ks, opt) - p.price(Kl, opt)
            pl = prob_itm(S, Kl, p.T, R, p.iv(Kl, opt), opt)
            ps = prob_itm(S, Ks, p.T, R, p.iv(Ks, opt), opt)
            cost = round_trip([(opt, Ks, -1, p.price(Ks, opt)), (opt, Kl, 1, p.price(Kl, opt))], lot, 0.5)
            print(f"{opt:<5}{Ks:>7}{p.delta(Ks,opt):>7.2f}{w:>6}{c:>8.1f}{c/w:>6.2f}{pl*100:>11.0f}%{-cost:>17.0f}")
print("* at fair (model) prices the expected value of any spread is minus its costs;\n  profit needs implied vol > realised vol, i.e. a variance risk premium.")
# iron fly
atm = round(S / 50) * 50
for w in (200, 300, 400):
    c = p.price(atm, "CE") + p.price(atm, "PE") - p.price(atm + w, "CE") - p.price(atm - w, "PE")
    print(f"IRON FLY {atm} wings {w}: credit {c:.1f}  c/w {c/w:.2f}  breakevens {atm-c:.0f}/{atm+c:.0f}  max loss {(w-c)*lot:,.0f}/lot")
