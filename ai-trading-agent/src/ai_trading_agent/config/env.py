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
    return {key: os.getenv(key, value) for key, value in values.items()}

