# NIFTY trade card: Mon 02 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 23,299.70 | Yahoo |
| India VIX | 15.67 | Yahoo |
| Expiry | Mon 09 Nov 2026 (7.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.2% | chain |
| 1-SD expected move | ±497 → 22,802 – 23,797 | |

## Regime
* IV percentile (1y): **72**
* Trend: **RANGE**  (20-DMA 22,751, 50-DMA 23,239)
* 20-day realised vol 14.9% vs implied 15.2% → premium +0.3 vol pts
* VIX flat/mixed (5-day high 17.16)
* Today's opening gap: +0.73%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 24000 (39,052) · PE 23000 (38,416)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22800 PE | 53.00 | 52.90/53.10 | 17.4% | -0.17 | 82% | 36% | 23,011 |
| SELL | 22900 PE | 68.08 | 67.95/68.20 | 16.9% | -0.21 | 78% | 45% | 28,862 |
| BUY (hedge, first) | 23700 CE | 55.28 | 55.20/55.35 | 14.0% | +0.21 | 79% | 40% | 36,160 |
| SELL | 23600 CE | 81.35 | 81.20/81.50 | 14.1% | +0.28 | 72% | 54% | 19,006 |
* ❌ credit/width PE 15.1/100 = 0.15, CE 26.1/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹219 = 8.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22900PE is beyond the 23000 wall (38,416 OI); short 23600CE is at/inside the 24000 wall (39,052 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 41.15 pts = ₹2,675/lot · max loss ₹3,941/lot · margin ~₹15,145/lot · net at 50% target ₹1,118/lot
* Exits: **take profit** when spread ≤ 20.57 · **stop** when spread ≥ 123.45 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23700 CE | 55.28 | 55.20/55.35 | 14.0% | +0.21 | 79% | 40% | 36,160 |
| SELL | 23600 CE | 81.35 | 81.20/81.50 | 14.1% | +0.28 | 72% | 54% | 19,006 |
* ✅ credit/width CE 26.1/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹111 = 6.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23600CE is at/inside the 24000 wall (39,052 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 26.07 pts = ₹1,695/lot · max loss ₹4,864/lot · margin ~₹15,145/lot · net at 50% target ₹737/lot
* Exits: **take profit** when spread ≤ 13.04 · **stop** when spread ≥ 78.22 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22900 PE | 68.08 | 67.95/68.20 | 16.9% | -0.21 | 78% | 45% | 28,862 |
| SELL | 23000 PE | 88.30 | 88.15/88.45 | 16.5% | -0.27 | 73% | 56% | 38,416 |
* ❌ credit/width PE 20.2/100 = 0.20 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹113 = 8.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23000PE is at/inside the 23000 wall (38,416 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 20.23 pts = ₹1,315/lot · max loss ₹5,246/lot · margin ~₹15,145/lot · net at 50% target ₹544/lot
* Exits: **take profit** when spread ≤ 10.11 · **stop** when spread ≥ 60.68 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
