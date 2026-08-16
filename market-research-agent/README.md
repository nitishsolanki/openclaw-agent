# Market Research Agent

A production-ready Python agent for daily market research, opportunity ranking, and risk-adjusted position sizing. Combines company-level watchlist analysis with live market data, macro regime detection, and sector-adjusted scoring.

## Overview

The Market Research Agent automates the workflow of:
- **Live data collection**: Real-time news, prices, and macro snapshots
- **Opportunity scoring**: Weighted model combining conviction, themes, catalysts, momentum, and risk
- **Sector rotation**: Thematic leadership analysis with sector-specific weighting
- **Macro regime detection**: Risk-on/risk-off positioning adjustments
- **Position sizing**: Risk-aware allocation based on score, macro, and conviction
- **Daily reporting**: Markdown reports with ranked ideas and actionable intelligence
- **Scheduled automation**: Daily, continuous, or manual execution modes

## Quick Start

### Prerequisites

- Python 3.14+
- Dependencies: `requests`, `yfinance` (optional for live data fallback)

### Installation

```bash
# Clone the repository
git clone https://github.com/nitishsolanki/openclaw-agent.git
cd openclaw-agent/market-research-agent

# Install optional dependencies for live data
pip install requests yfinance
```

### Single Run

```bash
python agent.py --root . --output-dir reports
```

Output:
- `reports/latest.md` — formatted daily market research report
- `reports/last_run.json` — structured data with rankings and state

### Daily Automation

```bash
# Run every day at 8:00 AM
python scheduler.py --mode daily --root . --run-time "08:00"

# Run every 4 hours
python scheduler.py --mode continuous --root . --interval 4

# Run once (useful for testing)
python scheduler.py --mode once --root .
```

See [SCHEDULER.md](SCHEDULER.md) for Windows Task Scheduler integration.

## Core Features

### 1. Weighted Opportunity Scoring

Each idea is scored on a 0–100 scale:

| Component | Weight | Notes |
|-----------|--------|-------|
| **Conviction** | 35 pt max | High/Medium/Low from watchlist summaries |
| **Theme Alignment** | 20 pt max | Keywords: AI, semiconductors, cloud, defense, cybersecurity |
| **Catalyst Strength** | 20 pt max | Earnings, guidance, backlog, demand, expansion signals |
| **Momentum** | 15 pt max | 5-day price change weighted × 3 |
| **Risk Offset** | 0–10 pt | Reduced for valuation, execution, competition concerns |

**Total**: Capped at 100 after sector and macro adjustments.

### 2. Sector-Adjusted Weighting

Scores are multiplied by sector weights reflecting market leadership:

| Sector | Multiplier | Themes |
|--------|-----------|--------|
| Semiconductors | 1.1× | AI infrastructure, data centers |
| Cybersecurity | 1.15× | Cloud security, defense |
| Defense | 1.2× | Government spending, contracting |
| Software | 1.0–1.05× | Enterprise, cloud, AI tools |
| Technology | 1.0× | Broad tech exposure |
| Other | 0.8–0.95× | Energy, space, mobility, automotive |

### 3. Macro Regime Detection

The agent reads macro headlines and adjusts scores:

- **Risk-On** (1.1× multiplier): Growth stocks, high-beta tech, semiconductors favored
- **Neutral** (1.0× multiplier): Balanced sector rotation
- **Risk-Off** (0.7× multiplier): Defensive positioning, lower-volatility names

### 4. Risk-Adjusted Position Sizing

Base allocation: 10% per position, adjusted by:
- Macro regime (risk-on/off/neutral)
- Conviction level (High/Medium/Low)
- Opportunity score (0–100)

**Range**: 2.5% minimum to 15% maximum per position.

Example:
- Score 75, High conviction, Risk-On regime → ~7.4% sizing
- Score 50, Medium conviction, Risk-Off regime → ~3.5% sizing

### 5. Daily Reporting

Generated reports include:

- **Market Overview**: Macro regime, news flow, risk posture
- **Sector Rotation**: Leadership breakdown by sector
- **Watchlist Opportunities**: Company summaries with conviction levels
- **Highest Conviction Ideas**: Top 5 ranked opportunities with:
  - Composite score (0–100)
  - Conviction level (High/Medium/Low)
  - Sector classification
  - Risk-adjusted position sizing (% of portfolio)
- **Position Sizing Methodology**: Transparent rules and constraints
- **Key Risks**: Macro, valuation, earnings, geopolitical factors

## Project Structure

```
market-research-agent/
├── agent.py                 # Core agent logic (live data, scoring, reporting)
├── scheduler.py             # Daily automation scheduler
├── SCHEDULER.md             # Scheduler setup guide
├── AGENTS.md               # Agent configuration
├── watchlist.txt           # Stock universe (30+ tickers)
├── tests/
│   └── test_market_research.py  # Regression test suite (8 tests)
├── data/
│   ├── macro/              # Macroeconomic snapshots (daily)
│   ├── news/               # Market news summaries
│   ├── sec-filings/        # SEC filing reviews
│   └── stocks/             # Company snapshots (NVDA, AMD, MSFT, etc.)
└── reports/
    ├── latest.md           # Latest generated report
    └── last_run.json       # Structured output and rankings
```

## API Reference

### Core Functions

#### `run_market_research(root, output_dir=None)`
Runs the full market research pipeline and generates reports.

**Returns:**
```json
{
  "status": "completed",
  "report_path": "reports/latest.md",
  "state_path": "reports/last_run.json"
}
```

#### `rank_opportunities(root, limit=5)`
Scores and ranks all watchlist symbols.

**Returns:**
```python
[
  {
    "symbol": "NVDA",
    "score": 85,
    "conviction": "High",
    "sector": "semiconductors",
    "components": {
      "conviction": 35,
      "theme": 20,
      "catalyst": 15,
      "momentum": 12,
      "risk": 3
    },
    "adjustments": {
      "sector_weight": 1.1,
      "macro_multiplier": 1.1
    },
    "position_size": {
      "position_size": 8500.0,
      "percent_portfolio": 8.5
    },
    "price": 123.45,
    "momentum_pct": 3.2
  },
  ...
]
```

#### `detect_macro_regime(root)`
Analyzes macro headlines and returns regime state.

**Returns:**
```python
{
  "regime": "risk-on",  # or "risk-off", "neutral"
  "risk_signal": 1.1,   # multiplier
  "conviction": "macro backdrop risk-on"
}
```

#### `calculate_position_size(score, regime, conviction, portfolio_size=100000)`
Computes risk-adjusted position allocation.

**Returns:**
```python
{
  "position_size": 8500.0,
  "percent_portfolio": 8.5,
  "units_at_price": "use_current_market_price"
}
```

## Testing

Run the regression test suite to verify functionality:

```bash
python -m pytest tests/test_market_research.py -q
```

Expected output:
```
........ 
8 passed in ~8s
```

Tests cover:
- Watchlist loading
- Report generation
- Ranking and sorting
- Scoring components and caps
- Macro regime detection
- Position sizing bounds
- Live news fetching
- SEC filing extraction

## Configuration

### Watchlist

Edit `watchlist.txt` to customize the stock universe:

```
NVDA
AMD
AVGO
MSFT
ORCL
CRM
KTOS
LMT
CRWD
...
```

### Market Data

The agent reads from local markdown files:

- `data/stocks/*.md` — Company analyses with conviction levels
- `data/macro/*.md` — Macroeconomic context
- `data/news/*.md` — Market headlines and summaries
- `data/sec-filings/*.md` — Recent filing reviews

All data is read-only; the agent generates fresh reports without modifying source files.

## Live Data Integration

The agent attempts to fetch live data with graceful fallback:

### Live News
- **Source**: Yahoo Finance RSS feeds
- **Fallback**: Local markdown summaries in `data/news/`
- **Frequency**: Per-run (scheduler controls execution)

### Live Prices
- **Source**: yfinance (5-day history, % change calculation)
- **Fallback**: Price snapshots embedded in `data/stocks/*.md`
- **Frequency**: Per-run

### Macro Data
- **Source**: Local markdown files in `data/macro/`
- **Regime Detection**: Keyword analysis (risk-on/risk-off/neutral)
- **Frequency**: Updated externally, read per-run

## Output Example

### Daily Report (latest.md)

```markdown
# Daily Market Research

## Market Overview

- **Macro Regime**: RISK-ON — favorable backdrop for high-beta, growth-oriented tech and semiconductors.
- Macro backdrop: [current macro context]
- News flow: [top headlines]
- Focus list: NVDA, AMD, AVGO, MSFT, ORCL
- Risk posture: risk on positioning based on macro analysis.

## Sector Rotation Analysis

- Semiconductors: NVDA, AMD, AVGO
- Defense: KTOS, LMT, RTX
- Software: MSFT, ORCL, CRM

## Highest Conviction Ideas + Risk-Adjusted Sizing

1. NVDA — score 85/100 (High conviction, semiconductors sector, 8.5% sizing)
2. AMD — score 82/100 (High conviction, semiconductors sector, 8.2% sizing)
3. AVGO — score 80/100 (High conviction, semiconductors sector, 8.0% sizing)
4. KTOS — score 76/100 (High conviction, defense sector, 7.6% sizing)
5. MSFT — score 72/100 (High conviction, software sector, 7.2% sizing)

## Summary

This framework blends current market headlines with company-level watchlist context, sector-adjusted conviction scoring, and macro regime weighting so the agent can prioritize actionable swing ideas with risk-aware position sizing and keep risk in front of conviction.
```

### State File (last_run.json)

```json
{
  "date": "2026-08-15",
  "status": "completed",
  "report": "reports/latest.md",
  "watchlist": ["NVDA", "AMD", "AVGO", ...],
  "rankings": [
    {
      "symbol": "NVDA",
      "score": 85,
      "conviction": "High",
      ...
    }
  ],
  "notes": "Market research run completed using live market data and watchlist context."
}
```

## Next Steps

Potential enhancements:

1. **LLM-based summarization** — Use Claude/GPT for polished market commentary
2. **Technical analysis** — Add RSI, MACD, moving averages for confirmation
3. **Real SEC EDGAR extraction** — Parse 10-K/10-Q for structured metrics
4. **Alert system** — Email/Slack summaries and threshold-based notifications
5. **Multi-agent orchestration** — Parallel runs for macro, sector, and stock analysis
6. **Portfolio optimization** — Mean-variance allocation within sizing bounds

## License

MIT License — see LICENSE file for details.

## Contributing

Contributions welcome! Areas of focus:
- Enhanced scoring models
- Real-time data source integration
- UI/visualization for reports
- Cloud deployment (AWS Lambda, etc.)

## Support

- **Documentation**: [SCHEDULER.md](SCHEDULER.md) for automation setup
- **Tests**: Run `pytest` to verify functionality
- **Logs**: Check `scheduler.log` for scheduled execution traces
- **Issues**: File issues on GitHub with:
  - Python version and environment details
  - Exact command that failed
  - Error output and relevant logs

---

**Status**: Production-ready. Used for daily market research and opportunity ranking.

**Last Updated**: 2026-08-15
