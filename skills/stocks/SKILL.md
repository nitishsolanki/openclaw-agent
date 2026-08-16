---
name: stocks
description: Research and analyze every stock in the project watchlist.
---

# Stocks Skill

## Goal

Analyze every company listed in:

market-research-agent/watchlist.txt

## Workflow

1. Read watchlist.txt
2. Process one ticker at a time
3. Search recent information
4. Produce one markdown report per ticker

## Research Areas

For every company collect:

- Company overview
- Business summary
- Sector
- Industry

Recent developments:

- News
- Earnings
- Analyst upgrades/downgrades
- SEC filings
- Product announcements

Analysis:

- Bull thesis
- Bear thesis
- Risks
- Catalysts
- Long-term outlook

Rating:

- High
- Medium
- Low conviction

## Output

Save one file per company.

Examples:

data/stocks/NVDA.md

data/stocks/AMD.md

data/stocks/PLTR.md

Never overwrite reports for companies that were not requested.