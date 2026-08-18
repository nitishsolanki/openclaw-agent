# AI Trading Agent

Initial scanner foundation for the plan in `AI_Trading_Agent_VSCode_Plan.md`.
This package is signal-only: it does not connect to a broker or place orders.

## Current status

### Completed

- Project packaging with editable installation through `pyproject.toml`.
- YAML strategy configuration and configurable signal weights.
- Normalized market-data boundary with:
  - In-memory data for tests.
  - CSV data for offline development.
  - Read-only Alpaca adapter (optional dependency).
- Technical calculations:
  - VWAP and VWAP distance.
  - Volume ratio.
  - EMA-based trend score.
  - Relative strength versus a benchmark.
  - Momentum score.
- Market-regime detection using benchmark trend.
- Candidate scanner with reproducible 0–100 signal scoring.
- Sample OHLCV data for offline testing.
- Deterministic ATR-based trade setup generation.
- Deterministic risk engine with:
  - Risk-per-trade limits.
  - Maximum position size.
  - Sector exposure limits.
  - Daily-loss limits.
  - Maximum open positions.
  - Minimum risk/reward validation.
- SQLite signal journal and initial trade schema.
- Execution policy gate with `disabled`, `signal_only`, `paper`, and `live` modes.
- Read-only FastAPI endpoints: `/health`, `/scan`, and `/paper/orders`.
- Local paper-trading simulator with risk-gated order creation, fills, exits,
  P&L calculation, and SQLite persistence.
- Basic portfolio performance analytics and moving-average backtesting.
- OpenClaw trading-agent skill instructions and paper-order API endpoint.
- `.env.example` with signal-only defaults.
- Local `local.env` loading plus paper-only Alpaca and Telegram routing adapters.
- Automated test suite with 20 passing tests.

### Pending

- Replace sample sector scores with live sector ETF rotation data.
- Add complete stock-universe and liquidity filtering.
- Connect the Telegram router to a running bot and add `/analyze` and `/setup` response generation.
- Add Alpaca paper-order submission and reconciliation after installing `alpaca-py`.
- Add richer trade outcome journaling and walk-forward validation.
- Add real paper-trading validation with slippage and latency tracking.
- Add options/IV confirmation, earnings filters, and news analysis.
- Add Docker/container deployment support.
- Validate the strategy through a substantial paper-trading sample.

### Explicitly disabled

- Live broker execution.
- Autonomous live trading.
- LLM-generated orders without deterministic risk validation.

Current milestone: the offline scanner, deterministic risk engine, and local
paper-trading model are working. The system is not investment advice and should
not be used for live trading without independent validation.

## Run tests

```bash
python -m pytest
```

## Run the offline scanner

Install the package in editable mode, then run:

```bash
python -m pip install -e .
python -m ai_trading_agent scan
```

The command uses `data/sample/`, prints ranked signal candidates, and writes
signals to `trading.db`. It does not place orders.

## Local environment

Copy or edit `local.env` for machine-specific credentials and settings. It is
ignored by Git and must never be committed. Keep `EXECUTION_MODE=signal_only`
until paper-trading validation is complete.

## Optional API

```bash
python -m pip install -e ".[api]"
uvicorn ai_trading_agent.api.routes:create_app --factory --port 8000
```

Available endpoints are `/health`, `/scan`, and `/paper/orders`. The default execution policy is
`signal_only`; no endpoint places orders.
