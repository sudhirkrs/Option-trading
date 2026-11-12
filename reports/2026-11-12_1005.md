# NIFTY trade card: Thu 12 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,366.65 | Yahoo |
| India VIX | 17.17 | Yahoo |
| Expiry | Tue 17 Nov 2026 (5.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 16.7% | chain |
| 1-SD expected move | ±506 → 24,861 – 25,872 | |

## Regime
* IV percentile (1y): **78**
* Trend: **UP**  (20-DMA 23,520, 50-DMA 23,312)
* 20-day realised vol 15.1% vs implied 16.7% → premium +1.5 vol pts
* VIX RISING (5-day high 17.56)
* Today's opening gap: -0.16%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (164,796) · PE 25000 (127,571)

## Verdict
**NO TRADE today.**
* uptrend but VIX rising: no put selling
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24950 PE | 57.53 | 57.45/57.60 | 17.3% | -0.20 | 80% | 41% | 24,856 |
| SELL | 25050 PE | 78.28 | 78.15/78.40 | 17.0% | -0.25 | 74% | 53% | 31,484 |
* ❌ credit/width PE 20.8/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹111 = 8.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25050PE is inside by 50 pts (tolerance 100) the 25000 wall (127,571 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 20.75 pts = ₹1,349/lot · max loss ₹5,210/lot · margin ~₹16,488/lot · net at 50% target ₹564/lot
* Exits: **take profit** when spread ≤ 10.38 · **stop** when spread ≥ 62.25 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25800 CE | 63.58 | 63.50/63.65 | 17.0% | +0.22 | 79% | 42% | 96,041 |
| SELL | 25700 CE | 85.83 | 85.70/85.95 | 16.8% | +0.28 | 73% | 53% | 68,778 |
* ❌ credit/width CE 22.2/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 7.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25700CE is inside by 300 pts (tolerance 100), too far inside the 26000 wall (164,796 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.25 pts = ₹1,446/lot · max loss ₹5,113/lot · margin ~₹16,488/lot · net at 50% target ₹611/lot
* Exits: **take profit** when spread ≤ 11.12 · **stop** when spread ≥ 66.75 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24850 PE | 42.08 | 42.00/42.15 | 17.6% | -0.15 | 84% | 32% | 31,315 |
| SELL | 24950 PE | 57.53 | 57.45/57.60 | 17.3% | -0.20 | 80% | 41% | 24,856 |
| BUY (hedge, first) | 25900 CE | 47.05 | 47.00/47.10 | 17.2% | +0.17 | 84% | 32% | 43,430 |
| SELL | 25800 CE | 63.58 | 63.50/63.65 | 17.0% | +0.22 | 79% | 42% | 96,041 |
* ❌ credit/width PE 15.5/100 = 0.15, CE 16.5/100 = 0.17 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹214 = 10.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24950PE is beyond the 25000 wall (127,571 OI); short 25800CE is inside by 200 pts (tolerance 100), too far inside the 26000 wall (164,796 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 31.98 pts = ₹2,078/lot · max loss ₹4,534/lot · margin ~₹16,488/lot · net at 50% target ₹825/lot
* Exits: **take profit** when spread ≤ 15.99 · **stop** when spread ≥ 95.93 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
