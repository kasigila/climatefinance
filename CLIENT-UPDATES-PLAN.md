# Client Updates Implementation Plan

This plan summarizes all content received from your client (via WhatsApp) and proposes where each piece should be placed on the Africa Climate Finance website.

---

## 1. PRIORITY: Two Stories After Key Insights (COP Engagements Page)

**Client request (Swahili):** *"Naomba hizo two stories za Nyasa and Aswile in Iringa weka at the end of this Financial mandate just after key insights"*

**Translation:** Place the Nyasa Masala and Power Porridge (Aswile) stories at the end of the "A Financial Mandate for the Green Decade" section, immediately after the Key Insights block.

**File to edit:** `cop-engagements.html`  
**Location:** After line 701 (after `</div>` of the Key Insights block, before `</div>` of the cop-card)

### Story A: Nyasa Masala
- **Title:** "Nyasa Masala": Spicing Up Climate Resilience and Nutrition in Tanzania
- **Full text:** [Provided – Mbeya Region, spice blends, climate-smart agriculture, decarbonizing supply chain, food utilization]
- **Images (7 total):** Hand holding Tea Masala, man with product in agricultural setting, Nyasa Spice Chai Masala container
- **Testimonial quote:** "One of our beneficiaries, we financed him for making spices to improve food security and food systems to navigate through climate shocks"

### Story B: Power Porridge (Aswile Francis Mwaihola, Iringa)
- **Title:** Empowering Student Success and Climate Action in Iringa
- **Text:** [Provided – truncated at Climate Action bullet; may need client to complete]
- **Image (1):** Man (Aswile) in storage facility with maize flour sacks (25 kg)
- **Note:** Complete the Climate Action bullet: "By streamlining the supply chain and delivering…" (client to provide remainder)

---

## 2. TESTIMONIALS PAGE (New)

**Client request:** *"We have this great stories of we can also have a page for testimonials like the below"*

**Action:** Create a new `testimonials.html` page showcasing impact stories.

**Proposed content for Testimonials page:**
1. **Ginger Farmers (Isajilo, Tukuyu)** – Full article with 3 images
2. **Nyasa Masala (Mbeya)** – Condensed story + testimonial quote + product images
3. **Power Porridge (Iringa)** – Condensed story + image
4. **Beneficiary testimonial block** – Quote + optional cattle/dairy imagery (6 images, no text – use as generic "farmer impact" visuals)

**Add to navigation:** Footer (`inc/footer.html`) and any main nav that lists site pages.

---

## 3. GINGER FARMERS STORY (Isajilo, Tukuyu)

**Content:** Full article about climate finance for smallholder ginger farmers in the Southern Highlands.

**Suggested placement:**
- **Option A:** Featured section on homepage (index.html) – "From the Field" or "Impact Stories"
- **Option B:** Dedicated section on Testimonials page (primary)
- **Option C:** New "Our Impact" subsection on About page

**Images (3):**
- Farmer standing in ginger field
- Farmer crouching, inspecting ginger plants
- Landscape view of ginger farm, rolling hills

---

## 4. LEADERSHIP & EVENTS CONTENT

### Group CEO
- **Caption:** "Our group CEO advocating organic food security seedlings"
- **Image:** CEO in plant nursery holding seedling
- **Placement:** About page (CSR or leadership intro), or Team page, or dedicated "Leadership" callout

### Event Participation Images (13 images, no text)
Use on **COP Engagements page** (`cop-engagements.html`) to enrich existing COP29/COP30 sections:
- COP29 banner, Nest Climate Campus, Namibia Programme, UN Azerbaijan, FAO, LSE, UNCCD, CGAP, Tanzania flag, GCF panel, Jamaica Climate Resilience flyer
- Consider a new "Event Highlights" gallery or integrate into existing COP sections

### LSE Engagement
- **Caption:** "Engaging with academia's institutions @ LSE"
- **Image:** Panel with "I am a Banker, and also an Avocado Farmer!" (CRDB Bank)
- **Placement:** COP Engagements page or new "Partnerships" / "Academic Engagement" section

---

## 5. COMMUNITY & EDUCATION INITIATIVES

| Content | Caption | Image | Suggested Placement |
|---------|---------|-------|---------------------|
| Small farm preparation | "Preparing a small farm class" | Man tilling soil on hillside | About → CSR or Loan Program (Production Activities) |
| Education support | "Education support to primary school teachers" | Group of 8 adults in school office | About → CSR section |
| Community engagement | "Community engagement visiting a primary school" | Children in uniform with adults, football | About → CSR section |

---

## 6. CATTLE/DAIRY IMAGES (6 images, no text)

**Use:** Generic "livestock farmer" or "production activities" imagery.
- **Placement:** About → Loan Program → Step 3 "Production Activities" (currently has placeholder "Production activity photos coming soon")
- Or: Testimonials page as supporting visuals

---

## 7. IMAGE FILE PATHS & ORGANIZATION

**Current state:** Images saved to workspace assets folder with WhatsApp-style filenames.

**Action:** Copy/organize images into `assets/img/` for web use:
- `assets/img/stories/` – Ginger, Nyasa, Power Porridge
- `assets/img/cop/` – Event participation, LSE, COP29
- `assets/img/highlights/` – CSR, education, community, CEO, farm prep, livestock

**Image inventory:**

| Content | Filename pattern | Count |
|---------|------------------|-------|
| Ginger farmers | WhatsApp_Image_2026-03-08_* | 3 |
| Nyasa Masala | WhatsApp_Image_2026-03-07_at_14.07*, 09.26* | 7 |
| Power Porridge | WhatsApp_Image_2026-03-07_at_14.05.48* | 1 |
| Cattle/dairy | WhatsApp_Image_2026-03-07_at_09.39* | 6 |
| Group CEO (nursery) | WhatsApp_Image_2026-03-07_at_08.55.20* | 1 |
| Event participation | WhatsApp_Image_2026-03-06* | 13 |
| LSE panel | WhatsApp_Image_2026-03-06_at_13.41.52* | 1 |
| Farm prep | WhatsApp_Image_2026-03-06_at_13.37.58* | 1 |
| Education support | WhatsApp_Image_2026-03-06_at_13.35.29* | 1 |
| Community engagement | WhatsApp_Image_2026-03-06_at_13.33.53* | 1 |

---

## 8. IMPLEMENTATION ORDER

### Phase 1: Client-requested placement
1. **Add Nyasa + Aswile stories** after Key Insights in `cop-engagements.html`
2. Ensure images are in correct paths; add responsive image markup

### Phase 2: New Testimonials page
3. Create `testimonials.html` with Ginger, Nyasa, Power Porridge, beneficiary quote
4. Add link in footer and navigation

### Phase 3: Enrich existing pages
5. Add Group CEO + CSR/community images to About page
6. Add event images to COP Engagements
7. Add production/livestock images to Loan Program Step 3

### Phase 4: Content completion
8. Request truncated Power Porridge text from client (Climate Action bullet)
9. Add i18n keys if site uses localization (I18N-README.md present)

---

## 9. OPEN QUESTIONS FOR CLIENT

1. **Power Porridge** – Please send the rest of the Climate Action bullet: "By streamlining the supply chain and delivering…"
2. **Cattle/dairy images** – Do these have an associated story or beneficiary name, or are they generic impact visuals?
3. **Testimonials page** – Should it be linked in the main header nav, or only in footer/About?

---

*Plan created from WhatsApp content collected [session date].*
