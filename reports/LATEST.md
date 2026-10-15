# NIFTY trade card: Thu 15 Oct 2026, 11:08 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,927.35 | Yahoo |
| India VIX | 14.64 | Yahoo |
| Expiry | Tue 27 Oct 2026 (12.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 13.2% | chain |
| 1-SD expected move | ±554 → 22,373 – 23,482 | |

## Regime
* IV percentile (1y): **71**
* Trend: **RANGE**  (20-DMA 22,844, 50-DMA 23,577)
* 20-day realised vol 15.5% vs implied 13.2% → premium -2.3 vol pts
* VIX flat/mixed (5-day high 15.28)
* Today's opening gap: +0.21%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23500 (150,002) · PE 22000 (85,438)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22350 PE | 59.50 | 59.35/59.65 | 15.9% | -0.17 | 83% | 36% | 7,329 |
| SELL | 22450 PE | 73.42 | 73.25/73.60 | 15.4% | -0.20 | 79% | 43% | 4,508 |
| BUY (hedge, first) | 23500 CE | 41.25 | 41.20/41.30 | 12.1% | +0.16 | 85% | 29% | 150,002 |
| SELL | 23400 CE | 59.00 | 58.90/59.10 | 12.1% | +0.21 | 80% | 39% | 36,281 |
* ❌ credit/width PE 13.9/100 = 0.14, CE 17.8/100 = 0.18 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹216 = 10.5% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22450PE is at/inside the 22000 wall (85,438 OI); short 23400CE is at/inside the 23500 wall (150,002 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 31.67 pts = ₹2,059/lot · max loss ₹4,555/lot · margin ~₹14,903/lot · net at 50% target ₹813/lot
* Exits: **take profit** when spread ≤ 15.84 · **stop** when spread ≥ 95.02 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23400 CE | 59.00 | 58.90/59.10 | 12.1% | +0.21 | 80% | 39% | 36,281 |
| SELL | 23300 CE | 82.83 | 82.65/83.00 | 12.2% | +0.27 | 74% | 50% | 52,196 |
* ❌ credit/width CE 23.8/100 = 0.24 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹111 = 7.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23300CE is at/inside the 23500 wall (150,002 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 23.83 pts = ₹1,549/lot · max loss ₹5,011/lot · margin ~₹14,903/lot · net at 50% target ₹663/lot
* Exits: **take profit** when spread ≤ 11.91 · **stop** when spread ≥ 71.48 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22500 PE | 82.20 | 82.00/82.40 | 15.2% | -0.22 | 77% | 48% | 80,982 |
| SELL | 22600 PE | 102.08 | 101.90/102.25 | 14.8% | -0.27 | 72% | 57% | 42,468 |
* ❌ credit/width PE 19.9/100 = 0.20 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹116 = 9.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22600PE is at/inside the 22000 wall (85,438 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 19.88 pts = ₹1,292/lot · max loss ₹5,270/lot · margin ~₹14,903/lot · net at 50% target ₹530/lot
* Exits: **take profit** when spread ≤ 9.94 · **stop** when spread ≥ 59.62 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
