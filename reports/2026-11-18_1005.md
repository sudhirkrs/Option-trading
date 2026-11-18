# NIFTY trade card: Wed 18 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,303.20 | Yahoo |
| India VIX | 15.74 | Yahoo |
| Expiry | Mon 23 Nov 2026 (5.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 14.7% | chain |
| 1-SD expected move | ±444 → 24,859 – 25,747 | |

## Regime
* IV percentile (1y): **71**
* Trend: **UP**  (20-DMA 23,990, 50-DMA 23,415)
* 20-day realised vol 13.9% vs implied 14.7% → premium +0.8 vol pts
* VIX flat/mixed (5-day high 17.56)
* Today's opening gap: -0.25%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (247,625) · PE 25000 (185,230)

## Verdict
**NO TRADE today.**
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24950 PE | 55.42 | 55.40/55.45 | 15.5% | -0.21 | 79% | 44% | 21,502 |
| SELL | 25050 PE | 79.10 | 79.00/79.20 | 15.4% | -0.27 | 72% | 57% | 25,745 |
* ❌ credit/width PE 23.7/100 = 0.24 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹110 = 7.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25050PE is inside by 50 pts (tolerance 100) the 25000 wall (185,230 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 23.67 pts = ₹1,539/lot · max loss ₹5,020/lot · margin ~₹16,447/lot · net at 50% target ₹659/lot
* Exits: **take profit** when spread ≤ 11.84 · **stop** when spread ≥ 71.02 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25700 CE | 48.17 | 48.10/48.25 | 14.4% | +0.20 | 80% | 38% | 75,765 |
| SELL | 25600 CE | 68.67 | 68.60/68.75 | 14.1% | +0.27 | 74% | 51% | 77,056 |
* ❌ credit/width CE 20.5/100 = 0.20 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹108 = 8.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25600CE is inside by 400 pts (tolerance 100), too far inside the 26000 wall (247,625 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 20.50 pts = ₹1,332/lot · max loss ₹5,225/lot · margin ~₹16,447/lot · net at 50% target ₹558/lot
* Exits: **take profit** when spread ≤ 10.25 · **stop** when spread ≥ 61.50 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24850 PE | 38.67 | 38.60/38.75 | 15.7% | -0.15 | 84% | 32% | 19,885 |
| SELL | 24950 PE | 55.42 | 55.40/55.45 | 15.5% | -0.21 | 79% | 44% | 21,502 |
| BUY (hedge, first) | 25800 CE | 33.00 | 32.95/33.05 | 14.6% | +0.15 | 86% | 28% | 65,294 |
| SELL | 25700 CE | 48.17 | 48.10/48.25 | 14.4% | +0.20 | 80% | 38% | 75,765 |
* ❌ credit/width PE 16.8/100 = 0.17, CE 15.2/100 = 0.15 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹210 = 10.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24950PE is beyond the 25000 wall (185,230 OI); short 25700CE is inside by 300 pts (tolerance 100), too far inside the 26000 wall (247,625 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 31.92 pts = ₹2,075/lot · max loss ₹4,534/lot · margin ~₹16,447/lot · net at 50% target ₹828/lot
* Exits: **take profit** when spread ≤ 15.96 · **stop** when spread ≥ 95.77 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
