# ASCII 2 Canvas

Convert text-based diagrams into polished PNG images using Mermaid JS.

```
Mermaid .txt ──► config.json ──► main.py ──► PNG
```

## Installation

```bash
pip install -r requirements.txt
playwright install chromium
```

## Usage

1. Write diagrams in Mermaid syntax inside `.txt` files under `examples/`
2. List them in `config.json`
3. Run:

```bash
python main.py
```

Output PNGs appear in `outputs/` with matching filenames.

## Config

```json
{
  "theme": "dark",
  "input_dir": "examples",
  "output_dir": "outputs",
  "files": [
    "pipeline.txt",
    "architecture.txt",
    "rag_flow.txt"
  ]
}
```

## Example

| Input | Output |
|-------|--------|
| `pipeline.txt` | `outputs/pipeline.png` |
| `architecture.txt` | `outputs/architecture.png` |
| `rag_flow.txt` | `outputs/rag_flow.png` |

## Features

- Renders with Mermaid JS (flowcharts, sequence diagrams, etc.)
- Dark & light themes
- Clean PNG output
- Auto-sized canvas

## Project Structure

```
├── config.json
├── main.py
├── requirements.txt
├── examples/
│   ├── pipeline.txt
│   ├── architecture.txt
│   └── rag_flow.txt
├── outputs/
└── src/
    ├── config_loader.py
    ├── parser.py
    ├── renderer.py
    └── themes.py
```

## Requirements

- Python 3.10+
- Playwright + Chromium
