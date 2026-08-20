"""Replace the local scan universe with the current S&P 500 constituents."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from ai_trading_agent.data.universe import replace_symbol_universe
from ai_trading_agent.journal.database import connect

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

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
    with urlopen(request, timeout=30) as response:
        parser = ConstituentsParser()
        parser.feed(response.read().decode("utf-8"))
    symbols = list(dict.fromkeys(parser.rows))
    if len(symbols) < 490:
        raise RuntimeError(f"S&P 500 source returned only {len(symbols)} symbols")
    return symbols

root = Path(__file__).parents[1]
symbols = fetch_symbols()
count = replace_symbol_universe(connect(root / "trading.db"), symbols)
print(f"cached_sp500_assets={count}")
