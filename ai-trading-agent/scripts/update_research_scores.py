"""Recompute report boosted scores without rerunning market scans."""
from __future__ import annotations

import json
from pathlib import Path
import sys

root = Path(__file__).parents[1]
sys.path.insert(0, str(root / "src"))
sys.path.insert(0, str(root))

from ai_trading_agent.research.bridge import boosted_score, load_research
from reports.generate_site import build

report_path = root / "reports" / "latest.json"
report = json.loads(report_path.read_text(encoding="utf-8"))
research = load_research(root)
updated = 0
for items in [report.get("signals", [])] + list(report.get("profiles", {}).values()):
    for item in items:
        symbol = str(item.get("symbol", "")).upper()
        row = research.get(symbol)
        if not row:
            continue
        item["research"] = row
        item["boosted_score"] = boosted_score(float(item.get("score", 0)), row)
        updated += 1

report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
build(report_path, root / "reports" / "site")
print(f"research_scores_updated={updated}")
