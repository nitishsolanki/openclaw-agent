"""Run the local OpenClaw research handoff safely."""
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path


def run_research(root: Path, prompt_path: Path, expected_symbols: set[str]) -> Path:
    """Ask local OpenClaw for enrichment and write validated JSON.

    The function fails closed: no output file is replaced unless the response
    contains valid research for every requested symbol.
    """
    binary = os.environ.get("OPENCLAW_BIN", "openclaw")
    agent = os.environ.get("OPENCLAW_AGENT", "main")
    command = [binary, "agent", "--agent", agent, "--message-file", str(prompt_path)]
    if binary.lower().endswith(".ps1"):
        command = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", binary,
                   "agent", "--agent", agent, "--message-file", str(prompt_path)]
    elif binary.lower().endswith(".cmd"):
        command = ["cmd.exe", "/d", "/s", "/c", binary, "agent", "--agent", agent, "--message-file", str(prompt_path)]
    result = subprocess.run(
        command,
        cwd=str(root), text=True, capture_output=True, timeout=900,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"OpenClaw failed ({result.returncode}): {result.stderr[-1000:]}")

    match = re.search(r"\{.*\}", result.stdout, flags=re.DOTALL)
    if not match:
        raise RuntimeError("OpenClaw returned no JSON research payload")
    payload = json.loads(match.group(0))
    rows = payload.get("research")
    if not isinstance(rows, list):
        raise RuntimeError("OpenClaw JSON must contain a research list")

    normalized = {}
    for row in rows:
        symbol = str(row.get("symbol", "")).upper().strip()
        score = row.get("research_score")
        if symbol not in expected_symbols or not isinstance(score, (int, float)) or not 0 <= score <= 100:
            raise RuntimeError(f"Invalid research row for {symbol or 'unknown symbol'}")
        normalized[symbol] = row
    missing = expected_symbols - normalized.keys()
    if missing:
        raise RuntimeError(f"OpenClaw omitted symbols: {', '.join(sorted(missing))}")

    output = root / "reports" / "research_enrichment.json"
    temporary = output.with_suffix(".json.tmp")
    temporary.write_text(json.dumps({"research": list(normalized.values())}, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output)
    return output
