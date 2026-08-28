"""Build a static research library from data/stocks/*.md."""
from __future__ import annotations
import html
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parents[1]
OUT = ROOT / "reports" / "site"
STYLE = "body{font-family:system-ui;max-width:1050px;margin:auto;padding:24px;background:#f5f7fb;color:#172033;line-height:1.55}a{color:#155eef;text-decoration:none}.card,header{background:white;border:1px solid #e1e6ef;border-radius:14px;padding:20px;margin-bottom:16px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}.muted{color:#667085;font-size:.9rem}"

def date_for(path: Path) -> str:
    try:
        value = subprocess.check_output(["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(ROOT))], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
        if value: return value
    except (OSError, subprocess.CalledProcessError): pass
    return datetime.fromtimestamp(path.stat().st_mtime).date().isoformat()

def page(body: str, title: str) -> str:
    return f"<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(title)}</title><style>{STYLE}</style></head><body>{body}</body></html>"

def render_md(text: str) -> str:
    out=[]; listed=False
    for line in text.splitlines():
        if line.startswith("# "): continue
        if line.startswith("## ") or line.startswith("### "):
            if listed: out.append("</ul>"); listed=False
            level=3 if line.startswith("### ") else 2
            out.append(f"<h{level}>{html.escape(line[level+1:])}</h{level}>")
        elif line.startswith("- "):
            if not listed: out.append("<ul>"); listed=True
            out.append(f"<li>{html.escape(line[2:])}</li>")
        elif line.strip():
            if listed: out.append("</ul>"); listed=False
            out.append(f"<p>{html.escape(line)}</p>")
    if listed: out.append("</ul>")
    return "".join(out)

def section_body(text: str, wanted: str) -> str:
    parts = re.split(r"^##\s+(.+)$", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        if parts[i].strip().lower() == wanted.lower():
            return parts[i + 1].strip()
    return ""

def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    records=[]
    for path in (ROOT / "data" / "stocks").glob("*.md"):
        symbol=path.stem.upper(); text=path.read_text(encoding="utf-8"); date=date_for(path)
        records.append((date,symbol,text))
        overview=section_body(text, "Overview")
        conviction=""
        parts=re.split(r"^##\s+(.+)$", text, flags=re.MULTILINE)
        for i in range(1,len(parts),2):
            if "conviction" in parts[i].lower(): conviction=parts[i+1].strip()
        nav=f"<p><a href='index.html'>← All analyses</a> · <a href='{symbol.lower()}-full.html'>Full view</a> · <a href='{symbol.lower()}.html'>Telegram view</a></p>"
        recent=section_body(text, "Recent Developments / News / Earnings / Analyst / SEC / Product Notes")
        short_source=(overview[:650] if overview else text[:650])
        if conviction: short_source += "\n\n## Conviction\n" + conviction[:500]
        if recent:
            bullets=[line for line in recent.splitlines() if line.startswith("- ")][:3]
            if bullets: short_source += "\n\n## Key updates\n" + "\n".join(bullets)
        short=render_md(short_source)
        full=render_md(text)
        (OUT/f"{symbol.lower()}.html").write_text(page(f"<header><h1>{html.escape(symbol)}</h1><p class='muted'>Updated {date}</p>{nav}</header><main><h2>Telegram view</h2>{short}</main>",f"{symbol} · Telegram view"),encoding="utf-8")
        (OUT/f"{symbol.lower()}-full.html").write_text(page(f"<header><h1>{html.escape(symbol)}</h1><p class='muted'>Updated {date}</p>{nav}</header><main><h2>Full analysis</h2>{full}</main>",f"{symbol} · Full analysis"),encoding="utf-8")
    records.sort(reverse=True)
    cards="".join(f"<article class='card'><h2><a href='{s.lower()}.html'>{html.escape(s)}</a></h2><p class='muted'>Updated {d}</p><p><a href='{s.lower()}.html'>Telegram view</a> · <a href='{s.lower()}-full.html'>Full view</a></p></article>" for d,s,_ in records)
    content=f"<header><h1>Market Research Library</h1><p class='muted'>{len(records)} analyses · newest first</p><input id='q' placeholder='Search ticker...' oninput='filter()' style='width:100%;padding:10px'></header><main id='cards' class='grid'>{cards}</main><script>function filter(){{let q=document.getElementById('q').value.toLowerCase();document.querySelectorAll('.card').forEach(x=>x.style.display=x.innerText.toLowerCase().includes(q)?'':'none')}}</script>"
    (OUT/"index.html").write_text(page(content,"Market Research Library"),encoding="utf-8")

if __name__ == "__main__":
    build(); print(f"built {OUT}")
