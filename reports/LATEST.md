# NIFTY trade card: Fri 06 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 24,614.15 | Yahoo |
| India VIX | 16.81 | Yahoo |
| Expiry | Tue 17 Nov 2026 (11.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 16.0% | chain |
| 1-SD expected move | ±690 → 23,924 – 25,304 | |

## Regime
* IV percentile (1y): **78**
* Trend: **RANGE**  (20-DMA 23,096, 50-DMA 23,240)
* 20-day realised vol 15.5% vs implied 16.0% → premium +0.5 vol pts
* VIX RISING (5-day high 15.72)
* Today's opening gap: +0.01%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 25700 (33,944) · PE 24500 (22,641)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23950 PE | 82.28 | 82.10/82.45 | 18.8% | -0.18 | 81% | 39% | 2,237 |
| SELL | 24050 PE | 99.22 | 99.00/99.45 | 18.5% | -0.21 | 78% | 46% | 1,266 |
| BUY (hedge, first) | 25300 CE | 55.60 | 55.50/55.70 | 14.8% | +0.17 | 84% | 31% | 8,086 |
| SELL | 25200 CE | 71.70 | 71.55/71.85 | 14.6% | +0.20 | 80% | 38% | 9,870 |
* ❌ credit/width PE 16.9/100 = 0.17, CE 16.1/100 = 0.16 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹225 = 10.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24050PE is beyond the 24500 wall (22,641 OI); short 25200CE is inside by 500 pts (tolerance 100), too far inside the 25700 wall (33,944 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 33.05 pts = ₹2,148/lot · max loss ₹4,471/lot · margin ~₹15,999/lot · net at 50% target ₹849/lot
* Exits: **take profit** when spread ≤ 16.52 · **stop** when spread ≥ 99.15 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25150 CE | 81.67 | 81.55/81.80 | 14.6% | +0.23 | 78% | 42% | 1,579 |
| SELL | 25050 CE | 104.30 | 104.10/104.50 | 14.5% | +0.27 | 73% | 51% | 3,477 |
* ❌ credit/width CE 22.6/100 = 0.23 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹116 = 7.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25050CE is inside by 650 pts (tolerance 100), too far inside the 25700 wall (33,944 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.62 pts = ₹1,471/lot · max loss ₹5,092/lot · margin ~₹15,999/lot · net at 50% target ₹619/lot
* Exits: **take profit** when spread ≤ 11.31 · **stop** when spread ≥ 67.88 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24100 PE | 108.95 | 108.75/109.15 | 18.4% | -0.23 | 76% | 50% | 7,272 |
| SELL | 24200 PE | 131.65 | 131.40/131.90 | 18.1% | -0.27 | 72% | 58% | 11,436 |
* ❌ credit/width PE 22.7/100 = 0.23 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹123 = 8.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 24200PE is beyond the 24500 wall (22,641 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.70 pts = ₹1,476/lot · max loss ₹5,091/lot · margin ~₹15,999/lot · net at 50% target ₹615/lot
* Exits: **take profit** when spread ≤ 11.35 · **stop** when spread ≥ 68.10 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
