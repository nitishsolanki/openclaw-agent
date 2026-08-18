from pathlib import Path
from types import SimpleNamespace
from ai_trading_agent.theme.manager import active_theme, refresh_theme

def test_theme_refresh_is_persisted(tmp_path):
    root = Path(__file__).parents[1]
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "themes.yaml").write_text((root / "config" / "themes.yaml").read_text())
    ranks = [SimpleNamespace(sector="Technology", score=90), SimpleNamespace(sector="Energy", score=40)]
    theme = refresh_theme(tmp_path, ranks)
    assert theme["name"] == "technology_leadership"
    assert active_theme(tmp_path)["sectors"] == ["Technology"]

