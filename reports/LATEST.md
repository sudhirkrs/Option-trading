# NIFTY trade card: Tue 17 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,367.35 | Yahoo |
| India VIX | 15.06 | Yahoo |
| Expiry | Mon 23 Nov 2026 (6.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 14.0% | chain |
| 1-SD expected move | ±463 → 24,905 – 25,830 | |

## Regime
* IV percentile (1y): **65**
* Trend: **UP**  (20-DMA 23,868, 50-DMA 23,386)
* 20-day realised vol 14.8% vs implied 14.0% → premium -0.8 vol pts
* VIX calming (5-day high 17.56)
* Today's opening gap: -0.05%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (174,501) · PE 25000 (158,966)

## Verdict
**NO TRADE today.**
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25000 PE | 52.50 | 52.40/52.60 | 14.3% | -0.20 | 80% | 42% | 158,966 |
| SELL | 25100 PE | 73.50 | 73.40/73.60 | 14.1% | -0.26 | 74% | 55% | 45,325 |
* ❌ credit/width PE 21.0/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹109 = 8.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25100PE is inside by 100 pts (tolerance 100) the 25000 wall (158,966 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.00 pts = ₹1,365/lot · max loss ₹5,193/lot · margin ~₹16,489/lot · net at 50% target ₹573/lot
* Exits: **take profit** when spread ≤ 10.50 · **stop** when spread ≥ 63.00 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25750 CE | 59.55 | 59.45/59.65 | 13.9% | +0.23 | 78% | 43% | 5,547 |
| SELL | 25650 CE | 85.17 | 85.05/85.30 | 13.9% | +0.30 | 71% | 56% | 5,756 |
* ✅ credit/width CE 25.6/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹112 = 6.7% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25650CE is inside by 350 pts (tolerance 100), too far inside the 26000 wall (174,501 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.62 pts = ₹1,666/lot · max loss ₹4,894/lot · margin ~₹16,489/lot · net at 50% target ₹721/lot
* Exits: **take profit** when spread ≤ 12.81 · **stop** when spread ≥ 76.88 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24900 PE | 37.38 | 37.30/37.45 | 14.6% | -0.15 | 85% | 31% | 31,566 |
| SELL | 25000 PE | 52.50 | 52.40/52.60 | 14.3% | -0.20 | 80% | 42% | 158,966 |
| BUY (hedge, first) | 25750 CE | 59.55 | 59.45/59.65 | 13.9% | +0.23 | 78% | 43% | 5,547 |
| SELL | 25650 CE | 85.17 | 85.05/85.30 | 13.9% | +0.30 | 71% | 56% | 5,756 |
* ❌ credit/width PE 15.1/100 = 0.15, CE 25.6/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹217 = 8.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25000PE is inside by 0 pts (tolerance 100) the 25000 wall (158,966 OI); short 25650CE is inside by 350 pts (tolerance 100), too far inside the 26000 wall (174,501 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 40.75 pts = ₹2,649/lot · max loss ₹3,966/lot · margin ~₹16,489/lot · net at 50% target ₹1,108/lot
* Exits: **take profit** when spread ≤ 20.38 · **stop** when spread ≥ 122.25 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
