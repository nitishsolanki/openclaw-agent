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
        return "".join(f"<article class='card' style='font-size:.9rem'><div class='row'><h3 style='font-size:1.1rem'>{escape(str(item['symbol']))}</h3><span class='badge'>{float(item.get('boosted_score', item['score'])):.1f}/100</span></div><p>{escape(str(item['direction']))} · {escape(str(item.get('sector', 'Unknown')))} · {escape(str(item.get('profile_status', 'QUALIFIED')))}</p><p class='muted'>Technical: {float(item['score']):.1f} · Research: {float(item.get('research', {}).get('research_score', 0)):.1f} · Boosted: {float(item.get('boosted_score', item['score'])):.1f}</p><a href='details/{escape(str(item['symbol']).upper())}.html'>View details →</a></article>" for item in items)
    profile_signals = report.get("profiles", {}) or {"swing": report.get("signals", [])}
    candidate_sections = "".join(f"<section><h2>{escape(profile.title())} Top Candidates</h2><div class='grid'>{candidate_cards(items, profile)}</div></section>" for profile, items in profile_signals.items())
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>AI Trading Market Report</title><link rel='stylesheet' href='assets/styles.css'></head><body><main><header><p class='eyebrow'>AI TRADING AGENT · PAPER MODE</p><h1>Market Intelligence</h1><p class='muted'>Generated {escape(report.get('generated_at', 'unknown'))} · Source: {escape(str(report.get('data_source', 'unknown')))}</p></header><section class='hero'><div class='active-theme-compact'><span class='eyebrow'>ACTIVE THEME</span><strong>{escape(report['theme']['name'])}</strong><span class='muted'>{', '.join(report['theme'].get('sectors', []))}</span></div></section>{{SECTOR_ROTATION}}{candidate_sections}<footer>{escape(report.get('disclaimer', ''))}</footer></main></body></html>"""

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
    heatmap_history = history[-10:]
    dates = [str(item.get("date", "")) for item in heatmap_history]
    heatmap_rows_parts = []
    def five_day_change(item):
        values = [day.get("scores", {}).get(item["sector"]) for day in history]
        values = [float(value) for value in values if value is not None]
        return values[-1] - values[-6] if len(values) >= 6 else 0.0

    for sector in sorted(sectors, key=five_day_change, reverse=True):
        cells = []
        for day in heatmap_history:
            value = day.get("scores", {}).get(sector["sector"])
            display = "—" if value is None else f"{float(value):.1f}"
            bucket = 0 if value is None else min(100, max(0, int(float(value) // 10) * 10))
            title = f"{sector['sector']} · {day.get('date', '')} · {display}"
            cells.append(f"<td class='heat-{bucket}' title='{escape(title)}'>{display}</td>")
        score_values = [day.get("scores", {}).get(sector["sector"]) for day in history]
        valid_scores = [float(value) for value in score_values if value is not None]
        current_score = valid_scores[-1] if valid_scores else float(sector.get("score", 0))
        five_day = current_score - valid_scores[-6] if len(valid_scores) >= 6 else 0.0
        twenty_day = current_score - valid_scores[-21] if len(valid_scores) >= 21 else 0.0
        trend = "Gaining" if five_day > 0.25 else "Losing" if five_day < -0.25 else "Stable"
        summary = f"<td>{five_day:+.1f}</td><td>{twenty_day:+.1f}</td><td><strong>{current_score:.1f}</strong></td><td>{trend}</td>"
        heatmap_rows_parts.append(f"<tr><th>{escape(str(sector['sector']))}</th><td class='sector-etf'>{escape(str(sector.get('symbol', '—')))}</td>{''.join(cells)}{summary}</tr>")
    heatmap_rows = "".join(heatmap_rows_parts)
    heatmap = f"<div class='table-scroll'><table class='sector-heatmap'><thead><tr><th>Sector</th><th>ETF</th>{''.join(f'<th>{escape(format_date(date))}</th>' for date in dates)}<th>5D Δ</th><th>20D Δ</th><th>Current</th><th>Trend</th></tr></thead><tbody>{heatmap_rows}</tbody></table></div>"
    latest = history[-1] if history else {}
    previous = history[-2] if len(history) > 1 else {}
    ranking = "".join(f"<div class='ranking-row'><span>{escape(str(sector['sector']))}</span><div class='ranking-bar'><b style='width:{float(sector.get('score', 0)):.1f}%'></b></div><strong>{float(sector.get('score', 0)):.1f}</strong><em>{float(latest.get('scores', {}).get(sector['sector'], 0)) - float(previous.get('scores', {}).get(sector['sector'], latest.get('scores', {}).get(sector['sector'], 0))):+.1f}</em></div>" for sector in sorted(sectors, key=lambda item: float(item.get('score', 0)), reverse=True))
    ranking_html = f"<div class='sector-ranking'>{ranking}</div>"
    current_table = "<div class='table-scroll'><table><thead><tr><th>Sector</th><th>ETF</th><th>Score</th><th>Current Price</th><th>Price Δ</th><th>Trend</th></tr></thead><tbody>" + "".join(
        f"<tr><td>{escape(str(item['sector']))}</td><td>{escape(str(item['symbol']))}</td><td>{float(item['score']):.1f}</td><td>{float(report.get('sector_current_prices', {}).get(item['sector'], 0)):.2f}</td><td>{price_trend:+.2f}%</td><td>{'Gaining' if price_trend > 0.25 else 'Losing' if price_trend < -0.25 else 'Stable'}</td></tr>"
        for item, price_trend in ((item, ((float(history[-1].get('prices', {}).get(item['sector'], 0)) / float(history[0].get('prices', {}).get(item['sector'], 0)) - 1) * 100 if len(history) >= 2 and history[0].get('prices', {}).get(item['sector']) not in (None, 0) else 0.0)) for item in sorted(sectors, key=lambda value: float(value.get('score', 0)), reverse=True))
    ) + "</tbody></table></div>"
    def correlation(left, right):
        pairs = [(a, b) for a, b in zip(left, right) if a is not None and b is not None]
        if len(pairs) < 3:
            return None
        xs, ys = zip(*pairs)
        mean_x, mean_y = sum(xs) / len(xs), sum(ys) / len(ys)
        numerator = sum((x - mean_x) * (y - mean_y) for x, y in pairs)
        denominator = (sum((x - mean_x) ** 2 for x in xs) * sum((y - mean_y) ** 2 for y in ys)) ** 0.5
        return None if denominator == 0 else max(-1.0, min(1.0, numerator / denominator))

    sector_names = [str(item["sector"]) for item in sectors]
    movements = {}
    for name in sector_names:
        scores = [day.get("scores", {}).get(name) for day in history]
        movements[name] = [None if a is None or b is None else float(b) - float(a) for a, b in zip(scores, scores[1:])]
    matrix = {a: {b: (1.0 if a == b else correlation(movements[a], movements[b])) for b in sector_names} for a in sector_names}
    # Average-linkage hierarchical clustering: merge the two groups with the
    # strongest average relationship, then flatten the final tree so related
    # sectors appear next to each other in the matrix.
    clusters = [[name] for name in sector_names]
    while len(clusters) > 1:
        best_pair = None
        best_score = float("-inf")
        for left_index, left in enumerate(clusters):
            for right_index in range(left_index + 1, len(clusters)):
                right = clusters[right_index]
                values = [matrix[a][b] for a in left for b in right if matrix[a][b] is not None]
                score = sum(values) / len(values) if values else -1.0
                if score > best_score:
                    best_pair = (left_index, right_index)
                    best_score = score
        if best_pair is None:
            break
        left_index, right_index = best_pair
        merged = clusters[left_index] + clusters[right_index]
        clusters = [cluster for index, cluster in enumerate(clusters) if index not in best_pair]
        clusters.append(merged)
    ordered = [name for cluster in reversed(clusters) for name in cluster]
    def corr_label(value):
        if value is None: return "Insufficient data"
        if value >= .70: return "Strong positive correlation"
        if value >= .40: return "Moderate positive correlation"
        if value <= -.70: return "Strong inverse correlation"
        if value <= -.40: return "Moderate inverse correlation"
        return "Weak / little relationship"
    def corr_class(value):
        if value is None: return "corr-na"
        return "corr-positive" if value >= .4 else "corr-negative" if value <= -.4 else "corr-neutral"
    corr_rows_parts = []
    for name in ordered:
        cells = []
        for other in ordered:
            value = matrix[name][other]
            display = "N/A" if value is None else f"{value:+.2f}"
            title = f"{name} ↔ {other} · {display} · {corr_label(value)}"
            cells.append(f"<td class='{corr_class(value)}' title='{escape(title)}'>{display}</td>")
        corr_rows_parts.append(f"<tr><th>{escape(name)}</th>{''.join(cells)}</tr>")
    corr_rows = "".join(corr_rows_parts)
    history_json = json.dumps([
        {"date": day.get("date", ""), "scores": day.get("scores", {})}
        for day in history
    ], separators=(",", ":"))
    fallback_tickers = {}
    for profile_items in (report.get("profiles", {}) or {}).values():
        for item in profile_items:
            sector = item.get("sector", "Unknown")
            symbol = item.get("symbol")
            if sector != "Unknown" and symbol:
                fallback_tickers.setdefault(sector, []).append({"symbol": symbol, "change": 0})
    ticker_json = json.dumps(report.get("sector_tickers") or fallback_tickers, separators=(",", ":"))
    options = "".join(f"<option value='{escape(name)}'{' selected' if name.lower() == 'technology' else ''}>{escape(name)}</option>" for name in sector_names)
    correlation_html = """
<div class='correlation-controls'><label for='reference-sector'>Reference sector</label><select id='reference-sector'>""" + options + """</select><span class='muted'>Rolling correlation of daily score changes</span></div>
<div class='chart-scroll'><svg id='reference-correlation-chart' viewBox='0 0 920 390' role='img' aria-label='Reference-sector correlation chart'></svg></div>
<div id='reference-correlation-legend' class='sector-legend-wrap'></div>
<script>
(() => {
  const history = """ + history_json + """;
  const names = """ + json.dumps(sector_names) + """;
  const colors = ['#70d6c3','#f6c85f','#ff7f66','#8ea7ff','#c792ea','#7bdff2','#f29e4c','#9be564','#e07aaf','#a6e3a1'];
  const svg = document.getElementById('reference-correlation-chart');
  const select = document.getElementById('reference-sector');
  const legend = document.getElementById('reference-correlation-legend');
  const NS = 'http://www.w3.org/2000/svg';
  function correlation(a, b) {
    const pairs = a.map((value, index) => [value, b[index]]).filter(pair => pair[0] != null && pair[1] != null);
    if (pairs.length < 3) return null;
    const ax = pairs.reduce((sum, pair) => sum + pair[0], 0) / pairs.length;
    const bx = pairs.reduce((sum, pair) => sum + pair[1], 0) / pairs.length;
    const numerator = pairs.reduce((sum, pair) => sum + (pair[0] - ax) * (pair[1] - bx), 0);
    const denominator = Math.sqrt(pairs.reduce((sum, pair) => sum + (pair[0] - ax) ** 2, 0) * pairs.reduce((sum, pair) => sum + (pair[1] - bx) ** 2, 0));
    return denominator ? numerator / denominator : null;
  }
  function draw() {
    const reference = select.value;
    const changes = name => history.slice(1).map((day, index) => {
      const previous = history[index].scores[name], current = day.scores[name];
      return previous == null || current == null ? null : Number(current) - Number(previous);
    });
    const ref = changes(reference), width = 920, rowHeight = 32, labelX = 210, plotLeft = 300, zeroX = 610, plotRight = 880, top = 20, bottom = 20;
    const values = names.filter(name => name !== reference).map(name => ({name, value: correlation(ref, changes(name))})).sort((a, b) => (b.value ?? -2) - (a.value ?? -2));
    const height = Math.max(150, top + bottom + values.length * rowHeight);
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    svg.innerHTML = `<line x1='${zeroX}' y1='${top}' x2='${zeroX}' y2='${height-bottom}' stroke='#52627d'/><text x='${zeroX}' y='${top-6}' text-anchor='middle' fill='#8e9bb0' font-size='11'>0.00 · Reference: ${reference}</text><text x='${plotLeft}' y='${top-6}' text-anchor='start' fill='#8e9bb0' font-size='10'>Inverse</text><text x='${plotRight}' y='${top-6}' text-anchor='end' fill='#8e9bb0' font-size='10'>Positive</text>`;
    legend.innerHTML = `<span class='sector-legend reference-legend'><i></i>Reference: ${reference}</span>`;
    values.forEach((item, index) => {
      const y = top + index * rowHeight + 8, value = item.value;
      const label = document.createElementNS(NS, 'text'); label.setAttribute('x', value >= 0 ? zeroX - 14 : zeroX + 14); label.setAttribute('y', y + 14); label.setAttribute('text-anchor', value >= 0 ? 'end' : 'start'); label.setAttribute('fill', '#b5c0d2'); label.setAttribute('font-size', '12'); label.textContent = item.name; svg.appendChild(label);
      if (value == null) return;
      const bar = document.createElementNS(NS, 'rect');
      const scale = Math.min(zeroX - plotLeft, plotRight - zeroX);
      bar.setAttribute('x', value >= 0 ? zeroX : zeroX + value * scale); bar.setAttribute('y', y); bar.setAttribute('width', Math.abs(value) * scale); bar.setAttribute('height', '16'); bar.setAttribute('rx', '4'); bar.setAttribute('fill', value >= 0.4 ? '#1f806f' : value <= -0.4 ? '#7d3f46' : '#665f3d');
      const title = document.createElementNS(NS, 'title');
      title.textContent = `${item.name} correlation with ${reference}: ${value.toFixed(2)}`;
      bar.appendChild(title); svg.appendChild(bar);
      const score = document.createElementNS(NS, 'text'); score.setAttribute('x', value >= 0 ? zeroX + Math.abs(value) * scale + 8 : zeroX + value * scale - 8); score.setAttribute('y', y + 13); score.setAttribute('text-anchor', value >= 0 ? 'start' : 'end'); score.setAttribute('fill', '#b5c0d2'); score.setAttribute('font-size', '11'); score.textContent = value.toFixed(2); svg.appendChild(score);
    });
  }
  select.addEventListener('change', draw); draw();
})();
</script>"""
    rotation_html = """
<div class='chart-scroll'><svg id='sector-rotation-flow' viewBox='0 0 920 420' role='img' aria-label='Probable next sector rotation flow'></svg></div>
<script>
(() => {
  const history = """ + history_json + """;
  const sectors = """ + json.dumps(sector_names) + """;
  const tickers = """ + ticker_json + """;
  const svg = document.getElementById('sector-rotation-flow');
  const values = name => history.map(day => day.scores[name]).filter(value => value != null).map(Number);
  const stats = sectors.map(name => { const v = values(name), recent = v.length > 5 ? v[v.length-1] - v[v.length-6] : 0, long = v.length > 20 ? v[v.length-1] - v[v.length-21] : recent; return {name, recent, long, score: Math.max(0, Math.min(100, 50 + recent * 3 + (recent - long / 4) * 2))}; }).sort((a,b) => b.score-a.score);
  const winners = stats.filter(x => x.recent > 0).slice(0, 5), losers = stats.filter(x => x.recent < 0).sort((a,b) => a.recent-b.recent).slice(0, 5);
  const width = 920, height = 420, left = 28, center = 460, top = 34, row = 62;
  svg.innerHTML = `<text x='${left}' y='18' fill='#8e9bb0' font-size='11'>WEAKENING / OUTFLOW PROXY</text><text x='${center+20}' y='18' fill='#8e9bb0' font-size='11'>IMPROVING / INFLOW PROXY</text><line x1='${center}' y1='${top}' x2='${center}' y2='${height-20}' stroke='#52627d'/>`;
  const count = Math.max(winners.length, losers.length);
  for (let i=0; i<count; i++) {
    const y = top + i * row + 18, loser = losers[i], winner = winners[i];
    const tickerText = name => (tickers[name] || []).map(item => item.symbol).join(', ') || 'No screened tickers available';
    const tickerColor = name => (tickers[name] || []).some(item => Number(item.change) > 0) ? '#70d6c3' : '#ff8a80';
    if (loser) { svg.insertAdjacentHTML('beforeend', `<text x='${center-18}' y='${y}' text-anchor='end' fill='#b5c0d2' font-size='13'>${loser.name}</text><text x='${center-18}' y='${y+17}' text-anchor='end' fill='#ff8a80' font-size='11'>${loser.recent.toFixed(1)} pts · ${tickerText(loser.name)}</text>`); }
    if (winner) { const probability = Math.round(winner.score); svg.insertAdjacentHTML('beforeend', `<line x1='${center+12}' y1='${y-5}' x2='${center+150}' y2='${y-5}' stroke='#70d6c3' stroke-width='2' marker-end='url(#arrow)'/><text x='${center+170}' y='${y}' fill='#b5c0d2' font-size='13'>${winner.name}</text><text x='${center+170}' y='${y+17}' fill='${tickerColor(winner.name)}' font-size='11'>Rotation ${probability}/100 · ${tickerText(winner.name)}</text>`); }
  }
  svg.insertAdjacentHTML('afterbegin', `<defs><marker id='arrow' markerWidth='8' markerHeight='8' refX='7' refY='3' orient='auto'><path d='M0,0 L0,6 L8,3 z' fill='#70d6c3'/></marker></defs>`);
})();
</script>"""
    marker = "{SECTOR_ROTATION}"
    replacement = f"<section><h2>Sector Rotation</h2><h3>Sector Rotation — Heatmap</h3>{heatmap}<div class='sector-chart-columns'><div><h3>Reference-Sector Correlation</h3>{correlation_html}</div><div><h3>Probable Next Sector Rotation</h3>{rotation_html}</div></div></section>"
    return html.replace(marker, replacement, 1)

def build(input_path: Path, output_dir: Path) -> None:
    report = json.loads(input_path.read_text(encoding="utf-8"))
    (output_dir / "assets").mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render(report), encoding="utf-8")
    (output_dir / "data").mkdir(exist_ok=True)
    (output_dir / "data" / "latest.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    details_dir = output_dir / "details"
    details_dir.mkdir(parents=True, exist_ok=True)
    for item in [item for profile_items in report.get("profiles", {}).values() for item in profile_items]:
        symbol = str(item.get("symbol", "")).upper()
        research = item.get("research", {}) or {}
        components = item.get("components", {}) or {}
        if not components:
            for reason in item.get("reasons", []) or []:
                if isinstance(reason, str) and ":" in reason:
                    key, value = reason.rsplit(":", 1)
                    try:
                        components[key.strip()] = float(value.strip())
                    except ValueError:
                        pass
        weights = item.get("weights", {}) or {
            "market": 0.10, "sector": 0.10, "relative_strength": 0.20,
            "vwap": 0.15, "trend": 0.15, "volume": 0.10,
            "momentum": 0.10, "volatility": 0.05, "options": 0.00,
            "extension": 0.05,
        }
        component_rows = "".join(f"<tr><td>{escape(str(key).replace('_', ' ').title())}</td><td>{float(value):.1f}</td><td>{float(weights.get(key, 0)) * 100:.1f}%</td><td>{float(value) * float(weights.get(key, 0)):.1f}</td></tr>" for key, value in components.items() if isinstance(value, (int, float)))
        research_rows_parts = []
        for key, value in research.items():
            if key in {"symbol", "research_score"}:
                continue
            label = escape(str(key).replace("_", " ").title())
            if isinstance(value, list):
                content = "<ul class='research-list'>" + "".join(f"<li>{escape(str(entry))}</li>" for entry in value) + "</ul>"
            elif key.lower() == "summary":
                content = f"<p class='research-summary'>{escape(str(value))}</p>"
            else:
                content = escape(str(value))
            research_rows_parts.append(f"<tr><th>{label}</th><td>{content}</td></tr>")
        research_rows = "".join(research_rows_parts)
        research_score = float(research.get("research_score", 0))
        research_highlights = f"<div class='research-highlights'><div><span class='eyebrow'>RESEARCH SCORE</span><strong>{research_score:.1f}/100</strong></div><div><span class='eyebrow'>CONVICTION</span><strong>{escape(str(research.get('conviction', 'Unavailable')))}</strong></div></div>"
        python_score = float(item.get("score", 0))
        research_score = float(research.get("research_score", 0))
        boosted_score = float(item.get("boosted_score", python_score))
        contribution = (f"<section><h2>Score Contribution</h2><p class='muted'>Boosted score = Technical score × 70% + Research score × 30%.</p><table><thead><tr><th>Source</th><th>Raw score</th><th>Weight</th><th>Contribution</th></tr></thead><tbody><tr><td>Technical</td><td>{python_score:.1f}</td><td>70%</td><td>{python_score * .70:.1f}</td></tr><tr><td>Research</td><td>{research_score:.1f}</td><td>30%</td><td>{research_score * .30:.1f}</td></tr><tr><th>Boosted total</th><th colspan='2'></th><th>{boosted_score:.1f}</th></tr></tbody></table></section>")
        detail = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{escape(symbol)} Details</title><link rel='stylesheet' href='../assets/styles.css'></head><body><main><p><a href='../index.html'>← Back to Market Intelligence</a></p><h1>{escape(symbol)} Details</h1><p class='muted'>Day-trading candidate · {escape(str(item.get('direction', 'UNKNOWN')))}</p><section><h2>Score Summary</h2><table><tbody><tr><th>Technical score</th><td>{float(item.get('score', 0)):.1f}</td></tr><tr><th>Research score</th><td>{float(research.get('research_score', 0)):.1f}</td></tr><tr><th>Boosted score</th><td>{float(item.get('boosted_score', item.get('score', 0))):.1f}</td></tr></tbody></table></section><section><h2>Technical Indicators and Components</h2><p class='muted'>Contribution = component score × profile weight. The contributions sum to the technical score.</p><table><thead><tr><th>Component</th><th>Score</th><th>Weight</th><th>Contribution</th></tr></thead><tbody>{component_rows}</tbody></table></section><section><h2>Research Details</h2>{research_highlights}<table><tbody>{research_rows or '<tr><td colspan=\"2\">No research details available.</td></tr>'}</tbody></table></section><p><a href='../index.html'>← Back to Market Intelligence</a></p></main></body></html>"
        detail = detail.replace("</section><section><h2>Python Filters and Components</h2>", f"</section>{contribution}<section><h2>Python Filters and Components</h2>")
        detail = detail.replace("<h2>Technical Indicators and Components</h2>", "<h2>Technical Indicators and Components</h2><p class='muted'>These component metrics form the technical score: market regime, sector strength, relative strength, VWAP, trend, volume, momentum, volatility, options confirmation, and extension.</p>")
        (details_dir / f"{symbol}.html").write_text(detail, encoding="utf-8")
    css = Path(__file__).parent / "styles.css"
    extra_css = """
.sector-legend-wrap{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0 20px}.sector-legend{font-size:.8rem;color:#b5c0d2;white-space:nowrap}.sector-legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;background:#8e9bb0}.reference-legend i{background:#fff;border:1px solid #70d6c3}.active-theme-compact{font-size:.82rem}.active-theme-compact strong{font-size:1rem;margin-right:8px}.active-theme-compact .muted{font-size:.78rem}
.research-highlights{display:flex;gap:12px;flex-wrap:wrap;margin:12px 0}.research-highlights>div{min-width:150px;padding:12px 14px;background:#111b2d;border:1px solid #263650;border-radius:10px}.research-highlights strong{display:block;font-size:1.15rem;margin-top:4px}.research-list{margin:0;padding-left:20px}.research-list li{margin:5px 0}.research-summary{margin:0;line-height:1.55;color:#d4dbea}
.sector-chart-columns{display:grid;grid-template-columns:1fr;gap:28px;align-items:start}.sector-chart-columns>div{min-width:0}.sector-chart-columns h3{margin-top:18px}
.sector-chart-columns svg{width:100%;height:auto;min-height:300px}.sector-chart-columns svg text{font-size:14px!important}.sector-chart-columns .sector-legend{font-size:.95rem}.sector-chart-columns select{font-size:1rem;padding:6px 8px}.sector-chart-columns .muted{font-size:.95rem}
.sector-heatmap th,.sector-heatmap td{padding:9px 10px;text-align:center;white-space:nowrap}.sector-heatmap th:first-child{text-align:left;position:sticky;left:0;background:#131d30}.sector-heatmap td{border:1px solid #263650}.heat-0,.heat-10,.heat-20,.heat-30,.heat-40{background:#7d3f46}.heat-50,.heat-60{background:#665f3d}.heat-70,.heat-80{background:#35655e}.heat-90,.heat-100{background:#1f806f}.sector-ranking{display:grid;gap:8px}.ranking-row{display:grid;grid-template-columns:minmax(110px,1.2fr) 3fr 45px 45px;gap:10px;align-items:center;font-size:.9rem}.ranking-bar{height:10px;background:#263650;border-radius:99px;overflow:hidden}.ranking-bar b{display:block;height:100%;background:#70d6c3;border-radius:99px}.ranking-row em{font-style:normal;color:#8e9bb0}.correlation-matrix th,.correlation-matrix td{padding:8px;text-align:center;white-space:nowrap;font-size:.82rem}.correlation-matrix th:first-child{text-align:left;position:sticky;left:0;background:#131d30}.corr-positive{background:#1f806f}.corr-neutral{background:#665f3d}.corr-negative{background:#7d3f46}.corr-na{background:#263650;color:#8e9bb0}.cluster-summary,.divergence{margin-top:14px;padding:14px;background:#111b2d;border:1px solid #263650;border-radius:10px}.cluster-summary h4,.divergence h4{margin:0 0 8px}@media(max-width:650px){.ranking-row{grid-template-columns:90px 1.5fr 38px 38px;font-size:.78rem}}
"""
    (output_dir / "assets" / "styles.css").write_text(css.read_text(encoding="utf-8") + extra_css, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).parent / "sample_report.json")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "site")
    args = parser.parse_args()
    build(args.input, args.output)
    print(f"site_generated={args.output}")
