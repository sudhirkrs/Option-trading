# NIFTY trade card: Thu 29 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,757.50 | Yahoo |
| India VIX | 15.92 | Yahoo |
| Expiry | Tue 03 Nov 2026 (5.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 14.5% | chain |
| 1-SD expected move | ±394 → 22,364 – 23,151 | |

## Regime
* IV percentile (1y): **74**
* Trend: **RANGE**  (20-DMA 22,676, 50-DMA 23,273)
* 20-day realised vol 14.6% vs implied 14.5% → premium -0.1 vol pts
* VIX calming (5-day high 17.16)
* Today's opening gap: -0.04%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23000 (149,276) · PE 22700 (142,621)

## Verdict
**NO TRADE today.**
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22300 PE | 32.08 | 32.00/32.15 | 16.5% | -0.14 | 86% | 29% | 80,242 |
| SELL | 22400 PE | 46.42 | 46.35/46.50 | 16.1% | -0.19 | 80% | 40% | 70,961 |
| BUY (hedge, first) | 23200 CE | 21.42 | 21.40/21.45 | 13.1% | +0.12 | 88% | 23% | 86,894 |
| SELL | 23100 CE | 36.80 | 36.75/36.85 | 13.1% | +0.19 | 82% | 36% | 71,478 |
* ❌ credit/width PE 14.3/100 = 0.14, CE 15.4/100 = 0.15 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹205 = 10.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 22400PE is beyond the 22700 wall (142,621 OI); short 23100CE is beyond the 23000 wall (149,276 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 29.72 pts = ₹1,932/lot · max loss ₹4,674/lot · margin ~₹14,792/lot · net at 50% target ₹761/lot
* Exits: **take profit** when spread ≤ 14.86 · **stop** when spread ≥ 89.17 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23100 CE | 36.80 | 36.75/36.85 | 13.1% | +0.19 | 82% | 36% | 71,478 |
| SELL | 23000 CE | 60.12 | 60.05/60.20 | 13.2% | +0.27 | 73% | 52% | 149,276 |
* ❌ credit/width CE 23.3/100 = 0.23 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹106 = 7.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 23000CE is at/inside the 23000 wall (149,276 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 23.33 pts = ₹1,516/lot · max loss ₹5,040/lot · margin ~₹14,792/lot · net at 50% target ₹652/lot
* Exits: **take profit** when spread ≤ 11.66 · **stop** when spread ≥ 69.98 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22400 PE | 46.42 | 46.35/46.50 | 16.1% | -0.19 | 80% | 40% | 70,961 |
| SELL | 22500 PE | 67.03 | 66.95/67.10 | 15.9% | -0.26 | 74% | 54% | 112,246 |
* ❌ credit/width PE 20.6/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹108 = 8.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 22500PE is beyond the 22700 wall (142,621 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 20.60 pts = ₹1,339/lot · max loss ₹5,218/lot · margin ~₹14,792/lot · net at 50% target ₹562/lot
* Exits: **take profit** when spread ≤ 10.30 · **stop** when spread ≥ 61.80 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
