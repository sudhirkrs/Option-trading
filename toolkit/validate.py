"""Sanity checks for optlib. Run: python3 validate.py"""
import math
from optlib import bs_price, bs_greeks, implied_vol, prob_itm, prob_touch
from costs import round_trip

S, K, T, r, s = 100, 100, 1.0, 0.05, 0.20
c, p = bs_price(S, K, T, r, s, "CE"), bs_price(S, K, T, r, s, "PE")
assert abs(c - 10.4506) < 1e-3, c
assert abs((c - p) - (S - K * math.exp(-r * T))) < 1e-9
gc, gp = bs_greeks(S, K, T, r, s, "CE"), bs_greeks(S, K, T, r, s, "PE")
assert abs(gc["delta"] - gp["delta"] - 1) < 1e-9
assert abs(gc["gamma"] - gp["gamma"]) < 1e-12 and abs(gc["vega"] - gp["vega"]) < 1e-12
h = 1e-4
num_vega = (bs_price(S, K, T, r, s + h) - bs_price(S, K, T, r, s - h)) / (2 * h) / 100
assert abs(num_vega - gc["vega"]) < 1e-6
num_theta = (bs_price(S, K, T - 1 / 365, r, s) - c)
assert abs(num_theta - gc["theta"]) < 5e-3
for KK in (80, 95, 100, 105, 120):
    for ss in (0.1, 0.2, 0.5):
        for TT in (0.02, 0.25, 1.0):
            for o in ("CE", "PE"):
                px = bs_price(S, KK, TT, r, ss, o)
                iv = implied_vol(px, S, KK, TT, r, o)
                if not math.isnan(iv):
                    assert abs(iv - ss) < 1e-6, (KK, ss, TT, o, iv)
assert prob_touch(22600, 23000, 7 / 365, 0.06, 0.15) > prob_itm(22600, 23000, 7 / 365, 0.06, 0.15)
rt = round_trip([("PE", 0, -1, 30.0)], 65)
assert 40 < rt < 70, rt
print("all checks passed; 1-lot NIFTY Rs30 short round-trip cost = Rs%.0f" % rt)
