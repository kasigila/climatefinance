#!/usr/bin/env bash
# Build step: WebP conversion, asset minification, sitemap, favicon/OG assets
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

BUILD_VERSION="${BUILD_VERSION:-$(git rev-parse --short HEAD 2>/dev/null || date +%Y%m%d%H%M)}"
export BUILD_VERSION
echo "$BUILD_VERSION" > assets/build-version.txt
echo "==> Build version: $BUILD_VERSION"

echo "==> Converting images to WebP"
find assets/img -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) ! -name 'favicon*' ! -name 'logo*' ! -name 'apple-touch*' ! -name 'og-image*' | while read -r img; do
  out="${img%.*}.webp"
  if [[ ! -f "$out" ]] || [[ "$img" -nt "$out" ]]; then
    cwebp -q 82 "$img" -o "$out" 2>/dev/null || true
  fi
done

echo "==> Optimizing favicon PNG"
if [[ -f assets/img/favicon-f.png ]]; then
  cwebp -q 90 assets/img/favicon-f.png -o assets/img/favicon.webp 2>/dev/null || true
  sips -Z 32 assets/img/favicon-f.png --out assets/img/favicon-32.png >/dev/null 2>&1 || cp assets/img/favicon-f.png assets/img/favicon-32.png
  sips -Z 180 assets/img/logo.png --out assets/img/apple-touch-icon.png >/dev/null 2>&1 || cp assets/img/logo.png assets/img/apple-touch-icon.png
fi

echo "==> Generating OG image PNG"
if command -v rsvg-convert >/dev/null 2>&1; then
  rsvg-convert -w 1200 -h 630 assets/img/og-image.svg -o assets/img/og-image.png 2>/dev/null || true
fi
if [[ ! -f assets/img/og-image.png ]]; then
  if [[ -f assets/img/green.jpg ]]; then
    sips -z 630 1200 assets/img/green.jpg --out assets/img/og-image.png >/dev/null 2>&1 || cp assets/img/green.jpg assets/img/og-image.png
  else
    cp assets/img/logo.png assets/img/og-image.png
  fi
fi
if [[ -f assets/img/og-image.png ]]; then
  cwebp -q 85 assets/img/og-image.png -o assets/img/og-image.webp 2>/dev/null || true
fi

echo "==> Minifying custom CSS"
{
  cat assets/css/mobile.css
  cat assets/css/design-system.css
  sed '/@import url/d' assets/css/enhancements.css
  cat assets/css/footer-modern.css assets/css/home.css assets/css/contact.css assets/css/team.css assets/css/cop.css assets/css/cookie-consent.css
} | npx --yes clean-css-cli -o assets/css/acf.bundle.min.css 2>/dev/null || {
  cat assets/css/mobile.css assets/css/design-system.css assets/css/enhancements.css assets/css/footer-modern.css assets/css/home.css assets/css/contact.css assets/css/team.css assets/css/cop.css assets/css/cookie-consent.css > assets/css/acf.bundle.min.css
}

echo "==> Minifying custom JS"
cat assets/js/cookie-consent.js assets/js/contact-form-script.js assets/js/main.js 2>/dev/null | npx --yes terser --compress --mangle -o assets/js/acf.bundle.min.js 2>/dev/null || cp assets/js/main.js assets/js/acf.bundle.min.js

echo "==> Generating sitemap.xml"
python3 scripts/generate-sitemap.py

echo "==> Applying HTML improvements"
python3 scripts/apply-site-improvements.py

echo "==> Build complete"
