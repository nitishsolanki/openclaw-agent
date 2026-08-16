# OpenClaw Agent Workspace

This repository contains a small multi-agent workspace for market research and agent experimentation. It is organized as a shared workspace with one active market research agent and reusable shared skill modules.

## Goals

- Build a practical market-research workflow
- Keep agent logic modular and reusable
- Provide a structure that can scale to additional agents over time
- Keep the public repo free of local-only secrets and generated state

## Repository structure

```text
openclaw-agent/
├── .gitignore
├── AGENTS.md
├── HEARTBEAT.md
├── IDENTITY.md
├── SOUL.md
├── TOOLS.md
├── USER.md
├── README.md
├── data/
│   └── news/
├── market-research-agent/
│   ├── AGENTS.md
│   ├── README.md
│   ├── agent.py
│   ├── watchlist.txt
│   ├── config/
│   ├── data/
│   ├── prompts/
│   ├── reports/
│   ├── scripts/
│   ├── skills/
│   └── state/
├── skills/
│   ├── macro/
│   ├── news/
│   ├── portfolio/
│   ├── report-generator/
│   ├── scheduler/
│   ├── sec-filings/
│   ├── sector-rotation/
│   ├── shared/
│   └── stocks/
└── memory/
```

## Getting started

1. Open the project in a Python environment.
2. Run the market research agent from the agent directory:

```powershell
cd market-research-agent
python agent.py --root . --output-dir reports
```

3. Or run the script wrapper:

```powershell
cd market-research-agent
python scripts/run_daily.py --root . --output-dir reports
```

## Current implementation status

The repo includes:
- a working baseline `agent.py` that reads the watchlist and produces a report
- a local report generator and state file output
- prompts and templates for a larger market-research workflow

It is still intentionally modular, with many advanced skills left as extension points rather than fully integrated production services.

## Public repo guidance

This repo is structured for a public GitHub repository. The root `.gitignore` deliberately excludes:
- virtual environments
- editor metadata
- local workspace state
- personal memory files
- generated reports and caches
- secret/environment files

## Next recommended work

- Add live news and macro data fetchers
- Add SEC filing parsing and processing
- Add a scoring model for watchlist opportunities
- Add a scheduler and automation layer
- Expand agent-specific workflows beyond the initial market research pass

## License

This repository is provided as a starter project for experimentation and learning. Add a license file if you plan to distribute it more broadly.
