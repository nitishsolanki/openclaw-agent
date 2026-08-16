# Market Research Agent Scheduler

## Overview

The scheduler provides multiple automation modes for running the market research agent:

1. **Once**: Single execution (useful for manual testing or one-off runs)
2. **Daily**: Scheduled execution at a specific time each day (default 8:00 AM)
3. **Continuous**: Repeated execution at fixed intervals (default every 4 hours)

## Usage

### Single Run
```bash
python scheduler.py --mode once --root .
```

### Daily Automation
```bash
python scheduler.py --mode daily --root . --run-time "08:00"
```

This will run the market research agent every day at 8:00 AM and log results to `scheduler.log`.

### Continuous Monitoring
```bash
python scheduler.py --mode continuous --root . --interval 4
```

This will run the market research agent every 4 hours indefinitely.

## Windows Task Scheduler Setup

To schedule daily runs on Windows, create a new task:

1. Open **Task Scheduler**
2. Create a new basic task
3. Set trigger: Daily at your preferred time (e.g., 8:00 AM)
4. Set action: Start a program
   - Program: `C:\Path\To\Python314\python.exe`
   - Arguments: `scheduler.py --mode once --root C:\Users\nitis\.openclaw\workspace\market-research-agent`
   - Start in: `C:\Users\nitis\.openclaw\workspace\market-research-agent`

## Logging

The scheduler logs all activity to `scheduler.log` including:
- Run start/end times
- Success/failure status
- Next scheduled run time
- Any errors encountered

## Integration with CI/CD

For GitHub Actions or similar CI/CD systems, use:
```bash
python scheduler.py --mode once --root .
```

## Position Sizing and Risk Management

The scheduler inherits all risk management features from the agent:

- **Position sizing** is automatically calculated based on:
  - Macro regime (risk-on/off/neutral)
  - Conviction level (High/Medium/Low)
  - Opportunity score (0-100)
  
- **Sector weighting** adapts to market conditions
- **Portfolio allocation** defaults to 10% per position, capped at 15% maximum

All position sizing recommendations are logged in the daily report.
