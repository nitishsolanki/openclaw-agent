from dataclasses import dataclass
import pandas as pd

from ..data.market_data import MarketDataProvider
from .rotation import sector_score

SECTOR_ETFS = {
    "Technology": "XLK", "Financials": "XLF", "Energy": "XLE", "Healthcare": "XLV",
    "Industrials": "XLI", "Consumer Discretionary": "XLY", "Consumer Staples": "XLP",
    "Utilities": "XLU", "Materials": "XLB", "Real Estate": "XLRE", "Communication Services": "XLC",
}

@dataclass(frozen=True)
class SectorRank:
    sector: str
    symbol: str
    score: float
    rank: int

def rank_sectors(provider: MarketDataProvider, benchmark_symbol: str = "SPY") -> list[SectorRank]:
    benchmark = provider.get_bars(benchmark_symbol)
    scores = []
    for sector, symbol in SECTOR_ETFS.items():
        try:
            score = sector_score(provider.get_bars(symbol), benchmark["close"])
        except (KeyError, ValueError, IndexError, FileNotFoundError):
            continue
        scores.append((sector, symbol, round(score, 2)))
    scores.sort(key=lambda item: item[2], reverse=True)
    return [SectorRank(sector, symbol, score, rank) for rank, (sector, symbol, score) in enumerate(scores, 1)]

def sector_score_history(provider: MarketDataProvider, days: int = 5,
                         benchmark_symbol: str = "SPY") -> list[dict]:
    """Calculate date-specific scores for the most recent available sessions."""
    benchmark = provider.get_bars(benchmark_symbol)
    if benchmark.empty:
        return []
    frames = {}
    for sector, symbol in SECTOR_ETFS.items():
        try:
            frames[sector] = provider.get_bars(symbol)
        except (KeyError, ValueError, IndexError, FileNotFoundError):
            continue
    dates = list(benchmark.index.sort_values().unique())[-days:]
    snapshots = []
    for date in dates:
        scores = {}
        prices = {}
        benchmark_slice = benchmark.loc[benchmark.index <= date]
        for sector, frame in frames.items():
            sector_slice = frame.loc[frame.index <= date]
            try:
                scores[sector] = round(sector_score(sector_slice, benchmark_slice["close"]), 2)
                prices[sector] = round(float(sector_slice["close"].iloc[-1]), 2)
            except (KeyError, ValueError, IndexError, ZeroDivisionError):
                continue
        if scores:
            snapshots.append({"date": date.strftime("%Y-%m-%d"), "scores": scores, "prices": prices})
    return snapshots
