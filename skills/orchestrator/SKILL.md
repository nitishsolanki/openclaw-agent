---
name: orchestrator
description: Coordinate the complete daily market research workflow.
---
## Model Selection

Before executing a skill:

1. Read config/models.yaml.
2. Use the configured primary model.
3. If the model is unavailable, rate-limited, or returns a transient error:
   - Retry up to 3 times with exponential backoff.
   - If it still fails, use the configured fallback model.
4. Log which model was used for each step.

# Market Research Orchestrator

## Goal

Execute the entire daily market research process from start to finish.

## Workflow

### Step 1

Use the **news** skill.

Save results to:

market-research-agent/data/news/

---

### Step 2

Use the **macro** skill.

Save results to:

market-research-agent/data/macro/

---

### Step 3

Use the **sec-filings** skill.

Save results to:

market-research-agent/data/sec-filings/

---

### Step 4

Use the **stocks** skill.

Read:

market-research-agent/watchlist.txt

Generate one markdown report per ticker.

Save to:

market-research-agent/data/stocks/

---

### Step 5

Use the **report-generator** skill.

Read:

- data/news
- data/macro
- data/sec-filings
- data/stocks

Generate:

reports/latest.md

---

Do not skip any steps.

Always report progress.

Stop immediately if a required skill fails.