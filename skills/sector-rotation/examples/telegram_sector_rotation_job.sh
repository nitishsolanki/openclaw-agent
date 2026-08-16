#!/usr/bin/env bash
set -euo pipefail

# Example cron wrapper for the sector rotation Telegram alert.
# Replace the env vars and command path with your real values.

export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-}"
export TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-}"
export PYTHON_BIN="${PYTHON_BIN:-/c/Users/nitis/AppData/Local/Programs/Python/Python312/python.exe}"

"$PYTHON_BIN" - <<'PY'
import os
import sys
from datetime import datetime

try:
    import yfinance as yf
except ImportError as exc:
    print(f"Missing dependency: {exc}", file=sys.stderr)
    sys.exit(1)

# Sector ETFs and SPY comparison window.
assets = [
    "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "XLP", "XLU", "XLB", "XLRE", "XLC", "SPY"
]

# Use a single same-day return window.
prices = {}
for symbol in assets:
    try:
        prices[symbol] = yf.Ticker(symbol).history(period="1d", interval="1m")
    except Exception as exc:
        print(f"Unable to load {symbol}: {exc}", file=sys.stderr)
        prices[symbol] = None

# Build a very simple relative-strength summary.
rows = []
spy_last = None
if prices.get("SPY") is not None and not prices["SPY"].empty:
    spy_last = float(prices["SPY"]["Close"].iloc[-1])

if spy_last is None:
    message = "Where is money moving today?\n\nData is delayed or unavailable right now."
else:
    for symbol in assets:
        if symbol == "SPY":
            continue
        hist = prices.get(symbol)
        if hist is None or hist.empty:
            continue
        close = float(hist["Close"].iloc[-1])
        # Approximate same-day percent change from first intraday print to last close.
        start = float(hist["Close"].iloc[0])
        sector_return = (close - start) / start * 100
        spy_start = float(prices["SPY"]["Close"].iloc[0])
        spy_return = (spy_last - spy_start) / spy_start * 100
        rel = sector_return - spy_return
        rows.append((symbol, round(sector_return, 2), round(rel, 2)))

    rows.sort(key=lambda x: x[2], reverse=True)
    leaders = rows[:5]
    laggards = sorted(rows, key=lambda x: x[2])[:5]

    leader_lines = "\n".join(f"{s} {r:+.2f}% vs SPY {rel:+.2f}%" for s, r, rel in leaders)
    laggard_lines = "\n".join(f"{s} {r:+.2f}% vs SPY {rel:+.2f}%" for s, r, rel in laggards)

    summary = "Money is rotating toward the strongest relative leaders while defensive and energy sectors remain lagging."
    message = f"Where is money moving today?\n\n{leader_lines}\n\nWeakest:\n{laggard_lines}\n\n{summary}"

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
if not bot_token or not chat_id:
    print(message)
    sys.exit(0)

import urllib.parse
import urllib.request

safe_message = urllib.parse.quote(message)
url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={safe_message}"
with urllib.request.urlopen(url, timeout=20) as response:
    print(response.read().decode())
PY
