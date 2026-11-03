# NIFTY trade card: Tue 03 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 23,623.15 | Yahoo |
| India VIX | 15.86 | Yahoo |
| Expiry | Mon 09 Nov 2026 (6.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.2% | chain |
| 1-SD expected move | ±470 → 23,153 – 24,093 | |

## Regime
* IV percentile (1y): **73**
* Trend: **RANGE**  (20-DMA 22,811, 50-DMA 23,230)
* 20-day realised vol 15.6% vs implied 15.2% → premium -0.4 vol pts
* VIX flat/mixed (5-day high 16.40)
* Today's opening gap: +0.60%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 24000 (65,292) · PE 23000 (68,639)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23100 PE | 48.22 | 48.15/48.30 | 18.3% | -0.16 | 83% | 34% | 21,157 |
| SELL | 23200 PE | 63.35 | 63.30/63.40 | 17.9% | -0.20 | 79% | 43% | 34,695 |
| BUY (hedge, first) | 24100 CE | 34.83 | 34.75/34.90 | 14.1% | +0.15 | 85% | 29% | 29,936 |
| SELL | 24000 CE | 50.88 | 50.75/51.00 | 13.9% | +0.21 | 79% | 40% | 65,292 |
* ❌ credit/width PE 15.1/100 = 0.15, CE 16.0/100 = 0.16 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹212 = 10.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23200PE is inside by 200 pts (tolerance 100), too far inside the 23000 wall (68,639 OI); short 24000CE is inside by 0 pts (tolerance 100) the 24000 wall (65,292 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 31.17 pts = ₹2,026/lot · max loss ₹4,585/lot · margin ~₹15,355/lot · net at 50% target ₹801/lot
* Exits: **take profit** when spread ≤ 15.59 · **stop** when spread ≥ 93.52 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24050 CE | 42.00 | 41.90/42.10 | 14.0% | +0.18 | 82% | 34% | 5,256 |
| SELL | 23950 CE | 60.55 | 60.45/60.65 | 13.7% | +0.24 | 76% | 46% | 5,680 |
* ❌ credit/width CE 18.5/100 = 0.19 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹107 = 8.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 23950CE is inside by 50 pts (tolerance 100) the 24000 wall (65,292 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 18.55 pts = ₹1,206/lot · max loss ₹5,350/lot · margin ~₹15,355/lot · net at 50% target ₹496/lot
* Exits: **take profit** when spread ≤ 9.27 · **stop** when spread ≥ 55.65 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23200 PE | 63.35 | 63.30/63.40 | 17.9% | -0.20 | 79% | 43% | 34,695 |
| SELL | 23300 PE | 83.62 | 83.45/83.80 | 17.6% | -0.25 | 74% | 54% | 34,471 |
* ❌ credit/width PE 20.3/100 = 0.20 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 8.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23300PE is inside by 300 pts (tolerance 100), too far inside the 23000 wall (68,639 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 20.28 pts = ₹1,318/lot · max loss ₹5,242/lot · margin ~₹15,355/lot · net at 50% target ₹547/lot
* Exits: **take profit** when spread ≤ 10.14 · **stop** when spread ≥ 60.83 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
