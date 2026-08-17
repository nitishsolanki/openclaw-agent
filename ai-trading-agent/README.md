# AI Trading Agent

Initial scanner foundation for the plan in `AI_Trading_Agent_VSCode_Plan.md`.
This package is signal-only: it does not connect to a broker or place orders.

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

## Optional API

```bash
python -m pip install -e ".[api]"
uvicorn ai_trading_agent.api.routes:create_app --factory --port 8000
```

Available endpoints are `/health` and `/scan`. The default execution policy is
`signal_only`; no endpoint places orders.
