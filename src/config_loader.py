import json
from pathlib import Path


def load_config(path: str = "config.json") -> dict:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {path}")

    try:
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

    required = {"theme", "input_dir", "output_dir", "files"}
    missing = required - set(config)
    if missing:
        raise ValueError(f"Missing keys: {', '.join(sorted(missing))}")

    if config["theme"] not in ("dark", "light"):
        raise ValueError(f"Unknown theme '{config['theme']}'. Use 'dark' or 'light'.")

    if not isinstance(config["files"], list) or not config["files"]:
        raise ValueError("'files' must be a non-empty list of filenames")

    return config
