#!/usr/bin/env python3
"""Generate sitemap.xml for all public HTML pages."""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://climatefinance.co.tz"
SKIP = {"owl.video.play.html", "error-404.html"}
PREFERRED = {
    "index.html": "",
    "about.php.html": "about.php.html",
}

def page_url(name: str) -> str:
    if name == "index.html":
        return f"{BASE}/"
    return f"{BASE}/{name}"

def main():
    pages = sorted(
        p.name for p in ROOT.glob("*.html")
        if p.name not in SKIP and not p.name.startswith("_")
    )
    today = date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for name in pages:
        path = ROOT / name
        lastmod = date.fromtimestamp(path.stat().st_mtime).isoformat()
        priority = "1.0" if name == "index.html" else "0.8"
        changefreq = "weekly" if name == "index.html" else "monthly"
        lines.extend([
            "  <url>",
            f"    <loc>{page_url(name)}</loc>",
            f"    <lastmod>{lastmod}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ])
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote sitemap.xml ({len(pages)} URLs)")

if __name__ == "__main__":
    main()
