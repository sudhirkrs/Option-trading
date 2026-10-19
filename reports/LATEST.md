# NIFTY trade card: Mon 19 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 23,069.95 | Yahoo |
| India VIX | 14.63 | Yahoo |
| Expiry | Tue 27 Oct 2026 (8.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 13.2% | chain |
| 1-SD expected move | ±456 → 22,614 – 23,526 | |

## Regime
* IV percentile (1y): **70**
* Trend: **RANGE**  (20-DMA 22,827, 50-DMA 23,518)
* 20-day realised vol 16.1% vs implied 13.2% → premium -2.9 vol pts
* VIX flat/mixed (5-day high 15.25)
* Today's opening gap: +0.02%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23500 (168,640) · PE 23000 (100,147)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22600 PE | 44.92 | 44.85/45.00 | 15.0% | -0.16 | 83% | 34% | 60,583 |
| SELL | 22700 PE | 61.05 | 61.00/61.10 | 14.7% | -0.21 | 78% | 45% | 79,599 |
| BUY (hedge, first) | 23550 CE | 33.15 | 33.05/33.25 | 12.3% | +0.15 | 85% | 28% | 12,458 |
| SELL | 23450 CE | 49.15 | 49.05/49.25 | 12.1% | +0.21 | 80% | 39% | 20,773 |
* ❌ credit/width PE 16.1/100 = 0.16, CE 16.0/100 = 0.16 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹211 = 10.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22700PE is beyond the 23000 wall (100,147 OI); short 23450CE is at/inside the 23500 wall (168,640 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 32.12 pts = ₹2,088/lot · max loss ₹4,522/lot · margin ~₹14,995/lot · net at 50% target ₹833/lot
* Exits: **take profit** when spread ≤ 16.06 · **stop** when spread ≥ 96.38 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23500 CE | 40.67 | 40.60/40.75 | 12.2% | +0.18 | 83% | 34% | 168,640 |
| SELL | 23400 CE | 60.40 | 60.30/60.50 | 12.1% | +0.24 | 76% | 46% | 47,127 |
* ❌ credit/width CE 19.7/100 = 0.20 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹106 = 8.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23400CE is at/inside the 23500 wall (168,640 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 19.73 pts = ₹1,282/lot · max loss ₹5,274/lot · margin ~₹14,995/lot · net at 50% target ₹535/lot
* Exits: **take profit** when spread ≤ 9.86 · **stop** when spread ≥ 59.18 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22700 PE | 61.05 | 61.00/61.10 | 14.7% | -0.21 | 78% | 45% | 79,599 |
| SELL | 22800 PE | 83.53 | 83.35/83.70 | 14.5% | -0.27 | 72% | 57% | 45,134 |
* ❌ credit/width PE 22.5/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 7.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 22800PE is beyond the 23000 wall (100,147 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.48 pts = ₹1,461/lot · max loss ₹5,098/lot · margin ~₹14,995/lot · net at 50% target ₹619/lot
* Exits: **take profit** when spread ≤ 11.24 · **stop** when spread ≥ 67.43 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
