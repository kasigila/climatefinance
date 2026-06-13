#!/usr/bin/env python3
"""Update team, beneficiaries, insights, contact, FAQ, COP pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def patch_team():
    path = ROOT / "team.php.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        '<p data-i18n="team.leadershipDesc">Executive leadership, financial inclusion, and technical implementation across Africa.</p>',
        '<p data-i18n="team.leadershipDesc">Executive leadership, financial inclusion, and technical implementation across Africa.</p>\n                            <p data-i18n="team.intro">Our team combines 25+ years of banking, data science, and grassroots finance to deliver climate solutions from village level to global policy forums.</p>',
    )
    text = re.sub(
        r'\s*<div class="team-field-coming">.*?</div>\s*',
        '\n',
        text,
        flags=re.DOTALL,
    )
    text = text.replace(
        '''<article class="team-card-modern">
                                <div class="team-card-media">
                                    <img src="assets/img/team/happy.png" alt="Happy Kasigila">
                                </div>
                                <div class="team-card-body">
                                    <h3>Happy Kasigila</h3>
                                    <span class="team-role">Manager</span>
                                    <p class="team-excerpt">Bridge between executive strategy and daily execution. Integrates Data Science insights into operations, maintains institutional compliance, and manages human capital for the group&apos;s green targets.</p>
                                </div>
                            </article>''',
        '''<article class="team-card-modern">
                                <div class="team-card-media">
                                    <img src="assets/img/team/happy.png" alt="Happy Kasigila">
                                </div>
                                <div class="team-card-body">
                                    <h3>Happy Kasigila</h3>
                                    <span class="team-role">Manager</span>
                                    <p class="team-excerpt">Bridge between executive strategy and daily execution. Integrates Data Science insights into operations, maintains institutional compliance, and manages human capital for the group&apos;s green targets.</p>
                                    <div class="team-card-actions">
                                        <ul class="social-profile style1 list-style">
                                            <li><a href="mailto:happy.kasigila@climatefinance.co.tz" aria-label="Email Happy"><i class="ri-mail-line"></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </article>''',
    )
    text = text.replace(
        'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';"',
        '',
    )
    text = text.replace(
        '<div class="team-avatar-fallback" style="display:none" aria-hidden="true">SM</div>',
        '',
    )
    path.write_text(text, encoding="utf-8")
    print("Updated team.php.html")


INSIGHTS_BODY = '''
                <div class="breadcrumb-wrap bg-f br-1 ds-hero-override">
                    <div class="container">
                        <div class="breadcrumb-title">
                            <h2>Insights on Climate Policy &amp; Finance</h2>
                            <p class="cop-hero-subtitle">Thought leadership from global forums to village classrooms</p>
                            <ul class="breadcrumb-menu list-style"><li><a href="index.html">Home</a></li><li>Insights</li></ul>
                        </div>
                    </div>
                </div>
                <section class="about-wrap style1 ptb-100 ds-section">
                    <div class="container ds-container">
                        <div class="ds-recognition-strip">
                            <span>Recognition &amp; Affiliations</span>
                            <strong>UNDP BIOFIN</strong>
                            <strong>London School of Economics</strong>
                        </div>

                        <article class="ds-article-block">
                            <div class="ds-article-meta"><span class="badge-date">2025</span><span>United Nations Development Programme (UNDP) Initiative</span></div>
                            <h3 class="ds-h3 green-dark">Tanzania National BIOFIN Technical Committee</h3>
                            <div class="ds-article-photo">
                                <a href="assets/img/stories/biofin-launch-tanzania.png" data-fancybox="insights-biofin"><img src="assets/img/stories/biofin-launch-tanzania.png" alt="Launch of Biodiversity Finance Initiative in Tanzania with UNDP"></a>
                            </div>
                            <p class="ds-body"><strong>Kenneth Davis Kasigila</strong> participated in the initial working group for Tanzania&apos;s National Biodiversity Finance Initiative (BIOFIN) Technical Committee under the UNDP.</p>
                            <p class="ds-body">His involvement centers on connecting national biodiversity finance policy with practical climate finance implementation. This role serves as a functional bridge between high-level biodiversity finance planning and day-to-day microfinance operations, ensuring that national conservation strategies are actively supported by financial institutions.</p>
                            <div class="ds-takeaways"><h4>Core Focus Areas</h4><ul><li><strong>Policy Implementation:</strong> Translating national biodiversity targets into actionable frameworks for financial institutions.</li><li><strong>Microfinance Integration:</strong> Connecting macro-level environmental finance planning with grassroots microfinance solutions.</li><li><strong>Framework Alignment:</strong> Ensuring that biodiversity objectives align seamlessly with Tanzania&apos;s existing climate finance initiatives.</li></ul></div>
                        </article>

                        <article class="ds-article-block">
                            <div class="ds-article-meta"><span class="badge-date">2025</span><span>London School of Economics · Panel</span></div>
                            <h3 class="ds-h3 green-dark">&quot;I Am a Banker, and Also an Avocado Farmer&quot;</h3>
                            <div class="ds-article-photo">
                                <a href="assets/img/stories/WhatsApp_Image_2026-03-06_at_13.41.52-9e6c26f4-14bd-4513-98c7-ef6327128158.png" data-fancybox="insights-lse"><img src="assets/img/stories/WhatsApp_Image_2026-03-06_at_13.41.52-9e6c26f4-14bd-4513-98c7-ef6327128158.png" alt="Kenneth Kasigila at LSE panel"></a>
                            </div>
                            <p class="ds-body">At the London School of Economics, Kenneth presented on embedding climate-smart agriculture into banking practice — demonstrating how finance professionals can connect high-level policy with on-the-ground farming impact.</p>
                            <div class="ds-takeaways"><h4>Key takeaways</h4><ul><li>Climate finance theory must connect to agricultural practice</li><li>Bankers as farmers — a model for authentic climate leadership</li><li>Academic partnerships strengthen policy-to-practice bridges</li></ul></div>
                        </article>

                        <article class="ds-article-block">
                            <div class="ds-article-meta"><span class="badge-date">2026</span><span>Mbeya, Tanzania · Field visit</span></div>
                            <h3 class="ds-h3 green-dark">Cultivating Change: Global Sustainability with Local Roots</h3>
                            <p class="ds-body">At Africa Climate Finance, sustainability is grown from the ground up. A recent visit to a C.A.F.E. Practices model farm in Mbeya reinforced how conglomerate-backed organic initiatives drive sustainable agriculture — and how climate finance must connect boardroom strategy to field practice.</p>
                            <p class="ds-body mb-0"><a href="kenneth.php.html">Full profile — Kenneth Davis Kasigila →</a> · <a href="cop-engagements.php.html">COP engagements →</a></p>
                        </article>
                    </div>
                </section>
'''


def patch_insights():
    path = ROOT / "climate-policy-insights.php.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"<!-- Breadcrumb Start -->.*?<!-- Content wrapper end -->",
        "<!-- Content Start -->\n" + INSIGHTS_BODY.strip() + "\n            </div>\n\n            <!-- Content wrapper end -->",
        text,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(text, encoding="utf-8")
    print("Updated climate-policy-insights.php.html")


BENEFICIARY_PATCHES = [
    (
        '<div class="cop-block-header">\n                            <span class="cop-eyebrow">Impact Story</span>\n                            <h2>Climate Finance for Ginger Farmers — Isajilo, Tukuyu</h2>\n                        </div>',
        '''<div class="cop-block-header">
                            <span class="cop-eyebrow">Impact Story</span>
                            <h2>Climate Finance for Ginger Farmers — Isajilo, Tukuyu</h2>
                        </div>
                        <blockquote class="ds-pull-quote">&quot;Before, one bad rain meant one lost season. With organic ginger and a financial buffer, we can plan beyond the next storm.&quot;<cite>— Ginger farmer, Isajilo Ward</cite></blockquote>
                        <div class="ds-metrics-row">
                            <div class="ds-metric"><div class="val">Organic</div><div class="lbl">Certified farming transition</div></div>
                            <div class="ds-metric"><div class="val">Export</div><div class="lbl">Premium market access</div></div>
                            <div class="ds-metric"><div class="val">Resilient</div><div class="lbl">Drought-resistant practices</div></div>
                        </div>''',
    ),
    (
        '<h5 class="text-success mb-3">Nyasa Masala: Spicing Up Climate Resilience and Nutrition in Tanzania</h5>',
        '''<blockquote class="ds-pull-quote">&quot;We financed him for making spices to improve food security and navigate climate shocks.&quot;<cite>— Africa Climate Finance, Nyasa Masala beneficiary</cite></blockquote>
                                    <h5 class="text-success mb-3">Nyasa Masala: Spicing Up Climate Resilience and Nutrition in Tanzania</h5>''',
    ),
]


def patch_testimonials():
    path = ROOT / "testimonials.php.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("<title>Our Beneficiaries - Africa Climate Finance</title>", "<title>Our Beneficiaries - Africa Climate Finance</title>")
    for old, new in BENEFICIARY_PATCHES:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("Updated testimonials.php.html")


def patch_contact():
    path = ROOT / "contact.php.html"
    text = path.read_text(encoding="utf-8")
    invite = '''
                        <div class="ds-contact-invite">
                            <p class="mb-1"><strong>We respond within 24 hours.</strong></p>
                            <p class="mb-0">Partnerships and project inquiries: <a href="mailto:hello@climatefinance.co.tz">hello@climatefinance.co.tz</a> · General: <a href="mailto:info@climatefinance.co.tz">info@climatefinance.co.tz</a></p>
                        </div>
'''
    text = text.replace(
        '<div class="section-title style1 text-center mb-40">',
        invite + '\n                        <div class="section-title style1 text-center mb-40">',
        1,
    )
    path.write_text(text, encoding="utf-8")
    print("Updated contact.php.html")


FAQ_SECTION = '''
                <section class="faq-wrap ptb-100 ds-section" id="how-we-work">
                    <div class="container ds-container">
                        <div class="ds-section-header">
                            <span class="ds-eyebrow">How We Work</span>
                            <h2 class="ds-h2">From Concept Note to Funding Proposal</h2>
                        </div>
                        <div class="ds-card ds-mb">
                            <p class="ds-body mb-2"><strong>Concept Notes (CNs)</strong> are early project summaries submitted to climate funders like the GCF — outlining objectives, beneficiaries, and estimated impact.</p>
                            <p class="ds-body mb-2"><strong>Project Preparation Facilities (PPFs)</strong> provide funding to develop a full Funding Proposal — including feasibility studies, environmental and social safeguards, and stakeholder engagement.</p>
                            <p class="ds-body mb-0"><strong>Funding Proposals (FPs)</strong> are comprehensive applications for climate finance — such as GCF FP179 (US$200M) and FP223 (US$1.5B pipeline) that our leadership has supported.</p>
                        </div>
                    </div>
                </section>
'''


def patch_faq():
    path = ROOT / "faq.html"
    text = path.read_text(encoding="utf-8")
    if "how-we-work" not in text:
        text = text.replace(
            '<div id="footer-placeholder"></div>',
            FAQ_SECTION + '\n        <div id="footer-placeholder"></div>',
        )
    path.write_text(text, encoding="utf-8")
    print("Updated faq.html")


def patch_cop_gallery():
    path = ROOT / "cop-engagements.php.html"
    text = path.read_text(encoding="utf-8")
    # Add visible captions under global forums grid
    text = text.replace(
        'class="cop-image-grid cop-grid-many">',
        'class="ds-gallery-captioned">',
    )
    # Wrap each forum image with figure - simpler: add caption class via CSS on alt as title attribute visible
    # Add timeline date to COP30 header
    text = text.replace(
        '<h2>COP30 Brazil — Belém 2025</h2>',
        '<div class="ds-timeline-date">November 2025 · Most Recent</div><h2>COP30 Brazil — Belém 2025</h2>',
    )
    text = text.replace(
        '<h2>COP29 Azerbaijan — Baku 2024</h2>',
        '<div class="ds-timeline-date">November 2024</div><h2>COP29 Azerbaijan — Baku 2024</h2>',
    )
    path.write_text(text, encoding="utf-8")
    print("Updated cop-engagements.php.html")


if __name__ == "__main__":
    patch_team()
    patch_insights()
    patch_testimonials()
    patch_contact()
    patch_faq()
    patch_cop_gallery()
