# NIFTY trade card: Fri 13 Nov 2026, 10:05 IST

## Data
| Item | Value | Source |
|---|---|---|
| NIFTY spot | 25,206.25 | Yahoo |
| India VIX | 16.34 | Yahoo |
| Expiry | Mon 23 Nov 2026 (10.2 calendar days) | NSE |
| Option prices | LIVE | NSE live option chain |
| ATM IV (this expiry) | 15.2% | chain |
| 1-SD expected move | ±643 → 24,563 – 25,849 | |

## Regime
* IV percentile (1y): **74**
* Trend: **UP**  (20-DMA 23,645, 50-DMA 23,333)
* 20-day realised vol 15.1% vs implied 15.2% → premium +0.1 vol pts
* VIX calming (5-day high 17.56)
* Today's opening gap: -0.35%
* Events up to expiry: none listed
* OI walls (largest OI within 2 SD): CE 26000 (116,888) · PE 25000 (105,763)

## Verdict
**NO TRADE today.**
* BULL PUT SPREAD failed a gate (see ❌ below)

### BULL PUT SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24750 PE | 94.38 | 94.15/94.60 | 16.5% | -0.23 | 76% | 49% | 2,722 |
| SELL | 24850 PE | 119.15 | 118.95/119.35 | 16.4% | -0.28 | 72% | 59% | 3,385 |
* ❌ credit/width PE 24.8/100 = 0.25 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹120 = 7.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ✅ OI wall: short 24850PE is beyond the 25000 wall (105,763 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 24.78 pts = ₹1,610/lot · max loss ₹4,954/lot · margin ~₹16,384/lot · net at 50% target ₹686/lot
* Exits: **take profit** when spread ≤ 12.39 · **stop** when spread ≥ 74.33 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

<details><summary>Other structures (for reference only)</summary>


### BEAR CALL SPREAD
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 25750 CE | 76.40 | 76.25/76.55 | 14.7% | +0.22 | 79% | 41% | 2,225 |
| SELL | 25650 CE | 97.50 | 97.25/97.75 | 14.6% | +0.26 | 74% | 50% | 2,297 |
* ❌ credit/width CE 21.1/100 = 0.21 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹115 = 8.4% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 25650CE is inside by 350 pts (tolerance 100), too far inside the 26000 wall (116,888 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 21.10 pts = ₹1,371/lot · max loss ₹5,190/lot · margin ~₹16,384/lot · net at 50% target ₹571/lot
* Exits: **take profit** when spread ≤ 10.55 · **stop** when spread ≥ 63.30 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

### IRON CONDOR
| Leg | Strike | Price | Bid/Ask | IV | Delta | P(OTM) | P(touch) | OI |
|---|---|---|---|---|---|---|---|---|
| BUY (hedge, first) | 24600 PE | 65.60 | 65.55/65.65 | 16.7% | -0.17 | 82% | 37% | 17,510 |
| SELL | 24700 PE | 84.08 | 83.95/84.20 | 16.6% | -0.21 | 78% | 45% | 16,098 |
| BUY (hedge, first) | 25850 CE | 59.25 | 59.10/59.40 | 14.9% | +0.18 | 83% | 33% | 1,792 |
| SELL | 25750 CE | 76.40 | 76.25/76.55 | 14.7% | +0.22 | 79% | 41% | 2,225 |
* ❌ credit/width PE 18.5/100 = 0.18, CE 17.2/100 = 0.17 (need ≥ 0.25)
* ✅ short delta ≤ 0.30
* ✅ cost ₹222 = 9.6% of credit (net ≥ 4× cost)
* ✅ liquidity: OK
* ❌ OI wall: short 24700PE is beyond the 25000 wall (105,763 OI); short 25750CE is inside by 250 pts (tolerance 100), too far inside the 26000 wall (116,888 OI)
* ✅ size: 1 lot(s) within 2% risk (₹10,000), cap 1
* Credit 35.63 pts = ₹2,316/lot · max loss ₹4,302/lot · margin ~₹16,384/lot · net at 50% target ₹935/lot
* Exits: **take profit** when spread ≤ 17.81 · **stop** when spread ≥ 106.88 (loss = 2× credit) · **time exit** Fri 20 Nov 15:00 IST

</details>

_Estimates for analysis. Verify lot size, expiry, margin and charges against the exchange and your broker before trading. Not investment advice._
