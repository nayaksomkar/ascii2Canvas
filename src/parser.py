from pathlib import Path


def parse_diagram(filepath: str | Path) -> str:
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(path, encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        raise ValueError(f"Empty diagram: {filepath}")

    return content
