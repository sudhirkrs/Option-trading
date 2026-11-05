# NIFTY trade card: Thu 05 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 24,399.25 | Yahoo |
| India VIX | 15.22 | Yahoo |
| Expiry | Tue 17 Nov 2026 (12.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 13.0% | chain |
| 1-SD expected move | ±581 → 23,818 – 24,981 | |

## Regime
* IV percentile (1y): **69**
* Trend: **RANGE**  (20-DMA 22,970, 50-DMA 23,231)
* 20-day realised vol 16.5% vs implied 13.0% → premium -3.5 vol pts
* VIX flat/mixed (5-day high 15.72)
* Today's opening gap: +1.74%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 24500 (26,010) · PE 23500 (15,644)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23800 PE | 66.42 | 66.30/66.55 | 15.9% | -0.17 | 82% | 37% | 14,880 |
| SELL | 23900 PE | 81.65 | 81.50/81.80 | 15.5% | -0.21 | 79% | 45% | 6,161 |
| BUY (hedge, first) | 25000 CE | 40.12 | 40.05/40.20 | 11.6% | +0.15 | 85% | 28% | 24,977 |
| SELL | 24900 CE | 55.20 | 55.10/55.30 | 11.5% | +0.20 | 81% | 36% | 25,495 |
* ❌ credit/width PE 15.2/100 = 0.15, CE 15.1/100 = 0.15 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹218 = 11.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23900PE is inside by 400 pts (tolerance 100), too far inside the 23500 wall (15,644 OI); short 24900CE is beyond the 24500 wall (26,010 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 30.30 pts = ₹1,970/lot · max loss ₹4,645/lot · margin ~₹15,860/lot · net at 50% target ₹767/lot
* Exits: **take profit** when spread ≤ 15.15 · **stop** when spread ≥ 90.90 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24900 CE | 55.20 | 55.10/55.30 | 11.5% | +0.20 | 81% | 36% | 25,495 |
| SELL | 24800 CE | 77.12 | 76.95/77.30 | 11.5% | +0.25 | 75% | 47% | 6,122 |
* ❌ credit/width CE 21.9/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹110 = 7.7% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 24800CE is beyond the 24500 wall (26,010 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.92 pts = ₹1,425/lot · max loss ₹5,133/lot · margin ~₹15,860/lot · net at 50% target ₹602/lot
* Exits: **take profit** when spread ≤ 10.96 · **stop** when spread ≥ 65.77 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23950 PE | 90.53 | 90.35/90.70 | 15.3% | -0.23 | 77% | 49% | 1,169 |
| SELL | 24050 PE | 112.08 | 111.90/112.25 | 15.1% | -0.27 | 72% | 58% | 709 |
* ❌ credit/width PE 21.5/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹118 = 8.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24050PE is inside by 550 pts (tolerance 100), too far inside the 23500 wall (15,644 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.55 pts = ₹1,401/lot · max loss ₹5,163/lot · margin ~₹15,860/lot · net at 50% target ₹582/lot
* Exits: **take profit** when spread ≤ 10.77 · **stop** when spread ≥ 64.65 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
