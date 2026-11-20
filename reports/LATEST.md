# NIFTY trade card: Fri 20 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,508.05 | Yahoo |
| India VIX | 17.08 | Yahoo |
| Expiry | Tue 01 Dec 2026 (11.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 14.7% | chain |
| 1-SD expected move | ±658 → 24,850 – 26,166 | |

## Regime
* IV percentile (1y): **77**
* Trend: **UP**  (20-DMA 24,262, 50-DMA 23,480)
* 20-day realised vol 13.6% vs implied 14.7% → premium +1.1 vol pts
* VIX RISING (5-day high 16.62)
* Today's opening gap: -0.57%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (47,237) · PE 25000 (35,757)

## Verdict
**NO TRADE today.**
* uptrend but VIX rising: no put selling
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25050 PE | 98.70 | 98.45/98.95 | 16.0% | -0.23 | 76% | 50% | 2,945 |
| SELL | 25150 PE | 123.72 | 123.55/123.90 | 15.9% | -0.28 | 71% | 60% | 3,036 |
* ✅ credit/width PE 25.0/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹121 = 7.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25150PE is inside by 150 pts (tolerance 100), too far inside the 25000 wall (35,757 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.02 pts = ₹1,627/lot · max loss ₹4,939/lot · margin ~₹16,580/lot · net at 50% target ₹693/lot
* Exits: **take profit** when spread ≤ 12.51 · **stop** when spread ≥ 75.07 (loss = 2× credit) · **time exit** Mon 30 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 26050 CE | 75.35 | 75.20/75.50 | 13.7% | +0.22 | 79% | 41% | 1,914 |
| SELL | 25950 CE | 98.45 | 98.25/98.65 | 13.7% | +0.27 | 74% | 50% | 2,007 |
* ❌ credit/width CE 23.1/100 = 0.23 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹115 = 7.7% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25950CE is inside by 50 pts (tolerance 100) the 26000 wall (47,237 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 23.10 pts = ₹1,502/lot · max loss ₹5,060/lot · margin ~₹16,580/lot · net at 50% target ₹636/lot
* Exits: **take profit** when spread ≤ 11.55 · **stop** when spread ≥ 69.30 (loss = 2× credit) · **time exit** Mon 30 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25050 PE | 98.70 | 98.45/98.95 | 16.0% | -0.23 | 76% | 50% | 2,945 |
| SELL | 25150 PE | 123.72 | 123.55/123.90 | 15.9% | -0.28 | 71% | 60% | 3,036 |
| BUY (hedge, first) | 26150 CE | 57.23 | 57.10/57.35 | 13.8% | +0.17 | 83% | 33% | 1,919 |
| SELL | 26050 CE | 75.35 | 75.20/75.50 | 13.7% | +0.22 | 79% | 41% | 1,914 |
* ❌ credit/width PE 25.0/100 = 0.25, CE 18.1/100 = 0.18 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹231 = 8.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25150PE is inside by 150 pts (tolerance 100), too far inside the 25000 wall (35,757 OI); short 26050CE is beyond the 26000 wall (47,237 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 43.15 pts = ₹2,805/lot · max loss ₹3,819/lot · margin ~₹16,580/lot · net at 50% target ₹1,172/lot
* Exits: **take profit** when spread ≤ 21.57 · **stop** when spread ≥ 129.45 (loss = 2× credit) · **time exit** Mon 30 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
