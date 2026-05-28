#!/usr/bin/env python3
"""Apply sitewide redesign patches to HTML pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ACTIVE_MAP = {
    "index.html": "home",
    "about.php.html": "about",
    "team.php.html": "team",
    "team.html": "team",
    "climate-policy-insights.php.html": "climate-policy",
    "climate-policy-insights.html": "climate-policy",
    "cop-engagements.php.html": "cop",
    "cop-engagements.html": "cop",
    "testimonials.php.html": "beneficiaries",
    "testimonials.html": "beneficiaries",
    "women-empowerment.php.html": "women-empowerment",
    "loan-program.php.html": "loan-program",
    "contact.php.html": "contact",
    "contact.html": "contact",
    "donation.html": "donate",
    "faq.html": "faq",
    "kenneth.php.html": "team",
    "kenneth.html": "team",
    "karen.php.html": "team",
    "karen.html": "team",
    "market-analysis.php.html": "market-analysis",
    "financial-modelling.php.html": "financial-modelling",
    "microfinance.php.html": "microfinance",
    "gender-assessment.php.html": "gender-assessment",
    "stakeholders-engagement.php.html": "stakeholders-engagement",
    "scientific-assessment.php.html": "scientific-assessment",
    "climate-risk.php.html": "climate-risk",
    "privacy-policy.html": "about",
    "terms-of-service.html": "about",
    "thank-you.html": "contact",
    "error-404.html": "home",
}

FONTS_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
)

HEADER_PATTERN = re.compile(
    r"<!-- Header Section Start -->.*?<!-- Header Section End -->",
    re.DOTALL,
)

PRELOADER_PATTERN = re.compile(
    r"<!--Preloader starts-->.*?<!--Preloader ends-->\s*",
    re.DOTALL,
)

THEME_PATTERN = re.compile(
    r"<!-- Theme Switcher Start -->.*?<!-- Theme Switcher End -->\s*",
    re.DOTALL,
)


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    active = ACTIVE_MAP.get(path.name, "home")

    text = PRELOADER_PATTERN.sub("", text)
    text = THEME_PATTERN.sub("", text)

    replacement = (
        f'<!-- Header Section Start -->\n'
        f'<div id="header-placeholder" data-active="{active}"></div>\n'
        f'<script src="assets/js/header-loader.js"></script>\n'
        f'<!-- Header Section End -->'
    )
    text = HEADER_PATTERN.sub(replacement, text)

    if FONTS_LINK not in text:
        text = text.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n\n    ' + FONTS_LINK,
            1,
        )

    if "design-system.css" not in text and path.name != "index.html":
        text = text.replace(
            'href="assets/css/enhancements.css">',
            'href="assets/css/enhancements.css">\n\n    <link rel="stylesheet" href="assets/css/design-system.css">',
            1,
        )

    if path != ROOT / "index.html" and 'class="home-page"' not in text:
        if 'body class="' in text:
            pass
        elif "<body>" in text:
            text = text.replace("<body>", '<body class="ds-page">', 1)
        elif '<body class="ds-header-compact' in text:
            pass

    if original != text:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    count = 0
    for path in sorted(ROOT.glob("*.html")):
        if patch_file(path):
            count += 1
            print(f"Patched {path.name}")
    print(f"Done. {count} files updated.")


if __name__ == "__main__":
    main()
