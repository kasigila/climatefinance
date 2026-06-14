#!/usr/bin/env python3
"""Apply sitewide SEO, performance, and polish improvements to HTML pages."""
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://climatefinance.co.tz"
SKIP = {"owl.video.play.html"}


def build_version() -> str:
    env = os.environ.get("BUILD_VERSION", "").strip()
    if env:
        return env[:12]
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            text=True,
        ).strip()[:12]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "dev"


VERSION = build_version()

CUSTOM_CSS_LINKS = [
    "assets/css/enhancements.css",
    "assets/css/footer-modern.css",
    "assets/css/design-system.css",
    "assets/css/home.css",
    "assets/css/contact.css",
    "assets/css/team.css",
    "assets/css/cop.css",
    "assets/css/cookie-consent.css",
]

DEFAULT_DESC = (
    "Africa Climate Finance bridges the climate finance gap in Africa by empowering "
    "vulnerable communities through microfinance, education, and climate-smart initiatives."
)

PAGE_META = {
    "index.html": {
        "title": "Africa Climate Finance - Tanzania",
        "description": DEFAULT_DESC,
        "schema": "Organization",
    },
    "about.php.html": {"title": "About Us | Africa Climate Finance", "description": "Learn how Africa Climate Finance connects grassroots microfinance with institutional climate capital across Tanzania and Africa."},
    "contact.php.html": {"title": "Contact Us | Africa Climate Finance", "description": "Partner with Africa Climate Finance. We respond within 24 hours to project and partnership inquiries."},
    "microfinance.php.html": {"title": "Microfinance for Climate | Africa Climate Finance", "description": "CBT-licensed climate-smart microfinance for cooperatives, SMEs, and vulnerable communities in Tanzania.", "schema": "Service", "service": "Microfinance for Climate"},
    "market-analysis.php.html": {"title": "Market Analysis | Africa Climate Finance", "description": "Demand studies, buyer mapping, and pricing analysis for bankable climate projects.", "schema": "Service", "service": "Market Analysis"},
    "financial-modelling.php.html": {"title": "Financial Modelling | Africa Climate Finance", "description": "Feasibility models, cashflow projections, and investment-ready financial structures.", "schema": "Service", "service": "Financial Modelling"},
    "gender-assessment.php.html": {"title": "Gender Assessment | Africa Climate Finance", "description": "Gender action plans and women-led enterprise assessments for climate finance proposals.", "schema": "Service", "service": "Gender Assessment"},
    "stakeholders-engagement.php.html": {"title": "Stakeholders Engagement | Africa Climate Finance", "description": "Stakeholder mapping, consultation, and FP documentation for climate projects.", "schema": "Service", "service": "Stakeholders Engagement"},
    "scientific-assessment.php.html": {"title": "Scientific Assessment | Africa Climate Finance", "description": "Climate science review, baseline data, and technical validation for proposals.", "schema": "Service", "service": "Scientific Assessment"},
    "climate-risk.php.html": {"title": "Climate Risk | Africa Climate Finance", "description": "Physical and transition risk analysis for portfolios and project pipelines.", "schema": "Service", "service": "Climate Risk Analysis"},
    "kenneth.php.html": {"title": "Kenneth Kasigila | Africa Climate Finance", "description": "Profile of Kenneth Kasigila, Group CEO of Africa Climate Finance and climate finance advisor.", "schema": "Person", "person": "Kenneth Kasigila"},
    "kenneth.html": {"title": "Kenneth Kasigila | Africa Climate Finance", "description": "Profile of Kenneth Kasigila, Group CEO of Africa Climate Finance and climate finance advisor.", "schema": "Person", "person": "Kenneth Kasigila"},
    "cop-engagements.php.html": {"title": "COP Engagements | Africa Climate Finance", "description": "Africa Climate Finance at COP29, COP30, and global climate finance forums."},
    "women-empowerment.php.html": {"title": "Women Empowerment | Africa Climate Finance", "description": "280+ women trained in financial literacy and climate-smart enterprise in Tanzania."},
    "privacy-policy.html": {"title": "Privacy Policy | Africa Climate Finance", "description": "How Africa Climate Finance collects, uses, and protects your personal information."},
    "terms-of-service.html": {"title": "Terms of Service | Africa Climate Finance", "description": "Terms governing use of the Africa Climate Finance website and services."},
    "error-404.html": {"title": "Page Not Found | Africa Climate Finance", "description": "The page you requested could not be found."},
}

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Africa Climate Finance",
    "url": BASE,
    "logo": f"{BASE}/assets/img/logo.png",
    "description": DEFAULT_DESC,
    "email": "info@climatefinance.co.tz",
    "telephone": "+255754763558",
    "address": {"@type": "PostalAddress", "addressLocality": "Rungwe", "addressRegion": "Mbeya", "addressCountry": "TZ"},
    "sameAs": [],
}


def canonical_url(name: str) -> str:
    if name == "index.html":
        return f"{BASE}/"
    return f"{BASE}/{name}"


def page_schema(meta: dict, name: str) -> str | None:
    st = meta.get("schema")
    if st == "Organization":
        return json.dumps(ORG_SCHEMA, ensure_ascii=False)
    if st == "Person":
        person = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": meta.get("person", ""),
            "jobTitle": "Group CEO",
            "worksFor": {"@type": "Organization", "name": "Africa Climate Finance"},
            "url": canonical_url(name),
        }
        return json.dumps(person, ensure_ascii=False)
    if st == "Service":
        service = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": meta.get("service", ""),
            "provider": {"@type": "Organization", "name": "Africa Climate Finance", "url": BASE},
            "areaServed": "Africa",
            "url": canonical_url(name),
        }
        return json.dumps(service, ensure_ascii=False)
    return None


def meta_block(name: str, meta: dict) -> str:
    title = meta.get("title", "Africa Climate Finance")
    desc = meta.get("description", DEFAULT_DESC)
    url = canonical_url(name)
    og_img = f"{BASE}/assets/img/og-image.png"
    lines = [
        f'    <meta name="description" content="{desc}">',
        f'    <link rel="canonical" href="{url}">',
        '    <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">',
        '    <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">',
        '    <link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png">',
        f'    <meta property="og:type" content="website">',
        f'    <meta property="og:site_name" content="Africa Climate Finance">',
        f'    <meta property="og:title" content="{title}">',
        f'    <meta property="og:description" content="{desc}">',
        f'    <meta property="og:image" content="{og_img}">',
        f'    <meta property="og:url" content="{url}">',
        f'    <meta name="twitter:card" content="summary_large_image">',
        f'    <meta name="twitter:title" content="{title}">',
        f'    <meta name="twitter:description" content="{desc}">',
        f'    <meta name="twitter:image" content="{og_img}">',
    ]
    schema = page_schema(meta, name)
    if schema:
        lines.append(f'    <script type="application/ld+json">{schema}</script>')
    return "\n".join(lines)


def remove_httrack(text: str) -> str:
    return re.sub(r"\n<!-- Mirrored from templates\.hibotheme\.com.*?-->\n", "\n", text, flags=re.S)


def fix_lang(text: str) -> str:
    return re.sub(r'<html lang="zxx">', '<html lang="en">', text)


def inject_meta(text: str, name: str) -> str:
    meta = PAGE_META.get(name, {"title": None, "description": DEFAULT_DESC})
    if not meta.get("title"):
        m = re.search(r"<title>([^<]+)</title>", text)
        meta["title"] = m.group(1).strip() if m else "Africa Climate Finance"
    block = meta_block(name, meta)
    text = re.sub(r'\s*<link rel="icon"[^>]+>\s*', "\n", text)
    text = re.sub(r"\s*<meta name=\"description\"[^>]+>\s*", "\n", text)
    text = re.sub(r"\s*<link rel=\"canonical\"[^>]+>\s*", "\n", text)
    text = re.sub(r"\s*<meta property=\"og:[^\"]+\"[^>]+>\s*", "\n", text)
    text = re.sub(r"\s*<meta name=\"twitter:[^\"]+\"[^>]+>\s*", "\n", text)
    text = re.sub(r"\s*<script type=\"application/ld\+json\">.*?</script>\s*", "\n", text, flags=re.S)
    text = re.sub(r"<title>[^<]+</title>", f"<title>{meta['title']}</title>", text, count=1)
    if "<title>" in text:
        text = re.sub(r"(<title>[^<]+</title>)", r"\1\n" + block, text, count=1)
    return text


def add_bundle_css(text: str) -> str:
    href = f"assets/css/acf.bundle.min.css?v={VERSION}"
    if "acf.bundle.min.css" not in text:
        bundle = f'    <link rel="stylesheet" href="{href}">\n'
        text = text.replace("</head>", bundle + "    </head>", 1)
    text = re.sub(
        r'href="assets/css/acf\.bundle\.min\.css(?:\?v=[^"]*)?"',
        f'href="{href}"',
        text,
    )
    for link in CUSTOM_CSS_LINKS:
        text = re.sub(rf'\s*<link rel="stylesheet" href="{re.escape(link)}">\s*\n', "\n", text)
    return text


def use_js_bundle(text: str) -> str:
    href = f"assets/js/acf.bundle.min.js?v={VERSION}"
    text = re.sub(r'\s*<script src="assets/js/contact-form-script\.js"></script>\s*\n', "\n", text)
    text = re.sub(r'\s*<script src="assets/js/main\.js"></script>\s*\n', "\n", text)
    text = re.sub(r'\s*<script src="assets/js/cookie-consent\.js" defer></script>\s*\n', "\n", text)
    if "acf.bundle.min.js" not in text:
        text = re.sub(
            r'(<script src="assets/js/i18n\.js"></script>)',
            rf'\1\n    <script src="{href}" defer></script>',
            text,
            count=1,
        )
    if "acf.bundle.min.js" not in text:
        text = text.replace("</body>", f'    <script src="{href}" defer></script>\n\n</body>', 1)
    text = re.sub(
        r'src="assets/js/acf\.bundle\.min\.js(?:\?v=[^"]*)?"',
        f'src="{href}"',
        text,
    )
    return text


def cleanup_artifacts(text: str) -> str:
    text = re.sub(r"\n?\s*<!-- /GetButton\.io widget -->\s*", "\n", text)
    text = re.sub(r"\n?\s*<!-- GetButton\.io widget -->\s*", "\n", text)
    return text


def fix_void_links(text: str) -> str:
    text = text.replace('href="javascript:void(0)" class="back-to-top', 'href="#top" class="back-to-top')
    text = text.replace('href="javascript:void(0)"><i class="ri-close-line">', 'href="#" role="button" aria-label="Close menu"><i class="ri-close-line">')
    text = text.replace('href="javascript:void(0)"><i class="ri-menu-line">', 'href="#" role="button" aria-label="Open menu"><i class="ri-menu-line">')
    return text


def fix_mixed_content(text: str) -> str:
    return text.replace("http://mbeyaavocados.co.tz/", "https://mbeyaavocados.co.tz/")


def fix_alt_text(text: str) -> str:
    text = text.replace('alt="Image"', 'alt="Section divider graphic"')
    text = text.replace('alt="IMage"', 'alt="Decorative team card shape"')
    text = re.sub(r'alt=""', 'alt="English language flag"', text, count=1)
    return text


def fix_nested_pictures(text: str) -> str:
    return re.sub(
        r'<picture><source srcset="([^"]+\.webp)" type="image/webp"><picture><source srcset="\1" type="image/webp">(<img[^>]+>)</picture></picture>',
        r'<picture><source srcset="\1" type="image/webp">\2</picture>',
        text,
    )


def add_lazy_and_picture(text: str, name: str) -> str:
    text = fix_nested_pictures(text)
    above_fold = {"logo.png", "logo-white.png", "favicon", "hero/", "breadcrumb/"}

    def inside_picture(pos: int) -> bool:
        before = text[:pos]
        return before.rfind("<picture") > before.rfind("</picture>")

    def repl_img(match: re.Match) -> str:
        tag = match.group(0)
        if inside_picture(match.start()) or "<picture" in tag:
            return tag
        src_m = re.search(r'src="([^"]+)"', tag)
        if not src_m:
            return tag
        src = src_m.group(1)
        if any(p in src for p in above_fold):
            if 'loading="lazy"' not in tag:
                return tag
            return re.sub(r'\s*loading="lazy"', "", tag)
        alt_m = re.search(r'alt="([^"]*)"', tag)
        alt = alt_m.group(1) if alt_m else ""
        webp = re.sub(r"\.(png|jpe?g)$", ".webp", src, flags=re.I)
        lazy = "" if 'loading="lazy"' in tag else ' loading="lazy"'
        if not re.search(r"\.(png|jpe?g)$", src, re.I):
            return tag if not lazy else tag.replace("<img ", f"<img{lazy} ")
        inner = f'<img src="{src}" alt="{alt}"{lazy}>'
        return f'<picture><source srcset="{webp}" type="image/webp">{inner}</picture>'

    return re.sub(r"<img[^>]+>", repl_img, text)


def remove_getbutton_inline(text: str) -> str:
    return re.sub(
        r"\n?\s*<!-- GetButton\.io widget -->.*?(?:<!-- /GetButton\.io widget -->|</script>\s*)\n?",
        "\n",
        text,
        flags=re.S,
    )


def ensure_cookie_script(text: str) -> str:
    return text


def add_reveal_classes(text: str, name: str) -> str:
    if name == "index.html":
        replacements = [
            ('class="ds-service-icon-card"', 'class="ds-service-icon-card reveal"'),
            ('class="ds-esg-card"', 'class="ds-esg-card reveal"'),
            ('class="home-section-header"', 'class="home-section-header reveal"'),
            ('class="home-feature-content"', 'class="home-feature-content reveal"'),
            ('class="home-feature-chart"', 'class="home-feature-chart reveal"'),
        ]
        for old, new in replacements:
            if new not in text:
                text = text.replace(old, new)
    if name in ("team.php.html", "team.html"):
        text = text.replace('class="acf-team-card"', 'class="acf-team-card reveal"')
    return text


def enhance_404_content(text: str, name: str) -> str:
    if name not in ("error-404.html", "404.html"):
        return text
    needle = "doesn&apos;t exist or has been moved."
    links = '<p class="mt-3"><a href="about.php.html">About Us</a> · <a href="market-analysis.php.html">Our Services</a> · <a href="contact.php.html">Contact</a> · <a href="cop-engagements.php.html">COP Engagements</a></p>'
    if links not in text and needle in text:
        text = text.replace(
            f"<p>{needle}</p>",
            f"<p>{needle}</p>\n                            {links}",
        )
    return text


def fix_stat_counters(text: str, name: str) -> str:
    return text


def add_top_anchor(text: str) -> str:
    if 'id="top"' in text:
        return text
    return text.replace("<body", '<body id="top"', 1)


def process_file(path: Path) -> None:
    name = path.name
    text = path.read_text(encoding="utf-8", errors="replace")
    text = remove_httrack(text)
    text = fix_lang(text)
    text = inject_meta(text, name)
    text = add_bundle_css(text)
    text = use_js_bundle(text)
    text = cleanup_artifacts(text)
    text = fix_void_links(text)
    text = fix_mixed_content(text)
    text = fix_alt_text(text)
    text = add_lazy_and_picture(text, name)
    text = remove_getbutton_inline(text)
    text = ensure_cookie_script(text)
    text = add_reveal_classes(text, name)
    text = enhance_404_content(text, name)
    text = fix_stat_counters(text, name)
    text = add_top_anchor(text)
    path.write_text(text, encoding="utf-8")
    print(f"  updated {name}")


def process_partials() -> None:
    for rel in ("inc/header.html", "inc/footer.html", "inc/service-cta.html", "inc/service-related.html"):
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        text = fix_void_links(text)
        text = fix_mixed_content(text)
        text = fix_alt_text(text)
        p.write_text(text, encoding="utf-8")
        print(f"  updated {rel}")


def main():
    print("Applying HTML improvements...")
    for path in sorted(ROOT.glob("*.html")):
        if path.name in SKIP:
            continue
        process_file(path)
    process_partials()
    # GitHub Pages 404
    err = ROOT / "error-404.html"
    if err.exists():
        process_file(err)
        (ROOT / "404.html").write_text(err.read_text(encoding="utf-8"), encoding="utf-8")
        print("  wrote 404.html")


if __name__ == "__main__":
    main()
