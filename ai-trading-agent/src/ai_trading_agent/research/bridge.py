import json
from pathlib import Path

def export_top_candidates(root: str | Path, signals: list, limit: int = 5) -> Path:
    path = Path(root) / "reports" / "top_candidates.json"
    payload = [{"symbol": item.symbol, "score": item.final_score,
                "direction": item.direction, "sector": item.components.get("sector_name", "Unknown"),
                "components": {key: value for key, value in item.components.items() if isinstance(value, (int, float))}}
               for item in signals[:limit]]
    path.write_text(json.dumps({"candidates": payload}, indent=2) + "\n", encoding="utf-8")
    return path

def load_research(root: str | Path, allowed_symbols: set[str] | None = None) -> dict[str, dict]:
    path = Path(root) / "reports" / "research_enrichment.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    items = payload.get("research", payload if isinstance(payload, list) else [])
    result = {}
    for item in items:
        symbol = str(item.get("symbol", "")).upper()
        if not symbol or (allowed_symbols is not None and symbol not in allowed_symbols):
            continue
        try:
            score = float(item["research_score"])
        except (KeyError, TypeError, ValueError):
            continue
        if 0 <= score <= 100:
            result[symbol] = {**item, "research_score": score}
    return result

def boosted_score(base_score: float, research: dict | None) -> float:
    if not research:
        return round(base_score, 2)
    try:
        research_score = max(0.0, min(100.0, float(research["research_score"])))
    except (KeyError, TypeError, ValueError):
        return round(base_score, 2)
    return round(max(0.0, min(100.0, base_score * 0.70 + research_score * 0.30)), 2)
