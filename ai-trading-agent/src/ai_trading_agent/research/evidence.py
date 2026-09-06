"""Collect bounded, source-labelled evidence for OpenClaw research."""
from __future__ import annotations

from datetime import date, timedelta
import json
from pathlib import Path

from ..config.env import load_env
from ..data.external import FinnhubProvider, PolygonProvider


def _read_matches(directory: Path, symbol: str, limit: int = 3000) -> list[str]:
    if not directory.exists():
        return []
    matches = []
    for path in sorted(directory.glob("*.md"), reverse=True):
        text = path.read_text(encoding="utf-8")
        if symbol.upper() in text.upper() or path.stem.upper() == symbol.upper():
            matches.append(f"[{path.name}]\n{text[:limit]}")
    return matches[:2]


def _safe_call(function, default):
    try:
        return function()
    except Exception:
        return default


def collect_evidence(root: str | Path, symbols: set[str]) -> dict[str, dict]:
    """Collect local and optional live evidence without failing the scan."""
    root = Path(root)
    env = load_env(root / "local.env")
    finnhub = FinnhubProvider(env["FINNHUB_API_KEY"]) if env.get("FINNHUB_API_KEY") else None
    polygon = PolygonProvider(env["POLYGON_API_KEY"]) if env.get("POLYGON_API_KEY") else None
    today = date.today()
    earnings = _safe_call(
        lambda: finnhub.earnings_calendar(today, today + timedelta(days=90)) if finnhub else {},
        {},
    )
    earnings_rows = earnings.get("earningsCalendar", []) if isinstance(earnings, dict) else []
    output = {}
    for symbol in sorted({item.upper() for item in symbols}):
        local_stock = _read_matches(root.parent / "market-research-agent" / "data" / "stocks", symbol, 5000)
        local_news = _read_matches(root.parent / "market-research-agent" / "data" / "news", symbol, 2500)
        local_sec = _read_matches(root.parent / "market-research-agent" / "data" / "sec-filings", symbol, 2500)
        company_earnings = [row for row in earnings_rows if str(row.get("symbol", "")).upper() == symbol]
        finnhub_news = _safe_call(lambda: finnhub.company_news(symbol, today - timedelta(days=14), today) if finnhub else [], [])
        polygon_news = _safe_call(lambda: polygon.ticker_news(symbol, limit=5) if polygon else {}, {})
        fundamentals = _safe_call(lambda: finnhub.fundamentals(symbol) if finnhub else {}, {})
        output[symbol] = {
            "local_research": local_stock,
            "local_news": local_news,
            "local_sec_filings": local_sec,
            "finnhub_news": finnhub_news[:5] if isinstance(finnhub_news, list) else [],
            "polygon_news": polygon_news.get("results", [])[:5] if isinstance(polygon_news, dict) else [],
            "earnings": company_earnings[:5],
            "fundamentals": fundamentals.get("metric", {}) if isinstance(fundamentals, dict) else {},
            "source_status": {
                "local_research": bool(local_stock),
                "local_news": bool(local_news),
                "local_sec_filings": bool(local_sec),
                "finnhub_news": bool(finnhub_news),
                "polygon_news": bool(polygon_news.get("results")) if isinstance(polygon_news, dict) else False,
                "earnings": bool(company_earnings),
                "fundamentals": bool(fundamentals),
            },
        }
    return output


def evidence_json(evidence: dict[str, dict]) -> str:
    return json.dumps(evidence, indent=2, default=str)
