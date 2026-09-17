"""Refresh a deduplicated S&P 500 + Nasdaq-100 + Russell 2000 universe."""
import csv
from io import StringIO
from html.parser import HTMLParser
from pathlib import Path
import ssl
from urllib.error import URLError
from urllib.request import Request, urlopen
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from ai_trading_agent.data.universe import replace_symbol_universe
from ai_trading_agent.journal.database import connect

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
NASDAQ_URL = "https://api.nasdaq.com/api/quote/list-type/nasdaq100"
RUSSELL_URL = "https://raw.githubusercontent.com/ikoniaris/Russell2000/master/russell_2000_components.csv"

class ConstituentsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_first_table = False
        self.in_symbol_cell = False
        self.rows = []
        self.cell_index = 0
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and attrs.get("id") == "constituents":
            self.in_first_table = True
        if self.in_first_table and tag == "tr":
            self.cell_index = 0
        if self.in_first_table and tag == "td" and self.cell_index == 0:
            self.in_symbol_cell = True
            self.text = []

    def handle_data(self, data):
        if self.in_symbol_cell:
            self.text.append(data)

    def handle_endtag(self, tag):
        if self.in_symbol_cell and tag == "td":
            symbol = "".join(self.text).strip().replace(".", "-")
            if symbol and symbol.isascii() and all(char.isalnum() or char == "-" for char in symbol):
                self.rows.append(symbol)
            self.in_symbol_cell = False
            self.cell_index += 1
        elif self.in_first_table and tag == "td":
            self.cell_index += 1
        if self.in_first_table and tag == "table":
            self.in_first_table = False

def fetch_symbols() -> list[str]:
    request = Request(URL, headers={"User-Agent": "ai-trading-agent/1.0"})
    try:
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    try:
        response = urlopen(request, timeout=30)
    except (ssl.SSLCertVerificationError, URLError) as error:
        if isinstance(error, URLError) and not isinstance(error.reason, ssl.SSLCertVerificationError):
            raise
        # Some Windows/Python installations have an outdated CA bundle. This
        # fallback is limited to the public, non-sensitive constituent page.
        response = urlopen(request, timeout=30, context=ssl._create_unverified_context())
    with response:
        parser = ConstituentsParser()
        parser.feed(response.read().decode("utf-8"))
    symbols = list(dict.fromkeys(parser.rows))
    if len(symbols) < 490:
        raise RuntimeError(f"S&P 500 source returned only {len(symbols)} symbols")
    return symbols

def _clean(symbol: str) -> str:
    return symbol.strip().upper().replace(".", "-")

def fetch_nasdaq100() -> list[str]:
    import json
    request = Request(NASDAQ_URL, headers={
        "User-Agent": "Mozilla/5.0 (compatible; ai-trading-agent/1.0)",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.nasdaq.com",
        "Referer": "https://www.nasdaq.com/",
    })
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    rows = ((payload.get("data") or {}).get("rows") or [])
    symbols = []
    for row in rows:
        if isinstance(row, dict):
            value = row.get("symbol") or row.get("ticker") or row.get("tickerSymbol") or row.get("Symbol")
            if value:
                symbols.append(_clean(str(value)))
    if len(symbols) < 90:
        def walk(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    if str(key).lower() in {"symbol", "ticker", "tickersymbol"} and isinstance(child, str):
                        symbols.append(_clean(child))
                    else:
                        walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)
        walk(payload)
    symbols = [value for value in symbols if value.isascii() and all(char.isalnum() or char == "-" for char in value)]
    if len(symbols) >= 90:
        return list(dict.fromkeys(symbols))
    raise RuntimeError("Nasdaq-100 source did not contain a valid ticker table")

def fetch_russell2000() -> list[str]:
    request = Request(RUSSELL_URL, headers={"User-Agent": "ai-trading-agent/1.0"})
    with urlopen(request, timeout=60) as response:
        raw_text = response.read().decode("utf-8-sig", errors="replace")
    rows = list(csv.DictReader(raw_text.splitlines()))
    ticker_key = next((key for key in (rows[0].keys() if rows else []) if str(key).strip().lower() in {"ticker", "symbol"}), None)
    if ticker_key is None:
        raise RuntimeError("Russell 2000 source did not contain a ticker column")
    symbols = [_clean(str(row.get(ticker_key, ""))) for row in rows]
    symbols = [value for value in symbols if value.isascii() and all(char.isalnum() or char == "-" for char in value)]
    if len(symbols) < 1500:
        raise RuntimeError(f"Russell 2000 source returned only {len(symbols)} symbols")
    return list(dict.fromkeys(symbols))

root = Path(__file__).parents[1]
sp500 = fetch_symbols()
nasdaq100 = fetch_nasdaq100()
russell2000 = fetch_russell2000()
symbols = sorted(set(sp500) | set(nasdaq100) | set(russell2000))
count = replace_symbol_universe(connect(root / "trading.db"), symbols, name="S&P 500 + Nasdaq-100 + Russell 2000")
print(f"cached_market_universe={count} sp500={len(sp500)} nasdaq100={len(nasdaq100)} russell2000={len(russell2000)} overlaps={len(sp500) + len(nasdaq100) + len(russell2000) - len(symbols)}")
