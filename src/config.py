import json
from pathlib import Path

def load_config():
    config_path = Path("config.json")
    if not config_path.exists():
        return {}

    with open(config_path, "r") as f:
        return json.load(f)
