---
name: sector-rotation
description: Compare sector ETF relative performance against SPY and send a Telegram market rotation alert twice daily.
---

# Sector Rotation Skill

## Goal

Identify where money is rotating by comparing major U.S. sector ETFs against SPY and sending a concise Telegram alert at 8:15 ET and 9:15 ET.

## Inputs

Use the latest available prices for:

- XLK — Technology
- XLF — Financials
- XLE — Energy
- XLV — Healthcare
- XLI — Industrials
- XLY — Consumer Discretionary
- XLP — Consumer Staples
- XLU — Utilities
- XLB — Materials
- XLRE — Real Estate
- XLC — Communication Services
- SPY — S&P 500

## Required Analysis

1. Pull the current market data for each sector ETF and SPY.
2. Compare each sector ETF against SPY using the same time window and return basis.
3. Rank relative performance from strongest to weakest.
4. Flag leadership, lagging sectors, and rotation themes.
5. Keep the message short and highly actionable.

## Signal Rules

- Strong leadership: sector ETF materially outperforming SPY.
- Weak leadership: sector ETF materially lagging SPY.
- Rotation call: focus on where relative strength is broad, persistent, and not just driven by a single day of noise.
- Treat the message as a market-timing clue, not a trade recommendation.

## Telegram Output Format

Use this exact headline:

> Where is money moving today?

Then provide a short sector-by-sector comparison. Keep the final message under 1,500 characters.

Suggested structure:

- 3–5 strongest sectors relative to SPY
- 3–5 weakest sectors relative to SPY
- One sentence summarizing the broad market rotation

Example format:

> Where is money moving today?
> XLK +1.4% vs SPY +0.7% — strongest leadership
> XLY +1.1% vs SPY +0.7% — cyclical strength
> XLF +0.8% vs SPY +0.7% — financials participating
> XLE -0.5% vs SPY +0.7% — rotation out of energy
> XLU -0.3% vs SPY +0.7% — defensive lagging
> Money is rotating toward growth/cyclicals while defensives and energy lag.

## Scheduling

Run twice per trading day:

- 8:15 ET
- 9:15 ET

This is a market pulse check, not a full research report.

## Output

Send the Telegram message only after calculating the relative strength check.

Never fabricate sector data.

If the market data is unavailable, state that the alert is delayed and explain the data issue briefly.
