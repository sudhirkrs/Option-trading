"""Replay saved trade cards under alternative gate settings.

Reads ../reports/*.md (the cards auto.py wrote), re-evaluates the main
structure's checklist with the credit/width and OI-wall rules swapped for each
scenario, and prints how many days would have produced a TRADE.

Only the two rules in question are changed. Every other check on the card
(delta, cost, liquidity, size) and every non-gate reason (event, IVP, gap, VIX)
stays exactly as the original card recorded it.

  python3 replay.py [--reports ../reports] [--verbose]

Limits: it can only re-judge the one structure the card picked, using the strikes
the card chose. A looser rule could have let auto.py pick a different strike, so
treat the counts as a floor, not a forecast. It says nothing about whether the
extra trades would have made money.
"""
import argparse
import glob
import os
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

# name: (min credit/width, wall mode, wall tolerance in points)
#   wall mode: "strict" = short strictly beyond wall (current rule)
#              "near"   = short may sit up to `tol` points inside the wall
#              "off"    = ignore the wall
SCENARIOS = {
    "1 current rules":             (0.25, "strict", 0),
    "2 soft wall (100 pts)":       (0.25, "near", 100),
    "3 no wall gate":              (0.25, "off", 0),
    "4 credit 0.20, strict wall":  (0.20, "strict", 0),
    "5 credit 0.20, soft wall":    (0.20, "near", 100),
    "6 no wall, credit 0.20":      (0.20, "off", 0),
}

RATIO = re.compile(r"(CE|PE) ([\d.]+)/(\d+) = ")
WALL = re.compile(r"short (\d+)(CE|PE) is (?:beyond|at/inside) the (\d+) wall")


def parse(path):
    text = open(path).read()
    main = text.split("<details>")[0]
    name = os.path.basename(path)
    m = re.match(r"(\d{4}-\d{2}-\d{2})_(\d{4})", name)
    if not m:
        return None
    day, hhmm = m.groups()
    card = dict(day=day, time=hhmm, trade_orig="NO TRADE" not in main,
                ratios=[], walls=[], other_fail=[], other_reasons=[])
    in_verdict = False
    for line in main.splitlines():
        if line.startswith("## Verdict"):
            in_verdict = True
            continue
        if line.startswith("###"):
            in_verdict = False
        if in_verdict and line.startswith("* ") and "failed a gate" not in line:
            card["other_reasons"].append(line[2:])
        if "credit/width" in line and ("✅" in line or "❌" in line):
            card["ratios"] = [float(c) / int(w) for _, c, w in RATIO.findall(line)]
        elif "OI wall:" in line:
            card["walls"] = [(int(s), o, int(w)) for s, o, w in WALL.findall(line)]
        elif "❌" in line and "failed a gate" not in line:
            card["other_fail"].append(line)
    return card


def passes(card, min_ratio, mode, tol):
    if card["other_reasons"] or card["other_fail"]:
        return False
    if card["ratios"] and min(card["ratios"]) < min_ratio:
        return False
    if mode != "off":
        for short, opt, wall in card["walls"]:
            slack = 0 if mode == "strict" else tol
            ok = short > wall - slack if opt == "CE" else short < wall + slack
            if not ok:
                return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports", default=os.path.join(HERE, "..", "reports"))
    ap.add_argument("--verbose", action="store_true", help="list each day")
    a = ap.parse_args()

    cards = [c for c in (parse(p) for p in sorted(glob.glob(os.path.join(a.reports, "2026-*_*.md"))))
             if c and c["ratios"]]
    # LATEST.md has no timestamp so it is skipped by the glob above
    days = defaultdict(list)
    for c in cards:
        days[c["day"]].append(c)

    print(f"{len(cards)} cards over {len(days)} days "
          f"({sum(c['trade_orig'] for c in cards)} originally TRADE)\n")
    print(f"{'scenario':30} {'cards':>6} {'days':>5}")
    results = {}
    for name, (r, mode, tol) in SCENARIOS.items():
        ok = [c for c in cards if passes(c, r, mode, tol)]
        results[name] = {c["day"] for c in ok}
        print(f"{name:30} {len(ok):>6} {len(results[name]):>5}")

    if a.verbose:
        print()
        names = list(SCENARIOS)
        print("day         " + " ".join(n.split()[0] for n in names))
        for d in sorted(days):
            print(f"{d}  " + " ".join("Y" if d in results[n] else "." for n in names))


if __name__ == "__main__":
    main()
