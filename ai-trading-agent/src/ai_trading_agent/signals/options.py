def options_confirmation(snapshots) -> float:
    """Score options confirmation from available snapshot Greeks/volume; neutral if absent."""
    values = snapshots.values() if hasattr(snapshots, "values") else snapshots or []
    values = list(values)
    if not values:
        return 50.0
    volume = sum(float(getattr(item, "daily_volume", 0) or 0) for item in values)
    open_interest = sum(float(getattr(item, "open_interest", 0) or 0) for item in values)
    if not volume and not open_interest:
        return 50.0
    return min(100.0, 50.0 + min(25.0, volume / 1000) + min(25.0, open_interest / 10000))

