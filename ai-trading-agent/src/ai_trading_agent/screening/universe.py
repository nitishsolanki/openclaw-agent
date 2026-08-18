import pandas as pd

def liquid_candidates(snapshot: pd.DataFrame, minimum_price: float = 5.0,
                      minimum_average_volume: int = 1_000_000) -> pd.DataFrame:
    required = {"symbol", "price", "average_volume"}
    missing = required - set(snapshot.columns)
    if missing:
        raise ValueError(f"missing universe fields: {sorted(missing)}")
    return snapshot[(snapshot["price"] > minimum_price) &
                    (snapshot["average_volume"] >= minimum_average_volume)].copy()

