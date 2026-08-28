"""Publish only stock-analysis Markdown changes to GitHub."""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).parents[1]


def run(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def publish() -> str:
    run("git", "add", "--", "data/stocks")
    staged = run("git", "diff", "--cached", "--name-only", "--", "data/stocks")
    if not staged:
        return "no_changes"
    message = os.environ.get("RESEARCH_COMMIT_MESSAGE", "research: update stock analysis")
    run("git", "-c", "user.name=OpenClaw Research Agent", "-c",
        "user.email=openclaw-research@users.noreply.github.com", "commit", "-m", message)
    run("git", "push", "origin", "main")
    return f"published\n{staged}"


if __name__ == "__main__":
    print(publish())
