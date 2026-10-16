# NIFTY trade card: Fri 16 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 23,053.45 | Yahoo |
| India VIX | 14.17 | Yahoo |
| Expiry | Tue 27 Oct 2026 (11.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 12.6% | chain |
| 1-SD expected move | ±510 → 22,544 – 23,563 | |

## Regime
* IV percentile (1y): **67**
* Trend: **RANGE**  (20-DMA 22,836, 50-DMA 23,547)
* 20-day realised vol 15.9% vs implied 12.6% → premium -3.3 vol pts
* VIX flat/mixed (5-day high 15.25)
* Today's opening gap: +0.29%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23500 (155,599) · PE 22500 (93,983)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22550 PE | 55.58 | 55.40/55.75 | 14.7% | -0.17 | 82% | 37% | 6,669 |
| SELL | 22650 PE | 73.10 | 72.95/73.25 | 14.5% | -0.22 | 78% | 47% | 6,525 |
| BUY (hedge, first) | 23450 CE | 60.52 | 60.40/60.65 | 11.4% | +0.23 | 78% | 42% | 6,292 |
| SELL | 23350 CE | 86.22 | 86.05/86.40 | 11.4% | +0.30 | 71% | 55% | 6,178 |
* ❌ credit/width PE 17.5/100 = 0.18, CE 25.7/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹221 = 7.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22650PE is at/inside the 22500 wall (93,983 OI); short 23350CE is at/inside the 23500 wall (155,599 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 43.22 pts = ₹2,810/lot · max loss ₹3,808/lot · margin ~₹14,985/lot · net at 50% target ₹1,183/lot
* Exits: **take profit** when spread ≤ 21.61 · **stop** when spread ≥ 129.67 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23450 CE | 60.52 | 60.40/60.65 | 11.4% | +0.23 | 78% | 42% | 6,292 |
| SELL | 23350 CE | 86.22 | 86.05/86.40 | 11.4% | +0.30 | 71% | 55% | 6,178 |
* ✅ credit/width CE 25.7/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 6.7% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23350CE is at/inside the 23500 wall (155,599 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.70 pts = ₹1,670/lot · max loss ₹4,889/lot · margin ~₹14,985/lot · net at 50% target ₹723/lot
* Exits: **take profit** when spread ≤ 12.85 · **stop** when spread ≥ 77.10 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22650 PE | 73.10 | 72.95/73.25 | 14.5% | -0.22 | 78% | 47% | 6,525 |
| SELL | 22750 PE | 95.60 | 95.35/95.85 | 14.3% | -0.27 | 72% | 58% | 10,372 |
* ❌ credit/width PE 22.5/100 = 0.23 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹114 = 7.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22750PE is at/inside the 22500 wall (93,983 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.50 pts = ₹1,462/lot · max loss ₹5,099/lot · margin ~₹14,985/lot · net at 50% target ₹617/lot
* Exits: **take profit** when spread ≤ 11.25 · **stop** when spread ≥ 67.50 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
