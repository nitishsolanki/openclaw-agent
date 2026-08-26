"""Create the Top-5 handoff prompt for the local OpenClaw research agent."""
from pathlib import Path
import json
import sys

root = Path(__file__).parents[1]
sys.path.insert(0, str(root / "src"))
from ai_trading_agent.cli import run_scan
from ai_trading_agent.research.bridge import export_top_candidates


def write_prompt(root: Path, signals) -> Path:
    workspace = root.parent
    candidate_path = export_top_candidates(root, signals)
    payload = json.loads(candidate_path.read_text(encoding="utf-8"))
    sections = []
    for candidate in payload["candidates"]:
        symbol = candidate["symbol"]
        files = list((workspace / "market-research-agent" / "data" / "stocks").glob(f"{symbol}.md"))
        research = files[0].read_text(encoding="utf-8") if files else "No local stock research file exists. Use available provider data only."
        sections.append(f"## {symbol}\nTrading candidate:\n```json\n{json.dumps(candidate, indent=2)}\n```\nExisting research:\n{research[:6000]}")
    prompt = """# OpenClaw Top-5 Research Handoff

Review each candidate using the supplied trading data and existing research. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts. Treat missing data as uncertainty. Keep Python's technical score authoritative; this research score is a 30% adjustment.

""" + "\n\n".join(sections)
    path = root / "reports" / "openclaw_research_prompt.md"
    path.write_text(prompt, encoding="utf-8")
    return path


if __name__ == "__main__":
    signals = run_scan(root, require_live=True)
    print(f"research_prompt={write_prompt(root, signals)}")
