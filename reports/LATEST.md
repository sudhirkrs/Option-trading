# NIFTY trade card: Wed 11 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,362.20 | Yahoo |
| India VIX | 17.62 | Yahoo |
| Expiry | Tue 17 Nov 2026 (6.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 17.7% | chain |
| 1-SD expected move | ±587 → 24,775 – 25,950 | |

## Regime
* IV percentile (1y): **81**
* Trend: **UP**  (20-DMA 23,393, 50-DMA 23,290)
* 20-day realised vol 15.7% vs implied 17.7% → premium +2.0 vol pts
* VIX RISING (5-day high 17.47)
* Today's opening gap: +1.17%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (155,416) · PE 25000 (121,152)

## Verdict
**NO TRADE today.**
* uptrend but VIX rising: no put selling

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24950 PE | 80.55 | 80.45/80.65 | 18.2% | -0.23 | 77% | 48% | 16,137 |
| SELL | 25050 PE | 105.78 | 105.65/105.90 | 18.1% | -0.28 | 71% | 59% | 14,783 |
* ✅ credit/width PE 25.2/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹116 = 7.1% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25050PE is inside by 50 pts (tolerance 100) the 25000 wall (121,152 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 25.22 pts = ₹1,640/lot · max loss ₹4,923/lot · margin ~₹16,485/lot · net at 50% target ₹703/lot
* Exits: **take profit** when spread ≤ 12.61 · **stop** when spread ≥ 75.67 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25850 CE | 77.80 | 77.70/77.90 | 18.1% | +0.23 | 78% | 43% | 16,978 |
| SELL | 25750 CE | 99.95 | 99.80/100.10 | 17.9% | +0.28 | 73% | 53% | 20,620 |
* ❌ credit/width CE 22.1/100 = 0.22 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹115 = 8.0% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25750CE is inside by 250 pts (tolerance 100), too far inside the 26000 wall (155,416 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 22.15 pts = ₹1,440/lot · max loss ₹5,122/lot · margin ~₹16,485/lot · net at 50% target ₹605/lot
* Exits: **take profit** when spread ≤ 11.07 · **stop** when spread ≥ 66.45 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24950 PE | 80.55 | 80.45/80.65 | 18.2% | -0.23 | 77% | 48% | 16,137 |
| SELL | 25050 PE | 105.78 | 105.65/105.90 | 18.1% | -0.28 | 71% | 59% | 14,783 |
| BUY (hedge, first) | 26000 CE | 53.20 | 53.10/53.30 | 18.5% | +0.17 | 84% | 31% | 155,416 |
| SELL | 25900 CE | 68.40 | 68.35/68.45 | 18.2% | +0.20 | 80% | 39% | 40,247 |
* ❌ credit/width PE 25.2/100 = 0.25, CE 15.2/100 = 0.15 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹225 = 8.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 25050PE is inside by 50 pts (tolerance 100) the 25000 wall (121,152 OI); short 25900CE is inside by 100 pts (tolerance 100) the 26000 wall (155,416 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 40.42 pts = ₹2,628/lot · max loss ₹3,992/lot · margin ~₹16,485/lot · net at 50% target ₹1,089/lot
* Exits: **take profit** when spread ≤ 20.21 · **stop** when spread ≥ 121.27 (loss = 2× credit) · **time exit** Mon 16 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
