# NIFTY trade card: Thu 22 Oct 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 22,589.55 | Yahoo |
| India VIX | 16.29 | Yahoo |
| Expiry | Tue 27 Oct 2026 (5.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.5% | chain |
| 1-SD expected move | ±420 → 22,169 – 23,010 | |

## Regime
* IV percentile (1y): **77**
* Trend: **DOWN**  (20-DMA 22,751, 50-DMA 23,439)
* 20-day realised vol 16.7% vs implied 15.5% → premium -1.1 vol pts
* VIX RISING (5-day high 15.68)
* Today's opening gap: -0.54%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 23000 (265,142) · PE 22500 (165,561)

## Verdict
**NO TRADE today.**
* BEAR CALL SPREAD failed a gate (see ❌ below)

### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 23000 CE | 44.53 | 44.45/44.60 | 16.0% | +0.19 | 82% | 36% | 265,142 |
| SELL | 22900 CE | 63.08 | 63.00/63.15 | 15.7% | +0.25 | 75% | 48% | 117,658 |
* ❌ credit/width CE 18.5/100 = 0.19 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹107 = 8.9% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22900CE is at/inside the 23000 wall (265,142 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 18.55 pts = ₹1,206/lot · max loss ₹5,351/lot · margin ~₹14,683/lot · net at 50% target ₹496/lot
* Exits: **take profit** when spread ≤ 9.27 · **stop** when spread ≥ 55.65 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22250 PE | 52.25 | 52.15/52.35 | 16.6% | -0.21 | 79% | 43% | 39,172 |
| SELL | 22350 PE | 73.25 | 73.15/73.35 | 16.2% | -0.27 | 72% | 57% | 29,720 |
* ❌ credit/width PE 21.0/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹109 = 8.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 22350PE is beyond the 22500 wall (165,561 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.00 pts = ₹1,365/lot · max loss ₹5,193/lot · margin ~₹14,683/lot · net at 50% target ₹573/lot
* Exits: **take profit** when spread ≤ 10.50 · **stop** when spread ≥ 63.00 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 22150 PE | 37.38 | 37.30/37.45 | 17.1% | -0.15 | 84% | 32% | 38,114 |
| SELL | 22250 PE | 52.25 | 52.15/52.35 | 16.6% | -0.21 | 79% | 43% | 39,172 |
| BUY (hedge, first) | 23050 CE | 37.15 | 37.10/37.20 | 16.2% | +0.16 | 84% | 31% | 71,041 |
| SELL | 22950 CE | 52.75 | 52.65/52.85 | 15.8% | +0.22 | 79% | 42% | 58,112 |
* ❌ credit/width PE 14.9/100 = 0.15, CE 15.6/100 = 0.16 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹210 = 10.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 22250PE is beyond the 22500 wall (165,561 OI); short 22950CE is at/inside the 23000 wall (265,142 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 30.47 pts = ₹1,981/lot · max loss ₹4,629/lot · margin ~₹14,683/lot · net at 50% target ₹780/lot
* Exits: **take profit** when spread ≤ 15.24 · **stop** when spread ≥ 91.42 (loss = 2× credit) · **time exit** Mon 26 Oct 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
