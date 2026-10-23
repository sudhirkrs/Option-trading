# NIFTY trade card: Fri 23 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,561.00 | Yahoo |
| India VIX | 16.64 | Yahoo |
| Expiry | Tue 03 Nov 2026 (11.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 16.6% | chain |
| 1-SD expected move | ±655 → 21,906 – 23,216 | |

## Regime
* IV percentile (1y): **78**
* Trend: **DOWN**  (20-DMA 22,712, 50-DMA 23,403)
* 20-day realised vol 16.4% vs implied 16.6% → premium +0.2 vol pts
* VIX RISING (5-day high 15.76)
* Today's opening gap: +0.24%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23000 (29,840) · PE 22000 (22,491)

## Verdict
**NO TRADE today.**
* BEAR CALL SPREAD failed a gate (see ❌ below)

### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23100 CE | 86.00 | 85.85/86.15 | 16.4% | +0.23 | 78% | 43% | 16,724 |
| SELL | 23000 CE | 112.80 | 112.65/112.95 | 16.6% | +0.28 | 73% | 53% | 29,840 |
* ✅ credit/width CE 26.8/100 = 0.27 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹118 = 6.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23000CE is at/inside the 23000 wall (29,840 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 26.80 pts = ₹1,742/lot · max loss ₹4,822/lot · margin ~₹14,665/lot · net at 50% target ₹753/lot
* Exits: **take profit** when spread ≤ 13.40 · **stop** when spread ≥ 80.40 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22100 PE | 83.83 | 83.65/84.00 | 16.8% | -0.22 | 77% | 47% | 5,373 |
| SELL | 22200 PE | 103.72 | 103.50/103.95 | 16.4% | -0.26 | 73% | 56% | 14,878 |
* ❌ credit/width PE 19.9/100 = 0.20 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹116 = 9.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22200PE is at/inside the 22000 wall (22,491 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 19.90 pts = ₹1,293/lot · max loss ₹5,269/lot · margin ~₹14,665/lot · net at 50% target ₹530/lot
* Exits: **take profit** when spread ≤ 9.95 · **stop** when spread ≥ 59.70 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22000 PE | 67.70 | 67.60/67.80 | 17.2% | -0.18 | 81% | 39% | 22,491 |
| SELL | 22100 PE | 83.83 | 83.65/84.00 | 16.8% | -0.22 | 77% | 47% | 5,373 |
| BUY (hedge, first) | 23100 CE | 86.00 | 85.85/86.15 | 16.4% | +0.23 | 78% | 43% | 16,724 |
| SELL | 23000 CE | 112.80 | 112.65/112.95 | 16.6% | +0.28 | 73% | 53% | 29,840 |
* ❌ credit/width PE 16.1/100 = 0.16, CE 26.8/100 = 0.27 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹230 = 8.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22100PE is at/inside the 22000 wall (22,491 OI); short 23000CE is at/inside the 23000 wall (29,840 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 42.93 pts = ₹2,790/lot · max loss ₹3,833/lot · margin ~₹14,665/lot · net at 50% target ₹1,165/lot
* Exits: **take profit** when spread ≤ 21.46 · **stop** when spread ≥ 128.78 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
