"""Publish generated paper-trading report artifacts without exposing local state."""
import subprocess
from pathlib import Path

root = Path(__file__).parents[1]
repo = root.parent
paths = [
    "ai-trading-agent/reports/latest.json",
    "ai-trading-agent/reports/sector_history.json",
    "ai-trading-agent/reports/top_candidates.json",
    "ai-trading-agent/reports/research_enrichment.json",
    "ai-trading-agent/reports/openclaw_research_prompt.md",
    "ai-trading-agent/reports/site",
]
def git(*args):
    return subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True)

def publish():
    for path in paths:
        git("add", "--", path)
    staged = git("diff", "--cached", "--quiet")
    if staged.returncode == 0:
        print("paper_report_publish=no_changes")
        return
    commit = git("commit", "-m", "data: publish paper trading report")
    if commit.returncode:
        raise SystemExit(commit.stderr.strip() or "git commit failed")
    pushed = git("push", "origin", "main")
    if pushed.returncode:
        print(f"paper_report_publish=commit_only push_error={pushed.stderr.strip()}")
    else:
        print("paper_report_publish=pushed")

if __name__ == "__main__":
    publish()
