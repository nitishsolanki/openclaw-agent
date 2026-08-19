import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from html import escape

def render(report: dict) -> str:
    history = report.get("sector_history", [])[-5:]
    oldest = history[0].get("scores", {}) if history else {}
    sectors = "".join(f"<tr><td>{item['rank']}</td><td>{escape(str(item['sector']))}</td><td>{escape(str(item['symbol']))}</td><td>{float(item['score']):.1f}</td><td>{float(item['score']) - float(oldest.get(item['sector'], item['score'])):+.1f}</td></tr>" for item in report.get("sectors", []))
    history_headers = "".join(f"<th>{escape(str(item.get('date', '')))}</th>" for item in history)
    history_rows = "".join(f"<tr><td>{escape(str(item['sector']))}</td>" + "".join(f"<td>{float(day.get('scores', {}).get(item['sector'], 0)):.1f}</td>" for day in history) + "</tr>" for item in report.get("sectors", []))
    signals = "".join(f"<article class='card'><div class='row'><h3>{escape(str(item['symbol']))}</h3><span class='badge'>{float(item['score']):.1f}/100</span></div><p>{escape(str(item['direction']))} · {escape(str(item.get('sector', 'Unknown')))}</p><ul>{''.join(f'<li>{escape(str(reason))}</li>' for reason in item.get('reasons', []))}</ul></article>" for item in report.get("signals", []))
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>AI Trading Market Report</title><link rel='stylesheet' href='assets/styles.css'></head><body><main><header><p class='eyebrow'>AI TRADING AGENT · PAPER MODE</p><h1>Market Intelligence</h1><p class='muted'>Generated {escape(report.get('generated_at', 'unknown'))} · Source: {escape(str(report.get('data_source', 'unknown')))}</p></header><section class='hero'><div><span class='eyebrow'>MARKET REGIME</span><strong>{escape(report['market']['label'])}</strong><span class='score'>{report['market']['score']}/100</span></div><div><span class='eyebrow'>ACTIVE THEME</span><strong>{escape(report['theme']['name'])}</strong><span class='muted'>{', '.join(report['theme'].get('sectors', []))}</span></div></section><section><h2>Sector Rotation · Current Ranking</h2><p class='muted'>Ranked by current score. Momentum is current score minus the oldest displayed score.</p><table><thead><tr><th>Rank</th><th>Sector</th><th>ETF</th><th>Current</th><th>Momentum</th></tr></thead><tbody>{sectors}</tbody></table></section><section><h2>Five-Day Sector History</h2><div class='table-scroll'><table><thead><tr><th>Sector</th>{history_headers}</tr></thead><tbody>{history_rows}</tbody></table></div></section><section><h2>Top Candidates</h2><div class='grid'>{signals}</div></section><footer>{escape(report.get('disclaimer', ''))}</footer></main></body></html>"""

def build(input_path: Path, output_dir: Path) -> None:
    report = json.loads(input_path.read_text(encoding="utf-8"))
    (output_dir / "assets").mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render(report), encoding="utf-8")
    (output_dir / "data").mkdir(exist_ok=True)
    (output_dir / "data" / "latest.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    css = Path(__file__).parent / "styles.css"
    (output_dir / "assets" / "styles.css").write_text(css.read_text(encoding="utf-8"), encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).parent / "sample_report.json")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "site")
    args = parser.parse_args()
    build(args.input, args.output)
    print(f"site_generated={args.output}")
