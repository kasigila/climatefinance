# Africa Climate Finance - Tanzania

Static website for **Africa Climate Finance**, providing climate finance advisory and project development services in Tanzania and across Africa.

🌐 **Live site:** [climatefinance.co.tz](https://climatefinance.co.tz)

---

## About

Africa Climate Finance offers expertise in developing and managing projects and programmes that advance Climate Action (SDG 13) while delivering socio-economic benefits. Services include market analysis, financial modelling, gender assessment, stakeholder engagement, scientific assessment, climate risk analysis, and microfinance.

---

## Services

| Service | Description |
|---------|-------------|
| **Market Analysis** | Market studies to establish demand for specific projects and programmes |
| **Financial Modelling** | Financial analysis for financing needs and project viability |
| **Microfinance** | Inclusive finance for climate-resilient communities, smallholder farmers, and women-led enterprises |
| **Gender Assessment** | Stakeholder engagement for GCF Concept Notes, PPFs, and Funding Proposals |
| **Stakeholders Engagement** | Mapping, analysis, and engagement with communities, civil society, and private sector |
| **Scientific Assessment** | Climate data and science for climate impacts and societal benefits |
| **Climate Risk** | Identification, quantification, and mitigation of climate risks in financial products |

---

## Project Structure

```
climatefinance/
├── climatefinance.co.tz/     # Site root (served by GitHub Pages)
│   ├── index.html
│   ├── about.php.html
│   ├── contact.php.html
│   ├── microfinance.php.html
│   ├── financial-modelling.php.html
│   ├── market-analysis.php.html
│   ├── gender-assessment.php.html
│   ├── stakeholders-engagement.php.html
│   ├── scientific-assessment.php.html
│   ├── climate-risk.php.html
│   └── assets/
│       ├── css/
│       ├── js/
│       └── img/
├── .github/workflows/
│   └── deploy-pages.yml      # GitHub Pages deployment
└── README.md
```

---

## Local Development

Serve the site locally:

```bash
cd climatefinance.co.tz
python3 -m http.server 8000
# or: npx serve .
```

Open [http://localhost:8000](http://localhost:8000)

---

## Deployment (GitHub Pages)

1. Go to **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. Push to `main` — the workflow deploys automatically

**GitHub Pages URL:** `https://kasigila.github.io/climatefinance/`

---

## Contact

- **Location:** Masaki, Dar es Salaam. P.O. Box 6756
- **Phone:** +255 (0) 754 763 558
- **Email:** info@climatefinance.co.tz

---

*Powered by [Karen Marie Kasigila](https://kasigila.github.io)*
