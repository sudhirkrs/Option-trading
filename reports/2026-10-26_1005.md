# NIFTY trade card: Mon 26 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,638.10 | Yahoo |
| India VIX | 17.49 | Yahoo |
| Expiry | Tue 03 Nov 2026 (8.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 18.4% | chain |
| 1-SD expected move | ±626 → 22,012 – 23,264 | |

## Regime
* IV percentile (1y): **80**
* Trend: **DOWN**  (20-DMA 22,692, 50-DMA 23,368)
* 20-day realised vol 15.4% vs implied 18.4% → premium +3.0 vol pts
* VIX RISING (5-day high 16.86)
* Today's opening gap: -0.33%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23000 (34,571) · PE 22000 (29,234)

## Verdict
**TRADE: BEAR CALL SPREAD, 1 lot(s)** (prices are live)
Order: buy the hedge leg first, then sell the short leg, both as limit orders at mid.

### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23200 CE | 69.20 | 69.00/69.40 | 18.2% | +0.20 | 80% | 38% | 25,435 |
| SELL | 23100 CE | 94.35 | 94.10/94.60 | 18.5% | +0.25 | 75% | 48% | 25,556 |
* ✅ credit/width CE 25.1/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹114 = 7.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 23100CE is beyond the 23000 wall (34,571 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.15 pts = ₹1,635/lot · max loss ₹4,926/lot · margin ~₹14,715/lot · net at 50% target ₹704/lot
* Exits: **take profit** when spread ≤ 12.57 · **stop** when spread ≥ 75.45 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22200 PE | 82.57 | 82.30/82.85 | 18.7% | -0.22 | 77% | 47% | 16,274 |
| SELL | 22300 PE | 101.45 | 101.20/101.70 | 18.1% | -0.27 | 72% | 57% | 23,010 |
* ❌ credit/width PE 18.9/100 = 0.19 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹116 = 9.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22300PE is at/inside the 22000 wall (29,234 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 18.88 pts = ₹1,227/lot · max loss ₹5,335/lot · margin ~₹14,715/lot · net at 50% target ₹497/lot
* Exits: **take profit** when spread ≤ 9.44 · **stop** when spread ≥ 56.63 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22050 PE | 60.67 | 60.45/60.90 | 19.6% | -0.17 | 82% | 36% | 1,363 |
| SELL | 22150 PE | 74.75 | 74.55/74.95 | 19.0% | -0.20 | 79% | 43% | 1,938 |
| BUY (hedge, first) | 23200 CE | 69.20 | 69.00/69.40 | 18.2% | +0.20 | 80% | 38% | 25,435 |
| SELL | 23100 CE | 94.35 | 94.10/94.60 | 18.5% | +0.25 | 75% | 48% | 25,556 |
* ❌ credit/width PE 14.1/100 = 0.14, CE 25.1/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹224 = 8.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22150PE is at/inside the 22000 wall (29,234 OI); short 23100CE is beyond the 23000 wall (34,571 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 39.22 pts = ₹2,550/lot · max loss ₹4,070/lot · margin ~₹14,715/lot · net at 50% target ₹1,051/lot
* Exits: **take profit** when spread ≤ 19.61 · **stop** when spread ≥ 117.67 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
