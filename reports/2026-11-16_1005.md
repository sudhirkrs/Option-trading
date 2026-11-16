# NIFTY trade card: Mon 16 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,299.80 | Yahoo |
| India VIX | 15.65 | Yahoo |
| Expiry | Mon 23 Nov 2026 (7.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.1% | chain |
| 1-SD expected move | ±539 → 24,761 – 25,838 | |

## Regime
* IV percentile (1y): **70**
* Trend: **UP**  (20-DMA 23,757, 50-DMA 23,357)
* 20-day realised vol 14.8% vs implied 15.1% → premium +0.4 vol pts
* VIX calming (5-day high 17.56)
* Today's opening gap: +0.25%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (135,229) · PE 25000 (116,646)

## Verdict
**TRADE: BULL PUT SPREAD, 1 lot(s)** (prices are live)
Order: buy the hedge leg first, then sell the short leg, both as limit orders at mid.

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24950 PE | 81.00 | 80.90/81.10 | 15.7% | -0.24 | 75% | 51% | 4,585 |
| SELL | 25050 PE | 106.28 | 106.10/106.45 | 15.5% | -0.30 | 69% | 64% | 3,062 |
* ✅ credit/width PE 25.3/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹117 = 7.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25050PE is inside by 50 pts (tolerance 100) the 25000 wall (116,646 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.28 pts = ₹1,643/lot · max loss ₹4,920/lot · margin ~₹16,445/lot · net at 50% target ₹705/lot
* Exits: **take profit** when spread ≤ 12.64 · **stop** when spread ≥ 75.83 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25800 CE | 58.83 | 58.70/58.95 | 15.1% | +0.20 | 81% | 37% | 20,302 |
| SELL | 25700 CE | 80.00 | 79.85/80.15 | 15.1% | +0.25 | 75% | 48% | 29,593 |
* ❌ credit/width CE 21.2/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹111 = 8.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25700CE is inside by 300 pts (tolerance 100), too far inside the 26000 wall (135,229 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.17 pts = ₹1,376/lot · max loss ₹5,182/lot · margin ~₹16,445/lot · net at 50% target ₹577/lot
* Exits: **take profit** when spread ≤ 10.59 · **stop** when spread ≥ 63.52 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24950 PE | 81.00 | 80.90/81.10 | 15.7% | -0.24 | 75% | 51% | 4,585 |
| SELL | 25050 PE | 106.28 | 106.10/106.45 | 15.5% | -0.30 | 69% | 64% | 3,062 |
| BUY (hedge, first) | 25900 CE | 43.20 | 43.10/43.30 | 15.3% | +0.15 | 85% | 29% | 12,698 |
| SELL | 25800 CE | 58.83 | 58.70/58.95 | 15.1% | +0.20 | 81% | 37% | 20,302 |
* ❌ credit/width PE 25.3/100 = 0.25, CE 15.6/100 = 0.16 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹223 = 8.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25050PE is inside by 50 pts (tolerance 100) the 25000 wall (116,646 OI); short 25800CE is inside by 200 pts (tolerance 100), too far inside the 26000 wall (135,229 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 40.90 pts = ₹2,659/lot · max loss ₹3,960/lot · margin ~₹16,445/lot · net at 50% target ₹1,106/lot
* Exits: **take profit** when spread ≤ 20.45 · **stop** when spread ≥ 122.70 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
