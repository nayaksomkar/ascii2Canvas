import sys
from pathlib import Path

MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<script src="{cdn}"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: {bg}; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
.mermaid {{ padding: 24px; }}
</style>
</head>
<body>
<div class="mermaid">
{code}
</div>
<script>
mermaid.initialize({{
    theme:"{theme}",
    themeVariables: {{
        background: "{bg}",
        primaryColor: "{bg}",
        primaryTextColor: "#ffffff",
        primaryBorderColor: "#ffffff",
        lineColor: "#ffffff",
        secondaryColor: "{bg}",
        tertiaryColor: "{bg}",
    }}
}});
</script>
</body>
</html>"""


def render_diagram(
    code: str,
    output_path: str | Path,
    theme: dict,
) -> None:
    html = HTML_TEMPLATE.format(
        cdn=MERMAID_CDN,
        bg=theme["bg"],
        code=code.strip(),
        theme=theme["mermaid_theme"],
    )

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html, wait_until="networkidle")
            page.wait_for_selector(".mermaid svg", timeout=15000)
            page.wait_for_timeout(300)
            svg = page.locator(".mermaid svg")
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            svg.screenshot(path=str(output_path))
            browser.close()
    except Exception as e:
        msg = str(e)
        if "Executable doesn't exist" in msg:
            print("Chromium not found. Run: playwright install chromium", file=sys.stderr)
        else:
            print(f"Mermaid rendering failed: {e}", file=sys.stderr)
        sys.exit(1)
