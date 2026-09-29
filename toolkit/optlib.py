"""Black-Scholes pricing, Greeks, IV solver and probability helpers for NSE options."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm


def tte_years(days, basis="calendar"):
    return max(days, 1e-6) / (365.0 if basis == "calendar" else 252.0)


def _d(S, K, T, r, s, q=0.0):
    v = s * math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * s * s) * T) / v
    return d1, d1 - v


def _is_call(opt):
    return opt.upper() in ("CE", "C", "CALL")


def bs_price(S, K, T, r, s, opt="CE", q=0.0):
    call = _is_call(opt)
    if T <= 0 or s <= 0:
        return max(S - K, 0.0) if call else max(K - S, 0.0)
    d1, d2 = _d(S, K, T, r, s, q)
    dr, dq = math.exp(-r * T), math.exp(-q * T)
    if call:
        return S * dq * norm.cdf(d1) - K * dr * norm.cdf(d2)
    return K * dr * norm.cdf(-d2) - S * dq * norm.cdf(-d1)


def bs_greeks(S, K, T, r, s, opt="CE", q=0.0):
    """delta, gamma, vega (per vol point), theta (per calendar day)."""
    call = _is_call(opt)
    px = bs_price(S, K, T, r, s, opt, q)
    if T <= 0 or s <= 0:
        return dict(price=px, delta=0.0, gamma=0.0, vega=0.0, theta=0.0)
    d1, d2 = _d(S, K, T, r, s, q)
    dr, dq, pdf, rt = math.exp(-r * T), math.exp(-q * T), norm.pdf(d1), math.sqrt(T)
    delta = dq * (norm.cdf(d1) if call else norm.cdf(d1) - 1.0)
    gamma = dq * pdf / (S * s * rt)
    vega = S * dq * pdf * rt / 100.0
    t1 = -(S * dq * pdf * s) / (2 * rt)
    if call:
        theta = t1 - r * K * dr * norm.cdf(d2) + q * S * dq * norm.cdf(d1)
    else:
        theta = t1 + r * K * dr * norm.cdf(-d2) - q * S * dq * norm.cdf(-d1)
    return dict(price=px, delta=delta, gamma=gamma, vega=vega, theta=theta / 365.0)


def implied_vol(price, S, K, T, r, opt="CE", q=0.0, lo=0.005, hi=6.0, tick=0.05):
    """Solve IV from price. Returns nan when IV is not recoverable
    (price outside no-arbitrage band, vol-insensitive deep ITM, solver failure)."""
    if T <= 0 or price <= 0:
        return float("nan")
    dr, dq = math.exp(-r * T), math.exp(-q * T)
    if _is_call(opt):
        lower, upper = max(S * dq - K * dr, 0.0), S * dq
    else:
        lower, upper = max(K * dr - S * dq, 0.0), K * dr
    if price < lower - 1e-8 or price > upper + 1e-8:
        return float("nan")
    if bs_price(S, K, T, r, hi, opt, q) - bs_price(S, K, T, r, lo, opt, q) < tick:
        return float("nan")
    f = lambda s: bs_price(S, K, T, r, s, opt, q) - price
    try:
        if f(lo) * f(hi) > 0:
            return float("nan")
        sigma = brentq(f, lo, hi, maxiter=200, xtol=1e-10, rtol=1e-12)
    except Exception:
        return float("nan")
    if bs_greeks(S, K, T, r, sigma, opt, q)["vega"] < 1e-4:
        return float("nan")
    return sigma


def prob_itm(S, K, T, r, s, opt="CE", q=0.0):
    _, d2 = _d(S, K, T, r, s, q)
    return norm.cdf(d2) if _is_call(opt) else norm.cdf(-d2)


def prob_touch(S, K, T, r, s, q=0.0):
    """Probability the underlying touches K before expiry (~2x prob_itm)."""
    mu, a, vt = r - q - 0.5 * s * s, math.log(K / S), s * math.sqrt(T)
    if abs(a) < 1e-12:
        return 1.0
    sg = np.sign(a)
    p = norm.cdf((-abs(a) + mu * T * sg) / vt) + \
        math.exp(2 * mu * a / (s * s)) * norm.cdf((-abs(a) - mu * T * sg) / vt)
    return float(min(max(p, 0.0), 1.0))


def expected_move(S, s, T, sd=1.0):
    return S * s * math.sqrt(T) * sd


def skewed_iv(atm_iv, S, K, slope=0.5, curve=0.35):
    """Simple NIFTY-style skew: puts (K<S) richer than calls."""
    m = math.log(K / S)
    return atm_iv * (1 - slope * m + curve * m * m)


def payoff_at_expiry(legs, spots):
    """legs = [(opt, strike, qty, entry_premium)], qty<0 = short."""
    spots = np.asarray(spots, float)
    pnl = np.zeros_like(spots)
    for (o, K, q, p) in legs:
        if o.upper() in ("CE", "C", "CALL"):
            intr = np.maximum(spots - K, 0.0)
        elif o.upper() in ("PE", "P", "PUT"):
            intr = np.maximum(K - spots, 0.0)
        else:
            intr = spots - K
        pnl += q * (intr - p)
    return pnl
