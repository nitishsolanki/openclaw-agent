import json
from pathlib import Path
from reports.generate_site import build

def test_static_site_generation(tmp_path):
    source = Path(__file__).parents[1] / "reports" / "sample_report.json"
    output = tmp_path / "site"
    build(source, output)
    assert (output / "index.html").exists()
    assert "Market Intelligence" in (output / "index.html").read_text()
    assert json.loads((output / "data" / "latest.json").read_text())["market"]["score"] == 72

