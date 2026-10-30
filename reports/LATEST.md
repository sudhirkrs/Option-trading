# NIFTY trade card: Fri 30 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,961.60 | Yahoo |
| India VIX | 15.63 | Yahoo |
| Expiry | Mon 09 Nov 2026 (10.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.0% | chain |
| 1-SD expected move | ±576 → 22,386 – 23,537 | |

## Regime
* IV percentile (1y): **72**
* Trend: **RANGE**  (20-DMA 22,702, 50-DMA 23,253)
* 20-day realised vol 14.9% vs implied 15.0% → premium +0.1 vol pts
* VIX calming (5-day high 17.16)
* Today's opening gap: +0.12%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 24000 (26,214) · PE 22000 (31,530)

## Verdict
**NO TRADE today.**
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22400 PE | 61.50 | 61.40/61.60 | 17.1% | -0.17 | 82% | 37% | 9,672 |
| SELL | 22500 PE | 79.20 | 79.05/79.35 | 16.9% | -0.21 | 78% | 45% | 27,205 |
| BUY (hedge, first) | 23400 CE | 66.60 | 66.50/66.70 | 13.4% | +0.23 | 78% | 42% | 7,874 |
| SELL | 23300 CE | 92.92 | 92.75/93.10 | 13.5% | +0.29 | 72% | 54% | 8,458 |
* ❌ credit/width PE 17.7/100 = 0.18, CE 26.3/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹224 = 7.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22500PE is at/inside the 22000 wall (31,530 OI); short 23300CE is at/inside the 24000 wall (26,214 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 44.02 pts = ₹2,862/lot · max loss ₹3,758/lot · margin ~₹14,925/lot · net at 50% target ₹1,206/lot
* Exits: **take profit** when spread ≤ 22.01 · **stop** when spread ≥ 132.07 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23400 CE | 66.60 | 66.50/66.70 | 13.4% | +0.23 | 78% | 42% | 7,874 |
| SELL | 23300 CE | 92.92 | 92.75/93.10 | 13.5% | +0.29 | 72% | 54% | 8,458 |
* ✅ credit/width CE 26.3/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹113 = 6.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23300CE is at/inside the 24000 wall (26,214 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 26.33 pts = ₹1,711/lot · max loss ₹4,850/lot · margin ~₹14,925/lot · net at 50% target ₹742/lot
* Exits: **take profit** when spread ≤ 13.16 · **stop** when spread ≥ 78.98 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22500 PE | 79.20 | 79.05/79.35 | 16.9% | -0.21 | 78% | 45% | 27,205 |
| SELL | 22600 PE | 100.40 | 100.20/100.60 | 16.6% | -0.26 | 73% | 55% | 10,252 |
* ❌ credit/width PE 21.2/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹116 = 8.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22600PE is at/inside the 22000 wall (31,530 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.20 pts = ₹1,378/lot · max loss ₹5,184/lot · margin ~₹14,925/lot · net at 50% target ₹573/lot
* Exits: **take profit** when spread ≤ 10.60 · **stop** when spread ≥ 63.60 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
