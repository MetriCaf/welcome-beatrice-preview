from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: python configure_base_url.py https://example.com/welcome-beatrice")

base = sys.argv[1].rstrip("/")
for filename in ("index-square.html", "index-wide.html", "preview-only-square.html", "preview-only-wide.html"):
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    text = text.replace("__PUBLIC_BASE_URL__", base)
    path.write_text(text, encoding="utf-8")
    print(f"Configured {path} for {base}")
