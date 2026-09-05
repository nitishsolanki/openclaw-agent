# AI Trading Agent

The AI Trading Agent is a signal-only stock scanner and paper-trading framework. It
combines deterministic Python technical signals with optional market, sector, news,
earnings, options, and OpenClaw research inputs. It does not place live broker orders.

## How the agent works

1. Load the configured stock universe and OHLCV price data.
2. In live mode, remove stocks that fail the price, liquidity, history, or spread checks.
3. Calculate a 0–100 score for every remaining candidate.
4. Rank candidates and keep the top 10.
5. Label scores of 50 or higher `LONG`; lower scores are `WATCH`.
6. Record signals in SQLite and optionally create risk-checked paper trades.
7. Optionally enrich the top candidates with OpenClaw research; research changes the
   ranking blend but does not bypass deterministic risk controls.

## Quick start

From this directory:

```powershell
python -m pip install -e .
python -m ai_trading_agent scan

# Choose a scoring profile
python -m ai_trading_agent scan --profile day
python -m ai_trading_agent scan --profile swing
python -m ai_trading_agent scan --profile growth
```

This uses the offline sample data and writes signals to `trading.db`.

For the local API and Telegram bot, use separate terminals:

```powershell
python scripts/run_api.py
python scripts/run_telegram.py
```

Useful Telegram commands are `/scan`, `/sectors`, `/analyze SYMBOL`,
`/setup SYMBOL`, `/positions`, `/pnl`, and `/status`. `/analyze` is informational;
`/setup` calculates a possible entry, stop, target, and share quantity subject to
risk rules.

## Python stock-filtering rules

The main liquidity filters are implemented in
`src/ai_trading_agent/data/bars_batch.py`, function `fetch_liquid_bars()`.
Universe loading and live/offline selection are handled in
`src/ai_trading_agent/cli.py`, function `run_scan()`.

In live mode, `fetch_liquid_bars()` excludes a symbol when any of these checks fail:

| Rule | Requirement |
|---|---:|
| Minimum price | At least $10.00 |
| Price history | At least 60 bars |
| Average share volume | At least 1,000,000 shares over the latest 20 bars |
| Average dollar volume | At least $25,000,000 over the latest 20 bars |
| Median dollar volume | At least $15,000,000 over the latest 20 bars |
| Bid/ask spread | No more than 0.50%, when available |

Empty data, provider errors, or failed calculations also exclude the symbol. Offline
mode currently uses the sample universe (`AAA`, `BBB`, and `CCC`) and does not apply
the live liquidity download path.

After liquidity filtering, `run_scan()` may also apply the active weekly theme filter
in offline mode. In live mode it enriches sector names and applies sector scores;
these affect ranking rather than eligibility. The final scanner in
`src/ai_trading_agent/screening/scanner.py`, function `scan()`, sorts eligible stocks
by score and keeps the top 10.

These are eligibility and ranking rules, not trade approval. A stock that passes the
filters is scored and ranked; it is not automatically approved for a trade.

## Scoring profiles

Profiles are stored in `config/strategy_day.yaml`, `config/strategy_swing.yaml`,
and `config/strategy_growth.yaml`. The default is `swing`.

- `day`: emphasizes VWAP, current volume, momentum, and relative strength. Use with
  intraday bars; the current data adapter may still provide daily bars.
- `swing`: balances sector, trend, relative strength, VWAP, volume, and momentum for
  multi-day setups.
- `growth`: emphasizes market regime, sector, trend, and longer-horizon relative
  strength, with less dependence on current VWAP and volume. It is currently a
  technical growth proxy, not a fundamental long-term investing model.

See [Trading Candidate Profiles.md](Trading%20Candidate%20Profiles.md) for the
Day, Swing, and Growth top-candidate sections, profile weights, and Python
scoring rules.

## Current status

### Completed

- Offline and live stock scanning with reproducible 0–100 Python scoring.
- Price, liquidity, history, spread, sector, market-regime, news, earnings, and options inputs.
- Deterministic ATR trade setups and risk controls for paper trading.
- FastAPI, Telegram, SQLite journaling, paper-trading, backtesting, and validation tools.
- OpenClaw research handoff with a 70/30 Python/research ranking blend.
- Scheduled paper checks, sector rotation, GitHub Pages reports, Docker support, and automated tests.

### Pending

- Connect live sector rotation directly to the CLI universe.
- Finish broker fill polling and automatic reconciliation scheduling.
- Verify and connect live options confirmation to final ranking.
- Schedule weekly theme refresh and validate the active-theme filter.
- Accumulate a larger paper-trading sample for performance validation.

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

## GitHub Pages deployment

The workflow in `.github/workflows/market-pages.yml` generates reports at 9:35 AM
and 2:00 PM Chicago time on weekdays. Add `ALPACA_API_KEY`,
`ALPACA_SECRET_KEY`, `FINNHUB_API_KEY`, and `POLYGON_API_KEY` as repository
Actions secrets, then enable GitHub Pages with **GitHub Actions** as the source.

## Start local services

From the project directory, start the API and Telegram polling in separate
terminals:

```powershell
python scripts/run_api.py
python scripts/run_telegram.py
```

Telegram polling is signal-only. It does not submit broker orders.
## Local OpenClaw research handoff

To enrich the trading agent's top five candidates with local OpenClaw research:

```powershell
python scripts/prepare_research_handoff.py
```

Ask the local OpenClaw research agent to read `reports/openclaw_research_prompt.md` and write the returned JSON to `reports/research_enrichment.json`. Then run:

```powershell
python scripts/paper_autotrader.py
```

When `openclaw` is installed locally, `paper_autotrader.py` now performs this handoff automatically before scoring and paper-order submission. Set `OPENCLAW_AUTO_RESEARCH=0` in `local.env` to disable it. If OpenClaw fails or returns invalid research, the run logs `research_fallback=python` and continues using the Python score for that run.

The paper trader applies a 70/30 Python/research score blend, preserves all risk limits, and updates `reports/latest.json` and `reports/site/index.html`.

The scheduled paper-trader also publishes only these generated report artifacts to `main` after the run: the latest JSON report, sector history, Top-5 handoff, research enrichment, prompt, and Pages site. Credentials, `trading.db`, and runtime logs are never staged.
