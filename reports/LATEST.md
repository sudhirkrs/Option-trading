# NIFTY trade card: Mon 23 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,636.50 | Yahoo |
| India VIX | 17.99 | Yahoo |
| Expiry | Tue 01 Dec 2026 (8.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 17.7% | chain |
| 1-SD expected move | ±680 → 24,956 – 26,317 | |

## Regime
* IV percentile (1y): **82**
* Trend: **UP**  (20-DMA 24,429, 50-DMA 23,526)
* 20-day realised vol 13.8% vs implied 17.7% → premium +3.9 vol pts
* VIX RISING (5-day high 17.32)
* Today's opening gap: +0.50%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (98,529) · PE 25000 (43,071)

## Verdict
**NO TRADE today.**
* uptrend but VIX rising: no put selling
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25150 PE | 91.68 | 91.45/91.90 | 18.3% | -0.22 | 77% | 47% | 4,252 |
| SELL | 25250 PE | 117.50 | 117.15/117.85 | 18.4% | -0.27 | 72% | 57% | 4,800 |
* ✅ credit/width PE 25.8/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹119 = 7.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25250PE is inside by 250 pts (tolerance 100), too far inside the 25000 wall (43,071 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.82 pts = ₹1,679/lot · max loss ₹4,886/lot · margin ~₹16,664/lot · net at 50% target ₹720/lot
* Exits: **take profit** when spread ≤ 12.91 · **stop** when spread ≥ 77.47 (loss = 2× credit) · **time exit** Mon 30 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 26200 CE | 85.22 | 85.00/85.45 | 17.4% | +0.22 | 78% | 42% | 37,936 |
| SELL | 26100 CE | 107.88 | 107.50/108.25 | 17.4% | +0.27 | 74% | 51% | 21,118 |
* ❌ credit/width CE 22.7/100 = 0.23 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹117 = 8.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 26100CE is beyond the 26000 wall (98,529 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.65 pts = ₹1,472/lot · max loss ₹5,091/lot · margin ~₹16,664/lot · net at 50% target ₹619/lot
* Exits: **take profit** when spread ≤ 11.33 · **stop** when spread ≥ 67.95 (loss = 2× credit) · **time exit** Mon 30 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25150 PE | 91.68 | 91.45/91.90 | 18.3% | -0.22 | 77% | 47% | 4,252 |
| SELL | 25250 PE | 117.50 | 117.15/117.85 | 18.4% | -0.27 | 72% | 57% | 4,800 |
| BUY (hedge, first) | 26350 CE | 60.38 | 60.30/60.45 | 17.7% | +0.17 | 84% | 32% | 5,196 |
| SELL | 26250 CE | 77.03 | 76.95/77.10 | 17.6% | +0.20 | 80% | 39% | 7,721 |
* ❌ credit/width PE 25.8/100 = 0.26, CE 16.7/100 = 0.17 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹230 = 8.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25250PE is inside by 250 pts (tolerance 100), too far inside the 25000 wall (43,071 OI); short 26250CE is beyond the 26000 wall (98,529 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 42.47 pts = ₹2,761/lot · max loss ₹3,862/lot · margin ~₹16,664/lot · net at 50% target ₹1,151/lot
* Exits: **take profit** when spread ≤ 21.24 · **stop** when spread ≥ 127.42 (loss = 2× credit) · **time exit** Mon 30 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
