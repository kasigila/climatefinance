#!/usr/bin/env python3
"""Generate redesigned page content blocks."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGE_SHELL_HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/flaticon.css">
    <link rel="stylesheet" href="assets/css/remixicon.css">
    <link rel="stylesheet" href="assets/css/fancybox.css">
    <link rel="stylesheet" href="assets/css/aos.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/responsive.css">
    <link rel="stylesheet" href="assets/css/dark-theme.css">
    <link rel="stylesheet" href="assets/css/enhancements.css">
    <link rel="stylesheet" href="assets/css/design-system.css">
    <link rel="stylesheet" href="assets/css/footer-modern.css">
    <link rel="stylesheet" href="assets/css/cop.css">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="assets/img/favicon-f.png">
</head>
<body class="ds-header-compact ds-page">
<div class="page-wrapper">
<div id="header-placeholder" data-active="{active}"></div>
<script src="assets/js/header-loader.js"></script>
<div class="content-wrapper">
'''

PAGE_SHELL_FOOT = '''
</div>
<div id="footer-placeholder"></div>
<script src="assets/js/footer-loader.js"></script>
</div>
<a href="javascript:void(0)" class="back-to-top bounce"><i class="ri-arrow-up-s-line"></i></a>
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/fancybox.js"></script>
<script src="assets/js/i18n.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

WOMEN_BODY = '''
<div class="breadcrumb-wrap bg-f br-1 ds-hero-override">
  <div class="container">
    <div class="breadcrumb-title">
      <h2>Women Empowerment</h2>
      <p class="cop-hero-subtitle">280+ women trained in financial literacy and climate-smart practices in Isajilo Ward, January 2026</p>
      <ul class="breadcrumb-menu list-style"><li><a href="index.html">Home</a></li><li>Women Empowerment</li></ul>
    </div>
  </div>
</div>
<section class="about-wrap style1 ptb-100 ds-section" id="women-empowerment">
  <div class="container ds-container">
    <div class="ds-section-header">
      <span class="ds-eyebrow">Our Impact</span>
      <h2 class="ds-h2">Women Economic Empowerment</h2>
      <span class="badge bg-success rounded-pill mt-2">Empowering 280+ Women, January 2026</span>
    </div>
    <h3 class="ds-h3 green-dark text-center ds-mb">Taking Climate Finance to the Grassroots</h3>
    <div class="ds-numbered-cards ds-mb-lg">
      <div class="ds-numbered-card"><div class="num">01</div><h4 class="ds-card-title green-dark">The Return</h4><p class="ds-card-desc ds-mb-0">During annual leave in January 2026, our Group CEO returned to Rungwe to engage with mothers, smallholder farmers, and neighbors of Isajilo Ward.</p></div>
      <div class="ds-numbered-card"><div class="num">02</div><h4 class="ds-card-title green-dark">The Movement</h4><p class="ds-card-desc ds-mb-0">More than 280 women reached with financial literacy, climate change knowledge, and microfinance support.</p></div>
      <div class="ds-numbered-card"><div class="num">03</div><h4 class="ds-card-title green-dark">The Mission</h4><p class="ds-card-desc ds-mb-0">Translate complex banking and climate language into practical guidance for real harvest and livelihood decisions.</p></div>
    </div>
    <h3 class="ds-h3 green-dark text-center ds-mb" id="women-gallery">Classroom &amp; Community Engagement</h3>
    <div class="ds-gallery-captioned ds-mb-lg">
      <figure><a href="assets/img/highlights/women-280-community.png" data-fancybox="classroom"><img src="assets/img/highlights/women-280-community.png" alt="CEO with teachers and parents"></a><figcaption>Group CEO with school teachers and parents, Isajilo Ward</figcaption></figure>
      <figure><a href="assets/img/highlights/women-280-group.png" data-fancybox="classroom"><img src="assets/img/highlights/women-280-group.png" alt="Women from four villages"></a><figcaption>Women representatives from four villages, Rungwe District</figcaption></figure>
      <figure><a href="assets/img/highlights/women-280-session.png" data-fancybox="classroom"><img src="assets/img/highlights/women-280-session.png" alt="Education session"></a><figcaption>Financial literacy session, January 2026</figcaption></figure>
      <figure><a href="assets/img/highlights/women-280-outdoor-tree.png" data-fancybox="classroom"><img src="assets/img/highlights/women-280-outdoor-tree.png" alt="Outdoor session"></a><figcaption>Outdoor climate-smart training session</figcaption></figure>
      <figure><a href="assets/img/highlights/women-280-questionnaire.png" data-fancybox="classroom"><img src="assets/img/highlights/women-280-questionnaire.png" alt="Needs assessment"></a><figcaption>Grassroots questionnaire on finance and climate</figcaption></figure>
      <figure><a href="assets/img/highlights/women-280-women-seated.png" data-fancybox="classroom"><img src="assets/img/highlights/women-280-women-seated.png" alt="Women in session"></a><figcaption>Community participants, Mbeya Region</figcaption></figure>
    </div>
    <div class="text-center"><a href="testimonials.php.html" class="btn style2 rounded-pill">Read Beneficiary Stories</a></div>
  </div>
</section>
'''

LOAN_BODY = '''
<div class="breadcrumb-wrap bg-f br-1 ds-hero-override">
  <div class="container">
    <div class="breadcrumb-title">
      <h2>Loan Program</h2>
      <p class="cop-hero-subtitle">From financial literacy to climate-resilient production</p>
      <ul class="breadcrumb-menu list-style"><li><a href="index.html">Home</a></li><li>Loan Program</li></ul>
    </div>
  </div>
</div>
<section class="about-wrap style1 ptb-100 ds-section" id="loan-program">
  <div class="container ds-container">
    <div class="ds-section-header">
      <span class="ds-eyebrow">Our Impact</span>
      <h2 class="ds-h2">Loan Program: From Education to Production</h2>
      <p class="ds-subtitle">A structured pathway from financial literacy to sustainable livelihoods.</p>
    </div>
    <div class="ds-step-cards">
      <div class="ds-step-card">
        <span class="ds-step-badge">Step 1</span>
        <h4 class="ds-card-title green-dark">Education Before Loans</h4>
        <p class="ds-card-desc">Financial literacy and business training prepare beneficiaries for responsible borrowing.</p>
        <div class="ds-step-thumbs">
          <a href="assets/img/highlights/education-man-presenting.jpg" data-fancybox="loan-flow"><img src="assets/img/highlights/education-man-presenting.jpg" alt="Education session"></a>
          <a href="assets/img/highlights/education-panel.jpg" data-fancybox="loan-flow"><img src="assets/img/highlights/education-panel.jpg" alt="Panel discussion"></a>
          <a href="assets/img/highlights/education-classroom-group.jpg" data-fancybox="loan-flow"><img src="assets/img/highlights/education-classroom-group.jpg" alt="Classroom group"></a>
        </div>
      </div>
      <div class="ds-step-card">
        <span class="ds-step-badge">Step 2</span>
        <h4 class="ds-card-title green-dark">Groups That Received Loans</h4>
        <p class="ds-card-desc">Cooperatives and savings groups receive climate-smart microfinance.</p>
        <div class="ds-step-thumbs">
          <a href="assets/img/highlights/loan-groups-community.jpg" data-fancybox="loan-flow"><img src="assets/img/highlights/loan-groups-community.jpg" alt="Loan groups"></a>
          <a href="assets/img/highlights/loan-groups-celebration.jpg" data-fancybox="loan-flow"><img src="assets/img/highlights/loan-groups-celebration.jpg" alt="Celebration"></a>
        </div>
      </div>
      <div class="ds-step-card">
        <span class="ds-step-badge">Step 3</span>
        <h4 class="ds-card-title green-dark">Production Activities</h4>
        <p class="ds-card-desc">Loans deployed in climate-resilient farming, livestock, and small enterprises.</p>
        <div class="ds-step-thumbs">
          <a href="assets/img/stories/WhatsApp_Image_2026-03-07_at_09.39.40-21b35057-a734-443e-8418-56484619b7c1.png" data-fancybox="production"><img src="assets/img/stories/WhatsApp_Image_2026-03-07_at_09.39.40-21b35057-a734-443e-8418-56484619b7c1.png" alt="Livestock production"></a>
          <a href="assets/img/stories/WhatsApp_Image_2026-03-07_at_09.39.44-6ed8247e-ea2c-4fc1-9fd1-e8edba10ee89.png" data-fancybox="production"><img src="assets/img/stories/WhatsApp_Image_2026-03-07_at_09.39.44-6ed8247e-ea2c-4fc1-9fd1-e8edba10ee89.png" alt="Dairy farming"></a>
        </div>
      </div>
    </div>
    <div class="text-center mt-4"><a href="testimonials.php.html" class="btn style2 rounded-pill">See Beneficiary Outcomes</a></div>
  </div>
</section>
'''

def write_page(name, title, active, body):
    html = PAGE_SHELL_HEAD.format(title=title, active=active) + body + PAGE_SHELL_FOOT
    (ROOT / name).write_text(html, encoding="utf-8")
    print(f"Wrote {name}")

def patch_index():
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    start = text.find("<!-- Hero Section Start -->")
    end = text.find("<!-- Footer Section Start -->")
    if start == -1 or end == -1:
        print("Could not patch index.html")
        return
    new_main = (ROOT / "scripts" / "_index_main.html").read_text(encoding="utf-8")
    path.write_text(text[:start] + new_main + text[end:], encoding="utf-8")
    print("Patched index.html")

if __name__ == "__main__":
    write_page("women-empowerment.php.html", "Women Empowerment - Africa Climate Finance", "women-empowerment", WOMEN_BODY)
    write_page("loan-program.php.html", "Loan Program - Africa Climate Finance", "loan-program", LOAN_BODY)
    patch_index()
