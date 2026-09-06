"""Create the Top-5 handoff prompt for the local OpenClaw research agent."""
from pathlib import Path
import json
import sys

root = Path(__file__).parents[1]
sys.path.insert(0, str(root / "src"))
from ai_trading_agent.cli import run_scan
from ai_trading_agent.research.bridge import export_top_candidates
from ai_trading_agent.research.evidence import collect_evidence, evidence_json


def write_prompt(root: Path, signals) -> Path:
    workspace = root.parent
    candidate_path = export_top_candidates(root, signals, limit=len(signals))
    payload = json.loads(candidate_path.read_text(encoding="utf-8"))
    evidence = collect_evidence(root, {item["symbol"] for item in payload["candidates"]})
    sections = []
    for candidate in payload["candidates"]:
        symbol = candidate["symbol"]
        sections.append(f"## {symbol}\nTrading candidate:\n```json\n{json.dumps(candidate, indent=2)}\n```\nEvidence packet (source-labelled; missing sources must remain uncertain):\n```json\n{evidence_json(evidence.get(symbol, {}))}\n```")
    prompt = """# OpenClaw Candidate Research Handoff

Review each candidate using the supplied trading data and evidence packet. Do not place orders. Return only JSON in this format:

```json
{"research":[{"symbol":"MSFT","research_score":0,"conviction":"Low","catalysts":[],"risks":[],"summary":""}]}
```

Use a 0-100 research score. Do not invent facts or infer fundamentals from technical data. Treat missing data as uncertainty, name the missing source in risks, and use only dated/source-labelled news, earnings, filings, or fundamentals. Keep Python's technical score authoritative; this research score is a 30% adjustment.

""" + "\n\n".join(sections)
    path = root / "reports" / "openclaw_research_prompt.md"
    path.write_text(prompt, encoding="utf-8")
    return path


if __name__ == "__main__":
    signals = run_scan(root, require_live=True)
    print(f"research_prompt={write_prompt(root, signals)}")
