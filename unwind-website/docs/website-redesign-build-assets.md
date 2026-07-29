---
type: build-asset
domain: business
area: growth
sources: [website-redesign-strategy.md, unwind-vacations-1.hosted.ownerrez.com (staging audit 2026-07-06)]
last_updated: 2026-07-06
status: Phase 2 — v1 bundle, iterate on staging
---

# Website Redesign — Build Assets (paste-ready)

Companion to [[website-redesign-strategy]]. Two blocks, two destinations in OwnerRez.
Selectors below were captured from the real staging markup on 2026-07-06.

---

> **⚠️ Paste rules (learned 2026-07-06):** The Theme/Layout editor has four tabs:
> *Fonts & Colors · Footer · CSS · Head*. **Block 1 (HTML) goes in the HEAD tab —
> never the CSS tab** (SiteCss rejects any `<`/`>`). **Block 2 (CSS) goes in the CSS
> tab.** Copy only the contents INSIDE each code box — no ``` fence lines, no notes.

## BLOCK 0 — Fonts & Colors tab (native settings, do first)
- Accent Color: `#E76F51` · Heading Color: `#123B4F` · Text Color: `#1F2937` · Muted: `#6B7280`
- Main Font: pick **Inter** if the dropdown has it; otherwise leave as-is (CSS overrides).

## BLOCK 1 — HEAD tab (HTML) — v1.1, corrected 2026-07-11
**Where:** Theme & Layout → **Head** tab. **Replace the ENTIRE tab contents with the
block below** (select-all → delete → paste). The last line must be `</script>` — a
missing closer blanks the whole site (learned the hard way 2026-07-11).

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<script>
document.addEventListener('DOMContentLoaded', function () {
  var widget = document.querySelector('.ownerrez-widget[data-widget-type="Booking/Inquiry"]');
  if (!widget || window.innerWidth > 767) return;
  var price = '';
  document.querySelectorAll('h1,h2,h3').forEach(function(h){
    if (!price && /\$\d/.test(h.textContent)) price = h.textContent.trim();
  });
  var bar = document.createElement('div');
  bar.className = 'uw-sticky-bar';
  bar.innerHTML = '<span class="uw-sticky-price">' + (price || 'Book direct — best rate') + '</span>' +
                  '<button type="button" class="uw-btn-primary uw-sticky-btn">Check availability</button>';
  document.body.appendChild(bar);
  bar.querySelector('button').addEventListener('click', function () {
    widget.scrollIntoView({behavior: 'smooth', block: 'start'});
  });
});
</script>
```

GA4 note: **already installed** — tag `G-96L4KV3KEJ` is live on the site (found
2026-07-11), so no GA4 paste needed in Phase 6; just wire the thank-you conversion
event.

---

## BLOCK 2 — CSS tab (pure CSS only — no HTML)
**Where:** Theme & Layout → **CSS** tab. Replace whole tab contents on each
iteration; this is v1 (global shell + listing polish + sticky bar).

```css
/* ===== Unwind design tokens (strategy §5) ===== */
:root{
  --uw-navy:#123B4F; --uw-teal:#0E7C86; --uw-coral:#E76F51; --uw-coral-dark:#D45A3D;
  --uw-sand:#F6F1E7; --uw-ink:#1F2937; --uw-gray:#6B7280; --uw-line:#E5E7EB; --uw-gold:#E8A33D;
}

/* ===== Global type ===== */
body{font-family:'Inter',system-ui,sans-serif !important;color:var(--uw-ink);line-height:1.6}
h1,h2,.page-header{font-family:'Fraunces',Georgia,serif !important;color:var(--uw-navy)}
h1{font-size:40px;line-height:1.15}
h2,.page-header{font-size:30px}
@media(max-width:767px){h1{font-size:30px}h2,.page-header{font-size:24px}}
a{color:var(--uw-teal)}

/* ===== Buttons (template uses .btn-default heavily) ===== */
.btn-default{border-radius:8px;font-weight:500;border-color:var(--uw-line)}
.btn-default:hover{border-color:var(--uw-teal);color:var(--uw-teal)}
button[type=submit].btn,.btn-primary{
  background:var(--uw-coral) !important;border-color:var(--uw-coral) !important;
  color:#fff !important;border-radius:8px;font-weight:600;padding:10px 22px}
button[type=submit].btn:hover,.btn-primary:hover{
  background:var(--uw-coral-dark) !important;border-color:var(--uw-coral-dark) !important}

/* ===== Listing rows → card feel (real selectors from staging) ===== */
.thumbnail{border-radius:12px;border:1px solid var(--uw-line);overflow:hidden;padding:0}
.thumbnail .media-object,img.media-object{border-radius:12px;width:100%;object-fit:cover;aspect-ratio:4/3}
h2.media-heading a{font-family:'Inter',sans-serif !important;font-size:18px;font-weight:600;
  color:var(--uw-navy);text-decoration:none}
h2.media-heading a:hover{color:var(--uw-teal)}
/* price chip — the template renders "$524/night" in this exact element */
h3.media-heading{font-size:16px;font-weight:600;color:var(--uw-navy);
  background:var(--uw-sand);border-radius:999px;padding:6px 14px;margin-top:0}
.amenity-summary-size,.amenity-summary-amenities{color:var(--uw-gray);font-size:14px}
.amenity-list-item{font-size:14px}

/* ===== Sitewide rating band (inject via homepage HTML, styled here) ===== */
.uw-rating-band{background:var(--uw-sand);border-radius:12px;padding:14px 20px;
  text-align:center;font-size:16px;margin:16px 0}
.uw-rating-band .uw-stars{color:var(--uw-gold);font-weight:600}

/* ===== Sticky mobile booking bar (built by header JS) ===== */
.uw-sticky-bar{position:fixed;bottom:0;left:0;right:0;z-index:1000;background:#fff;
  border-top:1px solid var(--uw-line);box-shadow:0 -4px 16px rgba(18,59,79,.12);
  display:flex;align-items:center;justify-content:space-between;gap:12px;
  padding:12px 16px calc(12px + env(safe-area-inset-bottom))}
.uw-sticky-price{font-weight:600;color:var(--uw-navy);font-size:16px}
.uw-btn-primary,.uw-sticky-btn{background:var(--uw-coral);color:#fff;border:0;
  border-radius:8px;padding:12px 20px;font-weight:600;font-size:16px}
.uw-sticky-btn:active{background:var(--uw-coral-dark)}
@media(min-width:768px){.uw-sticky-bar{display:none}}

/* ===== Footer & header polish ===== */
footer{background:var(--uw-navy);color:#fff;padding:32px 16px;margin-top:64px}
footer a{color:#cfe6ea}
.header-line-container{border-bottom:1px solid var(--uw-line)}
```

---

## Rating band HTML (paste into homepage content, above the property list)
```html
<div class="uw-rating-band">
  <span class="uw-stars">★ 4.9</span> average from <strong>950+ verified guest reviews</strong>
  — every home managed by our local Grand Strand team.
</div>
```

---

## BLOCK 3 — Phase 3 homepage assets (added 2026-07-11)

### 3a. Hero — the single-photo trick (John clicks, ~15 min)
The staging homepage already runs the "full carousel + search" layout. A carousel
with ONE image = a static hero, search stays overlaid. Steps:
1. Pick the ONE hero photo: bright, wide/landscape, ocean or oceanfront-balcony view,
   no interiors. From your best listing photos.
2. Compress at **squoosh.app** → target ≤ 300 KB, width ~2000px.
3. Staging site settings → the home page / carousel image list → **remove all images
   except that one** (upload the compressed version).
4. Refresh on your phone: page should load dramatically faster.

### 3b. CSS v2 — APPEND to the bottom of the CSS tab (don't delete v1)
```css
/* ===== v2: hero headline overlay + homepage strips ===== */
#carousel-hero{position:relative}
#carousel-hero::after{content:"Your week at the beach starts here.";
  position:absolute;top:22%;left:50%;transform:translateX(-50%);width:92%;max-width:900px;
  text-align:center;font-family:'Fraunces',Georgia,serif;font-weight:700;color:#fff;
  font-size:clamp(28px,5vw,52px);line-height:1.15;text-shadow:0 2px 18px rgba(18,59,79,.55);
  pointer-events:none;z-index:5}
.uw-strip{display:flex;gap:24px;flex-wrap:wrap;justify-content:center;
  background:var(--uw-sand);border-radius:12px;padding:28px 24px;margin:24px 0}
.uw-strip-item{flex:1 1 260px;max-width:340px;text-align:center}
.uw-strip-item h3{font-size:17px;font-weight:600;color:var(--uw-navy);margin:0 0 6px}
.uw-strip-item p{font-size:14.5px;color:var(--uw-gray);margin:0}
.uw-owner-strip{background:var(--uw-navy);border-radius:12px;padding:36px 28px;
  text-align:center;color:#fff;margin:32px 0}
.uw-owner-strip h2{font-family:'Fraunces',Georgia,serif;color:#fff;font-size:26px;margin:0 0 8px}
.uw-owner-strip p{color:#cfe6ea;max-width:560px;margin:0 auto 18px}
```

### 3c. Homepage content HTML — paste into the home page content/text area
(above or below the property list, wherever the editor allows custom content)
```html
<div class="uw-rating-band">
  <span class="uw-stars">★ 4.9</span> average from <strong>950+ verified guest reviews</strong>
  — every home managed by our local Grand Strand team.
</div>

<div class="uw-strip">
  <div class="uw-strip-item">
    <h3>Best rate, guaranteed</h3>
    <p>Booking direct always beats the Airbnb price. Same home, no service fees.</p>
  </div>
  <div class="uw-strip-item">
    <h3>A real local team</h3>
    <p>Our office is on the Grand Strand. Text us — a person answers.</p>
  </div>
  <div class="uw-strip-item">
    <h3>Handpicked homes</h3>
    <p>We manage every home we list. No surprises at check-in.</p>
  </div>
</div>
```

### 3d. Owner strip HTML — paste at the BOTTOM of the same content area
**Prereq:** create an empty custom page at `/property-management` first (title:
"Property Management" — content lands in Phase 4) so the button link works.
```html
<div class="uw-owner-strip">
  <h2>Own a rental on the Grand Strand?</h2>
  <p>See what your property could earn with a local team on your side. Free,
  no-pressure projection — real numbers from real bookings.</p>
  <a class="uw-btn-primary" href="/property-management">Get my free rental projection</a>
</div>
```

## BLOCK 4 — Quick-filter bedroom chips (added 2026-07-13)
Airbnb-style one-tap browsing: chips under the hero search ("1 Bedroom / 2 Bedrooms /
3+ / 4+") that submit the existing search form with just that filter — no dates
required. (The /properties page ignores GET params — POST only — so the chips must
drive the form; verified 2026-07-13.)

### 4a. HEAD tab v1.2 — ⚠️ SUPERSEDED by v1.3 (see 4a-v1.3 below; kept for history)
(fonts + sticky bar + chips injector, all-in-one; last line must be `</script>`)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<script>
document.addEventListener('DOMContentLoaded', function () {
  /* --- sticky mobile booking bar (property pages) --- */
  var widget = document.querySelector('.ownerrez-widget[data-widget-type="Booking/Inquiry"]');
  if (widget && window.innerWidth <= 767) {
    var price = '';
    document.querySelectorAll('h1,h2,h3').forEach(function(h){
      if (!price && /\$\d/.test(h.textContent)) price = h.textContent.trim();
    });
    var bar = document.createElement('div');
    bar.className = 'uw-sticky-bar';
    bar.innerHTML = '<span class="uw-sticky-price">' + (price || 'Book direct — best rate') + '</span>' +
                    '<button type="button" class="uw-btn-primary uw-sticky-btn">Check availability</button>';
    document.body.appendChild(bar);
    bar.querySelector('button').addEventListener('click', function () {
      widget.scrollIntoView({behavior: 'smooth', block: 'start'});
    });
  }
  /* --- one-tap bedroom chips under the hero search --- */
  var searchBar = document.querySelector('.incarousel-search-bar');
  var form = searchBar ? searchBar.querySelector('form[action="/properties"]') : null;
  if (form) {
    var chips = document.createElement('div');
    chips.className = 'uw-chips';
    chips.innerHTML =
      '<span class="uw-chips-label">Just browsing?</span>' +
      '<button type="button" class="uw-chip" data-beds="1">1 Bedroom</button>' +
      '<button type="button" class="uw-chip" data-beds="2">2 Bedrooms</button>' +
      '<button type="button" class="uw-chip" data-beds="3">3+ Bedrooms</button>' +
      '<button type="button" class="uw-chip" data-beds="4">4+ Bedrooms</button>';
    searchBar.appendChild(chips);
    chips.addEventListener('click', function (e) {
      var b = e.target.getAttribute && e.target.getAttribute('data-beds');
      if (!b) return;
      form.querySelectorAll('select[name="Bedrooms"], #Bedrooms').forEach(function(s){ s.value = b; });
      form.submit();
    });
  }
});
</script>
```

### 4a-v1.3. HEAD tab — CURRENT (live on staging 2026-07-13) — exact bedroom filtering
Same as v1.2 plus: chips 1/2/3 filter results to EXACTLY that bedroom count
(client-side hide via sessionStorage flag, since the OwnerRez Bedrooms filter is
"N or more" only); 4+ chip keeps minimum semantics intentionally; a sand notice bar
("Showing 2-bedroom homes only · Show all homes") appears above filtered results.
Each listing renders desktop+mobile heading pairs → the script divides matches by 2
for the displayed count. Full v1.3 code was delivered in-chat 2026-07-13; the Head
tab on staging IS the source of truth — copy from there before any future edit.
Caveat (accepted): the page's own "55 properties" total reflects the server's
minimum-filter, not the exact filter; the durable fix is Block 4c tag pages.

### 4b. CSS — append to the bottom of the CSS tab
```css
/* ===== chips under hero search ===== */
.uw-chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;align-items:center;
  padding:10px 0 2px}
.uw-chips-label{font-size:14px;color:var(--uw-gray);margin-right:4px}
.uw-chip{background:#fff;border:1.5px solid var(--uw-teal);color:var(--uw-teal);
  border-radius:999px;padding:8px 16px;font-size:14px;font-weight:600;cursor:pointer}
.uw-chip:hover{background:var(--uw-teal);color:#fff}
@media(max-width:767px){.uw-chips{padding:8px 12px}.uw-chip{padding:10px 14px}}
/* ===== exact-filter notice bar (v1.3) ===== */
.uw-filter-note{background:var(--uw-sand);border-radius:12px;padding:12px 18px;
  margin:12px 0;display:flex;align-items:center;gap:14px;flex-wrap:wrap;font-size:15px}
```

### 4c. Later (Phase 5): tag-based collection pages
OwnerRez property-list pages can filter by property tags → create "Oceanfront,"
"Pet Friendly," and the 4 area pages as tagged collections (this doubles as the §6.8
area-page plan). Needs tags set on properties in OwnerRez first.

## BLOCK 5 — Owner landing page /property-management (added 2026-07-14)
John's locked decisions: proof = locally-owned · Airbnb SuperHost · ★4.9/950+ ·
data-driven · realtor-referred heritage (NO revenue number, NO fee % published);
onboarding promise = **7 days**; 24/7 guest support published.

### 5a. CSS — append to the bottom of the CSS tab
```css
/* ===== owner landing page ===== */
.uw-proof-bar{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;
  background:var(--uw-sand);border-radius:12px;padding:22px 20px;margin:24px 0}
.uw-proof-item{flex:1 1 200px;max-width:260px;text-align:center}
.uw-proof-item strong{display:block;font-size:17px;color:var(--uw-navy)}
.uw-proof-item span{font-size:13.5px;color:var(--uw-gray)}
.uw-3col{display:flex;flex-wrap:wrap;gap:20px;margin:24px 0}
.uw-3col>div{flex:1 1 260px;background:#fff;border:1px solid var(--uw-line);
  border-radius:12px;padding:22px}
.uw-3col h3{font-size:17px;color:var(--uw-navy);margin:0 0 8px}
.uw-3col p{font-size:14.5px;color:var(--uw-gray);margin:0}
.uw-3col .uw-win{border:2px solid var(--uw-teal)}
.uw-steps{counter-reset:step;list-style:none;padding:0;margin:24px 0;display:flex;
  flex-wrap:wrap;gap:20px}
.uw-steps li{flex:1 1 240px;background:var(--uw-sand);border-radius:12px;padding:20px}
.uw-steps li::before{counter-increment:step;content:counter(step);display:inline-flex;
  width:32px;height:32px;border-radius:50%;background:var(--uw-coral);color:#fff;
  align-items:center;justify-content:center;font-weight:700;margin-bottom:10px}
.uw-faq details{border-bottom:1px solid var(--uw-line);padding:14px 0}
.uw-faq summary{font-weight:600;color:var(--uw-navy);cursor:pointer;font-size:16px}
.uw-faq p{margin:10px 0 0;color:var(--uw-ink)}
.uw-cta-row{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin:18px 0}
.uw-cta-row .uw-btn-secondary{background:#fff;color:var(--uw-teal);
  border:1.5px solid var(--uw-teal);border-radius:8px;padding:12px 20px;
  font-weight:600;text-decoration:none;display:inline-block}
```

### 5b. Page HTML — paste into the /property-management custom page (via <> source view)
```html
<h1>Your beach property deserves better than a call center.</h1>
<p style="font-size:18px;max-width:720px">Unwind is a boutique, locally owned
management company on the Grand Strand — an Airbnb SuperHost team that treats your
property like the asset it is. See what your home could really earn.</p>
<div class="uw-cta-row" style="justify-content:flex-start">
  <a class="uw-btn-primary" href="#projection">Get my free rental projection</a>
  <a class="uw-btn-secondary" href="tel:8434389992">Or call (843) 438-9992</a>
</div>

<div class="uw-proof-bar">
  <div class="uw-proof-item"><strong>Locally owned &amp; operated</strong><span>Our office is on the Grand Strand — not three states away</span></div>
  <div class="uw-proof-item"><strong>Airbnb SuperHost</strong><span>Top-tier hosting status, earned stay after stay</span></div>
  <div class="uw-proof-item"><strong>★ 4.9 · 950+ reviews</strong><span>Verified guest reviews across our homes</span></div>
  <div class="uw-proof-item"><strong>Data-driven results</strong><span>Dynamic pricing tuned daily, not set-and-forget</span></div>
</div>

<h2>Three ways to run a beach rental</h2>
<div class="uw-3col">
  <div><h3>The big national brands</h3><p>Your home is a unit number. Guest problems route through a call center, and your "local contact" changes every season.</p></div>
  <div><h3>Going it alone</h3><p>Weekend guest texts, pricing guesswork, cleaner no-shows. A second job you didn't ask for.</p></div>
  <div class="uw-win"><h3>Unwind</h3><p>A boutique local team, professional pricing tools, 24/7 guest support — and a manager who's seen your actual living room. We've been realtor-referred since day one.</p></div>
</div>

<h2>What we handle (all of it)</h2>
<div class="uw-3col">
  <div><h3>Pricing that works daily</h3><p>Dynamic rates tuned to Grand Strand demand — events, seasons, booking pace.</p></div>
  <div><h3>Marketing everywhere</h3><p>Airbnb, Vrbo, Booking.com, Google — plus direct bookings that skip the fees.</p></div>
  <div><h3>24/7 guest support</h3><p>Guests get answers around the clock, so you never get the 2am call.</p></div>
  <div><h3>Cleaning &amp; inspections</h3><p>Professional turnovers with photo-verified inspections after every stay.</p></div>
  <div><h3>Maintenance coordination</h3><p>Trusted local vendors, handled fast, documented for you.</p></div>
  <div><h3>Owner portal &amp; statements</h3><p>Real-time calendar, monthly statements, your numbers always visible.</p></div>
</div>

<h2>Switching is easier than you think</h2>
<ol class="uw-steps">
  <li><strong>Tell us about your property.</strong> Two minutes — address, bedrooms, how you use it.</li>
  <li><strong>Get your free projection.</strong> Real numbers from comparable homes we already manage, in your inbox within one business day.</li>
  <li><strong>We handle the switch.</strong> Listings, photos, pricing, guest comms — <strong>onboarded within 7 days.</strong></li>
</ol>

<h2 id="projection">Get your free rental projection</h2>
<p>No pressure, no obligation — just real numbers from a local team.</p>
<!-- FORM EMBED GOES HERE: Vintory/GHL form (preferred, leads land in CRM) or OwnerRez contact form. Until then the buttons below carry the CTA. -->
<div class="uw-cta-row" style="justify-content:flex-start">
  <a class="uw-btn-primary" href="mailto:info@unwindvacations.com?subject=Free%20Rental%20Projection%20Request&body=Property%20address%3A%0ABedrooms%3A%0AYour%20name%3A%0APhone%3A">Email us for your projection</a>
  <a class="uw-btn-secondary" href="sms:8434389992">Text us</a>
  <a class="uw-btn-secondary" href="tel:8434389992">Call (843) 438-9992</a>
</div>

<h2>Owner questions, straight answers</h2>
<div class="uw-faq">
  <details><summary>What do you charge?</summary><p>A straightforward management fee with no surprise charges — no setup fees, no long menus of add-ons. We'll walk you through exactly how it works on a quick call, with your projection in hand.</p></details>
  <details><summary>How fast can my property be live?</summary><p>Onboarded within 7 days. Listings, photography coordination, pricing setup, and guest messaging — we handle the switch, including the handoff from your current manager.</p></details>
  <details><summary>Can I still use my property myself?</summary><p>Of course — it's your home. Block your dates in the owner portal anytime.</p></details>
  <details><summary>How do I get paid?</summary><p>Monthly payouts with a clear statement showing every booking, every charge, every dollar.</p></details>
  <details><summary>What makes you different from the big brands?</summary><p>We're not trying to manage 40,000 homes. We're trying to be the best manager on the Grand Strand — locally owned, realtor-referred since day one, with a team you can meet for coffee.</p></details>
</div>

<div class="uw-owner-strip">
  <h2>Ready to see your number?</h2>
  <p>Free projection, one business day, zero pressure.</p>
  <a class="uw-btn-primary" href="#projection">Get my free rental projection</a>
</div>
```

### 5c. Still needed to finish this page
- **Form embed**: build a 6-field form in Vintory/GHL (name, email, phone, address,
  bedrooms, notes) → leads land in the CRM with automations available; paste embed
  at the FORM EMBED marker. Interim email/text/call buttons work today.
- **Owner testimonials**: 1–2 real quotes with first name + property type
  `[JOHN ACTION: ask 2–3 happiest owners]` — slot goes between "What we handle" and
  "Switching."
- Thank-you page (once a real form exists): create /property-management/thank-you —
  "Got it — your projection will be in your inbox within one business day." (GA4
  conversion event fires on this URL, Phase 6.)

## LIVE SITE — Bedroom filter shipped 2026-07-XX (Claude-driven via Chrome)
The bedroom quick-filter chips are **LIVE on unwindvacations.com** (the "Unwind
Vacations" hosted site, id 573931745 — NOT the v2 staging site). Applied directly by
Claude in OwnerRez via the browser; verified 1BR→8, 2BR→27, 3BR→13 exact matches.

**Hard-won learnings (critical for any future live-site theme edits):**
1. **The CSS/Head tabs are ACE code editors, not plain textareas.** Setting
   `textarea.value` does NOT persist — ACE overwrites it on save. Must use the ACE
   API: `window.ace.edit(document.querySelectorAll('.ace_editor')[i])` then
   `.setValue(text,-1)`. Editor index order: [0]=FooterHtml, [1]=SiteCss, [2]=HeadHtml.
2. **`/properties` IGNORES GET query params — filtering is POST-only.** So you cannot
   deep-link `/properties?Bedrooms=3`. The chips must set the form's Bedrooms select
   and submit the form. And any client-side "fetch all matches" must page the FULL
   unfiltered list via `?Page=N` (pagination GET works) and filter client-side.
3. **Exact-bedroom filter = multi-page fetch.** OwnerRez Bedrooms filter is "N or more"
   and caps at 12/page. So chips 1/2/3 set a sessionStorage flag; on `/properties` the
   script fetches every page of the full list, keeps only exact `.amenity-summary-size`
   matches, replaces the card container, hides pagination, and removes orphaned `<hr>`
   dividers. 4+ chip keeps native "4 or more".
4. Live site already had custom Head (Facebook SDK) + 2914 chars CSS — **always append,
   never overwrite.** Live theme colors: accent #4bbfbf, heading/link navy #1b4f6b
   (chips use navy to match).
5. The Chrome `javascript_tool` blocks returning base64 / cookie-ish strings — read
   structure (tag counts, keywords) instead of raw content.

**Source of truth = the live site's Head tab** (Settings → Hosted Websites → Unwind
Vacations → Theme & Layout → Head). Full current script lives there; copy from it
before editing. Same code is portable to the v2 staging site if wanted.

## Iteration log
- **2026-07-XX chip v3 (perf fix)** — John reported 1BR/2BR "not working." Root cause:
  the v2 filter fetched result pages SEQUENTIALLY (5 awaited fetches) → several seconds
  of showing unfiltered premium-first big houses before it narrowed = looked broken,
  esp. on mobile/slow connections; and a single hung fetch could stall it. Fix:
  (a) hide all result cards INSTANTLY on tap + show "Finding…", (b) fetch all pages in
  PARALLEL via Promise.all with per-request .catch (failure-tolerant, near-instant),
  (c) reveal only exact matches. Verified live: 2BR→27 fast & clean. If a user still
  sees stale behavior it's their browser cache → hard refresh.
- **2026-07-13 v1.3 LIVE** — Exact bedroom chips confirmed working by John on staging.
  Hero = single photo (⚠️ still 2 MB — compression pending). Rating band pasted.
  Still pending from Block 3: v2 CSS headline overlay (3b), 3-col strip (3c),
  owner strip + /property-management shell (3d).
- **2026-07-11 v2** — Phase 2 confirmed live (CSS + Head + Fonts & Colors all saved;
  blank-site incident root-caused to missing `</script>`, fixed). GA4 already present
  (G-96L4KV3KEJ). Added Block 3: hero single-photo steps, v2 CSS (hero headline
  overlay + strips), homepage strips HTML, owner strip HTML.
- **2026-07-06 v1** — tokens, type, buttons, listing/card polish, price chip, rating
  band, sticky mobile bar.
