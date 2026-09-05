# Trading Candidate Profiles

## Overview

The trading engine uses three candidate profiles:

1. **Day Top Candidates** — short holding period / intraday opportunities
2. **Swing Top Candidates** — multi-day opportunities
3. **Growth Top Candidates** — technically strong growth-oriented stocks; fundamental growth is added when fundamental data becomes available

The profiles share a common factor engine but apply different weights and filters.

The system should separate:

* **Stock Quality** — Is this a stock worth trading?
* **Setup Quality** — Is there a valid setup?
* **Entry Timing** — Is this the right time to enter?
* **Risk** — Is the potential reward sufficient relative to the defined stop?

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

# Common Candidate Classifications

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

Price setup identifies whether there is an actionable trading structure.

This should be treated separately from trend.

### Strong setups

```text
Breakout + volume confirmation       100
Breakout + successful retest          95
Pullback to support + reversal        90
Pullback to 20/50 DMA                 85
VWAP reclaim                          85
Tight consolidation                   80
Range-bound                           50
Chasing extended move                 20
Breakdown                              0
```

The exact scoring thresholds should be configurable.

---

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

## Day Candidate Minimum Filters

Recommended minimum requirements:

```text
Market Regime >= 60
Sector >= 60
Relative Strength >= 65
Trend >= 60
Price Setup >= 70
VWAP >= 70
Volume >= 60
Momentum >= 55
Risk/Reward >= 2.0
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

## Day BREAKOUT WATCH

Use when:

```text
Strong trend
Strong relative strength
Tight consolidation
Resistance nearby
Volume not yet confirmed
```

Wait for:

```text
Resistance break
+
Volume expansion
+
VWAP confirmation
```

---

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

## Swing Minimum Filters

```text
Market Regime >= 55
Sector >= 60
Relative Strength >= 65
Trend >= 65
Price Setup >= 70
Volume >= 55
Momentum >= 60
Extension >= 55
Risk/Reward >= 2.0
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

## Swing BREAKOUT WATCH

Use when:

```text
Trend >= 70
AND
RS >= 70
AND
Price is near resistance
AND
Consolidation quality >= threshold
BUT
Breakout confirmation is missing
```

---

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

# Growth Minimum Filters

```text
Market Regime >= 60
Sector >= 65
Relative Strength >= 70
Trend >= 65
Price Setup >= 65
Volume >= 60
Momentum >= 60
Risk/Reward >= 2.0
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

# Growth BREAKOUT WATCH

Use when:

```text
Strong relative strength
+
Strong trend
+
Strong sector
+
Tight consolidation
+
Price near resistance
BUT
Breakout confirmation missing
```

---

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
                         |
                         v
              +----------------------+
              |  FACTOR ENGINE       |
              |----------------------|
              | Market               |
              | Sector               |
              | Relative Strength    |
              | Trend                |
              | Price Setup          |
              | VWAP                 |
              | Volume               |
              | Momentum             |
              | Volatility           |
              | Extension            |
              | Options              |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | PROFILE ENGINE       |
              +----------------------+
                 /        |        \
                /         |         \
               v          v          v
             DAY       SWING       GROWTH
                \         |         /
                 \        |        /
                         v
              +----------------------+
              | HARD GATES            |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | ENTRY TIMING ENGINE  |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | LLM CONTEXT CHECK    |
              | News / Catalyst/Risk |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | FINAL CLASSIFICATION |
              +----------------------+
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
          BUY NOW    PULLBACK      WATCH
```

---

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
