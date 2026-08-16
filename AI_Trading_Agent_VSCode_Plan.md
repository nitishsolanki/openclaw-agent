# AI Trading Agent --- OpenClaw + Python + Alpaca

## 1. Project Goal

Build a cost-effective AI-assisted trading system that can be operated
from Telegram through OpenClaw.

The system will:

-   Scan the U.S. stock market.
-   Identify sector rotation and market regime.
-   Rank stocks using relative strength, VWAP, volume, momentum,
    volatility, and options signals.
-   Produce a 0--100 trade score.
-   Generate a structured trade setup with entry, stop, targets,
    risk/reward, and rationale.
-   Support paper trading first.
-   Keep deterministic risk controls outside the LLM.
-   Eventually support live execution through a broker/execution layer.
-   Maintain a trade journal so the strategy can be measured and
    improved.

### Core principle

**Python/quantitative code determines the facts and enforces risk. The
AI interprets those facts and orchestrates the workflow.**

Do not allow the LLM to bypass risk controls or directly invent position
sizes, stops, or orders.

------------------------------------------------------------------------

# 2. Target Architecture

``` text
                         TELEGRAM
                            |
                            v
                     +-------------+
                     |   OpenClaw  |
                     |  AI Agent   |
                     +------+------+
                            |
                    Trading Skills
                            |
          +-----------------+-----------------+
          |                 |                 |
          v                 v                 v
    Market Scanner    Stock Analyzer    Trade Manager
          |                 |                 |
          +-----------------+-----------------+
                            |
                            v
                  +--------------------+
                  | Quant Engine       |
                  |                    |
                  | Market Regime      |
                  | Sector Rotation    |
                  | Relative Strength  |
                  | VWAP               |
                  | Volume             |
                  | Momentum           |
                  | Volatility         |
                  | Options            |
                  +---------+----------+
                            |
                            v
                  +--------------------+
                  | Signal Scoring     |
                  | 0 - 100            |
                  +---------+----------+
                            |
                            v
                  +--------------------+
                  | Risk Engine        |
                  |                    |
                  | Position sizing    |
                  | Max loss           |
                  | Max exposure       |
                  | Stop/target        |
                  | R:R requirement    |
                  +---------+----------+
                            |
                 +----------+----------+
                 |                     |
                 v                     v
          Paper Trading          Live Execution
                                   (later)
                 |
                 v
          Trade Journal / DB
```

------------------------------------------------------------------------

# 3. Recommended Low-Cost Technology Stack

  -------------------------------------------------------------------------
  Component               Initial Choice          Purpose
  ----------------------- ----------------------- -------------------------
  Agent                   OpenClaw                Telegram
                                                  interface/orchestration

  AI                      Low-cost capable LLM    Reasoning and explanation

  Language                Python 3.12+            Quantitative engine

  Market data             Alpaca free/basic tier  Development market data
                          initially               

  Trading                 Alpaca paper trading    Safe execution testing
                          initially               

  Database                SQLite                  Signals/trades/config

  API                     FastAPI                 Local service boundary

  Scheduling              APScheduler / cron      Periodic scans

  Indicators              pandas + numpy +        Technical indicators
                          pandas-ta or custom     
                          formulas                

  Testing                 pytest                  Unit/integration tests

  Config                  YAML                    Strategy parameters

  Containerization        Docker                  Optional later

  Version control         Git                     Source control
  -------------------------------------------------------------------------

Keep the first version on the existing computer/server. Do not pay for
cloud infrastructure until the strategy proves useful.

------------------------------------------------------------------------

# 4. Development Phases

## Phase 0 --- Repository and Environment

### Goal

Create a clean VS Code project with reproducible local development.

### Tasks

-   [ ] Create Git repository.
-   [ ] Create Python virtual environment.
-   [ ] Add `requirements.txt` or `pyproject.toml`.
-   [ ] Add `.env.example`.
-   [ ] Add `.gitignore`.
-   [ ] Add logging configuration.
-   [ ] Add basic pytest setup.
-   [ ] Add README.
-   [ ] Create configuration files.
-   [ ] Create SQLite database initialization.

### Initial directory structure

``` text
ai-trading-agent/
|
+-- README.md
+-- pyproject.toml
+-- .env.example
+-- .gitignore
+-- docker-compose.yml
|
+-- config/
|   +-- strategy.yaml
|   +-- sectors.yaml
|   +-- risk.yaml
|
+-- src/
|   +-- main.py
|   |
|   +-- config/
|   |   +-- settings.py
|   |
|   +-- data/
|   |   +-- market_data.py
|   |   +-- universe.py
|   |   +-- cache.py
|   |
|   +-- indicators/
|   |   +-- vwap.py
|   |   +-- trend.py
|   |   +-- momentum.py
|   |   +-- volatility.py
|   |   +-- volume.py
|   |   +-- relative_strength.py
|   |
|   +-- market/
|   |   +-- regime.py
|   |   +-- breadth.py
|   |
|   +-- sector/
|   |   +-- rotation.py
|   |   +-- ranking.py
|   |
|   +-- screening/
|   |   +-- stock_screener.py
|   |   +-- candidate_ranker.py
|   |
|   +-- signals/
|   |   +-- scoring.py
|   |   +-- signal.py
|   |
|   +-- risk/
|   |   +-- risk_engine.py
|   |   +-- position_sizing.py
|   |   +-- trade_limits.py
|   |
|   +-- execution/
|   |   +-- broker.py
|   |   +-- paper_trader.py
|   |   +-- order_manager.py
|   |
|   +-- portfolio/
|   |   +-- positions.py
|   |   +-- pnl.py
|   |
|   +-- journal/
|   |   +-- database.py
|   |   +-- trade_journal.py
|   |
|   +-- api/
|       +-- routes.py
|       +-- models.py
|
+-- tests/
|   +-- indicators/
|   +-- sector/
|   +-- screening/
|   +-- signals/
|   +-- risk/
|   +-- execution/
|
+-- openclaw/
    +-- skills/
        +-- trading-agent/
        |   +-- SKILL.md
        |
        +-- market-scanner/
        |   +-- SKILL.md
        |
        +-- stock-analyzer/
        |   +-- SKILL.md
        |
        +-- risk-manager/
        |   +-- SKILL.md
        |
        +-- trade-journal/
            +-- SKILL.md
```

------------------------------------------------------------------------

# 5. Phase 1 --- Market Data Layer

## Goal

Create a single normalized interface for market data.

Do not let the rest of the application depend directly on the broker
API.

Create:

``` python
class MarketDataProvider:
    def get_quote(self, symbol):
        ...

    def get_bars(self, symbol, timeframe, start, end):
        ...

    def get_volume(self, symbol):
        ...

    def get_snapshot(self, symbol):
        ...
```

Later implementations can include:

``` text
AlpacaMarketDataProvider
PolygonMarketDataProvider
OtherProvider
```

The rest of the system should not care which provider is being used.

### Data required

For stocks:

-   OHLCV
-   Daily bars
-   Intraday bars
-   Quote
-   Volume
-   Average volume
-   Market capitalization
-   Sector
-   Benchmark

For initial development, prioritize:

1.  SPY
2.  QQQ
3.  IWM
4.  Sector ETFs
5.  Candidate stocks

------------------------------------------------------------------------

# 6. Phase 2 --- Market Regime Engine

Create a market regime score from 0--100.

### Inputs

-   SPY trend
-   QQQ trend
-   IWM trend
-   Price vs VWAP
-   20 EMA
-   50 EMA
-   200 EMA
-   VIX
-   Market breadth
-   Nasdaq relative strength
-   Volume

Example:

``` text
Market Regime Score = 0–100

80–100  Strong Bull
65–79   Bull
45–64   Neutral
30–44   Bear
0–29    Strong Bear
```

The regime should influence how aggressive the stock scanner is.

Example:

``` text
Strong Bull:
    allow scores >= 75

Neutral:
    allow scores >= 82

Bear:
    allow scores >= 90

Strong Bear:
    no new long trades
```

These thresholds must be configurable.

------------------------------------------------------------------------

# 7. Phase 3 --- Sector Rotation Engine

Track major sector ETFs.

Initial universe:

``` text
XLK  Technology
XLF  Financials
XLE  Energy
XLV  Healthcare
XLI  Industrials
XLY  Consumer Discretionary
XLP  Consumer Staples
XLU  Utilities
XLB  Materials
XLRE Real Estate
XLC  Communication Services
```

### Calculate

For each sector:

-   1D return
-   5D return
-   10D return
-   20D return
-   Relative strength vs SPY
-   Relative strength vs QQQ
-   Volume vs average
-   VWAP position
-   Trend
-   Momentum

### Example sector score

``` text
Sector Score =
    20%  5D relative strength
    20%  10D relative strength
    15%  20D relative strength
    15%  trend
    15%  volume
    15%  VWAP/momentum
```

Make all weights configurable.

### Output

``` text
Technology       91
Industrials      86
Energy           78
Financials       72
Healthcare       61
Utilities        43
Real Estate      35
```

------------------------------------------------------------------------

# 8. Phase 4 --- Stock Screener

Start with a broad universe and progressively reduce it.

``` text
~5,000 stocks
       |
       v
Liquidity filter
       |
       v
~1,000
       |
       v
Sector filter
       |
       v
~500
       |
       v
Trend filter
       |
       v
~200
       |
       v
Relative strength
       |
       v
~100
       |
       v
VWAP + volume
       |
       v
~30
       |
       v
Signal scoring
       |
       v
Top 10
       |
       v
AI analysis
```

### Initial filters

``` text
Price > $5
Average daily volume > configurable threshold
Market cap > configurable threshold
Price > 20 EMA
20 EMA > 50 EMA
Relative strength > threshold
Volume ratio > threshold
```

Avoid over-filtering initially.

------------------------------------------------------------------------

# 9. Phase 5 --- VWAP Engine

VWAP is a core part of the strategy.

Implement:

### Standard intraday VWAP

``` text
VWAP = cumulative(price * volume) / cumulative(volume)
```

Use typical price initially:

``` text
(H + L + C) / 3
```

### Signals

Detect:

-   Price above VWAP
-   Price below VWAP
-   VWAP reclaim
-   VWAP rejection
-   VWAP breakout
-   VWAP breakdown
-   VWAP slope
-   Distance from VWAP
-   Volume confirmation

Example bullish setup:

``` text
Price crosses above VWAP
AND
VWAP slope > 0
AND
volume > 1.5x average
AND
relative strength > threshold
```

------------------------------------------------------------------------

# 10. Phase 6 --- Relative Strength Engine

For each stock calculate:

``` text
RS 1D
RS 5D
RS 20D
RS 60D
```

Basic calculation:

``` text
RS = stock return - benchmark return
```

Benchmark selection:

``` text
Technology      QQQ / XLK
Financials      SPY / XLF
Energy          SPY / XLE
General market  SPY
```

Rank stocks within their sector.

A stock can receive a major score boost when:

``` text
Sector strong
+
Stock outperforming sector
+
Stock outperforming SPY
```

------------------------------------------------------------------------

# 11. Phase 7 --- Technical Indicator Engine

Initial indicators:

### Trend

-   EMA 20
-   EMA 50
-   EMA 200
-   ADX

### Momentum

-   RSI
-   MACD
-   ROC

### Volatility

-   ATR
-   ATR percentage

### Volume

-   Volume SMA
-   Relative volume
-   Volume spike

### Price structure

-   Previous day high/low
-   Support
-   Resistance
-   Recent high/low
-   Breakout distance

Do not initially add dozens of indicators.

The objective is to determine which signals actually improve results.

------------------------------------------------------------------------

# 12. Phase 8 --- Options / IV Engine

This should be Phase 2 of the project, not MVP.

Potential inputs:

-   IV
-   IV rank
-   IV percentile
-   Put/call ratio
-   Options volume
-   Open interest
-   Unusual options activity
-   Expected move
-   Earnings date

Use options primarily as confirmation.

Example:

``` text
Technical Score      85
Sector Score         90
Relative Strength    93
Volume Score         88
Options Score        74
Risk Score           80

Final Score           87
```

------------------------------------------------------------------------

# 13. Phase 9 --- Signal Scoring

Create one standardized signal object.

``` python
@dataclass
class TradeSignal:
    symbol: str
    direction: str
    market_score: float
    sector_score: float
    trend_score: float
    vwap_score: float
    relative_strength_score: float
    volume_score: float
    momentum_score: float
    volatility_score: float
    options_score: float
    risk_score: float
    final_score: float
```

### Initial scoring model

``` text
Market regime             10%
Sector rotation            20%
Relative strength          20%
VWAP                       15%
Trend                      10%
Volume                     10%
Momentum                    5%
Volatility                  5%
Options                     5%
```

Then apply risk penalties.

### Suggested interpretation

``` text
90–100  A+ setup
85–89   Strong setup
80–84   Good setup
75–79   Watch
<75     No trade
```

These thresholds should be configuration values, not hard-coded.

------------------------------------------------------------------------

# 14. Phase 10 --- Risk Engine

This is a critical component.

The risk engine must be deterministic.

### Initial rules

``` text
Risk per trade:          0.5% of account
Maximum position:       10% of account
Maximum sector exposure:25%
Maximum daily loss:      2%
Maximum open positions:   8
Minimum R:R:              2.0
```

All values configurable.

### Position sizing

Basic formula:

``` text
risk_dollars =
    account_value * risk_percent

risk_per_share =
    abs(entry - stop)

shares =
    risk_dollars / risk_per_share
```

Then cap by:

-   maximum position size
-   liquidity
-   sector exposure
-   portfolio exposure

------------------------------------------------------------------------

# 15. Trade Setup Generator

For every candidate produce:

``` text
Symbol
Direction
Current Price

Market Regime
Sector
Sector Score
Relative Strength

VWAP
VWAP Distance
Volume Ratio
RSI
MACD
ATR

Entry
Stop
Target 1
Target 2
Risk/Reward

Position Size
Dollar Risk

Signal Score
Confidence

Reasons
Risks
Invalidation
```

Example:

``` text
APP — LONG

Signal Score: 88/100

Market: Bullish
Sector: Technology
Sector Score: 91
Relative Strength: 94
Price vs VWAP: +2.1%
Volume: 1.9x
RSI: 64
ATR: 4.2%

Entry: $XXX–$XXX
Stop: $XXX
Target 1: $XXX
Target 2: $XXX

R:R: 2.7

Why:
1. Technology is leading.
2. APP is outperforming QQQ.
3. Price reclaimed VWAP.
4. Volume confirms the move.

Risk:
- Extended from VWAP
- Elevated volatility
```

------------------------------------------------------------------------

# 16. OpenClaw Skills

## trading-agent/SKILL.md

Purpose:

Main conversational interface.

Commands:

``` text
/scan
/analyze APP
/setup APP
/positions
/orders
/pnl
/journal
/status
```

Natural language should also work:

``` text
scan market

find strongest stocks

analyze APP

what sectors are receiving money

show me today's top setups

should I buy VST?
```

------------------------------------------------------------------------

## market-scanner/SKILL.md

Responsibilities:

-   Get market regime.
-   Get sector rotation.
-   Run stock screener.
-   Rank candidates.
-   Return top candidates.

------------------------------------------------------------------------

## stock-analyzer/SKILL.md

Responsibilities:

-   Analyze a symbol.
-   Retrieve all quantitative signals.
-   Build trade setup.
-   Explain the setup.

------------------------------------------------------------------------

## risk-manager/SKILL.md

Responsibilities:

-   Validate proposed trade.
-   Calculate position size.
-   Check portfolio exposure.
-   Reject invalid trades.
-   Enforce hard limits.

The AI must never override this skill.

------------------------------------------------------------------------

## trade-journal/SKILL.md

Responsibilities:

-   Record every signal.
-   Record every trade.
-   Record reasoning.
-   Record outcome.
-   Calculate performance.

------------------------------------------------------------------------

# 17. Telegram Interface

Initial commands:

``` text
/scan
```

Returns top market opportunities.

``` text
/analyze APP
```

Returns detailed APP analysis.

``` text
/sectors
```

Returns sector rotation.

``` text
/market
```

Returns market regime.

``` text
/setup APP
```

Returns complete trade setup.

``` text
/positions
```

Returns current positions.

``` text
/pnl
```

Returns portfolio P&L.

``` text
/journal
```

Returns recent trades/signals.

``` text
/status
```

Returns system health.

------------------------------------------------------------------------

# 18. Execution Safety Model

Never go directly from:

``` text
AI → Broker
```

Use:

``` text
AI
 |
 v
Signal
 |
 v
Risk Engine
 |
 v
Policy Check
 |
 v
Order Manager
 |
 v
Broker
```

### Execution modes

``` yaml
execution_mode: paper
```

Supported values:

``` text
disabled
signal_only
paper
live
```

Default:

``` text
signal_only
```

Never make `live` the default.

------------------------------------------------------------------------

# 19. Three-Stage Validation

## Stage 1 --- Backtest

Use historical data.

Questions:

-   Does the strategy make money?
-   Maximum drawdown?
-   Win rate?
-   Average winner?
-   Average loser?
-   Sharpe?
-   Profit factor?
-   Number of trades?

## Stage 2 --- Paper trading

Run live signals without real money.

Minimum target:

``` text
100+ trades
```

Track:

-   slippage
-   entry quality
-   stop execution
-   signal latency
-   win rate
-   drawdown

## Stage 3 --- Small live deployment

Only after paper validation.

Start with a very small account allocation.

Gradually increase only if the live results remain consistent.

------------------------------------------------------------------------

# 20. Trade Journal Database

Initial tables:

## signals

``` text
id
timestamp
symbol
direction
market_score
sector_score
rs_score
vwap_score
volume_score
momentum_score
final_score
entry
stop
target
reasoning
```

## trades

``` text
id
signal_id
symbol
side
quantity
entry_price
exit_price
stop_price
target_price
status
realized_pnl
created_at
closed_at
```

## portfolio_snapshots

``` text
timestamp
account_value
cash
equity
daily_pnl
drawdown
```

## sector_snapshots

``` text
timestamp
sector
return_1d
return_5d
return_10d
relative_strength
volume_ratio
score
rank
```

------------------------------------------------------------------------

# 21. Performance Analytics

After enough trades, calculate:

``` text
Win rate
Average win
Average loss
Profit factor
Expectancy
Maximum drawdown
Average R
Sharpe ratio
Sortino ratio
```

Also segment results by:

``` text
Market regime
Sector
Signal score
VWAP setup
Relative strength
Volume
Time of day
Day of week
Holding period
```

This allows the system to discover which signals actually work.

------------------------------------------------------------------------

# 22. Configuration-Driven Strategy

Do not hard-code strategy values.

Example `config/strategy.yaml`:

``` yaml
screening:
  minimum_price: 5
  minimum_average_volume: 1000000

signals:
  market_regime_weight: 0.10
  sector_weight: 0.20
  relative_strength_weight: 0.20
  vwap_weight: 0.15
  trend_weight: 0.10
  volume_weight: 0.10
  momentum_weight: 0.05
  volatility_weight: 0.05
  options_weight: 0.05

thresholds:
  strong_setup: 85
  minimum_trade_score: 80
  minimum_rr: 2.0

vwap:
  volume_confirmation_ratio: 1.5

risk:
  risk_per_trade: 0.005
  max_position_percent: 0.10
  max_sector_percent: 0.25
  max_daily_loss_percent: 0.02
  max_open_positions: 8
```

This makes strategy experimentation much easier.

------------------------------------------------------------------------

# 23. AI Prompt Strategy

The AI should receive structured data rather than raw market data.

Example:

``` json
{
  "symbol": "APP",
  "market_regime": {
    "score": 78,
    "direction": "bullish"
  },
  "sector": {
    "name": "Technology",
    "score": 91,
    "rank": 1
  },
  "stock": {
    "relative_strength": 94,
    "vwap_score": 88,
    "volume_score": 90,
    "trend_score": 87,
    "momentum_score": 82
  },
  "risk": {
    "score": 80,
    "minimum_rr": 2.0
  }
}
```

The AI then answers:

``` text
1. Is the setup valid?
2. What are the strongest reasons?
3. What invalidates the trade?
4. What risks exist?
5. What action is appropriate?
```

Do not ask the AI to calculate indicators when Python can calculate them
reliably.

------------------------------------------------------------------------

# 24. MVP Definition

The first working version should NOT include everything.

### MVP v1

Build only:

``` text
Market regime
+
Sector rotation
+
Stock universe
+
Relative strength
+
VWAP
+
Volume
+
EMA trend
+
Signal score
+
Risk engine
+
Telegram
+
Paper trading
+
Trade journal
```

Do NOT initially build:

``` text
Options flow
News sentiment
Machine learning
Multiple brokers
Cloud infrastructure
Complex UI
Autonomous live trading
```

Those come later.

------------------------------------------------------------------------

# 25. Suggested Build Order

## Sprint 1

``` text
[ ] Repository
[ ] Python environment
[ ] Configuration
[ ] Logging
[ ] SQLite
[ ] Market data provider
[ ] SPY/QQQ data
```

## Sprint 2

``` text
[ ] Indicators
[ ] VWAP
[ ] EMA
[ ] RSI
[ ] ATR
[ ] Volume ratio
[ ] Relative strength
```

## Sprint 3

``` text
[ ] Market regime
[ ] Sector rotation
[ ] Sector ranking
```

## Sprint 4

``` text
[ ] Stock universe
[ ] Screening
[ ] Candidate ranking
[ ] Signal scoring
```

## Sprint 5

``` text
[ ] Risk engine
[ ] Position sizing
[ ] Trade setup generator
```

## Sprint 6

``` text
[ ] Alpaca paper trading
[ ] Order manager
[ ] Portfolio tracking
```

## Sprint 7

``` text
[ ] OpenClaw skills
[ ] Telegram commands
[ ] Natural language interface
```

## Sprint 8

``` text
[ ] Trade journal
[ ] Performance analytics
[ ] Backtesting
```

## Sprint 9

``` text
[ ] Options/IV
[ ] Earnings filter
[ ] News
```

## Sprint 10

``` text
[ ] Strategy optimization
[ ] Paper trading validation
[ ] Small live deployment
```

------------------------------------------------------------------------

# 26. VS Code Development Workflow

Open the repository in VS Code.

Recommended extensions:

-   Python
-   Pylance
-   Python Debugger
-   YAML
-   GitLens (optional)
-   Docker (optional)

Run:

``` bash
python -m venv .venv
```

Activate the environment.

Then:

``` bash
pip install -r requirements.txt
```

Run tests:

``` bash
pytest
```

Run the application:

``` bash
python -m src.main
```

------------------------------------------------------------------------

# 27. Environment Variables

Create `.env`:

``` text
ALPACA_API_KEY=
ALPACA_SECRET_KEY=

OPENAI_API_KEY=

TELEGRAM_BOT_TOKEN=

DATABASE_URL=sqlite:///trading.db

EXECUTION_MODE=signal_only
```

Never commit `.env`.

Commit only:

``` text
.env.example
```

------------------------------------------------------------------------

# 28. Important Engineering Rules

### Rule 1

**No LLM-generated order parameters without validation.**

### Rule 2

**Risk engine always runs before execution.**

### Rule 3

**Live trading is disabled by default.**

### Rule 4

**Every trade decision is journaled.**

### Rule 5

**Every signal must be reproducible from stored market data.**

### Rule 6

**All strategy thresholds are configurable.**

### Rule 7

**Never optimize the strategy against future data.**

Avoid look-ahead bias.

### Rule 8

**Separate signal generation from execution.**

### Rule 9

**Paper trade before live trade.**

### Rule 10

**Do not continuously change the strategy based on a handful of
trades.**

------------------------------------------------------------------------

# 29. First Milestone

The first meaningful milestone is:

> "I can type `/scan` in Telegram and receive the top 10 stocks based on
> market regime + sector rotation + relative strength + VWAP + volume +
> trend, with a 0--100 score."

Example:

``` text
MARKET: BULLISH 78

TOP SETUPS

1. APP   91
   Technology #1
   RS: 94
   VWAP: +2.1%
   Volume: 1.9x

2. VST   87
   Utilities #3
   RS: 88
   VWAP: +1.7%
   Volume: 1.6x

3. NVDA  85
   Technology #1
   RS: 91
   VWAP: +1.2%
   Volume: 1.5x
```

That is the first version worth building.

------------------------------------------------------------------------

# 30. Second Milestone

Type:

``` text
/analyze APP
```

Receive:

``` text
APP — LONG SETUP

Score: 91/100

Market       78
Sector       91
RS           94
VWAP         88
Volume       90
Trend        87

Entry        $XXX
Stop         $XXX
Target 1     $XXX
Target 2     $XXX
R:R          2.6

Risk         Medium

Decision:
VALID LONG SETUP

Invalidation:
Price loses VWAP with high volume.
```

------------------------------------------------------------------------

# 31. Third Milestone

Type:

``` text
/trade APP
```

The system should NOT immediately trade.

Instead:

``` text
Trade requested
      |
      v
Signal validation
      |
      v
Risk validation
      |
      v
Portfolio validation
      |
      v
Execution policy
      |
      v
Paper order
```

Return:

``` text
PAPER ORDER APPROVED

APP
BUY
25 shares
Entry: $XXX
Stop: $XXX
Risk: $XXX
Maximum allowed risk: $XXX
```

------------------------------------------------------------------------

# 32. Long-Term Architecture

Once the core system works:

``` text
                AI Trading Platform
                       |
       +---------------+----------------+
       |               |                |
       v               v                v
   Market AI       Portfolio AI      Research AI
       |               |                |
       v               v                v
 Sector/Stocks     Positions         Backtesting
       |               |                |
       +---------------+----------------+
                       |
                       v
                 Risk Engine
                       |
                       v
                 Execution API
                       |
              +--------+--------+
              |                 |
            Alpaca          Robinhood
```

Future capabilities:

-   Earnings analysis
-   News sentiment
-   Unusual options activity
-   Intraday alerts
-   Position management
-   Automated exits
-   Strategy backtesting
-   Walk-forward testing
-   Multiple strategies
-   ML-based ranking
-   Performance dashboard

------------------------------------------------------------------------

# 33. Definition of Done for V1

V1 is complete when all of the following work:

-   [ ] Market data loads reliably.
-   [ ] Indicators calculate correctly.
-   [ ] Sector rotation produces rankings.
-   [ ] Relative strength ranking works.
-   [ ] VWAP signals work.
-   [ ] Stock screener produces candidates.
-   [ ] Signal score is reproducible.
-   [ ] Risk engine rejects invalid trades.
-   [ ] Position sizing works.
-   [ ] Telegram `/scan` works.
-   [ ] Telegram `/analyze SYMBOL` works.
-   [ ] Paper order can be created.
-   [ ] Every signal is journaled.
-   [ ] Every paper trade is journaled.
-   [ ] Basic performance report works.
-   [ ] Live execution remains disabled.

------------------------------------------------------------------------

# 34. Immediate Next Coding Task

Start with these five files:

``` text
src/data/market_data.py
src/indicators/vwap.py
src/indicators/relative_strength.py
src/sector/rotation.py
src/signals/scoring.py
```

Then implement this pipeline:

``` text
Market Data
    ↓
Sector Rotation
    ↓
Relative Strength
    ↓
VWAP
    ↓
Volume
    ↓
Trend
    ↓
Signal Score
```

Once that works, add the risk engine and OpenClaw integration.

**Do not start with autonomous trading. Start with a reliable scanner.**

That gives you the cheapest and safest path from an idea to a working AI
trading system.
