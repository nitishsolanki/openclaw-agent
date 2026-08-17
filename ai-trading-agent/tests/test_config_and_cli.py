from pathlib import Path
from ai_trading_agent.config.settings import load_strategy
from ai_trading_agent.cli import run_scan

def test_strategy_weights_load():
    config = load_strategy(Path(__file__).parents[1] / "config" / "strategy.yaml")
    assert sum(config["weights"].values()) == 1.0

def test_offline_scan_journals_signals(tmp_path):
    root = Path(__file__).parents[1]
    # The CLI uses fixed sample data but writes its journal under the supplied root.
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "strategy.yaml").write_text((root / "config" / "strategy.yaml").read_text())
    import shutil
    shutil.copytree(root / "data", tmp_path / "data")
    results = run_scan(tmp_path)
    assert len(results) == 3
    assert (tmp_path / "trading.db").exists()
