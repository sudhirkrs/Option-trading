# NIFTY trade card: Wed 21 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,986.75 | Yahoo |
| India VIX | 14.91 | Yahoo |
| Expiry | Tue 27 Oct 2026 (6.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 14.0% | chain |
| 1-SD expected move | ±422 → 22,565 – 23,408 | |

## Regime
* IV percentile (1y): **72**
* Trend: **RANGE**  (20-DMA 22,797, 50-DMA 23,483)
* 20-day realised vol 16.5% vs implied 14.0% → premium -2.5 vol pts
* VIX RISING (5-day high 14.77)
* Today's opening gap: +0.56%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23500 (231,942) · PE 22500 (141,829)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22550 PE | 36.48 | 36.45/36.50 | 15.3% | -0.15 | 84% | 32% | 25,046 |
| SELL | 22650 PE | 51.55 | 51.50/51.60 | 14.9% | -0.20 | 79% | 43% | 24,534 |
| BUY (hedge, first) | 23450 CE | 32.35 | 32.30/32.40 | 13.9% | +0.15 | 85% | 29% | 38,702 |
| SELL | 23350 CE | 49.45 | 49.40/49.50 | 13.8% | +0.21 | 79% | 40% | 36,076 |
* ❌ credit/width PE 15.1/100 = 0.15, CE 17.1/100 = 0.17 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹209 = 10.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22650PE is at/inside the 22500 wall (141,829 OI); short 23350CE is at/inside the 23500 wall (231,942 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 32.18 pts = ₹2,091/lot · max loss ₹4,518/lot · margin ~₹14,941/lot · net at 50% target ₹837/lot
* Exits: **take profit** when spread ≤ 16.09 · **stop** when spread ≥ 96.53 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23400 CE | 40.12 | 40.05/40.20 | 13.8% | +0.18 | 82% | 34% | 88,369 |
| SELL | 23300 CE | 60.80 | 60.70/60.90 | 13.8% | +0.25 | 76% | 47% | 112,258 |
* ❌ credit/width CE 20.7/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹106 = 7.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23300CE is at/inside the 23500 wall (231,942 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 20.67 pts = ₹1,344/lot · max loss ₹5,212/lot · margin ~₹14,941/lot · net at 50% target ₹565/lot
* Exits: **take profit** when spread ≤ 10.34 · **stop** when spread ≥ 62.02 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22650 PE | 51.55 | 51.50/51.60 | 14.9% | -0.20 | 79% | 43% | 24,534 |
| SELL | 22750 PE | 73.00 | 72.90/73.10 | 14.6% | -0.27 | 72% | 57% | 32,925 |
* ❌ credit/width PE 21.5/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹109 = 7.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22750PE is at/inside the 22500 wall (141,829 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.45 pts = ₹1,394/lot · max loss ₹5,164/lot · margin ~₹14,941/lot · net at 50% target ₹588/lot
* Exits: **take profit** when spread ≤ 10.73 · **stop** when spread ≥ 64.35 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
