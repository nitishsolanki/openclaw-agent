# AI Trading Agent

## README structure

- **Part I — Business and Trading Knowledge:** what the agent looks for, how the
  profiles differ, how setup maturity works, and how to interpret candidates.
- **Part II — IT Operations and Python References:** installation, commands,
  configuration, services, tests, scheduled jobs, reports, and source files.

# Part I — Business and Trading Knowledge

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

## Market eligibility and score calculation

In live mode, a stock is excluded when any of these eligibility checks fail:

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

After liquidity filtering, the active theme, market regime, sector leadership, and
technical factors influence ranking. These are eligibility and ranking rules, not
trade approval. A stock that passes the filters is scored and ranked; it is not
automatically approved for a trade.

The Sector Rotation heatmap compares each sector ETF with the benchmark and scores
relative strength, trend, momentum, and recent price behavior. The date cells show
the historical sector score. The 5D and 20D columns compare the latest sector score
with the score five and twenty sessions earlier. ETF Current Δ compares the latest
ETF close with the previous available close; positive values are green and negative
values are red. Rows are ordered by five-day sector-score improvement.

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

All three lists use the same stock universe and reusable Early Setup layer, but
apply different technical priorities and filters:

| List | Main focus | Most important factors |
| --- | --- | --- |
| **Day** | Short-term intraday momentum | Market regime, sector strength, trend, relative strength, VWAP, options |
| **Swing** | Multi-day to multi-week moves | Relative strength, VWAP, trend, momentum, volume |
| **Growth** | Stronger medium/long-term candidates | Market regime, sector strength, relative strength, trend, volume |

The Early Setup layer classifies candidates as `BUILDING`, `BREAKOUT_READY`,
`CONFIRMED_BREAKOUT`, `PULLBACK`, or `EXTENDED`. Extended candidates are treated
as `WAIT` candidates rather than automatic buys.

See [Trading Candidate Profiles.md](Trading%20Candidate%20Profiles.md) for a
business-level explanation of the Day, Swing, and Growth candidate profiles.

When no stock passes every profile gate in a market snapshot, the report shows
the highest-ranked long-only candidates with `FILTER_FALLBACK` status for review.
Fallback candidates are not eligible for automatic paper entries; setup and risk
checks remain mandatory.

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

# Part II — IT Operations and Python References

## Quick start

From this directory:

```powershell
python -m pip install -e .
python -m ai_trading_agent scan
python -m ai_trading_agent scan --profile day
python -m ai_trading_agent scan --profile swing
python -m ai_trading_agent scan --profile growth
```

For the local API and Telegram bot, use separate terminals:

```powershell
python scripts/run_api.py
python scripts/run_telegram.py
```

Useful Telegram commands are `/scan`, `/sectors`, `/analyze SYMBOL`,
`/setup SYMBOL`, `/positions`, `/pnl`, and `/status`.

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

## Python source reference

| Area | File | Purpose |
| --- | --- | --- |
| CLI orchestration | `src/ai_trading_agent/cli.py` | Loads profiles, universe, market data, and runs scans |
| Liquidity filtering | `src/ai_trading_agent/data/bars_batch.py` | Price, history, volume, dollar-volume, and spread checks |
| Profile scoring | `src/ai_trading_agent/screening/scanner.py` | Technical components, filters, and ranking |
| Early setup layer | `src/ai_trading_agent/screening/early_setup.py` | Maturity, compression, extension, timing, and opportunity metrics |
| Strategy configuration | `config/strategy_day.yaml`, `strategy_swing.yaml`, `strategy_growth.yaml` | Profile weights, filters, and early-setup thresholds |
| Report generation | `reports/build_live_report.py` and `reports/generate_site.py` | JSON report, candidate tables, charts, and detail pages |
| Paper execution | `scripts/paper_autotrader.py` | Research handoff, exits, reconciliation, and paper entries |

The scanner's primary output is a `TradeSignal` containing the profile score and
component dictionary. The report builder serializes those components together
with research, setup maturity, timing, and opportunity fields.

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

The workflow in `.github/workflows/market-pages.yml` generates reports at 9:00 AM,
12:00 PM, and 2:00 PM Chicago time on weekdays. Add `ALPACA_API_KEY`,
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

When only research scores change, skip the market scan and refresh the report with:

```powershell
python scripts/update_research_scores.py
python scripts/publish_paper_report.py
```

This reuses the existing Day, Swing, and Growth candidates, recalculates only
the research-enriched scores, rebuilds the static site, and triggers the
lightweight Pages deployment. It does not refresh the universe, rerun Alpaca
market scans, or submit orders.

The scheduled paper-trader also publishes only these generated report artifacts to `main` after the run: the latest JSON report, sector history, Top-5 handoff, research enrichment, prompt, and Pages site. Credentials, `trading.db`, and runtime logs are never staged.
