# Trading Candidate Profiles

## Overview

The trading engine uses one common setup-maturity layer across three scoring profiles:

1. **Day Top Candidates** — short holding period / intraday opportunities
2. **Swing Top Candidates** — multi-day opportunities
3. **Growth Top Candidates** — technically strong growth-oriented stocks; fundamental growth is added when fundamental data becomes available

The profiles share a common factor engine but apply different weights and filters.

The dashboard groups candidates by setup maturity first. Day, Swing, and Growth are profile applicability labels shown within those maturity groups.

| User-facing category | Meaning | Priority |
| --- | --- | --- |
| **EARLY RADAR** | Early evidence of improvement and factor convergence, but not enough structure to qualify as Building. | Watch |
| **BUILDING** | Multiple independent factors are converging into a constructive setup. | High |
| **BREAKOUT** | Setup is mature and price is near/testing the trigger; confirmation is pending. | High |
| **CONFIRMED** | Breakout has occurred and is confirmed by price, volume, and structure. | Actionable |
| **PULLBACK** | A previously confirmed move is retracing constructively toward support or the breakout level. | Actionable |

**Status modifiers — not separate maturity categories:**

- `EXTENDED` — entry is too far from an acceptable risk point.
- `FAILED` — expected setup progression failed.
- `INVALIDATED` — setup thesis is no longer valid.

The formal maturity lifecycle is therefore:

```text
EARLY RADAR → BUILDING → BREAKOUT → CONFIRMED → PULLBACK → RE-ENTRY / CONFIRMED
```

`EARLY RADAR` is an early-warning scanner state, not an approval to trade.

Each candidate can show one or more applicable profiles: `Day`, `Swing`, `Growth`, or a combination such as `Day/Swing/Growth`. The profile describes how the stock scored; setup maturity describes when it may be actionable.

The system should separate:

* **Stock Quality** — Is this a stock worth trading?
* **Setup Quality** — Is there a valid setup?
* **Entry Timing** — Is this the right time to enter?
* **Risk** — Is the potential reward sufficient relative to the defined stop?

## Setup Lifecycle

The scanner should classify both the current setup state and the direction of state transition.

```text
                         STOCK QUALITY
                               |
                               v
                         +-----------+
                         | BUILDING  |
                         +-----+-----+
                               |
                         setup matures
                               |
                               v
                         +-----------+
                         | BREAKOUT  |
                         +-----+-----+
                               |
                         confirmation
                               |
                               v
                        +--------------+
                        |  CONFIRMED   |
                        +------+-------+
                               |
                  +------------+------------+
                  |                         |
             continuation                retracement
                  |                         |
                  v                         v
             EXTENDED*                 PULLBACK
                                            |
                                      re-entry / support
                                            |
                                            v
                                        CONFIRMED

* EXTENDED is a state modifier, not a maturity stage.

At any stage:
    FAILED / INVALIDATED
```

The key scanner question changes from:

> "Does this stock have a high score?"

to:

> **"What state is this stock in, is the setup improving or deteriorating, and how close is it to the next state?"**

This is intended to identify developing setups earlier rather than waiting for a large move to make the stock score highly on already-confirmed breakout factors.


A high overall score should **not automatically result in a BUY**. Hard gates must be passed first.

---

# Common Scoring Framework

Each factor produces a normalized score from **0–100**.

```text
0   = Very weak / unfavorable
25  = Weak
50  = Neutral
75  = Strong
100 = Excellent
```

The profile score is calculated using the applicable factor weights.

```text
Profile Score =
    Σ(Factor Score × Factor Weight)
```

Factors not applicable to a profile have a weight of 0%.

---

# Trade Action Layer

Trade actions are separate from setup maturity. Maturity answers **where the setup is in its lifecycle**; the action layer answers **what to do now**.

A candidate may therefore be `CONFIRMED + EXTENDED`, `BUILDING + WATCH`, or `PULLBACK + BUY NOW` depending on entry timing and risk.

## BUY NOW

Candidate meets:

* Minimum profile score
* Minimum factor requirements
* Entry timing requirements
* Risk/reward requirement
* No critical risk/news rejection

## BUY ON PULLBACK

Candidate has strong quality and setup but is currently too extended for immediate entry.

## BREAKOUT WATCH

Candidate is close to a valid setup but does not yet have confirmation.

## WATCH

Candidate is interesting but does not currently meet the entry requirements.

## AVOID

Candidate fails one or more critical filters.

---

# Common Hard Gates

A candidate should not receive a `BUY NOW` classification merely because its weighted score is high.

The following gates should be applied after scoring.

```text
Market Regime >= minimum threshold
Sector >= minimum threshold
Trend >= minimum threshold
Relative Strength >= minimum threshold
Setup >= minimum threshold
Risk/Reward >= 2.0
Extension must not be excessive
```

Additional profile-specific gates are defined below.

---

# Common Factor Definitions

## 1. Market Regime

Measures whether the overall market environment is favorable.

Suggested inputs:

* SPY relative to 20-day moving average
* SPY relative to 50-day moving average
* SPY relative to 200-day moving average
* QQQ trend
* Market breadth
* VIX / volatility regime
* Market momentum

### Interpretation

```text
80–100 = Strong bullish environment
65–79  = Bullish
50–64  = Neutral
35–49  = Weak
0–34   = Bearish
```

For long strategies, bearish market regimes should significantly reduce candidate ranking.

---

# 2. Sector Strength

Measures whether the stock's sector is outperforming the overall market.

Suggested inputs:

* Sector ETF return vs SPY
* Sector ETF above 20 DMA
* Sector ETF above 50 DMA
* Sector ETF above 200 DMA
* Sector momentum
* Stock performance relative to sector

### Preferred condition

```text
Strong Sector
+
Strong Stock
=
Higher probability setup
```

---

# 3. Relative Strength

Measures whether the stock is outperforming the market and its sector.

Recommended comparison periods:

* 5 trading days
* 20 trading days
* 60 trading days

Example:

```text
Stock 20-day return = +12%
SPY 20-day return   = +5%

Relative outperformance = +7%
```

Relative strength should be calculated against:

1. SPY
2. Relevant sector ETF

---

# 4. Trend

Trend evaluates the stock's price structure.

Recommended indicators:

* 20 DMA
* 50 DMA
* 200 DMA
* Moving-average slopes
* Price relative to moving averages

### Strong bullish structure

```text
Price > 20 DMA
20 DMA > 50 DMA
50 DMA > 200 DMA
```

Trend score should also consider whether the moving averages are rising.

---

# 5. Price Setup

Price setup identifies the structure and stage of the trade setup. It should be separated from trend and from breakout confirmation.

## Setup Development

The setup-development layer identifies whether the ingredients for a future move are converging.

Preferred Building characteristics:

```text
Strong / improving stock quality
+
Trend constructive or improving
+
Relative strength improving
+
Price forming a base or controlled consolidation
+
Identifiable resistance
+
Volatility contracting or stabilizing
+
Constructive volume behavior
+
Momentum improving
=
BUILDING
```

The scanner should **not require price to already be directly at resistance** for BUILDING.

### Strong setup structures

```text
Tight consolidation
Base formation
Higher lows below resistance
Volatility contraction
Controlled pullback within an established trend
Improving relative strength during consolidation
```

### Setup Development Score

Use a separate score to measure how strongly the setup is converging toward a breakout:

| Component | Weight |
| --- | ---: |
| Trend improvement | 20% |
| Relative-strength improvement | 20% |
| Base / consolidation quality | 20% |
| Resistance proximity | 15% |
| Volume behavior | 10% |
| Volatility contraction | 10% |
| Momentum improvement | 5% |
| **Total** | **100%** |

This score should emphasize **change and convergence**, not simply the absolute strength of the stock.

## Breakout Confirmation

Once a setup becomes mature, the scanner can classify it as BREAKOUT.

Preferred BREAKOUT characteristics:

```text
Strong setup has developed
AND
Price is testing / near resistance
AND
Base / consolidation is mature
AND
Volume is beginning to expand
AND
Breakout trigger is within actionable range
BUT
confirmation is not yet complete
```

A breakout should not be considered CONFIRMED merely because price briefly trades above resistance intraday.

Preferred confirmation:

```text
Close > resistance by configurable threshold
AND
Volume expansion
AND
Relative strength remains strong
AND
Price holds above breakout level
AND
No immediate rejection
```

Suggested initial configurable thresholds:

```text
Breakout close threshold >= 0.5 ATR above resistance
RVOL >= 1.5
Breakout volume > 20-day average
Close remains above breakout level
```

These are starting parameters only and must be backtested.

## Price Setup Scoring

Use setup stage as context rather than allowing one static setup score to drive the entire classification.

```text
Confirmed breakout + volume confirmation       100
Breakout + successful retest                    95
Pullback to support + reversal                  90
Pullback to 20/50 DMA                           85
VWAP reclaim                                    85
Tight consolidation                             80
Range-bound                                     50
Chasing extended move                           20
Breakdown                                        0
```

The exact scoring thresholds should remain configurable.

# 6. VWAP

VWAP is primarily important for entry timing.

Suggested inputs:

* Price vs VWAP
* VWAP slope
* Distance from VWAP
* VWAP reclaim
* VWAP rejection
* Volume during VWAP reclaim

### Strong bullish intraday structure

```text
Price > VWAP
VWAP rising
Pullback toward VWAP
VWAP holds/reclaims
Volume increases on reclaim
```

VWAP should not be interpreted as a standalone BUY signal.

---

# 7. Volume / Relative Volume

Use both absolute volume and relative volume.

```text
RVOL = Current Volume / Average Volume
```

Suggested RVOL scoring:

```text
RVOL > 2.0       = 100
1.5–2.0          = 80
1.2–1.5          = 60
0.8–1.2          = 40
< 0.8            = 20
```

Volume behavior should also be considered.

### Preferred breakout structure

```text
Consolidation
    ↓
Volume contracts
    ↓
Breakout
    ↓
Volume expands
```

---

# 8. Momentum

Recommended inputs:

* RSI
* RSI slope
* MACD
* Rate of Change
* Momentum acceleration

RSI should not be treated as:

```text
RSI < 30 = BUY
RSI > 70 = SELL
```

Instead, determine whether momentum is strengthening or weakening within the current trend.

---

# 9. Volatility

Recommended inputs:

* ATR
* ATR %
* Historical volatility
* Bollinger Band width
* Volatility expansion/contraction

Volatility is useful for:

* Position sizing
* Stop placement
* Detecting compression
* Detecting excessive movement

A volatility contraction followed by a controlled expansion can be a useful setup signal.

---

# 10. Extension

Extension measures how far the current price has moved away from a reference point.

Recommended references:

* 20 DMA
* VWAP
* Recent breakout
* ATR

Example:

```text
Extension in ATR =
Distance from reference price / ATR
```

### Suggested interpretation

```text
0–0.5 ATR       = Ideal
0.5–1.0 ATR     = Good
1.0–1.5 ATR     = Caution
1.5–2.0 ATR     = Extended
>2.0 ATR        = Highly extended
```

Extension should act primarily as a **risk/entry penalty**, not simply another bullish factor.

---

# 11. Options

Options data should be treated as a confirmation factor rather than a standalone bullish signal.

Potential inputs:

* Options volume
* Call/put volume
* Open interest
* Open-interest change
* Implied volatility
* IV Rank
* Unusual options activity
* Put/call ratio
* Expiration proximity

High options volume by itself does not indicate bullishness.

Options should therefore be interpreted in the context of the technical setup.

---

# 12. Risk / Reward

For every potential trade:

```text
Risk = Entry Price - Stop Price

Reward = Target Price - Entry Price

Risk/Reward = Reward / Risk
```

For long trades:

```text
Minimum acceptable R:R = 2.0
Preferred R:R >= 2.5
Excellent R:R >= 3.0
```

A candidate with insufficient reward relative to risk should not receive `BUY NOW`, regardless of its profile score.

---

# ## Day Top Candidates

## Purpose

The Day profile identifies stocks suitable for **short holding periods and intraday trading**.

The Day profile prioritizes:

* Current market environment
* Sector strength
* Relative strength
* Immediate price setup
* VWAP
* Volume
* Intraday momentum

The key question is:

> **Is this a strong stock with an actionable setup right now?**

---

## Day Profile Weights

| Component         |   Weight |
| ----------------- | -------: |
| Market regime     |      10% |
| Sector            |      10% |
| Relative strength |      10% |
| Trend             |      10% |
| Price setup       |      15% |
| VWAP              |      15% |
| Volume / RVOL     |      10% |
| Momentum          |       7% |
| Volatility        |       5% |
| Extension         |       5% |
| Options           |       3% |
| **Total**         | **100%** |

---

## Day Shortlist Filters

These relaxed thresholds create a review shortlist. They do not approve a trade.
The stricter `BUY NOW` conditions below remain required before entry.

```text
Market Regime >= 55
Sector >= 55
Relative Strength >= 60
Trend >= 60
VWAP >= 60
Volume >= 45
Momentum >= 50
```

Additionally:

```text
Extension must not indicate excessive chasing.
```

---

## Day Entry Setup

Preferred long setup:

```text
Strong market
    ↓
Strong sector
    ↓
Stock showing relative strength
    ↓
Price above major trend averages
    ↓
Intraday consolidation/pullback
    ↓
Price approaches VWAP/support
    ↓
VWAP holds or is reclaimed
    ↓
Bullish price confirmation
    ↓
Volume increases
    ↓
Entry
```

---

## Day BUY NOW Conditions

A Day candidate can be classified as `BUY NOW` when:

```text
Profile Score >= 80
AND
Market >= 60
AND
Sector >= 60
AND
RS >= 65
AND
Price Setup >= 70
AND
VWAP >= 70
AND
Volume >= 60
AND
R:R >= 2.0
AND
No excessive extension
AND
No critical negative catalyst
```

---

## Day BUY ON PULLBACK

Use when:

```text
Profile Score >= 80
AND
Stock quality is strong
AND
Setup is valid
BUT
Price is currently extended
```

Example:

```text
Strong stock
Strong breakout
Strong volume
Strong VWAP
BUT
Price > 1.5 ATR above ideal entry
```

Result:

```text
BUY ON PULLBACK
```

---

## Day BUILDING

Use when an intraday candidate is developing toward a potential breakout but is not yet at the trigger.

```text
Market/sector supportive
AND
Strong or improving relative strength
AND
Constructive trend
AND
Intraday base / consolidation
AND
Resistance identifiable
AND
Momentum improving
AND
Volume constructive
AND
No confirmed breakout
```

The purpose is **early detection**, not immediate entry.

## Day BREAKOUT

Use when the Building setup has matured:

```text
Strong trend
AND
Strong relative strength
AND
Mature consolidation
AND
Price near resistance
AND
Breakout trigger within actionable range
AND
Volume beginning to expand
BUT
confirmation is missing
```

Wait for:

```text
Resistance break
+
Volume expansion
+
VWAP confirmation
+
Price hold
```

## Day CONFIRMED

Use when:

```text
Resistance broken
AND
Breakout confirmation threshold passed
AND
Volume confirms
AND
VWAP / intraday structure remains supportive
AND
Price holds above breakout
```

## Day Avoid Conditions

Avoid when:

```text
Market regime < 40
OR
Trend < 40
OR
Relative strength < 40
OR
Price setup < 40
OR
R:R < 1.5
OR
Extension > 2 ATR
```

---

# ## Swing Top Candidates

## Purpose

The Swing profile identifies **multi-day opportunities**, generally using daily and higher-timeframe information.

The key question is:

> **Is this a strong stock with a setup that can reasonably continue over several days?**

Swing trading should place more emphasis on:

* Relative strength
* Trend
* Price structure
* Momentum
* Volume
* Sector
* Market regime
* Extension

Intraday VWAP is useful but should receive less weight than it does for Day candidates.

---

## Swing Profile Weights

| Component         |   Weight |
| ----------------- | -------: |
| Market regime     |      10% |
| Sector            |      10% |
| Relative strength |      15% |
| Trend             |      15% |
| Price setup       |      15% |
| VWAP              |      10% |
| Volume / RVOL     |      10% |
| Momentum          |      10% |
| Volatility        |       5% |
| Extension         |      10% |
| Options           |       0% |
| **Total**         | **100%** |

---

## Swing Shortlist Filters

These relaxed thresholds create a review shortlist. They do not approve a trade.
The stricter `BUY NOW` conditions below remain required before entry.

```text
Market Regime >= 55
Sector >= 55
Relative Strength >= 60
Trend >= 60
Volume >= 45
Momentum >= 55
Extension >= 50
```

VWAP is used as supporting evidence rather than the primary entry trigger.

---

## Preferred Swing Setups

### 1. Breakout Retest

```text
Resistance
    ↓
Breakout
    ↓
Pullback
    ↓
Previous resistance becomes support
    ↓
Bullish reversal
    ↓
Entry
```

### 2. Moving Average Pullback

```text
Strong trend
    ↓
Controlled pullback
    ↓
20/50 DMA support
    ↓
Momentum stabilizes
    ↓
Volume returns
    ↓
Entry
```

### 3. Tight Consolidation

```text
Strong trend
    ↓
Price consolidates
    ↓
Volatility contracts
    ↓
Volume contracts
    ↓
Breakout
    ↓
Volume expansion
```

---

## Swing BUY NOW

Recommended requirements:

```text
Profile Score >= 80
AND
Trend >= 65
AND
Relative Strength >= 65
AND
Price Setup >= 70
AND
Momentum >= 60
AND
R:R >= 2.0
AND
No excessive extension
```

---

## Swing BUY ON PULLBACK

Use when:

```text
Profile Score >= 80
AND
Trend >= 70
AND
RS >= 70
AND
Setup >= 70
BUT
Extension is excessive
```

The stock remains a candidate but the system waits for a better entry.

---

## Swing BUILDING

Use when the multi-day setup is developing before the breakout trigger is mature.

```text
Trend constructive / improving
AND
RS improving
AND
Base / consolidation quality strong
AND
Resistance identifiable
AND
Volatility contracting or stabilizing
AND
Volume constructive
AND
Momentum improving
AND
No confirmed breakout
```

## Swing BREAKOUT

Use when:

```text
Trend >= 70
AND
RS >= 70
AND
Price is near resistance
AND
Consolidation quality >= threshold
AND
Breakout trigger is actionable
BUT
Breakout confirmation is missing
```

## Swing CONFIRMED

Use when:

```text
Resistance broken
AND
Close confirms the breakout
AND
Volume expansion confirms
AND
RS remains strong
AND
Price holds above the breakout level
```

# ## Growth Top Candidates

## Purpose

The Growth profile identifies stocks exhibiting **growth-like technical characteristics**.

Until reliable fundamental data is available, this profile is a:

> **Technical Growth Proxy**

It must **not** be interpreted as a complete fundamental growth ranking.

The profile looks for:

* Strong market environment
* Strong sector
* Strong relative strength
* Persistent trend
* Momentum
* Volume confirmation
* Constructive price structure

---

## Growth Profile — Technical Version

| Component         |  Weight |
| ----------------- | ------: |
| Market regime     |     10% |
| Sector            |     10% |
| Relative strength |     15% |
| Trend             |     10% |
| Price setup       |     10% |
| Volume / RVOL     |     10% |
| Momentum          |     10% |
| VWAP              |      5% |
| Volatility        |      5% |
| Extension         |      5% |
| Options           |      5% |
| **Total**         | **95%** |

### Important

The weights above total **95%**.

The remaining **5% should be reserved for Fundamental Growth** once reliable fundamental fields are available.

Until then, normalize the technical weights to 100%, or explicitly mark the profile as `technical-only`.

Recommended implementation:

```text
If fundamental data unavailable:
    Normalize technical weights to 100%

If fundamental data available:
    Fundamental Growth = 5%
    Technical factors = 95%
```

---

# Growth Fundamental Expansion

Once fundamental data is available, introduce:

| Fundamental Factor          | Suggested Weight |
| --------------------------- | ---------------: |
| Revenue growth              |               1% |
| EPS growth                  |               1% |
| Revenue acceleration        |               1% |
| EPS acceleration            |               1% |
| Earnings estimate revisions |               1% |

These can initially be incorporated into a broader:

```text
Fundamental Growth Score = 0–100
```

Then:

```text
Final Growth Score =
    Technical Growth Score × 95%
    +
    Fundamental Growth Score × 5%
```

The fundamental weight can be increased after sufficient backtesting.

---

# Growth Shortlist Filters

These relaxed thresholds create a review shortlist. They do not approve a trade.
The stricter `BUY NOW` conditions below remain required before entry.

```text
Market Regime >= 60
Sector >= 60
Relative Strength >= 65
Trend >= 60
Volume >= 45
Momentum >= 55
```

---

# Growth Preferred Characteristics

A strong Growth candidate should ideally show:

```text
Strong sector
+
Strong relative strength
+
Persistent trend
+
Positive momentum
+
Increasing volume on advances
+
Controlled pullbacks
+
Constructive consolidation
```

Avoid interpreting a rapidly rising stock as automatically being a growth candidate.

The system should distinguish:

```text
Healthy growth trend
```

from:

```text
Parabolic / speculative move
```

using extension and volatility.

---

# Growth BUY NOW

Recommended:

```text
Profile Score >= 82
AND
Market >= 60
AND
Sector >= 65
AND
RS >= 70
AND
Trend >= 65
AND
Setup >= 65
AND
Momentum >= 60
AND
R:R >= 2.0
AND
Extension acceptable
```

---

# Growth BUY ON PULLBACK

Use when:

```text
Growth Score >= 82
AND
Trend >= 70
AND
RS >= 70
AND
Momentum >= 65
BUT
Extension is excessive
```

---

# Growth BUILDING

Use when a technically strong growth candidate is developing a constructive base before the breakout trigger.

```text
Strong sector
+
Strong / improving relative strength
+
Persistent or improving trend
+
Constructive consolidation
+
Volatility contraction
+
Positive momentum
+
Constructive volume
+
Resistance identifiable
```

## Growth BREAKOUT

Use when:

```text
Strong relative strength
+
Strong trend
+
Strong sector
+
Mature consolidation
+
Price near resistance
+
Breakout trigger actionable
BUT
confirmation missing
```

## Growth CONFIRMED

Use when:

```text
Resistance broken
AND
Breakout confirmation threshold passed
AND
Volume confirms
AND
Relative strength remains strong
AND
Price holds above breakout
```

# Cross-Profile Ranking

The system should rank candidates separately within each profile.

Do not simply combine all Day, Swing, and Growth candidates into one ranking.

Example:

```text
Day Ranking
-----------
1. XYZ 91
2. ABC 88
3. DEF 85

Swing Ranking
-------------
1. DEF 93
2. XYZ 89
3. GHI 87

Growth Ranking
--------------
1. ABC 95
2. JKL 92
3. XYZ 90
```

The same stock can legitimately appear in multiple profiles.

---

# Early Radar

EARLY RADAR is the scanner's **early-warning layer**. It identifies stocks where several important factors are improving, but price structure has not matured enough to call the stock BUILDING.

## Early Radar Principle

```text
EARLY RADAR = improvement + convergence
BUILDING    = convergence + structure
BREAKOUT    = mature structure + trigger proximity
CONFIRMED   = trigger + price/volume confirmation
```

Do not use EARLY RADAR as a BUY signal.

## Early Radar Characteristics

```text
Relative strength improving
AND Trend improving
AND Momentum improving
AND Sector supportive
AND Price structure not bearish
AND No major deterioration
AND No excessive extension
```

EARLY RADAR should **not require resistance to be close** and should **not require a mature base**.

## Early Radar Score

| Component | Weight |
| --- | ---: |
| Relative-strength improvement | 25% |
| Trend improvement | 20% |
| Momentum improvement | 20% |
| Sector strength / improvement | 15% |
| Volume improvement | 10% |
| Price-structure improvement | 10% |
| **Total** | **100%** |

Evaluate improvement using 5-day, 10-day, and 20-day deltas plus slope/acceleration.

Suggested qualification:

```text
Radar Score >= 75
AND At least 3 major factors improving
AND No major bearish breakdown
AND Extension acceptable
```

## Early Radar Search Presentation

Show EARLY RADAR separately from the primary candidate list:

```text
EARLY RADAR
────────────────────────────────────────────
Ticker   Radar   Trend Δ   RS Δ   Momentum Δ
PBR       86       +8      +11       +9
SMCI      83       +6       +9      +12
DEF       78       +7       +6       +8
```

Each radar result should show:

```text
Current State
Radar Score
Next State
Why it is improving
Key missing condition
Factor deltas
```

For general searches, prioritize BUILDING, BREAKOUT, CONFIRMED, and PULLBACK, then show EARLY RADAR separately. For searches specifically asking what is starting to build, promote EARLY RADAR.

Do not present PRE-BUILDING, BUILDING, BREAKOUT, CONFIRMED, PULLBACK, EXTENDED, FAILED, and INVALIDATED as equal filters.

# Factor Improvement and Convergence

Static factor strength is not sufficient for early detection. Store current score, 5-day delta, 10-day delta, 20-day delta, slope, and acceleration for major factors.

Example:

```text
Stock A: RS 72 / Trend 68 / Momentum 70
Stock B: RS 55 → 63 → 72 / Trend 58 → 63 → 68 / Momentum 52 → 61 → 70
```

Stock B is more relevant to EARLY RADAR / BUILDING because factors are improving together.

## Compression

Preferred Building pattern:

```text
ATR % ↓
Bollinger width ↓
Daily range ↓
Volume → / ↓
while RS ↑, Trend ↑, Momentum ↑
```

Favor **strength + compression + improving momentum** over simple recent price acceleration.

# State Transition Engine

The maturity engine should track both the current state and the transition toward the next state.

## State Transition Rules

### BUILDING → BREAKOUT

Require a mature setup:

```text
Setup Development Score >= configurable threshold
AND
Resistance proximity <= configurable threshold
AND
Consolidation quality >= threshold
AND
No invalidation condition
```

### BREAKOUT → CONFIRMED

Require actual confirmation:

```text
Price closes above resistance
AND
Breakout exceeds minimum threshold
AND
Volume confirms
AND
Relative strength remains strong
AND
Price does not immediately reject the breakout
```

### CONFIRMED → PULLBACK

Require:

```text
Prior confirmed breakout
AND
Price retraces
AND
Pullback volume is controlled
AND
Breakout level / support remains intact
AND
Relative strength remains healthy
AND
Momentum stabilizes or reverses positively
```

### Any State → FAILED

Example:

```text
Expected progression invalidated
OR
Breakout rejected
OR
Support decisively lost
OR
Relative strength deteriorates materially
```

A failed setup should be retained in historical data for backtesting.

## EXTENDED State Modifier

EXTENDED is not a maturity stage.

It can be attached to any actionable maturity state:

```text
CONFIRMED + EXTENDED
BREAKOUT + EXTENDED
PULLBACK + EXTENDED
```

Apply EXTENDED when the distance from the acceptable entry/risk point becomes excessive.

Example:

```text
Extension <= 1.0 ATR       Normal
1.0–1.5 ATR                Caution
1.5–2.0 ATR                EXTENDED
>2.0 ATR                   HIGHLY EXTENDED
```

A stock can remain technically strong while being a poor fresh entry.

## Distance to Next State

Every candidate should expose:

```text
Current State
State Confidence
Next State
Distance to Next State
Setup Development Score
Breakout Readiness
Key Missing Condition
```

Example:

```text
Current State: BUILDING
Next State: BREAKOUT
Setup Development: 84
Breakout Readiness: 78
Resistance Distance: 1.2%
Volume Confirmation: Pending
Momentum: Improving
RS: Improving
```

This allows the scanner to identify **approaching setups**, not only already-tested setups.

# Entry Timing Layer

After profile scoring, calculate a separate Entry Timing Score.

Suggested inputs:

```text
Price vs VWAP
Price vs support
Distance from breakout
Volume confirmation
Intraday momentum
Extension
Recent price movement
ATR distance
```

Example:

```text
Entry Timing >= 80
    = Immediate entry candidate

Entry Timing 65–79
    = Wait for confirmation

Entry Timing 50–64
    = Watch

Entry Timing <50
    = Do not enter
```

---

# Final Trade Decision

The final decision should use both profile quality and entry quality.

Recommended structure:

```text
Profile Score = 70%
Entry Timing Score = 30%
```

Then apply hard gates.

Example:

```text
Profile Score = 91
Entry Timing = 55

Final Score =
91 × 70% + 55 × 30%
= 79.2
```

Despite a strong stock score, the candidate should **not automatically be a BUY NOW** because entry timing is weak.

---

# LLM Context Layer

The LLM should not replace the quantitative scoring engine.

The quantitative engine should calculate:

```text
Market
Sector
RS
Trend
Setup
VWAP
Volume
Momentum
Volatility
Extension
Options
Risk/Reward
```

The LLM should evaluate contextual information such as:

* News
* Earnings
* Guidance
* Analyst revisions
* Regulatory events
* Company-specific catalysts
* Unusual market events
* Contradictory information
* Potential reasons the technical setup may fail

The LLM should not invent missing data.

---

# Recommended Final Architecture

```text
MARKET DATA
    ↓
FACTOR ENGINE
    ↓
PROFILE ENGINE (Day / Swing / Growth)
    ↓
IMPROVEMENT ENGINE (deltas / slopes / acceleration)
    ↓
SETUP / STATE ENGINE
    ├── EARLY RADAR
    ├── BUILDING
    ├── BREAKOUT
    ├── CONFIRMED
    └── PULLBACK
    ↓
STATUS MODIFIERS (EXTENDED / FAILED / INVALIDATED)
    ↓
HARD GATES
    ↓
ENTRY TIMING ENGINE
    ↓
LLM CONTEXT CHECK
    ↓
FINAL ACTION (BUY NOW / PULLBACK / WATCH)
```

## User-Facing Dashboard

Primary sections:

```text
BUILDING
BREAKOUT
CONFIRMED
PULLBACK
```

Separate early-warning section:

```text
EARLY RADAR
```

Status badges:

```text
EXTENDED
FAILED
INVALIDATED
```

The dashboard remains simple while the engine retains the full lifecycle internally.

# Important Implementation Principle

The scoring system should **not be considered a proven trading edge until backtested**.

Store every candidate and every factor value:

```text
ticker
date
profile
market_score
sector_score
relative_strength_score
trend_score
price_setup_score
vwap_score
volume_score
momentum_score
volatility_score
extension_score
options_score
profile_score
entry_timing_score
risk_reward
classification
previous_state
current_state
next_state
state_confidence
radar_score
setup_development_score
breakout_readiness
factor_delta_5d
factor_delta_10d
factor_delta_20d
convergence_score
compression_score
state_transition_reason
entry_price
stop_price
target_price
outcome
return
maximum_favorable_excursion
maximum_adverse_excursion
```

This allows the weights and thresholds to be optimized based on actual historical performance rather than assumptions.

The first implementation should therefore be considered **Version 1**, with the weights and thresholds treated as configurable parameters.


---

# Version 3 — Simplified Setup Lifecycle + Early Radar

This version changes the scanner from primarily static candidate scoring to a **score + setup lifecycle + state-transition model**.

The intended lifecycle is:

```text
BUILDING
   ↓
BREAKOUT
   ↓
CONFIRMED
   ↓
PULLBACK
   ↓
RE-ENTRY / CONFIRMED
```

with independent modifiers:

```text
EXTENDED
FAILED
INVALIDATED
```

The numerical thresholds in this document are initial configurable values. They should be validated through historical backtesting, including state-transition outcomes, maximum favorable excursion, maximum adverse excursion, time-to-breakout, and false-breakout rates.