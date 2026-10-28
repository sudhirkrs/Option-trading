# NIFTY trade card: Wed 28 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,560.70 | Yahoo |
| India VIX | 16.76 | Yahoo |
| Expiry | Tue 03 Nov 2026 (6.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 17.1% | chain |
| 1-SD expected move | ±503 → 22,058 – 23,064 | |

## Regime
* IV percentile (1y): **78**
* Trend: **DOWN**  (20-DMA 22,667, 50-DMA 23,301)
* 20-day realised vol 14.8% vs implied 17.1% → premium +2.2 vol pts
* VIX flat/mixed (5-day high 17.16)
* Today's opening gap: -0.32%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23000 (144,496) · PE 22000 (112,224)

## Verdict
**NO TRADE today.**
* BEAR CALL SPREAD failed a gate (see ❌ below)

### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23000 CE | 59.62 | 59.55/59.70 | 17.1% | +0.21 | 80% | 40% | 144,496 |
| SELL | 22900 CE | 84.78 | 84.65/84.90 | 17.3% | +0.27 | 73% | 52% | 65,050 |
* ✅ credit/width CE 25.2/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 6.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22900CE is at/inside the 23000 wall (144,496 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.15 pts = ₹1,635/lot · max loss ₹4,925/lot · margin ~₹14,664/lot · net at 50% target ₹706/lot
* Exits: **take profit** when spread ≤ 12.58 · **stop** when spread ≥ 75.45 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22200 PE | 60.60 | 60.55/60.65 | 16.8% | -0.21 | 78% | 45% | 59,791 |
| SELL | 22300 PE | 82.08 | 81.95/82.20 | 16.4% | -0.27 | 72% | 58% | 69,716 |
* ❌ credit/width PE 21.5/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹111 = 8.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22300PE is at/inside the 22000 wall (112,224 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.48 pts = ₹1,396/lot · max loss ₹5,163/lot · margin ~₹14,664/lot · net at 50% target ₹587/lot
* Exits: **take profit** when spread ≤ 10.74 · **stop** when spread ≥ 64.43 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22100 PE | 44.03 | 43.95/44.10 | 17.2% | -0.16 | 83% | 34% | 47,039 |
| SELL | 22200 PE | 60.60 | 60.55/60.65 | 16.8% | -0.21 | 78% | 45% | 59,791 |
| BUY (hedge, first) | 23000 CE | 59.62 | 59.55/59.70 | 17.1% | +0.21 | 80% | 40% | 144,496 |
| SELL | 22900 CE | 84.78 | 84.65/84.90 | 17.3% | +0.27 | 73% | 52% | 65,050 |
* ❌ credit/width PE 16.6/100 = 0.17, CE 25.2/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹218 = 8.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22200PE is at/inside the 22000 wall (112,224 OI); short 22900CE is at/inside the 23000 wall (144,496 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 41.72 pts = ₹2,712/lot · max loss ₹3,903/lot · margin ~₹14,664/lot · net at 50% target ₹1,138/lot
* Exits: **take profit** when spread ≤ 20.86 · **stop** when spread ≥ 125.17 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
