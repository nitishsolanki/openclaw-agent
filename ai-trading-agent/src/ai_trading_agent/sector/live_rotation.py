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
