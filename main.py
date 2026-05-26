import sys
from pathlib import Path
from src.config_loader import load_config
from src.parser import parse_diagram
from src.renderer import render_diagram
from src.themes import THEMES


def main():
    try:
        config = load_config("config.json")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    theme = THEMES[config["theme"]]
    input_dir = Path(config["input_dir"])
    output_dir = Path(config["output_dir"])

    for filename in config["files"]:
        input_path = input_dir / filename
        output_name = Path(filename).with_suffix(".png")
        output_path = output_dir / output_name

        try:
            diagram = parse_diagram(input_path)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            continue

        try:
            render_diagram(diagram, output_path, theme)
            print(f"\u2713 {filename} \u2192 {output_path}")
        except Exception as e:
            print(f"Error rendering {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
