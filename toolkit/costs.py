"""Indian F&O charges and margin estimates.

VERIFY these rates before use - they are revised with the Budget.
STT figures reflect Budget 2026 (effective 1 Apr 2026).
"""
STT_SELL_PREMIUM = 0.0015     # 0.15% of premium, sell side
STT_EXERCISE = 0.0015         # 0.15% of intrinsic value if left to exercise
EXCHANGE_TXN = 0.00035        # NSE options, of premium turnover (approx)
SEBI_FEE = 0.0000010          # Rs 10 per crore
STAMP_DUTY_BUY = 0.00003      # 0.003% buy side
GST = 0.18                    # on brokerage + txn + SEBI fee
BROKERAGE_PER_ORDER = 20.0    # typical discount broker flat fee


def leg_cost(premium, lot, lots, is_sell, brokerage=BROKERAGE_PER_ORDER):
    turnover = abs(premium) * lot * abs(lots)
    stt = turnover * STT_SELL_PREMIUM if is_sell else 0.0
    txn = turnover * EXCHANGE_TXN
    sebi = turnover * SEBI_FEE
    stamp = 0.0 if is_sell else turnover * STAMP_DUTY_BUY
    gst = (brokerage + txn + sebi) * GST
    return stt + txn + sebi + stamp + gst + brokerage


def round_trip(legs, lot, exit_frac=0.5, brokerage=BROKERAGE_PER_ORDER):
    """legs = [(opt, strike, qty, premium)]; exit_frac = exit price as a
    fraction of entry premium (0.5 = closing at the 50% profit target)."""
    return sum(leg_cost(p, lot, q, q < 0, brokerage) +
               leg_cost(p * exit_frac, lot, q, q > 0, brokerage)
               for (_, _, q, p) in legs)


SPAN_PCT = {"index": 0.055, "stock": 0.095}
EXPO_PCT = {"index": 0.020, "stock": 0.035}


def estimate_margin(legs, spot, lot, underlying="index", hedged=False, max_loss=None):
    """Rough margin. Always confirm on the broker's SPAN calculator."""
    if hedged and max_loss is not None:
        return max(max_loss * 1.10, spot * lot * 0.010)
    n = sum(abs(q) for (_, _, q, _) in legs if q < 0)
    return spot * lot * (SPAN_PCT[underlying] + EXPO_PCT[underlying]) * n
