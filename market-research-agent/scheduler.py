"""
Daily scheduler for market research agent automation.

Usage:
  python scheduler.py --mode once          # Run once
  python scheduler.py --mode daily         # Run daily at 8:00 AM
  python scheduler.py --mode continuous   # Run every 4 hours
"""

from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime, time, timedelta
from pathlib import Path
import time as time_module

import agent


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scheduler.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def run_market_research_job(root: str | Path, output_dir: str | Path | None = None) -> dict:
    try:
        logger.info("Starting market research agent run...")
        result = agent.run_market_research(root, output_dir)
        logger.info(f"Agent run completed: {result}")
        return result
    except Exception as e:
        logger.error(f"Agent run failed: {e}", exc_info=True)
        return {"status": "failed", "error": str(e)}


def schedule_daily_run(root: str | Path, output_dir: str | Path | None = None, run_time: time = time(8, 0)) -> None:
    logger.info(f"Scheduler started in daily mode. Will run at {run_time} daily.")
    root_path = Path(root)

    while True:
        now = datetime.now()
        run_datetime = datetime.combine(now.date(), run_time)

        if now >= run_datetime:
            run_datetime = run_datetime + timedelta(days=1)

        wait_seconds = (run_datetime - now).total_seconds()
        logger.info(f"Next run scheduled for {run_datetime} (in {wait_seconds / 3600:.1f} hours)")

        time_module.sleep(wait_seconds)

        run_market_research_job(root_path, output_dir)


def schedule_continuous_run(root: str | Path, output_dir: str | Path | None = None, interval_hours: int = 4) -> None:
    logger.info(f"Scheduler started in continuous mode. Will run every {interval_hours} hours.")
    root_path = Path(root)
    interval_seconds = interval_hours * 3600

    while True:
        run_market_research_job(root_path, output_dir)
        logger.info(f"Sleeping for {interval_hours} hours until next run...")
        time_module.sleep(interval_seconds)


def run_once(root: str | Path, output_dir: str | Path | None = None) -> dict:
    logger.info("Running market research agent once...")
    return run_market_research_job(root, output_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Market research agent scheduler")
    parser.add_argument("--root", type=str, default=".", help="Path to the market research agent directory")
    parser.add_argument("--output-dir", type=str, default=None, help="Optional directory for generated reports")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["once", "daily", "continuous"],
        default="once",
        help="Scheduler mode: once (single run), daily (8 AM), or continuous (every 4 hours)",
    )
    parser.add_argument(
        "--run-time",
        type=str,
        default="08:00",
        help="Time to run daily mode (HH:MM format, default 08:00)",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=4,
        help="Interval in hours for continuous mode (default 4)",
    )

    args = parser.parse_args()

    if args.mode == "once":
        result = run_once(args.root, args.output_dir)
        print(json.dumps(result, indent=2))
    elif args.mode == "daily":
        try:
            run_hour, run_minute = map(int, args.run_time.split(":"))
            run_time_obj = time(run_hour, run_minute)
        except (ValueError, AttributeError):
            logger.error(f"Invalid time format: {args.run_time}. Use HH:MM format.")
            return
        schedule_daily_run(args.root, args.output_dir, run_time_obj)
    elif args.mode == "continuous":
        schedule_continuous_run(args.root, args.output_dir, args.interval)


if __name__ == "__main__":
    main()
