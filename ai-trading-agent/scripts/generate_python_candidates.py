"""Generate the Python-only Day, Swing, and Growth candidate artifact."""
import json
from pathlib import Path
from ai_trading_agent.cli import run_scan

root = Path(__file__).parents[1]
output = root / "reports" / "python_candidates.json"

def serialize(items):
    return [{"symbol": item.symbol, "direction": item.direction,
             "score": item.final_score,
             "components": {k: v for k, v in item.components.items()
                            if isinstance(v, (int, float))},
             "sector": item.components.get("sector_name", "Unknown")}
            for item in items]

payload = {profile: serialize(run_scan(root, require_live=True, profile=profile))
           for profile in ("day", "swing", "growth")}
output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(f"python_candidates={output}")
