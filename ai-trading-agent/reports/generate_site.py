import argparse
import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
from html import escape

def render(report: dict) -> str:
    try:
        generated = datetime.fromisoformat(str(report.get("generated_at", "")).replace("Z", "+00:00"))
        if generated.tzinfo is None:
            generated = generated.replace(tzinfo=timezone.utc)
        report = {**report, "generated_at": generated.astimezone(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %I:%M:%S %p %Z")}
    except (TypeError, ValueError):
        pass
    history = report.get("sector_history", [])[-5:]
    oldest = history[0].get("scores", {}) if history else {}
    ranked_sectors = sorted(report.get("sectors", []), key=lambda item: float(item.get("score", -1)), reverse=True)
    trends = {}
    price_trends = {}
    current_prices = report.get("sector_current_prices", {})
    for item in ranked_sectors:
        values = [float(day.get("scores", {}).get(item["sector"], 0)) for day in history]
        slope = 0.0
        if len(values) >= 2:
            center = (len(values) - 1) / 2
            average = sum(values) / len(values)
            slope = sum((index - center) * (value - average) for index, value in enumerate(values)) / max(sum((index - center) ** 2 for index in range(len(values))), 1)
        label = "Gaining" if slope > 0.25 else "Losing" if slope < -0.25 else "Stable"
        forecast = max(0.0, min(100.0, values[-1] + slope)) if values else float(item.get("score", 0))
        trends[item["sector"]] = (label, slope, forecast)
        prices = [float(day.get("prices", {}).get(item["sector"], 0)) for day in history if day.get("prices", {}).get(item["sector"]) is not None]
        price_trends[item["sector"]] = ((prices[-1] / prices[0] - 1) * 100 if len(prices) >= 2 and prices[0] else 0.0)
    history_sectors = sorted(ranked_sectors, key=lambda item: trends[item["sector"]][1], reverse=True)
    history_headers = "".join(f"<th>{escape(str(item.get('date', '')))}</th>" for item in history)
    history_rows = "".join(f"<tr><td>{item['rank']}</td><td>{escape(str(item['sector']))}</td><td>{escape(str(item['symbol']))}</td>" + "".join(f"<td>{float(day.get('scores', {}).get(item['sector'], 0)):.1f}</td>" for day in history) + f"<td>{float(item['score']) - float(oldest.get(item['sector'], item['score'])):+.1f}</td><td>{float(current_prices.get(item['sector'], 0)):.2f}</td><td>{price_trends[item['sector']]:+.2f}%</td><td>{trends[item['sector']][0]} {'↑' if trends[item['sector']][0] == 'Gaining' else '↓' if trends[item['sector']][0] == 'Losing' else '→'}</td></tr>" for item in history_sectors)
    def candidate_sector(item):
        sector = str(item.get("sector", "Unknown"))
        return sector if sector in price_trends else "Unknown"

    def candidate_trend(item):
        change = price_trends.get(candidate_sector(item), 0.0)
        arrow = "↑" if change > 0.05 else "↓" if change < -0.05 else "→"
        return f"{arrow} {change:+.2f}%"

    def candidate_cards(items):
        return "".join(f"<article class='card' style='font-size:.9rem'><div class='row'><h3 style='font-size:1.1rem'>{escape(str(item['symbol']))}</h3><span class='badge'>{float(item.get('boosted_score', item['score'])):.1f}/100</span></div><p>{escape(str(item['direction']))} · {escape(str(item.get('sector', 'Unknown')))}</p><p class='muted'>Python: {float(item['score']):.1f} · Research: {float(item.get('research', {}).get('research_score', 0)):.1f} · Boosted: {float(item.get('boosted_score', item['score'])):.1f}</p></article>" for item in items)
    profile_signals = report.get("profiles", {}) or {"swing": report.get("signals", [])}
    candidate_sections = "".join(f"<section><h2>{escape(profile.title())} Top Candidates</h2><div class='grid'>{candidate_cards(items)}</div></section>" for profile, items in profile_signals.items())
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>AI Trading Market Report</title><link rel='stylesheet' href='assets/styles.css'></head><body><main><header><p class='eyebrow'>AI TRADING AGENT · PAPER MODE</p><h1>Market Intelligence</h1><p class='muted'>Generated {escape(report.get('generated_at', 'unknown'))} · Source: {escape(str(report.get('data_source', 'unknown')))}</p></header><section class='hero'><div><span class='eyebrow'>MARKET REGIME</span><strong>{escape(report['market']['label'])}</strong><span class='score'>{report['market']['score']}/100</span></div><div><span class='eyebrow'>ACTIVE THEME</span><strong>{escape(report['theme']['name'])}</strong><span class='muted'>{', '.join(report['theme'].get('sectors', []))}</span></div></section><section><h2>Five-Day Sector Rotation Trend</h2><p class='muted'>Sorted by five-day score slope: gaining sectors first, stable sectors next, and losing sectors last.</p><div class='table-scroll'><table><thead><tr><th>Current Rank</th><th>Sector</th><th>ETF</th>{history_headers}<th>Score Δ</th><th>Current Price</th><th>Price Δ</th><th>Trend</th></tr></thead><tbody>{history_rows}</tbody></table></div></section>{candidate_sections}<footer>{escape(report.get('disclaimer', ''))}</footer></main></body></html>"""

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
