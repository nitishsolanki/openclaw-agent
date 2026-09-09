import argparse
import json
import math
import re
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
        rows = "".join(f"<tr><td>{escape(str(item['symbol']).upper())} <a class='detail-link' href='details/{escape(str(item['symbol']).upper())}.html' title='View details'>»</a></td><td>{float(item.get('score', 0)):.1f}</td><td>{float(item.get('research', {}).get('research_score', 0)):.1f}</td><td><strong>{float(item.get('boosted_score', item.get('score', 0))):.1f}</strong></td><td><span class='setup-badge setup-{escape(str(item.get('setup_maturity', 'BUILDING')).lower())}'>{escape(str(item.get('setup_maturity', 'BUILDING')))}</span></td></tr>" for item in items)
        return f"<div class='table-scroll candidate-table-wrap'><table class='candidate-table'><thead><tr><th>Ticker</th><th>Technical</th><th>Research</th><th>Boosted</th><th>Setup</th></tr></thead><tbody>{rows}</tbody></table></div>"
    profile_signals = report.get("profiles", {}) or {"swing": report.get("signals", [])}
    merged_candidates = {}
    for profile, items in profile_signals.items():
        for item in items:
            symbol = str(item.get("symbol", "")).upper()
            if not symbol:
                continue
            record = merged_candidates.setdefault(symbol, {**item, "profiles": set()})
            record["profiles"].add(profile.title())
            if float(item.get("boosted_score", item.get("score", 0))) > float(record.get("boosted_score", record.get("score", 0))):
                for key in ("score", "research", "boosted_score", "components", "setup_maturity", "early_setup_score", "entry_timing_score", "opportunity_score", "recommendation"):
                    if key in item:
                        record[key] = item[key]
    category_order = ["BUILDING", "BREAKOUT_READY", "CONFIRMED_BREAKOUT", "PULLBACK", "EXTENDED"]
    category_sections = []
    for category in category_order:
        items = [item for item in merged_candidates.values() if str(item.get("setup_maturity", "BUILDING")) == category]
        items.sort(key=lambda item: float(item.get("boosted_score", item.get("score", 0))), reverse=True)
        rows = "".join(f"<tr><td>{escape(str(item['symbol']).upper())} <a class='detail-link' href='details/{escape(str(item['symbol']).upper())}.html' title='View details'>»</a></td><td>{escape('/'.join(sorted(item['profiles'])))}</td><td>{float(item.get('score', 0)):.1f}</td><td>{float(item.get('research', {}).get('research_score', 0)):.1f}</td><td><strong>{float(item.get('boosted_score', item.get('score', 0))):.1f}</strong></td><td>{escape(str(item.get('recommendation', 'WATCH')))}</td></tr>" for item in items)
        if not rows:
            rows = "<tr><td colspan='6' class='muted'>No candidates in this category.</td></tr>"
        compact_rows = "".join(f"<div class='compact-stock'><a href='details/{escape(str(item['symbol']).upper())}.html'>{escape(str(item['symbol']).upper())} »</a><span>{float(item.get('boosted_score', item.get('score', 0))):.1f}</span></div>" for item in items[:3]) or "<div class='muted compact-empty'>No candidates in this category</div>"
        category_sections.append(f"<div class='maturity-card maturity-{category.lower()}'><h3>{category.replace('_', ' ').title()} <span>{len(items)}</span></h3>{compact_rows}<a class='category-more' href='#full-candidates'>View details →</a></div>")
    candidate_sections = "<section id='full-candidates'><div class='section-head'><h2>Opportunity command center</h2><a class='open-candidates' href='#candidate-details' onclick=\"document.getElementById('candidate-details').open=true\">Open full candidate list →</a></div><div class='maturity-grid'>" + "".join(category_sections) + "</div></section>"
    full_rows = []
    for category in category_order:
        items = [item for item in merged_candidates.values() if str(item.get('setup_maturity', 'BUILDING')) == category]
        items.sort(key=lambda item: float(item.get('boosted_score', item.get('score', 0))), reverse=True)
        rows = ''.join(f"<tr><td><a class='detail-link' href='details/{escape(str(item['symbol']).upper())}.html'>{escape(str(item['symbol']).upper())} »</a></td><td>{escape('/'.join(sorted(item['profiles'])))}</td><td>{float(item.get('score', 0)):.1f}</td><td>{float(item.get('research', {}).get('research_score', 0)):.1f}</td><td><strong>{float(item.get('boosted_score', item.get('score', 0))):.1f}</strong></td><td>{escape(str(item.get('recommendation', 'WATCH')))}</td></tr>" for item in items)
        if not rows:
            rows = "<tr><td colspan='6' class='muted'>No candidates in this category.</td></tr>"
        full_rows.append(f"<section><h3>{category.replace('_', ' ').title()} Candidates ({len(items)})</h3><div class='table-scroll candidate-table-wrap'><table class='candidate-table'><thead><tr><th>Ticker</th><th>Profiles</th><th>Technical</th><th>Research</th><th>Boosted</th><th>Recommendation</th></tr></thead><tbody>{rows}</tbody></table></div></section>")
    full_list_html = "<details id='candidate-details' class='full-candidate-disclosure'><summary>Open full candidate list →</summary><div class='full-candidate-content'><div class='section-head'><h2>Full candidate lists</h2><a href='#full-candidates'>Back to top candidates ↑</a></div>" + ''.join(full_rows) + "</div></details>"
    candidate_sections = candidate_sections.replace("href='#full-candidates'", "href='#candidate-details' onclick=\"document.getElementById('candidate-details').open=true\"") + full_list_html
    market_score = float(report.get('market', {}).get('score', 0) or 0)
    all_candidates = [item for values in profile_signals.values() for item in values]
    researched = sum(1 for item in all_candidates if float(item.get('research', {}).get('research_score', 0) or 0) > 0)
    unique_count = len(merged_candidates)
    maturity_counts = {category: sum(1 for item in merged_candidates.values() if str(item.get('setup_maturity', 'BUILDING')) == category) for category in category_order}
    pulse_html = f"<section class='pulse-grid'><div class='pulse-card'><span class='eyebrow'>MARKET REGIME</span><strong class='pulse-value'>{'Risk-on' if market_score >= 60 else 'Neutral' if market_score >= 45 else 'Risk-off'}</strong><span class='muted'>Market score {market_score:.1f}/100</span></div><div class='pulse-card'><span class='eyebrow'>ACTIVE THEME</span><strong class='pulse-value'>{escape(str(report.get('theme', {}).get('name', 'Market leadership')).replace('_', ' '))}</strong><span class='muted'>{escape(', '.join(report.get('theme', {}).get('sectors', [])))}</span></div><div class='pulse-card'><span class='eyebrow'>ACTIONABLE SETUPS</span><strong class='pulse-value'>{maturity_counts.get('BUILDING', 0) + maturity_counts.get('BREAKOUT_READY', 0) + maturity_counts.get('CONFIRMED_BREAKOUT', 0)}</strong><span class='muted'>{maturity_counts.get('BREAKOUT_READY', 0)} breakout-ready · {maturity_counts.get('BUILDING', 0)} building</span></div><div class='pulse-card'><span class='eyebrow'>RESEARCH COVERAGE</span><strong class='pulse-value'>{researched}/{unique_count}</strong><span class='muted'>researched candidates</span></div></section>"
    def format_index(index):
        change = index.get('change_pct')
        css_class = 'price-up' if change is not None and float(change) >= 0 else 'price-down'
        value = 'N/A' if change is None else f'{float(change):+.2f}%'
        return f"<div class='index-row'><span>{escape(str(index.get('label', index.get('symbol', 'Index'))))}</span><strong class='{css_class}'>{value}</strong></div>"
    try:
        scan_time = datetime.fromisoformat(str(report.get('generated_at', '')).replace('Z', '+00:00'))
        if scan_time.tzinfo is None:
            scan_time = scan_time.replace(tzinfo=timezone.utc)
        scan_hour = scan_time.astimezone(ZoneInfo('America/Chicago')).hour
    except (TypeError, ValueError):
        scan_hour = 0
    next_scan = '7:00 AM' if scan_hour < 7 or scan_hour >= 12 else '9:00 AM' if scan_hour < 9 else '12:00 PM'
    pulse_html = pulse_html.replace("<span class='muted'>researched candidates</span>", f"<span class='muted'>researched candidates</span><strong class='next-scan'>Next scan · {next_scan}</strong>")
    index_data = report.get('market', {}).get('indices', [])
    index_rows = ''.join(format_index(index) for index in index_data) or "<div class='index-empty'>Data unavailable — run the next live scan</div>"
    pulse_html = pulse_html.replace("<div class='pulse-card'><span class='eyebrow'>MARKET REGIME</span><strong class='pulse-value'>" + ('Risk-on' if market_score >= 60 else 'Neutral' if market_score >= 45 else 'Risk-off') + "</strong><span class='muted'>Market score " + f"{market_score:.1f}/100</span></div>", "<div class='pulse-card'><span class='eyebrow'>MARKET REGIME</span><div class='index-list'>" + index_rows + "</div><span class='muted'>Latest available index change</span></div>")
    top_sector = ranked_sectors[0]['sector'] if ranked_sectors else 'No sector data'
    top_candidate = sorted(merged_candidates.values(), key=lambda item: float(item.get('boosted_score', item.get('score', 0))), reverse=True)[:1]
    change_html = f"<section class='change-strip'><div class='section-head'><h2>What changed today?</h2><span class='muted'>Latest scan summary</span></div><div class='change-grid'><div><strong>{escape(str(top_candidate[0].get('symbol', 'No candidate'))) if top_candidate else 'No candidate'}</strong><span>Top opportunity by boosted score</span></div><div><strong>{escape(str(top_sector))} leadership</strong><span>Highest current sector score</span></div><div><strong>{maturity_counts.get('EXTENDED', 0)} extended setups</strong><span>Review before opening new positions</span></div></div></section>"
    candidate_sections = pulse_html + change_html + candidate_sections
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>AI Trading Market Report</title><link rel='stylesheet' href='assets/styles.css'></head><body><main><header><p class='eyebrow'>AI TRADING AGENT · PAPER MODE</p><h1>Market Intelligence</h1><p class='muted'>Generated {escape(report.get('generated_at', 'unknown'))} · Source: {escape(str(report.get('data_source', 'unknown')))}</p></header><section class='hero'><div class='active-theme-compact'><span class='eyebrow'>ACTIVE THEME</span><strong>{escape(report['theme']['name'])}</strong><span class='muted'>{', '.join(report['theme'].get('sectors', []))}</span></div></section>{{SECTOR_ROTATION}}{candidate_sections}<footer>{escape(report.get('disclaimer', ''))}</footer></main></body></html>"""

def render(report: dict) -> str:
    def format_date(value: str) -> str:
        try:
            parsed = datetime.strptime(str(value), "%Y-%m-%d")
            return f"{parsed.strftime('%b')} {parsed.day}"
        except (TypeError, ValueError):
            return str(value)

    html = _render_base(report)
    theme_sectors = report.get('theme', {}).get('sectors', []) or []
    theme_label = ' · '.join(str(value) for value in theme_sectors[:3]) or 'Market leadership'
    try:
        generated_value = datetime.fromisoformat(str(report.get('generated_at', '')).replace('Z', '+00:00'))
        if generated_value.tzinfo is None:
            generated_value = generated_value.replace(tzinfo=timezone.utc)
        generated_value = generated_value.astimezone(ZoneInfo('America/Chicago'))
        generated_display = f"{generated_value.strftime('%b')} {generated_value.day}, {generated_value.year} · {generated_value.strftime('%I:%M %p %Z').lstrip('0')}"
    except (TypeError, ValueError):
        generated_display = 'time unavailable'
    topbar = "<div class='mock-topbar'><strong>◈ AI TRADING AGENT</strong><span>LIVE PAPER MODE · Updated " + escape(generated_display) + "</span></div>"
    hero = "<section class='mock-hero'><div><span class='eyebrow'>MARKET BRIEFING</span><p>Technology and Financials are leading while early-stage setups continue to build beneath the surface.</p></div><div class='mock-actions'><a class='mock-button primary' style='display:inline-block;background:#55dfad;border:1px solid #55dfad;border-radius:9px;color:#06151a;font-weight:800;padding:10px 15px;text-decoration:none' href='#full-candidates'>View candidates</a><a class='mock-button' style='display:inline-block;background:#101d30;border:1px solid #263b55;border-radius:9px;color:#eef5ff;padding:10px 15px;text-decoration:none' href='#sector-rotation'>Sector rotation</a></div></section>"
    html = html.replace('<header>', topbar + '<header>', 1)
    html = html.replace('</header>', hero + '</header>', 1)
    raw_theme_label = str(report.get('theme', {}).get('name', 'Market leadership')).replace('_', ' ')
    html = html.replace(escape(raw_theme_label), escape(theme_label))
    html = html.replace("<p class='eyebrow'>AI TRADING AGENT Â· PAPER MODE</p>", "", 1)
    generated_line = f"<p class='muted'>Generated {escape(str(report.get('generated_at', 'unknown')))} Â· Source: {escape(str(report.get('data_source', 'unknown')))}</p>"
    html = html.replace(generated_line, "", 1)
    html = re.sub(r"<p class='muted'>Generated .*?</p>", "", html, count=1)
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
        price_values = [day.get("prices", {}).get(sector["sector"]) for day in history if day.get("prices", {}).get(sector["sector"]) is not None]
        price_change = ((float(price_values[-1]) / float(price_values[-2]) - 1) * 100) if len(price_values) >= 2 and float(price_values[-2]) else 0.0
        price_class = "price-up" if price_change > 0 else "price-down" if price_change < 0 else "price-flat"
        summary = f"<td>{five_day:+.1f}</td><td>{twenty_day:+.1f}</td><td><strong class='{price_class}'>{price_change:+.2f}%</strong></td><td>{trend}</td>"
        heatmap_rows_parts.append(f"<tr><th>{escape(str(sector['sector']))}</th><td class='sector-etf'>{escape(str(sector.get('symbol', '—')))}</td>{''.join(cells)}{summary}</tr>")
    heatmap_rows = "".join(heatmap_rows_parts)
    heatmap = f"<div class='table-scroll'><table class='sector-heatmap'><thead><tr><th>Sector</th><th>ETF</th>{''.join(f'<th>{escape(format_date(date))}</th>' for date in dates)}<th>5D Δ</th><th>20D Δ</th><th>ETF Current Δ</th><th>Trend</th></tr></thead><tbody>{heatmap_rows}</tbody></table></div>"
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
        {"date": day.get("date", ""), "scores": day.get("scores", {}), "prices": day.get("prices", {})}
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
<div class='correlation-controls'><label for='reference-sector'>Reference sector</label><select id='reference-sector'>""" + options + """</select><span class='muted'>Correlation of ETF daily percentage returns</span></div>
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
      const previous = history[index].prices[name], current = day.prices[name];
      return previous == null || current == null || Number(previous) === 0 ? null : (Number(current) / Number(previous) - 1) * 100;
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
    replacement = f"<section><h2>Sector Rotation</h2><h3>Sector Rotation — Heatmap</h3>{heatmap}<div class='sector-chart-columns'><div><h3>Reference-Sector Correlation</h3><p class='muted'>Based on ETF daily percentage returns.</p>{correlation_html}</div><div><h3>Probable Next Sector Rotation</h3>{rotation_html}</div></div></section>"
    # Keep the landing-page flow consistent with the mock: candidates first,
    # then the complete Sector Rotation section at the bottom.
    html = html.replace(marker, "", 1)
    rotation_summary = "<section id='sector-rotation' class='rotation-summary'><div class='section-head'><h2>Sector rotation</h2><span class='muted'>5-day score movement</span></div><div class='rotation-summary-grid'><div><div class='rotation-mini-row'><b>Technology</b><span class='rotation-bar'><i style='width:86%'></i></span><strong class='price-up'>+14.0</strong></div><div class='rotation-mini-row'><b>Financials</b><span class='rotation-bar'><i style='width:74%'></i></span><strong class='price-up'>+12.0</strong></div><div class='rotation-mini-row'><b>Industrials</b><span class='rotation-bar'><i style='width:58%'></i></span><strong class='price-up'>+9.0</strong></div><div class='rotation-mini-row'><b>Energy</b><span class='rotation-bar'><i class='downbar' style='width:42%'></i></span><strong class='price-down'>-6.0</strong></div></div><div class='probable-rotation'><span class='eyebrow'>PROBABLE NEXT ROTATION</span><p><span class='price-down'>Energy fading</span> <b>→</b> <span class='price-up'>Industrials improving</span></p><p><span class='price-down'>Staples fading</span> <b>→</b> <span class='price-up'>Technology improving</span></p></div></div><div class='rotation-summary-actions'><a class='mock-button' href='#sector-rotation-full' onclick=\"document.querySelector('#sector-rotation-full details').open=true\">Open full sector analysis →</a></div></section>"
    summary_rows = []
    for sector in sorted(sectors, key=lambda item: float(item.get('score', 0)), reverse=True):
        name = str(sector.get('sector', 'Unknown'))
        values = [day.get('scores', {}).get(name) for day in history if day.get('scores', {}).get(name) is not None]
        values = [float(value) for value in values]
        recent = values[-5:]
        five_avg = sum(recent) / len(recent) if recent else 0.0
        twenty_avg = sum(values[-20:]) / len(values[-20:]) if values else 0.0
        cells = ''.join(f"<span class='rotation-day'>{value:.1f}</span>" for value in recent)
        summary_rows.append(f"<div class='sector-summary-row'><b>{escape(name)}</b><span class='rotation-days'>{cells}</span><strong>{five_avg:.1f}</strong><strong>{twenty_avg:.1f}</strong></div>")
    rotation_summary = rotation_summary.replace("<span class='muted'>5-day score movement</span>", "<span class='muted rotation-subtitle'>Last 5 days · 5D avg · 20D avg</span>")
    marker = "<div class='rotation-summary-grid'>"
    summary_table = "<div class='sector-summary-card'><div class='sector-summary-header'><b>Sector</b><span>Last 5 days</span><b>5D avg</b><b>20D avg</b></div>" + ''.join(summary_rows) + "</div>"
    rotation_summary = rotation_summary.replace(marker, marker + summary_table, 1)
    summary_table = "<div class='sector-summary-card'><div class='sector-summary-header'><b>Sector</b><span>Last 5 sessions</span><b>5D avg</b><b>20D avg</b></div>" + ''.join(summary_rows) + "</div>"
    probable = "<div class='probable-rotation'><span class='eyebrow'>PROBABLE NEXT ROTATION</span><p><span class='price-down'>Energy fading</span> <b>→</b> <span class='price-up'>Industrials improving</span></p><p><span class='price-down'>Staples fading</span> <b>→</b> <span class='price-up'>Technology improving</span></p></div>"
    rotation_summary = "<section id='sector-rotation' class='rotation-summary'><div class='section-head'><h2>Sector rotation</h2><span class='muted rotation-subtitle'>Last 5 sessions · 5D avg · 20D avg</span></div><div class='rotation-summary-grid'>" + summary_table + probable + "</div><div class='rotation-summary-actions'><a class='mock-button' href='#sector-rotation-full' onclick=\"document.querySelector('#sector-rotation-full details').open=true\">Open full sector analysis →</a></div></section>"
    full_section = replacement.replace("<section>", "<section id='sector-rotation-full' class='full-sector-analysis'><details><summary>Full Sector Rotation analysis</summary>", 1).replace("</section>", "</details></section>", 1)
    return html.replace("</main>", rotation_summary + full_section + "</main>", 1)

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
.candidate-card{font-size:.82rem;padding:12px}.candidate-card h3{font-size:.95rem;margin:.15rem 0}.candidate-card p{margin:.35rem 0}.candidate-card .badge{font-size:.75rem;padding:3px 6px}.candidate-card a{font-size:.78rem}
.candidate-table{min-width:620px}.candidate-table th,.candidate-table td{padding:10px 12px;font-size:1rem}.candidate-table th:not(:first-child),.candidate-table td:not(:first-child){text-align:center}.candidate-table-wrap{margin-top:8px}.candidate-table a.detail-link{color:#70d6c3;text-decoration:none;font-size:1.15rem;font-weight:700;margin-left:4px}.candidate-table a.detail-link:hover{color:#fff}.setup-badge{display:inline-block;padding:5px 9px;border-radius:999px;font-size:.82rem;font-weight:700;letter-spacing:.01em}.setup-building{background:#a87900;color:#fff7d1}.setup-breakout_ready{background:#087f6b;color:#e7fff9}.setup-confirmed_breakout{background:#1264ad;color:#e5f3ff}.setup-pullback{background:#6b4bb5;color:#f3ebff}.setup-extended{background:#b8323e;color:#fff0f0}
.price-up{color:#70d6c3}.price-down{color:#ff7777}.price-flat{color:#b5c0d2}
.pulse-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:22px 0 18px}.pulse-card{padding:17px;border:1px solid #263650;border-radius:14px;background:linear-gradient(145deg,#14253b,#101b2d)}.pulse-value{display:block;font-size:1.45rem;margin:7px 0 2px;letter-spacing:-.03em}.change-strip{padding:18px 0 4px}.change-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.change-grid>div{padding:13px;border-left:3px solid #70d6c3;background:#111b2d;border-radius:9px}.change-grid strong{display:block}.change-grid span{display:block;color:#8e9bb0;font-size:.82rem;margin-top:3px}@media(max-width:800px){.pulse-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:550px){.pulse-grid,.change-grid{grid-template-columns:1fr}}
.mock-theme{color:#eef5ff}body{background:radial-gradient(circle at 78% -10%,#1e3b62 0,#08111f 42%);color:#eef5ff}main{max-width:1280px;padding:28px 24px 70px}header{margin-bottom:38px}.hero{display:none}.section-head{margin-bottom:15px}.section h2{font-size:18px;letter-spacing:-.02em}
.mock-topbar{display:flex;justify-content:space-between;gap:20px;align-items:center;margin-bottom:38px;color:#91a5bd;font-size:12px}.mock-topbar strong{color:#eef5ff;font-size:15px}.mock-hero p{color:#91a5bd;font-size:16px;margin:9px 0 0;max-width:600px}.mock-actions{display:flex;gap:10px}.mock-button{border:1px solid #263b55;border-radius:9px;padding:10px 15px;color:#eef5ff;background:#101d30;text-decoration:none;white-space:nowrap}.mock-button.primary{background:#55dfad;border-color:#55dfad;color:#06151a;font-weight:800}header>.eyebrow{display:none}
.index-list{display:grid;gap:6px;margin:8px 0 10px}.index-row{display:flex;justify-content:space-between;align-items:center;font-size:1.05rem;font-weight:700}.index-row strong{font-size:1.05rem}.pulse-card .index-row .price-up{color:#55dfad}.pulse-card .index-row .price-down{color:#ff7780}
.pulse-card:nth-child(4) .eyebrow{font-size:10px}.pulse-card:nth-child(4) .pulse-value{font-size:22px;font-weight:800}.pulse-card:nth-child(4) .muted{font-size:10.5px}.pulse-card:nth-child(4) .next-scan{display:block;color:#f4c95d;font-size:12px;font-weight:800;margin-top:8px}
.pulse-card:nth-child(-n+3) .eyebrow{font-size:10px}.pulse-card:nth-child(-n+3) .pulse-value{font-size:22px;font-weight:800}.pulse-card:nth-child(-n+3) .muted{font-size:10.5px}.pulse-card:nth-child(2) .pulse-value{line-height:1.35;max-width:210px}.pulse-card:nth-child(3) .pulse-value{line-height:1.1}
.open-candidates{color:#83a9ff;text-decoration:none;font-size:13px}.full-candidate-disclosure{margin-top:22px}.full-candidate-disclosure summary{cursor:pointer;color:#83a9ff;font-weight:700;list-style:none;text-align:right}.full-candidate-disclosure summary::-webkit-details-marker{display:none}.full-candidate-content{margin-top:18px}
.rotation-summary{margin-top:34px;padding:20px;border:1px solid #263b55;border-radius:15px;background:linear-gradient(145deg,#14253b,#101b2d)}.rotation-summary-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:14px}.rotation-summary-grid>div{padding:16px;border:1px solid #263b55;border-radius:11px;background:rgba(8,17,31,.45)}.rotation-mini-row{display:grid;grid-template-columns:110px 1fr 55px;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08)}.rotation-mini-row:last-child{border-bottom:0}.rotation-mini-row b{font-size:.92rem}.rotation-bar{height:8px;background:#263b55;border-radius:99px;overflow:hidden}.rotation-bar i{display:block;height:100%;background:#55dfad;border-radius:99px}.rotation-bar .downbar{background:#ff7780}.probable-rotation{padding:16px!important}.probable-rotation p{margin:13px 0;padding:10px;border-radius:8px;background:#14253b}.rotation-summary-actions{margin-top:15px;text-align:right}.full-sector-analysis{margin-top:18px}.full-sector-analysis>details>summary{cursor:pointer;color:#83a9ff;font-weight:700;list-style:none;text-align:right}.full-sector-analysis>details>summary::-webkit-details-marker{display:none}.full-sector-analysis>details>summary:after{content:'  +';font-size:1.1em}@media(max-width:700px){.rotation-summary-grid{grid-template-columns:1fr}}
.rotation-summary{margin-top:34px;padding:20px;border:1px solid #263b55;border-radius:15px;background:linear-gradient(145deg,#14253b,#101b2d)}.rotation-summary-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:14px}.rotation-summary-grid>div{padding:16px;border:1px solid #263b55;border-radius:11px;background:rgba(8,17,31,.45)}.rotation-mini-row{display:grid;grid-template-columns:110px 1fr 55px;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08)}.rotation-mini-row:last-child{border-bottom:0}.rotation-mini-row b{font-size:.92rem}.rotation-bar{height:8px;background:#263b55;border-radius:99px;overflow:hidden}.rotation-bar i{display:block;height:100%;background:#55dfad;border-radius:99px}.rotation-bar .downbar{background:#ff7780}.probable-rotation{padding:16px!important;grid-column:2}.probable-rotation p{margin:13px 0;padding:10px;border-radius:8px;background:#14253b}.rotation-summary-actions{display:none}.full-sector-analysis{margin-top:18px}.full-sector-analysis>details>summary{cursor:pointer;color:#83a9ff;font-weight:700;list-style:none;text-align:right}.full-sector-analysis>details>summary::-webkit-details-marker{display:none}.full-sector-analysis>details>summary:after{content:'  +';font-size:1.1em}@media(max-width:700px){.rotation-summary-grid{grid-template-columns:1fr}.probable-rotation{grid-column:1}}
.rotation-subtitle{margin-left:auto}.sector-summary-card{grid-column:1;padding:12px!important}.sector-summary-header,.sector-summary-row{display:grid;grid-template-columns:145px 1fr 60px 60px;gap:8px;align-items:center}.sector-summary-header{color:#91a5bd;font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;padding-bottom:8px}.sector-summary-header span{text-align:center}.sector-summary-row{padding:8px 0;border-top:1px solid rgba(255,255,255,.08)}.rotation-days{display:flex;gap:4px}.rotation-day{min-width:38px;padding:4px 3px;border-radius:4px;background:#1d7e6b;text-align:center;font-size:.76rem}.sector-summary-row strong{text-align:right;font-size:.85rem}.rotation-summary-grid>div:nth-child(2){display:none}.rotation-summary-grid>div:nth-child(3){grid-column:2;grid-row:1}@media(max-width:700px){.sector-summary-card{grid-column:1}.rotation-summary-grid>div:nth-child(3){grid-column:1;grid-row:auto}.sector-summary-header,.sector-summary-row{grid-template-columns:110px 1fr 52px 52px}}
.maturity-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.maturity-card{min-height:165px;padding:14px;border-radius:11px;background:#111b2d;border-top:3px solid #70d6c3}.maturity-card h3{font-size:.78rem;letter-spacing:.06em;margin:0 0 10px}.maturity-card h3 span{float:right;font-size:1.25rem;color:#70d6c3}.maturity-breakout_ready{border-color:#f4c95d}.maturity-confirmed_breakout{border-color:#83a9ff}.maturity-pullback{border-color:#ca9cff}.maturity-extended{border-color:#ff7777}.compact-stock{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #263650}.compact-stock a{color:#70d6c3;text-decoration:none;font-weight:700}.compact-stock span{color:#b5c0d2}.compact-empty{font-size:.82rem;margin:20px 0}.category-more{display:block;margin-top:10px;color:#83a9ff;text-decoration:none;font-size:.78rem}@media(max-width:900px){.maturity-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:550px){.maturity-grid{grid-template-columns:1fr}}
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
