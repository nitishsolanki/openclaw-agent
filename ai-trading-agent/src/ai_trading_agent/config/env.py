from pathlib import Path
import os

def load_env(path: str | Path = "local.env") -> dict[str, str]:
    values: dict[str, str] = {}
    file = Path(path)
    if file.exists():
        for line in file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                values[key.strip()] = value.strip().strip('"').strip("'")
    # Support both local.env development and GitHub Actions/CI environment variables.
    known_keys = {"ALPACA_API_KEY", "ALPACA_SECRET_KEY", "FINNHUB_API_KEY",
                  "POLYGON_API_KEY", "TELEGRAM_BOT_TOKEN", "DATABASE_URL", "EXECUTION_MODE",
                  "OPENAI_API_KEY", "OPENAI_MODEL"}
    keys = values.keys() | known_keys
    return {key: os.getenv(key, values.get(key, "")) for key in keys if os.getenv(key, values.get(key, ""))}
