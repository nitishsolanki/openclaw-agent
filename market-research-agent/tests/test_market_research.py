import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "agent.py"

spec = importlib.util.spec_from_file_location("market_research_agent", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def test_load_watchlist_reads_tickers():
    tickers = module.load_watchlist(ROOT)
    assert "NVDA" in tickers
    assert "KTOS" in tickers
    assert len(tickers) >= 10


def test_generate_report_includes_required_sections():
    report = module.build_daily_report(ROOT)
    assert "# Daily Market Research" in report
    assert "## Market Overview" in report
    assert "## Watchlist Opportunities" in report
    assert "## Key Risks" in report
    assert "NVDA" in report


def test_run_market_research_updates_state_and_report(tmp_path):
    out_dir = tmp_path / "agent-output"
    out_dir.mkdir()

    result = module.run_market_research(ROOT, output_dir=out_dir)

    assert result["status"] == "completed"
    assert (out_dir / "latest.md").exists()
    assert (out_dir / "last_run.json").exists()
    state = json.loads((out_dir / "last_run.json").read_text())
    assert state["status"] == "completed"


def test_rank_opportunities_returns_sorted_results():
    ranked = module.rank_opportunities(ROOT)
    assert ranked
    assert ranked[0]["symbol"] in {"NVDA", "AMD", "AVGO", "KTOS", "ORCL", "SMCI", "APP"}
    assert ranked[0]["score"] >= ranked[-1]["score"]
    assert all("score" in item for item in ranked)


def test_extract_macro_and_sec_review():
    macro = module.extract_macro_snapshot(ROOT)
    sec = module.extract_sec_review(ROOT)

    assert macro["highlights"]
    assert any("retail" in item.lower() for item in macro["highlights"])
    assert sec["status"] in {"no_fresh_filing", "verified"}
    assert "notes" in sec
