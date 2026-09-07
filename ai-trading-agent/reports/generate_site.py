import argparse
import json
import math
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
from html import escape

def _render_base(report: dict) -> str:
    try:
        generated = datetime.fromisoformat(str(report.get("generated_at", "")).replace("Z", "+00:00"))
        if generated.tzinfo is None:
            generated = generated.replace(tzinfo=timezone.utc)
        report = {**report, "generated_at": generated.astimezone(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %I:%M:%S %p %Z")}
    except (TypeError, ValueError):
        pass
    history = report.get("sector_history", [])
    display_history = history[-5:]
    oldest = display_history[0].get("scores", {}) if display_history else {}
    ranked_sectors = sorted(report.get("sectors", []), key=lambda item: float(item.get("score", -1)), reverse=True)
    trends = {}
    price_trends = {}
    current_prices = report.get("sector_current_prices", {})
    for item in ranked_sectors:
        values = [float(day.get("scores", {}).get(item["sector"], 0)) for day in display_history]
        slope = 0.0
        if len(values) >= 2:
            center = (len(values) - 1) / 2
            average = sum(values) / len(values)
            slope = sum((index - center) * (value - average) for index, value in enumerate(values)) / max(sum((index - center) ** 2 for index in range(len(values))), 1)
        label = "Gaining" if slope > 0.25 else "Losing" if slope < -0.25 else "Stable"
        forecast = max(0.0, min(100.0, values[-1] + slope)) if values else float(item.get("score", 0))
        trends[item["sector"]] = (label, slope, forecast)
        prices = [float(day.get("prices", {}).get(item["sector"], 0)) for day in display_history if day.get("prices", {}).get(item["sector"]) is not None]
        price_trends[item["sector"]] = ((prices[-1] / prices[0] - 1) * 100 if len(prices) >= 2 and prices[0] else 0.0)
    ranked_sectors = sorted(ranked_sectors, key=lambda item: trends[item["sector"]][1], reverse=True)
    history_sectors = ranked_sectors
    history_headers = "".join(f"<th>{escape(str(item.get('date', '')))}</th>" for item in display_history)
    history_rows = "".join(f"<tr><td>{item['rank']}</td><td>{escape(str(item['sector']))}</td><td>{escape(str(item['symbol']))}</td>" + "".join(f"<td>{float(day.get('scores', {}).get(item['sector'], 0)):.1f}</td>" for day in display_history) + f"<td>{float(item['score']) - float(oldest.get(item['sector'], item['score'])):+.1f}</td><td>{float(current_prices.get(item['sector'], 0)):.2f}</td><td>{price_trends[item['sector']]:+.2f}%</td><td>{trends[item['sector']][0]} {'↑' if trends[item['sector']][0] == 'Gaining' else '↓' if trends[item['sector']][0] == 'Losing' else '→'}</td></tr>" for item in history_sectors)
    def candidate_sector(item):
        sector = str(item.get("sector", "Unknown"))
        return sector if sector in price_trends else "Unknown"

    def candidate_trend(item):
        change = price_trends.get(candidate_sector(item), 0.0)
        arrow = "↑" if change > 0.05 else "↓" if change < -0.05 else "→"
        return f"{arrow} {change:+.2f}%"

    def candidate_cards(items, profile):
        return "".join(f"<article class='card' style='font-size:.9rem'><div class='row'><h3 style='font-size:1.1rem'>{escape(str(item['symbol']))}</h3><span class='badge'>{float(item.get('boosted_score', item['score'])):.1f}/100</span></div><p>{escape(str(item['direction']))} · {escape(str(item.get('sector', 'Unknown')))} · {escape(str(item.get('profile_status', 'QUALIFIED')))}</p><p class='muted'>Python: {float(item['score']):.1f} · Research: {float(item.get('research', {}).get('research_score', 0)):.1f} · Boosted: {float(item.get('boosted_score', item['score'])):.1f}</p>{f"<a href='details/{escape(str(item['symbol']).upper())}.html'>View details →</a>" if profile.lower() == 'day' else ''}</article>" for item in items)
    profile_signals = report.get("profiles", {}) or {"swing": report.get("signals", [])}
    candidate_sections = "".join(f"<section><h2>{escape(profile.title())} Top Candidates</h2><div class='grid'>{candidate_cards(items, profile)}</div></section>" for profile, items in profile_signals.items())
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>AI Trading Market Report</title><link rel='stylesheet' href='assets/styles.css'></head><body><main><header><p class='eyebrow'>AI TRADING AGENT · PAPER MODE</p><h1>Market Intelligence</h1><p class='muted'>Generated {escape(report.get('generated_at', 'unknown'))} · Source: {escape(str(report.get('data_source', 'unknown')))}</p></header><section class='hero'><div><span class='eyebrow'>MARKET REGIME</span><strong>{escape(report['market']['label'])}</strong><span class='score'>{report['market']['score']}/100</span></div><div><span class='eyebrow'>ACTIVE THEME</span><strong>{escape(report['theme']['name'])}</strong><span class='muted'>{', '.join(report['theme'].get('sectors', []))}</span></div></section><section><h2>Sector Rotation</h2><p class='muted'>Current sector score, price change, and five-day trend.</p><div class='table-scroll'><table><thead><tr><th>Sector</th><th>ETF</th><th>Score</th><th>Current Price</th><th>Price Δ</th><th>Trend</th></tr></thead><tbody>{''.join(f"<tr><td>{escape(str(item['sector']))}</td><td>{escape(str(item['symbol']))}</td><td>{float(item['score']):.1f}</td><td>{float(current_prices.get(item['sector'], 0)):.2f}</td><td>{price_trends[item['sector']]:+.2f}%</td><td>{trends[item['sector']][0]}</td></tr>" for item in ranked_sectors)}</tbody></table></div></section>{candidate_sections}<footer>{escape(report.get('disclaimer', ''))}</footer></main></body></html>"""

def render(report: dict) -> str:
    def format_date(value: str) -> str:
        try:
            parsed = datetime.strptime(str(value), "%Y-%m-%d")
            return f"{parsed.strftime('%b')} {parsed.day}"
        except (TypeError, ValueError):
            return str(value)

    html = _render_base(report)
    html = html.replace("Current sector score, price change, and five-day trend.", "Current sector score, price change, and trend.")
    history = report.get("sector_history", [])
    sectors = report.get("sectors", [])
    width, height, pad = 900, 360, 42
    dates = [str(item.get("date", "")) for item in history]
    chart_lines = []
    colors = ["#70d6c3", "#f6c85f", "#ff7f66", "#8ea7ff", "#c792ea", "#7bdff2", "#f29e4c", "#9be564"]
    momentum_values = [value for sector in sectors for value in [((float(day.get("prices", {}).get(sector["sector"])) / float(previous.get("prices", {}).get(sector["sector"])) - 1.0) * 100.0) for previous, day in zip(history, history[1:]) if day.get("prices", {}).get(sector["sector"]) is not None and previous.get("prices", {}).get(sector["sector"]) not in (None, 0)]]
    chart_min, chart_max = min([-5.0] + momentum_values), max([5.0] + momentum_values)
    for index, sector in enumerate(sectors):
        values = []
        previous_price = None
        for day in history:
            price = day.get("prices", {}).get(sector["sector"])
            values.append(0.0 if price is None or previous_price in (None, 0) else (float(price) / previous_price - 1.0) * 100.0)
            if price is not None:
                previous_price = float(price)
        if not values:
            continue
        points = []
        for pos, value in enumerate(values):
            x = pad + (width - 2 * pad) * pos / max(len(values) - 1, 1)
            bounded = max(chart_min, min(chart_max, value))
            y = height - pad - (height - 2 * pad) * (bounded - chart_min) / max(chart_max - chart_min, 1)
            points.append(f"{x:.1f},{y:.1f}")
        chart_lines.append(f"<polyline data-sector='{escape(str(sector['sector']))}' fill='none' stroke='{colors[index % len(colors)]}' stroke-width='2' points='{ ' '.join(points) }'/>")
    legend = "".join(f"<span class='sector-legend'><i style='background:{colors[i % len(colors)]}'></i>{escape(str(sector['sector']))}</span>" for i, sector in enumerate(sectors))
    ticks = [chart_min, (chart_min + chart_max) / 2, chart_max]
    tick_labels = "".join(f"<text x='8' y='{height - pad - (height - 2 * pad) * (tick - chart_min) / max(chart_max - chart_min, 1) + 4:.1f}' fill='#8e9bb0' font-size='11'>{tick:+.1f}%</text>" for tick in ticks)
    chart = f"<div class='chart-scroll'><svg viewBox='0 0 {width + 40} {height}' role='img' aria-label='Sector momentum score history'><line x1='{pad}' y1='{height-pad}' x2='{width}' y2='{height-pad}' stroke='#52627d'/><line x1='{pad}' y1='{pad}' x2='{pad}' y2='{height-pad}' stroke='#52627d'/>{tick_labels}{''.join(chart_lines)}{''.join(f"<text x='{pad + (width - 2*pad) * i / max(len(dates)-1,1):.1f}' y='{height-10}' fill='#8e9bb0' font-size='10'>{escape(format_date(date))}</text>" for i, date in enumerate(dates))}</svg></div><div class='sector-legend-wrap'>{legend}</div>"
    heatmap_rows_parts = []
    for sector in sorted(sectors, key=lambda item: float(item.get("score", 0)), reverse=True):
        cells = []
        for day in history:
            value = day.get("scores", {}).get(sector["sector"])
            display = "—" if value is None else f"{float(value):.1f}"
            bucket = 0 if value is None else min(100, max(0, int(float(value) // 10) * 10))
            title = f"{sector['sector']} · {day.get('date', '')} · {display}"
            cells.append(f"<td class='heat-{bucket}' title='{escape(title)}'>{display}</td>")
        heatmap_rows_parts.append(f"<tr><th>{escape(str(sector['sector']))}</th>{''.join(cells)}</tr>")
    heatmap_rows = "".join(heatmap_rows_parts)
    heatmap = f"<div class='table-scroll'><table class='sector-heatmap'><thead><tr><th>Sector</th>{''.join(f'<th>{escape(format_date(date))}</th>' for date in dates)}</tr></thead><tbody>{heatmap_rows}</tbody></table></div>"
    latest = history[-1] if history else {}
    previous = history[-2] if len(history) > 1 else {}
    ranking = "".join(f"<div class='ranking-row'><span>{escape(str(sector['sector']))}</span><div class='ranking-bar'><b style='width:{float(sector.get('score', 0)):.1f}%'></b></div><strong>{float(sector.get('score', 0)):.1f}</strong><em>{float(latest.get('scores', {}).get(sector['sector'], 0)) - float(previous.get('scores', {}).get(sector['sector'], latest.get('scores', {}).get(sector['sector'], 0))):+.1f}</em></div>" for sector in sorted(sectors, key=lambda item: float(item.get('score', 0)), reverse=True))
    ranking_html = f"<div class='sector-ranking'>{ranking}</div>"
    marker = "<section><h2>Sector Rotation</h2>"
    replacement = f"<section><h2>Sector Rotation</h2><p class='muted'>Track strength, momentum, and current sector leadership.</p><h3>Sector Rotation — Heatmap</h3>{heatmap}<h3>Sector Momentum</h3><p class='muted'>Day-over-day percentage change in current sector prices.</p>{chart}"
    return html.replace(marker, replacement, 1)

def build(input_path: Path, output_dir: Path) -> None:
    report = json.loads(input_path.read_text(encoding="utf-8"))
    (output_dir / "assets").mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render(report), encoding="utf-8")
    (output_dir / "data").mkdir(exist_ok=True)
    (output_dir / "data" / "latest.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    details_dir = output_dir / "details"
    details_dir.mkdir(parents=True, exist_ok=True)
    for item in report.get("profiles", {}).get("day", []):
        symbol = str(item.get("symbol", "")).upper()
        research = item.get("research", {}) or {}
        components = item.get("components", {}) or {}
        component_rows = "".join(f"<tr><td>{escape(str(key).replace('_', ' ').title())}</td><td>{float(value):.1f}</td></tr>" for key, value in components.items() if isinstance(value, (int, float)))
        research_rows = "".join(f"<tr><td>{escape(str(key).replace('_', ' ').title())}</td><td>{escape(str(value))}</td></tr>" for key, value in research.items() if key not in {"symbol"})
        python_score = float(item.get("score", 0))
        research_score = float(research.get("research_score", 0))
        boosted_score = float(item.get("boosted_score", python_score))
        contribution = (f"<section><h2>Score Contribution</h2><p class='muted'>Boosted score = Python score × 70% + Research score × 30%.</p><table><thead><tr><th>Source</th><th>Raw score</th><th>Weight</th><th>Contribution</th></tr></thead><tbody><tr><td>Python</td><td>{python_score:.1f}</td><td>70%</td><td>{python_score * .70:.1f}</td></tr><tr><td>Research</td><td>{research_score:.1f}</td><td>30%</td><td>{research_score * .30:.1f}</td></tr><tr><th>Boosted total</th><th colspan='2'></th><th>{boosted_score:.1f}</th></tr></tbody></table></section>")
        detail = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{escape(symbol)} Details</title><link rel='stylesheet' href='../assets/styles.css'></head><body><main><p><a href='../index.html'>← Back to Market Intelligence</a></p><h1>{escape(symbol)} Details</h1><p class='muted'>Day-trading candidate · {escape(str(item.get('direction', 'UNKNOWN')))}</p><section><h2>Score Summary</h2><table><tbody><tr><th>Python score</th><td>{float(item.get('score', 0)):.1f}</td></tr><tr><th>Research score</th><td>{float(research.get('research_score', 0)):.1f}</td></tr><tr><th>Boosted score</th><td>{float(item.get('boosted_score', item.get('score', 0))):.1f}</td></tr></tbody></table></section><section><h2>Python Filters and Components</h2><table><thead><tr><th>Component</th><th>Score</th></tr></thead><tbody>{component_rows}</tbody></table></section><section><h2>Research Details</h2><table><tbody>{research_rows or '<tr><td colspan=\"2\">No research details available.</td></tr>'}</tbody></table></section><p><a href='../index.html'>← Back to Market Intelligence</a></p></main></body></html>"
        detail = detail.replace("</section><section><h2>Python Filters and Components</h2>", f"</section>{contribution}<section><h2>Python Filters and Components</h2>")
        detail = detail.replace("<h2>Python Filters and Components</h2>", "<h2>Python Filters and Components</h2><p class='muted'>These component metrics are the basis of the Python score: market regime, sector strength, relative strength, VWAP, trend, volume, momentum, volatility, options confirmation, and extension.</p>")
        (details_dir / f"{symbol}.html").write_text(detail, encoding="utf-8")
    css = Path(__file__).parent / "styles.css"
    extra_css = """
.sector-heatmap th,.sector-heatmap td{padding:9px 10px;text-align:center;white-space:nowrap}.sector-heatmap th:first-child{text-align:left;position:sticky;left:0;background:#131d30}.sector-heatmap td{border:1px solid #263650}.heat-0,.heat-10,.heat-20,.heat-30,.heat-40{background:#7d3f46}.heat-50,.heat-60{background:#665f3d}.heat-70,.heat-80{background:#35655e}.heat-90,.heat-100{background:#1f806f}.chart-scroll{overflow-x:auto}.sector-legend-wrap{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0 20px}.sector-legend{font-size:.8rem;color:#b5c0d2}.sector-legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px}.sector-ranking{display:grid;gap:8px}.ranking-row{display:grid;grid-template-columns:minmax(110px,1.2fr) 3fr 45px 45px;gap:10px;align-items:center;font-size:.9rem}.ranking-bar{height:10px;background:#263650;border-radius:99px;overflow:hidden}.ranking-bar b{display:block;height:100%;background:#70d6c3;border-radius:99px}.ranking-row em{font-style:normal;color:#8e9bb0}@media(max-width:650px){.ranking-row{grid-template-columns:90px 1.5fr 38px 38px;font-size:.78rem}}
"""
    (output_dir / "assets" / "styles.css").write_text(css.read_text(encoding="utf-8") + extra_css, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).parent / "sample_report.json")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "site")
    args = parser.parse_args()
    build(args.input, args.output)
    print(f"site_generated={args.output}")
