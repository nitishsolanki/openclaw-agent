# Analyze Stock

Analyze the supplied stock ticker.

Produce a concise, trading-oriented markdown report. Preserve important facts, but avoid essay-style paragraphs.

Start with this table:

| Field | Value |
|---|---|
| Ticker | ... |
| Price / date | ... |
| Sector / industry | ... |
| Conviction | High / Medium / Low |
| Trading bias | Buy / Accumulate on weakness / Hold / Avoid |

Use short bullets and compact tables wherever possible. Put actionable trading information first.

## Hard Output Rules

- Keep the entire report between 350 and 450 words.
- Use exactly the section headings below, in the same order.
- Do not write paragraphs longer than two sentences.
- Use no more than 3 bullets in any section.
- Do not repeat the same fact in multiple sections.
- Never invent prices, scores, entry levels, stops, targets, dates, financial figures, or analyst opinions.
- If information is unavailable, write `Not available` rather than guessing.
- Do not add sections named Snapshot, Latest operating results, What would change the view, or Bottom line.

# Trading Snapshot

Use the opening table above, then continue with these exact sections.

# Key Fundamentals

Use a compact table with no more than five decision-relevant metrics.

| Metric | Latest value | Trading relevance |
|---|---:|---|
| ... | ... | ... |

# Recent Developments

Summarize the three most important recent news, earnings, filings, or product developments in one-line bullets.


# Earnings

Latest earnings highlights.

# Analyst Activity
Use no more than three concise coverage.

# Bull Case

Use no more than three concise bullets.

# Bear Case

Use no more than three concise bullets.

# Risks

Largest investment risks.

# Catalysts

Upcoming events that may move the stock. Use no more than three bullets and include dates only when verified.

# Trading View

| Item | View |
|---|---|
| Bias | ... |
| Entry condition | ... |
| Invalidation | ... |
| Time horizon | Swing / Position |
| Position guidance | ... |

Do not provide a specific entry, stop, target, or position size unless supported by supplied market-data calculations. If unavailable, describe the condition qualitatively.

End with one sentence stating the key fact or event that would change the view, followed by a brief source note and disclaimer.
