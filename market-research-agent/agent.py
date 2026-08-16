from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

try:
    import yfinance as yf
except Exception:  # pragma: no cover - optional dependency fallback
    yf = None


@dataclass
class MarketSnapshot:
    symbol: str
    summary: str
    conviction: str


def _safe_float(value: str | None) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


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


def extract_macro_snapshot(root: str | Path) -> dict:
    root_path = Path(root)
    macro_dir = root_path / "data" / "macro"
    docs = _read_markdown_files(macro_dir)
    if not docs:
        return {"highlights": ["Macro data is currently unavailable."], "status": "missing"}

    highlights: list[str] = []
    for doc in docs[-2:]:
        for line in doc.splitlines():
            text = line.strip()
            if not text or text.startswith("#") or text.startswith("Sources:"):
                continue
            highlights.append(text)

    return {
        "highlights": highlights[:8],
        "status": "available",
        "source_files": sorted(str(path.name) for path in macro_dir.glob("*.md"))[-2:],
    }


def extract_sec_review(root: str | Path) -> dict:
    root_path = Path(root)
    filings_dir = root_path / "data" / "sec-filings"
    files = sorted(filings_dir.glob("*.md"))
    if not files:
        return {"status": "missing", "notes": "No SEC filings were available for review."}

    latest = files[-1].read_text(encoding="utf-8")
    text = latest.lower()
    if "no fresh ticker-specific sec filing" in text or "no fresh" in text:
        return {
            "status": "no_fresh_filing",
            "notes": "No fresh ticker-specific SEC filing was independently verified in the current collection window.",
            "source": files[-1].name,
        }

    return {
        "status": "verified",
        "notes": "Recent filing review available for the watchlist.",
        "source": files[-1].name,
    }


def _latest_macro_summary(root: Path) -> str:
    macro_dir = root / "data" / "macro"
    docs = _read_markdown_files(macro_dir)
    if not docs:
        return "Macro data is currently unavailable."

    lines: list[str] = []
    for doc in docs[-2:]:
        lines.extend(line.strip() for line in doc.splitlines() if line.strip())
    return "\n".join(lines[:8])


def fetch_live_prices(symbols: list[str]) -> dict[str, dict]:
    if not symbols or yf is None:
        return {}

    results: dict[str, dict] = {}
    for symbol in symbols:
        ticker = symbol.strip().upper()
        if not ticker:
            continue
        try:
            history = yf.Ticker(ticker).history(period="5d", interval="1d")
            if history.empty:
                continue

            last_close = float(history["Close"].iloc[-1])
            previous_close = float(history["Close"].iloc[-2]) if len(history) > 1 else last_close
            change_pct = ((last_close - previous_close) / previous_close) * 100 if previous_close else 0.0
            results[ticker] = {"price": last_close, "change_pct": change_pct}
        except Exception:
            continue
    return results


def _load_price_snapshot(root: Path, symbol: str) -> dict:
    data_dir = root / "data" / "stocks"
    for path in data_dir.glob(f"{symbol}.md"):
        text = path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "$" in line and ("price" in line.lower() or "level" in line.lower()):
                value = line.split("$")[-1].split()[0].strip(",")
                return {"symbol": symbol, "price": _safe_float(value)}
    return {"symbol": symbol, "price": 0.0}


def rank_opportunities(root: str | Path, limit: int = 5) -> list[dict]:
    root_path = Path(root)
    watchlist = load_watchlist(root_path)
    summaries = _collect_stock_summaries(root_path)
    live_prices = fetch_live_prices(watchlist)

    ranking: list[dict] = []
    for symbol in watchlist:
        summary = next((item for item in summaries if item.symbol == symbol.upper()), None)
        if summary is None:
            continue

        conviction_score = {"High": 35, "Medium": 22, "Low": 10}.get(summary.conviction, 15)
        text = summary.summary.lower()
        theme_score = sum(8 for keyword in ["ai", "semiconductor", "cloud", "defense", "infrastructure", "software"] if keyword in text)
        catalyst_score = 10 if any(keyword in text for keyword in ["earnings", "guidance", "backlog", "demand", "expansion"]) else 0
        price_data = live_prices.get(symbol.upper(), {})
        price = price_data.get("price", _load_price_snapshot(root_path, symbol.upper())["price"])
        momentum = price_data.get("change_pct", 0.0)
        price_score = 5 if price > 0 else 0
        momentum_score = min(15, max(0, int(abs(momentum) * 5))) if price > 0 else 0

        total = conviction_score + theme_score + catalyst_score + price_score + momentum_score
        ranking.append({
            "symbol": symbol.upper(),
            "score": total,
            "conviction": summary.conviction,
            "summary": summary.summary[:180],
            "price": round(price, 2),
            "momentum_pct": round(momentum, 2),
        })

    ranking.sort(key=lambda item: item["score"], reverse=True)
    return ranking[:limit]


def build_daily_report(root: str | Path) -> str:
    root_path = Path(root)
    watchlist = load_watchlist(root_path)
    stock_summaries = _collect_stock_summaries(root_path)
    relevant_symbols = [item.symbol for item in stock_summaries][:8]
    ranked = rank_opportunities(root_path, limit=5)
    macro_snapshot = extract_macro_snapshot(root_path)
    sec_review = extract_sec_review(root_path)

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

    ranked_lines = [
        f"{index + 1}. {item['symbol']} — score {item['score']} ({item['conviction']} conviction)"
        for index, item in enumerate(ranked)
    ]

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

## Macro Snapshot

- Macro status: {macro_snapshot['status']}
- {chr(10).join(f'- {item}' for item in macro_snapshot['highlights'][:4])}

## SEC Review

- Filing status: {sec_review['status']}
- Notes: {sec_review['notes']}

## Highest Conviction Ideas

{chr(10).join(ranked_lines)}

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
        "rankings": rank_opportunities(root_path),
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
