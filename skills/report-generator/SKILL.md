---
name: report-generator
description: Generate the final daily market report from all collected research.
---

# Report Generator

## Goal

Generate a professional daily market report.

## Inputs

Read:

market-research-agent/data/news/

market-research-agent/data/macro/

market-research-agent/data/stocks/

market-research-agent/data/sec-filings/

## Tasks

Merge all collected information.

Remove duplicate information.

Prioritize important events.

Highlight the five highest conviction opportunities.

Summarize today's biggest risks.

## Output

Generate

market-research-agent/reports/latest.md

Also save

market-research-agent/data/reports/YYYY-MM-DD.md