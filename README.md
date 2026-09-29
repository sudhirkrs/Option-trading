# Covered (defined-risk) option selling: NIFTY playbook

Prepared 29 Sep 2026 (evening, IST) for trades starting **Wed 30 Sep 2026**.
Every structure here is **defined-risk**: each short option is paired with a long
option, or with stock you already own, so the worst-case loss is known before entry.
There is no naked selling anywhere in this plan.

> Estimates for analysis. Verify lot size, expiry, margin and charges against the
> exchange and your broker before trading. Not investment advice.

---

## 1. TL;DR: what to do tomorrow

| # | Strategy | When | Status |
|---|---|---|---|
| 1 | **NIFTY weekly bear call spread** (sell ~0.25-delta CE, buy 100 pts higher), 6-Oct expiry | Wed 30 Sep, 10:00-11:30 IST, **only if the entry filter passes** | **Primary** |
| 2 | **NIFTY iron condor**, 13-Oct weekly or 27-Oct monthly | From Thu 8 Oct, *after* the RBI policy, **only if VIX stops rising** | Conditional |
| 3 | **Covered calls on stocks you already hold** (1 F&O lot or more) | Any day; monthly 27-Oct expiry | Use if you hold the shares |
| 4 | Bull put spread | **Not now.** Only after NIFTY closes back above its 20-DMA and VIX falls | Parked |

**Entry filter for #1:** with live quotes, the 100-point call spread must collect
**≥ 25 points** (credit/width ≥ 0.25). If it doesn't, skip the day. The model says
it will be around 22 points, which is marginal (section 5), so a skip is quite possible.

**Hard exit for #1:** close by **Mon 5 Oct, 15:00**. Never hold it into Tuesday's
expiry, and never hold it through the RBI decision on 7 Oct.

---

## 2. Preflight (inputs and how sure we are)

| Item | Value used | Status |
|---|---|---|
| NIFTY spot | ~22,600 (traded 22,582 intraday on 29 Sep; closed 22,780 on 28 Sep) | **PROVISIONAL**: re-enter tomorrow's live spot |
| India VIX | ~14.5 (14.39-14.54 intraday 29 Sep; 13.69 on 28 Sep) | PROVISIONAL |
| India VIX 1-year range | 8.7-28.9 (peak during the West Asia conflict, Mar-Jun 2026) | From news reports |
| NIFTY lot size | **65** (from Jan 2026) | Verify in the broker's contract note |
| NIFTY weekly expiry | **Tuesday**. Next: **6 Oct**, then 13 Oct, then **19 Oct (Mon)**, because 20 Oct is a Dussehra holiday and the expiry moves back a day | Verify on the NSE circular |
| NIFTY monthly expiry | **27 Oct 2026** (last Tuesday) | Verify |
| Holidays | **Fri 2 Oct** (Gandhi Jayanti), **Tue 20 Oct** (Dussehra) | From NSE holiday list |
| STT | 0.15% of premium on sell; 0.15% of intrinsic value on exercise (Budget 2026, from 1 Apr 2026) | Confirmed by multiple sources |
| Other charges | Exchange ~0.035%, SEBI ₹10/cr, stamp 0.003% (buy), GST 18%, ₹20/order brokerage | Check your broker's charges page |
| Events | **RBI MPC 5-7 Oct** (decision ~7 Oct); Q2 results season begins ~2nd week of Oct; crude ~$107, USD/INR > 96, US 10-yr ~5.24%, India 10-yr 7.19% (2-year high) | Check an economic calendar |

---

## 3. Regime read

| Signal | Reading | What it means |
|---|---|---|
| IV level | VIX ~14.5 | Middle of the 1-year range |
| IV percentile | **~60-70 (estimated)**: VIX was lower than today for most of Oct 2025-Feb 2026 and Jul-Sep 2026, and higher only during Mar-Jun 2026 | Premium is fair to moderately rich. **Recompute** with `regime.py` on NSE's VIX CSV |
| VIX direction | **Rising fast**: 10.9 → 14.5 in one week | Volatility is expanding. Sellers usually get hurt when they sell *into* expansion rather than after the peak |
| Trend | **DOWN**: NIFTY at a 6-month low, 23,914 → ~22,600 in September, below 23,000 support; 47 of 50 NIFTY stocks fell on 28 Sep | Put side is the danger side; call side is the trend-aligned side |
| Macro | Oil, rupee, US and Indian yields all moving against equities | Gap risk is elevated in both directions (a relief rally can be sharp too) |
| 1-SD expected move (6-Oct expiry) | ±~430 pts → 22,170-23,030 | Where the market "expects" NIFTY to finish, with ~68% odds |

**Verdict:** a trade is allowed (IVP is above 30), but only with **defined risk,
small size, and on the call side**. This is a falling market with rising volatility,
the textbook setting where selling puts (even hedged ones) loses money. Selling into
the RBI decision is ruled out: event volatility is a fair price for real risk, not an edge.

---

## 4. Why these structures and not others

* **Short strangle / naked puts**: ruled out by your "covered only" rule, and in
  this regime they would be the most dangerous choice anyway.
* **Iron condor right now**: its put side is on the wrong side of the trend, and the
  model says 15-delta condors collect only ~11 pts per 100-pt wing (credit/width 0.11),
  so you'd risk ₹5,165 to make ₹519. **Rejected for now**, revisit after RBI.
* **Far-OTM "safe" spreads (10-15 delta)**: look like 90% winners, but collect
  ₹700-1,000 per lot against ₹5,000+ max loss, and costs eat 10-14% of the credit.
  One loss erases 6-8 wins. **Rejected.**
* **Bear call spread at ~0.25 delta**: trend-aligned, defined risk, collects enough
  to clear the cost gate. **Chosen**, subject to the live credit filter.
* **Iron fly**: high credit/width by construction, but the profit zone (±160-220 pts)
  sits well inside a ±430-pt expected move. Not suited to a trending, expanding-vol
  market. Rejected.
* **BANKNIFTY**: monthly only (27 Oct), and banks carry the most RBI and yield risk.
  Skip until after the policy.

### The one fact that matters most

At fair prices, **every** spread loses exactly its trading costs on average (see
`toolkit/sweep.py`, last column). Option selling makes money only when **implied
volatility is higher than the volatility that actually happens** (the "variance risk
premium"). So:

1. Sell when VIX is **high and falling** (the fear is being overpriced), not when it's
   rising (the fear is being discovered).
2. Take profits early (50%), because most of that premium is captured in the first
   half of the trade's life.
3. Keep costs under ~5-8% of the credit.

That is why strategy #1 is small, and why #2 waits for VIX to peak.

---

## 5. Strategy 1: NIFTY weekly bear call spread (primary)

**Structure (model, spot 22,600, VIX 14.5, entry 30 Sep 10:00):**

| Leg | Strike | Model IV | Premium | Delta | P(expires OTM) | P(touched before expiry) |
|---|---|---|---|---|---|---|
| SELL | 22,900 CE | 14.4% | 67.4 | 0.26 | 74% | 50% |
| BUY | 23,000 CE | 14.4% | 45.0 | 0.19 | 81% | 37% |

Economics per lot (65 qty):

| | |
|---|---|
| Net credit | 22.4 pts = **₹1,458** |
| Credit/width | 0.22 (**weak**, needs ≥ 0.25 live) |
| Round-trip cost (exit at 50%) | ₹108 (7.4% of credit): **passes** the 4× cost gate |
| Net profit at 50% target | **₹621** |
| Max loss (NIFTY ≥ 23,000 at exit) | **₹5,099** |
| Breakeven at expiry | 22,922 |
| Est. margin (hedged) | ~₹15,000 (confirm on the broker's SPAN calculator) |
| Return on margin at target | ~4% in 3 sessions |

**How to pick the strikes tomorrow (don't copy the numbers above blindly):**

1. At 10:00-10:15 IST, note NIFTY spot. **Skip the day if NIFTY opens more than 0.7%
   higher**: a sharp relief rally is the main risk to this trade.
2. Short strike: the **first call strike with |delta| ≤ 0.28** in your broker's
   option chain (expected ~250-300 pts above spot). It must sit **above**
   yesterday's high and above the largest call-OI strike nearby.
3. Long strike: **short + 100**.
4. Credit must be **≥ 25 pts** on a limit order at the mid-price. If it isn't, try
   one more time at 11:30; otherwise **no trade**.
5. Bid-ask on each leg ≤ 10% of mid. Order: **buy the hedge first, then sell**. This
   gets the hedge margin benefit and means you are never naked, even briefly.

**Exits (set as alerts or GTT orders the moment you're filled):**

| Trigger | Action |
|---|---|
| Spread value falls to 50% of the credit you received (e.g. 25 → 12.5) | Close, and take the win |
| Spread value reaches **3× credit** (i.e. loss = 2× credit, ~67 pts) | Close. No averaging, no rolling |
| NIFTY trades above the short strike | Close (P(touch) says this happens ~50% of the time; that's why size is small) |
| **Mon 5 Oct, 15:00** | Close whatever is left. Don't carry it into expiry day or into RBI |

**What kills this trade:** a sharp short-covering rally. Oversold markets bounce
hard, and a crude-oil reversal, an FII buying day or a global risk-on move can add
300-400 points in one session. The long 23,000 CE caps the damage at ~₹5,100/lot,
but it will be a full loss if the rally happens in the first day or two.

---

## 6. Strategy 2: iron condor after RBI (conditional)

**Don't pre-commit. Enter from Thu 8 Oct only if all of these hold:**

* RBI policy is out (no binary event left in the holding period);
* India VIX has **stopped rising**: today's close is below its 5-day high, and it
  has fallen on at least 2 of the last 3 days;
* NIFTY has held a range for 3+ sessions (no fresh 6-month low in the last 3 days);
* the live chain gives **≥ 25 pts per 100-pt wing** at ~0.20-0.25 delta shorts.

Expiry choice: the **13-Oct weekly** (enter 8 Oct, exit by 12 Oct), or the **27-Oct
monthly** (enter 8-9 Oct, take profit at 50% or exit by 23 Oct). The 19-Oct weekly
is a Monday expiry because of the Dussehra holiday; confirm before trading it.

Model check (27-Oct monthly, 19 days, VIX 14.5): 0.25-delta shorts at 22,150 PE /
23,200 CE with 100-pt wings collect ~22 pts each side (credit/width ~0.22). That is
still marginal at today's VIX. The condor becomes worthwhile if VIX is ≥ 16 **and
falling**, which is exactly the "sell after the spike" condition. Re-run
`planner.py` with live numbers.

---

## 7. Strategy 3: covered calls on stocks you already own

The most literally "covered" option-selling strategy: you own the shares, so a short
call has no upside risk beyond missing gains above the strike.

* Needs **≥ 1 full F&O lot** of the stock in your demat account. Pledge it for margin;
  most brokers then need little or no extra cash.
* Sell the **27-Oct monthly** call at **~0.20-0.25 delta**, above visible resistance.
* **Avoid stocks with Q2 results before 27 Oct** unless you're happy to have the
  shares called away at the strike.
* **Physical settlement:** if the call ends ITM, your shares are delivered at the
  strike. If you want to keep them, buy the call back by **Mon 19 Oct** (delivery
  margins ramp up from 4 trading days before expiry).
* Close at 50-60% of the premium captured; roll to November only for a net credit.
* Check the NSE **F&O ban list** daily. A banned stock allows only reduce-only trades,
  so you can't roll.
* The call offers only premium-sized downside protection. In a falling market, a
  covered call loses almost as much as the stock itself. If you'd sell the stock on a
  further fall, a **collar** (covered call + a ~5% OTM put bought with the call
  premium) is the defined-risk version.

Covered calls on a NIFTY ETF work the same way, but 1 lot needs ~₹14.7 lakh of ETF
units, so this is only practical for larger accounts.

---

## 8. Strategy 4 (parked): bull put spread

Selling puts is where option sellers lose big in India (see March 2020 and the June
2024 election day). Enable it only once NIFTY **closes above its 20-DMA** and
**VIX has come off its peak**. Same mechanics as strategy 1, mirrored below spot.

---

## 9. Position sizing

Risk per trade = **max loss**, capped at **2% of capital**. Margin used stays at
**≤ 50% of capital**. Total risk across all open short-vol positions stays at **≤ 6%
of capital**: NIFTY, BANKNIFTY and your stock calls all move together in a crash.

For the bear call spread (max loss ≈ ₹5,100/lot):

| Capital | 2% risk budget | Lots | Worst-case loss | Profit at 50% target |
|---|---|---|---|---|
| ₹3 lakh | ₹6,000 | 1 | ₹5,100 | ~₹620 |
| ₹5 lakh | ₹10,000 | 1 | ₹5,100 | ~₹620 |
| ₹10 lakh | ₹20,000 | 3 | ₹15,300 | ~₹1,860 |
| ₹25 lakh | ₹50,000 | 9 | ₹45,900 | ~₹5,600 |

These amounts are deliberately small. Premium selling at sane size produces
**modest, steady amounts with occasional sharp losses**. Anyone quoting 5-10% a month
is running naked or oversized positions. Start with **1 lot for the first 8-10
trades**, whatever your capital, and keep a journal (`journal-template.csv`).

---

## 10. Daily routine

**Before 09:15:** check GIFT Nifty, crude, USD/INR and US yields. Check the NSE F&O
ban list if you hold stock options. Check for events before your exit date.

**09:15-10:00:** watch only. Opening quotes are wide and IVs jump around.

**10:00-11:30:** run the entry checklist and place limit orders at the mid-price,
hedge leg first.

**Through the day:** alerts at the profit target, stop and short strike. Act on them
the same session.

**15:00:** handle any position that expires the next day. Nothing goes into expiry day.

**Weekly:** recompute IVP and trend (`regime.py`). Log every trade.

---

## 11. Failure modes to avoid

* Selling 5-10 delta options "because they never get hit": ~10% of credit goes to
  costs, and one loss wipes out months of gains.
* Selling on expiry day for "easy theta": maximum gamma for minimum premium.
* Averaging into or rolling a losing short. Rolling is not risk management.
* Treating margin as risk: a spread's risk is its max loss, not the ₹15k margin.
* Running NIFTY + BANKNIFTY + stock calls and calling it diversified.
* Leaving an ITM option to expire: STT of 0.15% on intrinsic value, and physical
  delivery on stock options. Square off instead.

---

## 12. Tax (factual summary, consult a CA)

F&O profits are **non-speculative business income**, taxed at your slab rate. Losses
carry forward 8 years if you file on time (ITR-3). For the tax-audit threshold,
"turnover" = the sum of absolute profits and losses on each trade, not the notional value.

---

## 13. Toolkit (`toolkit/`)

```bash
pip install numpy pandas scipy
cd toolkit
python3 validate.py                        # self-tests for the pricing maths

# Tomorrow morning: live spot + VIX
python3 planner.py --spot 22600 --vix 14.5 --entry "2026-09-30 10:00" \
    --expiry 2026-10-06 --capital 500000 --directional-delta 0.28 --widths 100,150

# Better: export the option chain from your broker to CSV (strike,type,bid,ask)
python3 planner.py --spot 22600 --atm-iv 15.2 --entry "2026-09-30 10:00" \
    --expiry 2026-10-06 --capital 500000 --chain chain.csv

python3 sweep.py 22600 14.5 6.2            # credit/width vs short-delta table
python3 regime.py --vix-csv vix.csv --nifty-csv nifty.csv   # IVP, trend, IV-RV
```

### Run it on GitHub (no install, works from phone)

1. Open the repo on GitHub → **Actions** tab → **Option planner** → **Run workflow**.
2. Enter live **NIFTY spot**, **India VIX**, **expiry**, your **capital**. Leave the
   entry time blank to use the current IST time.
3. Click **Run workflow** and open the run when it finishes (~1 min). The strike
   tables are on the run's **Summary** page.

To use real broker quotes: commit the chain CSV (`strike,type,bid,ask`) to the repo,
e.g. `chains/2026-09-30.csv`, and enter that path in **chain_file**.

`planner.py` prints strikes, credit/width, P(OTM), P(touch), costs, margin estimate,
breakevens, stop level and lot count. Without `--chain`, prices come from a model
(Black-Scholes on a skewed surface anchored on VIX). They are planning estimates,
not quotes.

**Limitations:** no live NSE data was available when this was prepared (the sandbox
blocks NSE and Yahoo), so spot, VIX, IVP and premiums are estimates from published
news figures and a pricing model. **No historical backtest** was run for the same
reason. Before scaling beyond 1 lot, backtest on NSE F&O bhavcopy data, including
the March 2020 and 4 June 2024 stress periods.

---

## Sources

* [ICICI Direct: Nifty Sep futures / cash close, 22 Sep 2026](https://www.icicidirect.com/futures-and-options/news/the-nifty-september-2026-futures-closed-at-23,410,-a-premium-of-8100-points-compared-with-the-niftys-closing-at-23,329-in-the-cash-market/5021030)
* [ICICI Direct: Nifty close 23,914, 2 Sep 2026](https://www.icicidirect.com/futures-and-options/news/the-nifty-september-2026-futures-closed-at-23,99480,-a-premium-of-8035-points-compared-with-the-niftys-closing-at-23,91445-in-the-cash-market/5014005)
* [Stockpil: Nifty −1.6% to 22,780, VIX 13.69, 28 Sep 2026](https://stockpil.com/india-markets-today-2026-09-28)
* [HDFC Sky: India VIX 14.54, Nifty below 22,700, 29 Sep 2026](https://hdfcsky.com/news/india-vix-rises-6-6percent-to-14-54-as-oil-us-yields-and-nifty-selling-lift-volatility-september-29-2026)
* [BusinessToday: Sensex, Nifty at six-month lows, 29 Sep 2026](https://www.businesstoday.in/markets/stocks/story/5-reasons-why-market-is-down-today-sensex-nifty-hit-six-month-lows-india-vix-spikes-558436-2026-09-29)
* [Business Standard live blog, 29 Sep 2026](https://www.business-standard.com/amp/markets/news/stock-market-live-updates-september-29-sensex-today-nifty50-gift-nifty-crude-oil-price-ipo-today-126092900092_1.html)
* [Angel One: India VIX below 12, 52-week high 28.91](https://www.angelone.in/news/market-updates/india-vix-falls-below-12-for-first-time-since-february-2026-down-59-from-52-week-high)
* [5paisa: RBI MPC schedule FY27](https://www.5paisa.com/blog/rbi-mpc-meeting-schedule)
* [Zerodha: NSE/BSE holiday calendar 2026](https://zerodha.com/marketintel/holiday-calendar/)
* [Zee Business: October 2026 market holidays](https://www.zeebiz.com/market-news/news-stock-market-holiday-october-2026-nse-bse-to-remain-closed-for-11-days-check-full-list-402881)
* [ICICI Direct: Budget 2026 STT changes](https://www.icicidirect.com/ilearn/futures-and-options/articles/stt-changes-in-budget-2026-what-f-o-traders-should-know)
* [Sahi: Nifty lot size 2026](https://www.sahi.com/blogs/nifty-lot-size-2026-bank-nifty-sensex)

> Estimates for analysis. Verify lot size, expiry, margin and charges against the
> exchange and your broker before trading. Not investment advice.
