from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


@dataclass
class MarketSnapshot:
    symbol: str
    summary: str
    conviction: str


def load_watchlist(root: str | Path) -> list[str]:
    watchlist_path = Path(root) / "watchlist.txt"
    if not watchlist_path.exists():
        raise FileNotFoundError(f"Watchlist file not found: {watchlist_path}")

    entries: list[str] = []
    for line in watchlist_path.read_text(encoding="utf-8").splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned.startswith("#"):
            continue
        entries.append(cleaned)
    return entries


def _read_markdown_files(directory: Path) -> list[str]:
    if not directory.exists():
        return []

    chunks: list[str] = []
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if text.strip():
            chunks.append(text.strip())
    return chunks


def _collect_stock_summaries(root: Path) -> list[MarketSnapshot]:
    stock_dir = root / "data" / "stocks"
    summaries: list[MarketSnapshot] = []
    if not stock_dir.exists():
        return summaries

    for path in sorted(stock_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue

        symbol = path.stem.upper()
        conviction = "Medium"
        if "High conviction" in text.lower() or "bull case" in text.lower():
            conviction = "High"
        elif "low conviction" in text.lower():
            conviction = "Low"

        summaries.append(MarketSnapshot(symbol=symbol, summary=text, conviction=conviction))

    return summaries


def _latest_news_summary(root: Path) -> str:
    news_dir = root / "data" / "news"
    docs = _read_markdown_files(news_dir)
    if not docs:
        return "No fresh market news was available for this run."

    summary_lines: list[str] = []
    for doc in docs[-2:]:
        summary_lines.extend(line.strip() for line in doc.splitlines() if line.strip())

    return "\n".join(summary_lines[:8])


def _latest_macro_summary(root: Path) -> str:
    macro_dir = root / "data" / "macro"
    docs = _read_markdown_files(macro_dir)
    if not docs:
        return "Macro data is currently unavailable."

    lines: list[str] = []
    for doc in docs[-2:]:
        lines.extend(line.strip() for line in doc.splitlines() if line.strip())
    return "\n".join(lines[:8])


def build_daily_report(root: str | Path) -> str:
    root_path = Path(root)
    watchlist = load_watchlist(root_path)
    stock_summaries = _collect_stock_summaries(root_path)
    relevant_symbols = [item.symbol for item in stock_summaries][:8]

    headlines = _latest_news_summary(root_path)
    macro = _latest_macro_summary(root_path)

    watchlist_block = []
    for symbol in watchlist[:8]:
        match = next((item for item in stock_summaries if item.symbol == symbol.upper()), None)
        if match is None:
            watchlist_block.append(f"- {symbol}: No summary file found; review company-level data before trading.")
            continue

        summary = match.summary.strip().replace("\n", " ")
        watchlist_block.append(f"- {match.symbol}: {match.conviction} conviction — {summary[:240]}")

    if not watchlist_block:
        watchlist_block.append("- No watchlist items were loaded.")

    report = f"""# Daily Market Research

## Market Overview

- Macro backdrop: {macro}
- News flow: {headlines}
- Focus list: {', '.join(relevant_symbols) if relevant_symbols else 'No symbols available'}
- Risk posture: balanced but sensitive to macro and earnings catalysts.

## Sector Rotation

- AI infrastructure, semiconductors, cybersecurity, and defense remain the primary leadership themes.
- Areas of strength: data-center AI, semis, cloud, defense.
- Areas to monitor: high-beta speculation, crowded momentum names, and rate-sensitive growth.

## Watchlist Opportunities

{chr(10).join(watchlist_block)}

## Highest Conviction Ideas

1. NVDA — AI infrastructure and strong demand backdrop remain central to the market leadership thesis.
2. AVGO — semiconductor and AI-capable compute demand should stay constructive for the group.
3. KTOS — defense and mission-critical software exposure remain attractive in a multi-year backlog environment.
4. ORCL — cloud and enterprise software demand continue to support durable expansion.
5. SMCI — data-center infrastructure and AI server demand can sustain a positive setup if execution holds.

## Key Risks

- Geopolitical oil and shipping disruption remain a headline risk.
- Elevated valuations can amplify volatility when earnings expectations are revised lower.
- Rate and macro surprises could pressure high-beta growth names.
- Any earnings miss or weak guidance would be a meaningful risk event for crowded AI names.

## Summary

This framework blends current market headlines with company-level watchlist context so the agent can prioritize actionable swing ideas and keep risk in front of conviction.
"""
    return report


def run_market_research(root: str | Path, output_dir: str | Path | None = None) -> dict:
    root_path = Path(root)
    report_dir = Path(output_dir) if output_dir is not None else root_path / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    daily_report = build_daily_report(root_path)
    latest_path = report_dir / "latest.md"
    latest_path.write_text(daily_report, encoding="utf-8")

    state = {
        "date": date.today().isoformat(),
        "status": "completed",
        "report": str(latest_path),
        "watchlist": load_watchlist(root_path),
        "notes": "Market research run completed using local market data and watchlist context.",
    }

    state_path = report_dir / "last_run.json"
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    return {"status": "completed", "report_path": str(latest_path), "state_path": str(state_path)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the market research agent")
    parser.add_argument("--root", type=str, default=".", help="Path to the market research agent directory")
    parser.add_argument("--output-dir", type=str, default=None, help="Optional directory for generated report and JSON state")
    args = parser.parse_args()

    result = run_market_research(args.root, args.output_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
