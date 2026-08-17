import argparse
from pathlib import Path
import pandas as pd

from .config.settings import load_strategy
from .data.market_data import CsvMarketData
from .journal.database import connect, record_signal
from .market.regime import detect_regime
from .screening.scanner import Candidate, scan

def run_scan(root: Path) -> list:
    config = load_strategy(root / "config" / "strategy.yaml")
    provider = CsvMarketData(root / "data" / "sample")
    symbols = ["AAA", "BBB", "CCC"]
    benchmark = provider.get_bars("SPY")["close"]
    regime = detect_regime(provider.get_bars("SPY"))
    candidates = [Candidate(symbol, {"AAA": "Technology", "BBB": "Energy", "CCC": "Industrials"}[symbol],
                             provider.get_bars(symbol), {"AAA": 90, "BBB": 65, "CCC": 75}[symbol])
                  for symbol in symbols]
    results = scan(candidates, benchmark, config["weights"], market_score=regime.score)
    journal = connect(root / "trading.db")
    for result in results:
        record_signal(journal, result.symbol, result.direction, result.final_score,
                      reasoning=str(result.components))
    return results

def main() -> None:
    parser = argparse.ArgumentParser(description="AI Trading Agent (signal-only scanner)")
    parser.add_argument("command", choices=["scan"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    for rank, result in enumerate(run_scan(args.root), 1):
        print(f"{rank}. {result.symbol} {result.final_score:.2f}/100 {result.direction}")
        print(f"   {result.components}")

if __name__ == "__main__":
    main()
