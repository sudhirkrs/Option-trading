# NIFTY trade card: Fri 27 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,842.40 | Yahoo |
| India VIX | 16.62 | Yahoo |
| Expiry | Tue 08 Dec 2026 (11.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.2% | chain |
| 1-SD expected move | ±690 → 25,153 – 26,532 | |

## Regime
* IV percentile (1y): **73**
* Trend: **UP**  (20-DMA 24,881, 50-DMA 23,665)
* 20-day realised vol 16.1% vs implied 15.2% → premium -0.8 vol pts
* VIX calming (5-day high 17.70)
* Today's opening gap: -0.17%
* Events up to expiry: 04 Dec RBI monetary policy decision (verify date)
* OI walls (largest OI within 2 SD): CE 26000 (29,281) · PE 25000 (21,223)

## Verdict
**NO TRADE today.**
* event before exit: 04 Dec RBI monetary policy decision (verify date)
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25350 PE | 100.57 | 100.30/100.85 | 16.6% | -0.23 | 76% | 49% | 1,529 |
| SELL | 25450 PE | 125.75 | 125.50/126.00 | 16.5% | -0.27 | 72% | 58% | 1,382 |
* ✅ credit/width PE 25.2/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹121 = 7.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25450PE is inside by 450 pts (tolerance 100), too far inside the 25000 wall (21,223 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.18 pts = ₹1,636/lot · max loss ₹4,929/lot · margin ~₹16,798/lot · net at 50% target ₹697/lot
* Exits: **take profit** when spread ≤ 12.59 · **stop** when spread ≥ 75.53 (loss = 2× credit) · **time exit** Mon 07 Dec 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 26350 CE | 93.38 | 93.20/93.55 | 14.3% | +0.25 | 76% | 46% | 1,526 |
| SELL | 26250 CE | 118.90 | 118.70/119.10 | 14.2% | +0.30 | 71% | 55% | 1,601 |
* ✅ credit/width CE 25.5/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹119 = 7.2% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 26250CE is beyond the 26000 wall (29,281 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.53 pts = ₹1,659/lot · max loss ₹4,906/lot · margin ~₹16,798/lot · net at 50% target ₹710/lot
* Exits: **take profit** when spread ≤ 12.76 · **stop** when spread ≥ 76.58 (loss = 2× credit) · **time exit** Mon 07 Dec 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25350 PE | 100.57 | 100.30/100.85 | 16.6% | -0.23 | 76% | 49% | 1,529 |
| SELL | 25450 PE | 125.75 | 125.50/126.00 | 16.5% | -0.27 | 72% | 58% | 1,382 |
| BUY (hedge, first) | 26350 CE | 93.38 | 93.20/93.55 | 14.3% | +0.25 | 76% | 46% | 1,526 |
| SELL | 26250 CE | 118.90 | 118.70/119.10 | 14.2% | +0.30 | 71% | 55% | 1,601 |
* ✅ credit/width PE 25.2/100 = 0.25, CE 25.5/100 = 0.26 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹240 = 7.3% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25450PE is inside by 450 pts (tolerance 100), too far inside the 25000 wall (21,223 OI); short 26250CE is beyond the 26000 wall (29,281 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 50.70 pts = ₹3,296/lot · max loss ₹3,335/lot · margin ~₹16,798/lot · net at 50% target ₹1,407/lot
* Exits: **take profit** when spread ≤ 25.35 · **stop** when spread ≥ 152.10 (loss = 2× credit) · **time exit** Mon 07 Dec 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
