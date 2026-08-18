from datetime import date, datetime

POSITIVE = {"upgrade", "beat", "growth", "record", "surge", "strong", "buy"}
NEGATIVE = {"downgrade", "miss", "loss", "fraud", "lawsuit", "weak", "cut"}

def news_confirmation(articles: list[dict]) -> float:
    if not articles:
        return 50.0
    positive = negative = 0
    for article in articles:
        text = f"{article.get('headline', '')} {article.get('summary', '')}".lower()
        positive += sum(word in text for word in POSITIVE)
        negative += sum(word in text for word in NEGATIVE)
    return max(0.0, min(100.0, 50.0 + (positive - negative) * 5.0))

def earnings_risk(calendar: dict, symbol: str, days: int = 7, today: date | None = None) -> float:
    today = today or date.today()
    for event in calendar.get("earningsCalendar", []):
        if event.get("symbol", "").upper() != symbol.upper():
            continue
        try:
            event_date = datetime.fromisoformat(event["date"]).date()
        except (KeyError, ValueError):
            continue
        if 0 <= (event_date - today).days <= days:
            return 25.0
    return 100.0

