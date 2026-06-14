#!/usr/bin/env python3
"""Slim About page and update key content pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ABOUT_NEW = '''
                <!-- Who We Are -->
                <section class="about-wrap style1 ptb-100 ds-section">
                    <div class="container ds-container">
                        <div class="ds-section-header">
                            <span class="ds-eyebrow">Who We Are</span>
                            <h2 class="ds-h2">Bridging Climate Finance in Africa</h2>
                            <p class="ds-subtitle">Africa Climate Finance connects village-level microfinance with institutional climate capital, from Rungwe cooperatives to major funding proposals.</p>
                        </div>
                        <div class="ds-two-col">
                            <div class="ds-media-card"><img src="assets/img/abouut.png" alt="Africa Climate Finance community work"></div>
                            <div>
                                <p class="ds-body ds-mb">We fill the gap of climate finance in Africa via microfinance for private and vulnerable communities while preparing bankable projects for climate action funders.</p>
                                <p class="ds-body ds-mb-0">Our work spans financial literacy training, climate-smart lending, market analysis, and project preparation, keeping 1.5°C alive through both grassroots action and institutional partnerships.</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Our Model -->
                <section class="about-wrap style1 ptb-100 bg-sand ds-section ds-section-alt">
                    <div class="container ds-container">
                        <div class="ds-section-header">
                            <span class="ds-eyebrow">Our Model</span>
                            <h2 class="ds-h2">From Community to Climate Funds</h2>
                        </div>
                        <div class="ds-model-flow ds-mb-lg">
                            <span class="ds-model-step">Community Education</span>
                            <span class="ds-model-arrow">→</span>
                            <span class="ds-model-step">Microfinance</span>
                            <span class="ds-model-arrow">→</span>
                            <span class="ds-model-step">Project Preparation</span>
                            <span class="ds-model-arrow">→</span>
                            <span class="ds-model-step">Climate Funds</span>
                        </div>
                        <div class="row gx-5">
                            <div class="col-lg-6">
                                <h3 class="ds-h3 green-dark">Our Mission</h3>
                                <p class="ds-body">We fill the gap of climate finance in Africa via microfinance for vulnerable communities aligned with low-carbon, climate-resilient pathways and SDG 13.</p>
                            </div>
                            <div class="col-lg-6">
                                <h3 class="ds-h3 green-dark">Our Pathway</h3>
                                <p class="ds-body">We establish the Climate-Smart Microfinance Initiative in Tanzania, using Central Bank licensing to de-risk and scale climate investment, then replicate proven models across Africa.</p>
                                <a href="microfinance.php.html" class="btn style2 mt-2">Explore Microfinance for Climate</a>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Leadership Spotlight -->
                <section class="about-wrap style1 ptb-100 ds-section">
                    <div class="container ds-container">
                        <div class="ds-section-header">
                            <span class="ds-eyebrow">Leadership</span>
                            <h2 class="ds-h2">Kenneth Davis Kasigila</h2>
                            <p class="ds-subtitle">Group CEO &amp; Founder, climate finance strategist and grassroots advocate</p>
                        </div>
                        <div class="ds-leadership">
                            <div class="ds-leadership-photo">
                                <a href="kenneth.php.html"><img src="assets/img/team/kenneth.png" alt="Kenneth Davis Kasigila"></a>
                            </div>
                            <div>
                                <p class="ds-body">Kenneth leads Africa Climate Finance with 25+ years in banking and deep expertise in climate project preparation. He led a US$200M commercial bank climate funding proposal and serves on Tanzania&apos;s National BIOFIN Technical Committee.</p>
                                <div class="ds-credential-pills">
                                    <span class="ds-credential-pill">Climate Finance, CRDB Bank</span>
                                    <span class="ds-credential-pill">US$200M+ Climate Proposals</span>
                                    <span class="ds-credential-pill">BIOFIN National Committee, UNDP</span>
                                    <span class="ds-credential-pill">COP29 &amp; COP30 Panelist</span>
                                </div>
                                <a href="kenneth.php.html" class="btn style2 mt-3">Read Full Bio</a>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Explore Impact -->
                <section class="about-wrap style1 ptb-100 bg-sand ds-section ds-section-alt">
                    <div class="container ds-container">
                        <div class="ds-section-header">
                            <span class="ds-eyebrow">Explore Impact</span>
                            <h2 class="ds-h2">See Our Work in the Field</h2>
                        </div>
                        <div class="ds-card-grid">
                            <div class="ds-card">
                                <div class="ds-card-icon"><i class="ri-heart-line"></i></div>
                                <h3 class="ds-card-title"><a href="testimonials.php.html">Our Beneficiaries</a></h3>
                                <p class="ds-card-desc">Ginger farmers, spice entrepreneurs, and community nutrition programmes with real stories from Tukuyu to Iringa.</p>
                                <a href="testimonials.php.html" class="link">Read stories →</a>
                            </div>
                            <div class="ds-card">
                                <div class="ds-card-icon"><i class="ri-women-line"></i></div>
                                <h3 class="ds-card-title"><a href="women-empowerment.php.html">Women Empowerment</a></h3>
                                <p class="ds-card-desc">280+ women trained in financial literacy and climate-smart practices in January 2026, Isajilo Ward.</p>
                                <a href="women-empowerment.php.html" class="link">View programme →</a>
                            </div>
                            <div class="ds-card">
                                <div class="ds-card-icon"><i class="ri-exchange-funds-line"></i></div>
                                <h3 class="ds-card-title"><a href="loan-program.php.html">Loan Program</a></h3>
                                <p class="ds-card-desc">Education → financing → production. A structured pathway from literacy to climate-resilient livelihoods.</p>
                                <a href="loan-program.php.html" class="link">See the process →</a>
                            </div>
                            <div class="ds-card">
                                <div class="ds-card-icon"><i class="ri-global-line"></i></div>
                                <h3 class="ds-card-title"><a href="cop-engagements.php.html">COP Engagements</a></h3>
                                <p class="ds-card-desc">COP29 Baku, COP30 Belém, GCA panels, and global climate finance forums.</p>
                                <a href="cop-engagements.php.html" class="link">View engagements →</a>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- CTA -->
                <section class="about-wrap style1 ptb-60 ds-section ds-section-compact">
                    <div class="container ds-container text-center">
                        <h3 class="ds-h3 green-dark ds-mb">Ready to partner?</h3>
                        <p class="ds-subtitle mx-auto ds-mb">Whether you are a community group, project developer, or institutional partner, we would like to hear from you.</p>
                        <div class="d-flex gap-3 justify-content-center flex-wrap">
                            <a href="contact.php.html" class="btn style1 rounded-pill px-4">Partner With Us</a>
                            <a href="testimonials.php.html" class="btn style2 rounded-pill px-4">Explore Our Impact</a>
                        </div>
                    </div>
                </section>
'''

def slim_about():
    path = ROOT / "about.php.html"
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"<!-- Climate Challenge Section Start -->.*?<!-- Team Section Start -->",
        re.DOTALL,
    )
    replacement = ABOUT_NEW.strip() + "\n\n                <!-- Team Section Start -->"
    text = pattern.sub(replacement, text, count=1)
    path.write_text(text, encoding="utf-8")
    print("Slimmed about.php.html")


SERVICES = {
    "market-analysis.php.html": {
        "title": "Market Analysis",
        "minimal": True,
        "deliverables": [
            "40-page market demand report with buyer mapping and pricing analysis",
            "Competitive landscape and go-to-market recommendations",
            "Demand validation for climate project concept notes and funding proposals",
        ],
        "form_subject": "Market Analysis inquiry",
        "cta": "Request a Market Analysis",
    },
    "financial-modelling.php.html": {
        "title": "Financial Modelling",
        "minimal": True,
        "deliverables": [
            "Integrated financial models with cashflow, sensitivity, and scenario analysis",
            "Investment-ready cost-benefit and feasibility structures",
            "Blended finance and de-risking instrument modelling",
        ],
        "form_subject": "Financial Modelling inquiry",
        "cta": "Request Financial Modelling",
    },
    "microfinance.php.html": {
        "title": "Microfinance for Climate",
        "deliverables": [
            "Climate-smart loan products for cooperatives and SMEs",
            "Financial literacy training before disbursement",
            "Portfolio monitoring for climate-resilient outcomes",
        ],
        "case_title": "Ginger farmers in Isajilo, Tukuyu",
        "case_text": "Microfinance enabling organic ginger farming with drought-resilient practices and export premiums.",
        "case_link": "testimonials.php.html#ginger-story",
        "form_subject": "Microfinance inquiry",
        "cta": "Discuss Microfinance Options",
    },
    "gender-assessment.php.html": {
        "title": "Gender Assessment",
        "deliverables": [
            "Gender action plans and assessments for climate finance proposals",
            "Stakeholder consultations with women-led groups",
            "Gender-responsive indicators and monitoring frameworks",
        ],
        "case_title": "280+ women empowerment programme",
        "case_text": "Grassroots gender-smart finance training across four villages in Isajilo Ward.",
        "case_link": "women-empowerment.php.html",
        "form_subject": "Gender Assessment inquiry",
        "cta": "Request a Gender Assessment",
    },
    "stakeholders-engagement.php.html": {
        "title": "Stakeholders Engagement",
        "deliverables": [
            "Stakeholder mapping and engagement plans for climate projects",
            "Consultation surveys and FP stakeholder documentation",
            "Free, prior, and informed consent processes where required",
        ],
        "case_title": "COP29 Tanzania Pavilion: Finance Day",
        "case_text": "Stakeholder coordination for NDC financing discussions with finance ministers and development banks.",
        "case_link": "cop-engagements.php.html#cop29",
        "form_subject": "Stakeholders Engagement inquiry",
        "cta": "Plan Stakeholder Engagement",
    },
    "scientific-assessment.php.html": {
        "title": "Scientific Assessment",
        "deliverables": [
            "Climate impact assessments grounded in IPCC-aligned data",
            "GHG baseline and mitigation potential calculations",
            "Adaptation benefit quantification for funding proposals",
        ],
        "case_title": "Climate-smart agriculture - Southern Highlands",
        "case_text": "Scientific grounding for regenerative agriculture programmes financed through our microfinance portfolio.",
        "case_link": "testimonials.php.html#ginger-story",
        "form_subject": "Scientific Assessment inquiry",
        "cta": "Request Scientific Assessment",
    },
    "climate-risk.php.html": {
        "title": "Climate Risk Assessment",
        "deliverables": [
            "Physical and transition risk identification and quantification",
            "Climate risk integration into financial products and operations",
            "Risk mitigation recommendations for portfolios and projects",
        ],
        "case_title": "Project risk frameworks",
        "case_text": "Climate risk assessment supporting FP179 and FP223 climate finance proposals.",
        "case_link": "cop-engagements.php.html#cop29",
        "form_subject": "Climate Risk inquiry",
        "cta": "Request Climate Risk Assessment",
    },
}


def update_service_page(filename, cfg):
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")
    deliverables_html = "".join(f"<li>{d}</li>" for d in cfg["deliverables"])
    if cfg.get("minimal"):
        new_desc = f'''
                                    <h1>{cfg["title"]}</h1>
                                    <h3 class="green-dark mt-4">What You Get</h3>
                                    <ul class="ds-deliverables">{deliverables_html}</ul>
'''
    else:
        new_desc = f'''
                                    <h1>{cfg["title"]}</h1>
                                    <h3 class="green-dark mt-4">What You Get</h3>
                                    <ul class="ds-deliverables">{deliverables_html}</ul>
                                    <h3 class="green-dark mt-4">Why It Matters</h3>
                                    <p>Climate projects fail without credible market data, robust financial structures, and stakeholder alignment. Our {cfg["title"].lower()} service delivers the specific outputs funders and investors require, not abstract recommendations.</p>
                                    <div class="ds-case-study">
                                        <h4><i class="ri-award-line"></i> {cfg["case_title"]}</h4>
                                        <p class="mb-2">{cfg["case_text"]}</p>
                                        <a href="{cfg["case_link"]}">View case study →</a>
                                    </div>
                                    <p class="mt-4 mb-0"><a href="faq.html#how-we-work">How we work with Concept Notes and Funding Proposals →</a></p>
'''
    text = re.sub(
        r"<div class=\"project-desc\">.*?</div>\s*</div>\s*\n\s*</div>",
        f'<div class="project-desc ds-service-page">{new_desc.strip()}\n                                </div>\n                            </div>\n                        </div>',
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace("Give Us A Message", cfg["cta"])
    text = text.replace(
        f'value="Message from {cfg["title"]} page"',
        f'value="{cfg["form_subject"]}"',
    )
    if "design-system.css" not in text:
        text = text.replace(
            'href="assets/css/footer-modern.css">',
            'href="assets/css/footer-modern.css">\n    <link rel="stylesheet" href="assets/css/design-system.css">',
        )
    path.write_text(text, encoding="utf-8")
    print(f"Updated {filename}")


if __name__ == "__main__":
    slim_about()
    for fname, cfg in SERVICES.items():
        update_service_page(fname, cfg)
