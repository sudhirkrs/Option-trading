# NIFTY trade card: Mon 09 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 24,924.00 | Yahoo |
| India VIX | 17.54 | Yahoo |
| Expiry | Tue 17 Nov 2026 (8.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 17.4% | chain |
| 1-SD expected move | ±652 → 24,272 – 25,576 | |

## Regime
* IV percentile (1y): **81**
* Trend: **RANGE**  (20-DMA 23,237, 50-DMA 23,262)
* 20-day realised vol 16.5% vs implied 17.4% → premium +0.9 vol pts
* VIX RISING (5-day high 17.47)
* Today's opening gap: +0.18%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (78,640) · PE 24000 (52,067)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24450 PE | 94.68 | 94.40/94.95 | 18.8% | -0.23 | 76% | 48% | 5,810 |
| SELL | 24550 PE | 120.50 | 120.30/120.70 | 18.8% | -0.27 | 72% | 58% | 8,250 |
| BUY (hedge, first) | 25600 CE | 58.88 | 58.80/58.95 | 17.5% | +0.17 | 84% | 32% | 21,064 |
| SELL | 25500 CE | 74.75 | 74.65/74.85 | 17.2% | +0.21 | 80% | 39% | 60,869 |
* ❌ credit/width PE 25.8/100 = 0.26, CE 15.9/100 = 0.16 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹230 = 8.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24550PE is inside by 550 pts (tolerance 100), too far inside the 24000 wall (52,067 OI); short 25500CE is inside by 500 pts (tolerance 100), too far inside the 26000 wall (78,640 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 41.70 pts = ₹2,710/lot · max loss ₹3,913/lot · margin ~₹16,201/lot · net at 50% target ₹1,125/lot
* Exits: **take profit** when spread ≤ 20.85 · **stop** when spread ≥ 125.10 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25450 CE | 83.58 | 83.40/83.75 | 17.1% | +0.23 | 78% | 43% | 2,910 |
| SELL | 25350 CE | 105.10 | 105.00/105.20 | 16.9% | +0.27 | 73% | 52% | 3,518 |
* ❌ credit/width CE 21.5/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹117 = 8.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25350CE is inside by 650 pts (tolerance 100), too far inside the 26000 wall (78,640 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.52 pts = ₹1,399/lot · max loss ₹5,164/lot · margin ~₹16,201/lot · net at 50% target ₹583/lot
* Exits: **take profit** when spread ≤ 10.76 · **stop** when spread ≥ 64.57 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24450 PE | 94.68 | 94.40/94.95 | 18.8% | -0.23 | 76% | 48% | 5,810 |
| SELL | 24550 PE | 120.50 | 120.30/120.70 | 18.8% | -0.27 | 72% | 58% | 8,250 |
* ✅ credit/width PE 25.8/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹120 = 7.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24550PE is inside by 550 pts (tolerance 100), too far inside the 24000 wall (52,067 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.82 pts = ₹1,679/lot · max loss ₹4,886/lot · margin ~₹16,201/lot · net at 50% target ₹720/lot
* Exits: **take profit** when spread ≤ 12.91 · **stop** when spread ≥ 77.47 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
