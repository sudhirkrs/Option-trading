# NIFTY trade card: Thu 01 Oct 2026, 10:45 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,557.85 | Yahoo |
| India VIX | 13.61 | Yahoo |
| Expiry | Tue 13 Oct 2026 (12.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 12.8% | chain |
| 1-SD expected move | ±528 → 22,030 – 23,086 | |

## Regime
* IV percentile (1y): **66**
* Trend: **DOWN**  (20-DMA 23,276, 50-DMA 23,873)
* 20-day realised vol 10.1% vs implied 12.8% → premium +2.7 vol pts
* VIX flat/mixed (5-day high 13.64)
* Today's opening gap: -0.34%
* Events up to expiry: 07 Oct RBI monetary policy decision
* OI walls (largest OI within 2 SD): CE 23000 (33,053) · PE 22000 (16,564)

## Verdict
**NO TRADE today.**
* event before exit: 07 Oct RBI monetary policy decision
* BEAR CALL SPREAD failed a gate (see ❌ below)

### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23000 CE | 68.62 | 68.55/68.70 | 12.6% | +0.23 | 78% | 43% | 33,053 |
| SELL | 22900 CE | 93.90 | 93.75/94.05 | 12.6% | +0.29 | 72% | 54% | 10,212 |
* ✅ credit/width CE 25.3/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹114 = 6.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22900CE is at/inside the 23000 wall (33,053 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.28 pts = ₹1,643/lot · max loss ₹4,918/lot · margin ~₹14,663/lot · net at 50% target ₹708/lot
* Exits: **take profit** when spread ≤ 12.64 · **stop** when spread ≥ 75.83 (loss = 2× credit) · **time exit** Mon 12 Oct 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22200 PE | 73.70 | 73.55/73.85 | 13.5% | -0.23 | 77% | 49% | 9,015 |
| SELL | 22300 PE | 94.70 | 94.50/94.90 | 13.1% | -0.28 | 71% | 61% | 8,499 |
* ❌ credit/width PE 21.0/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹114 = 8.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22300PE is at/inside the 22000 wall (16,564 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.00 pts = ₹1,365/lot · max loss ₹5,196/lot · margin ~₹14,663/lot · net at 50% target ₹568/lot
* Exits: **take profit** when spread ≤ 10.50 · **stop** when spread ≥ 63.00 (loss = 2× credit) · **time exit** Mon 12 Oct 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22050 PE | 50.30 | 50.15/50.45 | 14.0% | -0.16 | 83% | 35% | 1,410 |
| SELL | 22150 PE | 64.78 | 64.55/65.00 | 13.6% | -0.20 | 79% | 44% | 1,148 |
| BUY (hedge, first) | 23000 CE | 68.62 | 68.55/68.70 | 12.6% | +0.23 | 78% | 43% | 33,053 |
| SELL | 22900 CE | 93.90 | 93.75/94.05 | 12.6% | +0.29 | 72% | 54% | 10,212 |
* ❌ credit/width PE 14.5/100 = 0.14, CE 25.3/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹222 = 8.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22150PE is at/inside the 22000 wall (16,564 OI); short 22900CE is at/inside the 23000 wall (33,053 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 39.75 pts = ₹2,584/lot · max loss ₹4,034/lot · margin ~₹14,663/lot · net at 50% target ₹1,070/lot
* Exits: **take profit** when spread ≤ 19.88 · **stop** when spread ≥ 119.25 (loss = 2× credit) · **time exit** Mon 12 Oct 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
