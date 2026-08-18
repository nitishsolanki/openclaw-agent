import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import yaml

from ..journal.database import connect

def refresh_theme(root: str | Path, sector_ranks) -> dict:
    root = Path(root)
    config = yaml.safe_load((root / "config" / "themes.yaml").read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    ranked = [item for item in sector_ranks if item.score >= 60][:3]
    if not ranked:
        db = connect(root / "trading.db")
        previous = db.execute("SELECT name,sectors,industries,score FROM themes ORDER BY id DESC LIMIT 1").fetchone()
        if previous:
            return {"name": previous[0], "sectors": json.loads(previous[1]), "industries": json.loads(previous[2]), "score": previous[3], "source": "previous"}
        ranked = sector_ranks[:1]
    sectors = [item.sector for item in ranked]
    names = [config.get("sector_themes", {}).get(sector, {}).get("name", sector.lower()) for sector in sectors]
    industries = [industry for sector in sectors for industry in config.get("sector_themes", {}).get(sector, {}).get("industries", [])]
    theme = {"name": "+".join(names), "sectors": sectors, "industries": industries,
             "score": round(sum(item.score for item in ranked) / len(ranked), 2), "source": "sector_rotation"}
    expires = now + timedelta(days=7)
    db = connect(root / "trading.db")
    db.execute("INSERT INTO themes(name,sectors,industries,source,score,expires_at) VALUES (?,?,?,?,?,?)",
               (theme["name"], json.dumps(sectors), json.dumps(industries), theme["source"], theme["score"], expires.isoformat()))
    db.commit()
    return theme

def active_theme(root: str | Path) -> dict | None:
    db = connect(Path(root) / "trading.db")
    row = db.execute("SELECT name,sectors,industries,source,score,expires_at FROM themes ORDER BY id DESC LIMIT 1").fetchone()
    if not row:
        return None
    return {"name": row[0], "sectors": json.loads(row[1]), "industries": json.loads(row[2]),
            "source": row[3], "score": row[4], "expires_at": row[5]}

