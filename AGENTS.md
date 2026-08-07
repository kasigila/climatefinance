# AGENTS.md

## Cursor Cloud specific instructions

This is a **static HTML/CSS/JS website** (no build system, no package manager, no dependencies to install).

### Running the dev server

```bash
python3 -m http.server 8000
```

Open http://localhost:8000 to view the site.

### Key facts

- No `package.json`, no `node_modules`, no lockfiles — all CSS/JS libraries are vendored in `assets/`.
- No linting tools or test frameworks are configured.
- No build step is needed; the site is served directly from the repo root.
- The GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) copies files into `_site/` for deployment to GitHub Pages — this does not need to run locally.
- The contact form submits to a Google Apps Script endpoint (see `google-apps-script/README.md`). This is an external service and cannot be tested locally without the deployed Google endpoint.
- The i18n system (`assets/js/i18n.js`) uses `data-i18n` HTML attributes and supports English/Swahili via a language dropdown in the header. See `I18N-README.md` for details.
- HTML pages with `.php.html` extension are the "live" pages copied to `_site/` by CI; plain `.html` versions are legacy/alternative copies.
