# NIFTY trade card: Tue 27 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,790.20 | Yahoo |
| India VIX | 16.90 | Yahoo |
| Expiry | Tue 03 Nov 2026 (7.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 16.9% | chain |
| 1-SD expected move | ±543 → 22,247 – 23,333 | |

## Regime
* IV percentile (1y): **78**
* Trend: **RANGE**  (20-DMA 22,680, 50-DMA 23,338)
* 20-day realised vol 15.6% vs implied 16.9% → premium +1.3 vol pts
* VIX RISING (5-day high 17.16)
* Today's opening gap: -0.20%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23000 (67,096) · PE 22000 (41,723)

## Verdict
**NO TRADE today.**
* range-bound but VIX not calming: condor waits
* IRON CONDOR failed a gate (see ❌ below)

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22250 PE | 50.77 | 50.65/50.90 | 18.4% | -0.16 | 83% | 34% | 7,909 |
| SELL | 22350 PE | 65.92 | 65.80/66.05 | 18.0% | -0.20 | 79% | 43% | 5,485 |
| BUY (hedge, first) | 23250 CE | 61.50 | 61.35/61.65 | 16.3% | +0.21 | 80% | 40% | 6,862 |
| SELL | 23150 CE | 87.10 | 86.95/87.25 | 16.5% | +0.27 | 74% | 51% | 7,137 |
* ❌ credit/width PE 15.1/100 = 0.15, CE 25.6/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹220 = 8.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22350PE is at/inside the 22000 wall (41,723 OI); short 23150CE is beyond the 23000 wall (67,096 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 40.75 pts = ₹2,649/lot · max loss ₹3,968/lot · margin ~₹14,814/lot · net at 50% target ₹1,104/lot
* Exits: **take profit** when spread ≤ 20.37 · **stop** when spread ≥ 122.25 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23250 CE | 61.50 | 61.35/61.65 | 16.3% | +0.21 | 80% | 40% | 6,862 |
| SELL | 23150 CE | 87.10 | 86.95/87.25 | 16.5% | +0.27 | 74% | 51% | 7,137 |
* ✅ credit/width CE 25.6/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 6.7% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 23150CE is beyond the 23000 wall (67,096 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.60 pts = ₹1,664/lot · max loss ₹4,896/lot · margin ~₹14,814/lot · net at 50% target ₹720/lot
* Exits: **take profit** when spread ≤ 12.80 · **stop** when spread ≥ 76.80 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22400 PE | 74.92 | 74.80/75.05 | 17.8% | -0.23 | 77% | 48% | 23,814 |
| SELL | 22500 PE | 97.17 | 97.05/97.30 | 17.4% | -0.28 | 71% | 59% | 36,190 |
* ❌ credit/width PE 22.2/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹115 = 7.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22500PE is at/inside the 22000 wall (41,723 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.25 pts = ₹1,446/lot · max loss ₹5,115/lot · margin ~₹14,814/lot · net at 50% target ₹608/lot
* Exits: **take profit** when spread ≤ 11.12 · **stop** when spread ≥ 66.75 (loss = 2× credit) · **time exit** Mon 02 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
