# NIFTY trade card: Wed 04 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 23,927.65 | Yahoo |
| India VIX | 15.98 | Yahoo |
| Expiry | Mon 09 Nov 2026 (5.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 16.4% | chain |
| 1-SD expected move | ±471 → 23,457 – 24,398 | |

## Regime
* IV percentile (1y): **74**
* Trend: **RANGE**  (20-DMA 22,878, 50-DMA 23,227)
* 20-day realised vol 16.0% vs implied 16.4% → premium +0.4 vol pts
* VIX flat/mixed (5-day high 16.25)
* Today's opening gap: -0.29%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 24000 (151,223) · PE 23500 (113,802)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23400 PE | 42.92 | 42.85/43.00 | 19.0% | -0.15 | 84% | 32% | 79,170 |
| SELL | 23500 PE | 58.88 | 58.85/58.90 | 18.7% | -0.20 | 80% | 41% | 113,802 |
| BUY (hedge, first) | 24400 CE | 39.40 | 39.35/39.45 | 15.8% | +0.17 | 84% | 31% | 75,215 |
| SELL | 24300 CE | 53.72 | 53.65/53.80 | 15.3% | +0.22 | 79% | 41% | 79,703 |
* ❌ credit/width PE 16.0/100 = 0.16, CE 14.3/100 = 0.14 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹212 = 10.8% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 23500PE is inside by 0 pts (tolerance 100) the 23500 wall (113,802 OI); short 24300CE is beyond the 24000 wall (151,223 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 30.27 pts = ₹1,968/lot · max loss ₹4,643/lot · margin ~₹15,553/lot · net at 50% target ₹772/lot
* Exits: **take profit** when spread ≤ 15.14 · **stop** when spread ≥ 90.82 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24350 CE | 45.88 | 45.80/45.95 | 15.5% | +0.19 | 82% | 36% | 23,031 |
| SELL | 24250 CE | 62.62 | 62.55/62.70 | 15.0% | +0.25 | 76% | 47% | 30,193 |
* ❌ credit/width CE 16.8/100 = 0.17 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹107 = 9.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 24250CE is beyond the 24000 wall (151,223 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 16.75 pts = ₹1,089/lot · max loss ₹5,468/lot · margin ~₹15,553/lot · net at 50% target ₹437/lot
* Exits: **take profit** when spread ≤ 8.38 · **stop** when spread ≥ 50.25 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23500 PE | 58.88 | 58.85/58.90 | 18.7% | -0.20 | 80% | 41% | 113,802 |
| SELL | 23600 PE | 80.12 | 80.00/80.25 | 18.5% | -0.25 | 74% | 52% | 111,218 |
* ❌ credit/width PE 21.2/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹111 = 8.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 23600PE is inside by 100 pts (tolerance 100) the 23500 wall (113,802 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.25 pts = ₹1,381/lot · max loss ₹5,178/lot · margin ~₹15,553/lot · net at 50% target ₹580/lot
* Exits: **take profit** when spread ≤ 10.62 · **stop** when spread ≥ 63.75 (loss = 2× credit) · **time exit** Fri 06 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
