---
type: strategy
domain: business
area: growth
sources: [unwindvacations.com (live audit 2026-07-05), airbnb.com, vacasa.com, OwnerRez docs, vto-summary.md, owner-acquisition.md, one-year-plan.md]
last_updated: 2026-07-06
status: complete — build-ready (start at Section 9, Phase 0)
---

# Website Redesign Strategy — unwindvacations.com

A section-by-section, build-ready plan to fully redesign unwindvacations.com as a
dual-audience site (guests + property owners) on a $0 budget, keeping OwnerRez as
the booking engine.

## Changelog
- **2026-07-06 (build: Phase 1 ✅)** — Staging spikes run against unwind-vacations-1.hosted.ownerrez.com: R2 price native PASS, R2 rating → sitewide ★4.996/977-review band, R4 sticky bar PASS via header JS. Platform confirmed. v1 CSS bundle + header code shipped in `website-redesign-build-assets.md`. Cancellation-policy [CONFIRM] resolved from live data.
- **2026-07-06 (iter 9b)** — Coherence fix: removed a duplicate Section 3 that had survived at the end of the file from the interrupted iteration; merged its unique content (router principle, split-CTA rule, user-flow walkthroughs → §3.6) into the canonical Section 3. Canonical URLs are `/rentals` and top-level area slugs, matching Sections 6/9/10.
- **2026-07-06 (iter 9 — FINAL)** — Sections 9 (7-phase build sequence, 10–15 John-hours, Phase 0 = 15-item decision/baseline checklist, Phase 1 = R2/R4 staging spikes as the gate) and 10 (low-drama cutover via domain reassignment inside OwnerRez, Search Console SEO protection, 30/60/90 measurement plan) complete. Coherence pass done. **Doc is build-ready — execution starts at Section 9, Phase 0.**
- **2026-07-06 (iter 8)** — Sections 7 (mobile-first: 5 current leaks, per-page acceptance checklist, phone-testing ritual) and 8 (trust plan: layered guest/owner trust tables, review-capture flywheel, no-fake-urgency rule) complete.
- **2026-07-06 (iter 7)** — Section 6b complete: /property-management owner landing (proof bar, 3-column "difference" section, 6-field projection form, owner FAQ), /about story, /reviews approach, area-page template. Section 6 fully done.
- **2026-07-06 (iter 6)** — Section 6a (guest pages) complete: homepage, /rentals, property detail, /book-direct — wireframes + real draft copy in Unwind voice; [CONFIRM] flags for cancellation policy, rate-guarantee sweetener, years in business, fee-math example.
- **2026-07-06 (iter 5)** — Section 5 (design system) complete: coastal palette tokens, Fraunces+Inter type system, spacing/shape rules, paste-ready starter CSS for the OwnerRez CSS tab, Airbnb-anatomy card spec, $0 imagery rules.
- **2026-07-06 (iter 4)** — Section 4 (platform decision) complete: OwnerRez hosted site + CSS Magic + custom pages chosen at $0; WordPress kept as documented escape hatch; R1–R13 capability check with two early-spike risk items (R2 cards, R4 sticky bar); staging-safe setup steps. Also backfilled Section 3 body (a prior iteration logged it but the write was interrupted).
- **2026-07-05 (iter 3)** — Section 3 (IA + sitemap) complete: 5-item nav, full URL map for both audiences, dual-audience footer, homepage-as-router model.
- **2026-07-05 (iter 2)** — Section 2 (competitive teardown) complete: live audits of Vacasa homepage + Sea Star Realty (direct boutique comp in our own market), Airbnb pattern breakdown, steal/skip lists.
- **2026-07-05** — Doc created. Section 1 (goals + success metrics) complete. Outline + section tracker laid out.

## Section Tracker
| # | Section | Status |
|---|---------|--------|
| 1 | Goals, audiences & success metrics | ✅ Done |
| 2 | Competitive teardown (Airbnb, Vacasa, boutique) | ✅ Done |
| 3 | Information architecture + sitemap | ✅ Done |
| 4 | Platform decision (OwnerRez theme vs GoDaddy WP) | ✅ Done |
| 5 | Design system (palette, type, components) | ✅ Done |
| 6 | Page-by-page specs + copy + wireframes | ✅ Done (6a guest + 6b owner/shared) |
| 7 | Mobile-first requirements | ✅ Done |
| 8 | Trust / social-proof plan | ✅ Done |
| 9 | Step-by-step build sequence | ✅ Done |
| 10 | Launch + migration plan | ✅ Done |

---

## Section 1 — Goals, Audiences & Success Metrics

### The strategic problem
The current OwnerRez template site is *functional but flat*. It works as a catalog
of 54 properties but does two jobs poorly:
1. It doesn't convert **guests** into **direct bookings** (bypassing Airbnb/Vrbo's
   ~15% in host fees + the guest service fee), and
2. It barely speaks to **property owners** — the audience that actually drives the
   growth engine (VTO: 125 → 325 → 1000 units; owner-acquisition.md target is ~7 net
   new properties/month).

A single template can't serve a family looking for a beach week AND a condo owner
deciding who manages their $400k asset. This redesign splits those jobs cleanly.

### The two audiences

**Audience A — Guests (revenue today)**
- Who: families, couples, golf groups, girls' trips coming to the Grand Strand
  (Myrtle Beach, North Myrtle Beach, Little River, Murrells Inlet).
- Job-to-be-done: *"Find a place I'll love, trust it's legit, book it fast — ideally
  cheaper or better than Airbnb."*
- What they need: search-first experience, real prices + ratings on every card, a map,
  great photos, obvious trust signals, frictionless mobile booking.
- Why direct matters: every direct booking saves OTA fees and gives Unwind the guest
  relationship (email, rebooking, reviews).

**Audience B — Property Owners (growth engine)**
- Who: owners of 3BR+ condos/homes in core Grand Strand buildings; often reached via
  realtor referrals and Vintory outreach who then "check out the website."
- Job-to-be-done: *"Should I trust Unwind with my property? Will they make me more money
  than my current manager / than self-managing?"*
- What they need: a dedicated, credible "list your property" landing page — real proof
  (revenue, occupancy, reviews, local team), a clear pitch vs. Vacasa (boutique, local,
  not a faceless national brand), and one obvious CTA (book a call / get a free revenue
  estimate).
- Why it matters most: one owner signup can be worth $30k–$50k+/yr in managed revenue.
  The website is the *credibility backstop* for every other acquisition channel
  (realtors, Vintory, referrals) — those channels send prospects to the site to
  validate Unwind before signing.

### Positioning (the through-line for all copy)
> **Boutique, local, owner-obsessed.** Unwind is the Grand Strand specialist — not a
> national brand running your home from a call center three states away. Guests get a
> handpicked, well-run home; owners get a partner who treats their property like the
> asset it is.

This is the wedge against **both** north stars: warmer and more local than Vacasa,
more curated and trustworthy than a sea of Airbnb listings.

### Success metrics (how we'll know it worked)

**Guest side**
| Metric | Baseline (to capture) | Target (6–12 mo post-launch) |
|--------|----------------------|------------------------------|
| Direct bookings / mo | TBD from OwnerRez | +25–50% |
| Direct-booking revenue share | TBD | Move up meaningfully vs OTA |
| Site → booking conversion rate | TBD (GA4) | Beat template baseline |
| Bounce rate on homepage | TBD | Down (search-first hero) |
| Mobile booking completion | TBD | Up (mobile-first rebuild) |

**Owner side**
| Metric | Baseline | Target |
|--------|----------|--------|
| Owner-inquiry form fills / mo | TBD | Establish + grow |
| "Book a call" bookings from site | TBD | Establish + grow |
| Owner-page → inquiry conversion | TBD | Establish baseline first |

**Guardrail metric:** organic search rankings must **not** drop post-migration
(handled in Section 10 with redirects). The site currently ranks for local terms; a
botched cutover could cost bookings.

### Constraints (fixed inputs)
- **$0 out of pocket** — use only tools already paid for (OwnerRez subscription,
  GoDaddy hosting, Google Fonts, free stock/existing photography). John's time is the
  budget.
- **OwnerRez stays the booking engine** — calendar, payments, and the 54 listings must
  sync automatically. No re-keying inventory.
- **Keep the domain** unwindvacations.com (currently GoDaddy).
- **Build model:** Claude produces copy, design system, wireframes, specs, and HTML
  mockups; John publishes. John is a capable non-developer with dev learning goals.

### Open questions to resolve during the build
- Pull real baselines from OwnerRez (bookings/mo, direct vs OTA split) and GA4 (if
  installed) before launch, so targets above are grounded.
- Confirm whether GA4 / any analytics is currently on the site.
- Confirm current owner-inquiry path (form? phone? none?).

### Gaps remaining after this section
- Everything in sections 2–10. Next up: **Section 2 — Competitive teardown.**

---

## Section 2 — Competitive Teardown

Live audits done 2026-07-05: Vacasa homepage, Sea Star Realty (boutique, *same market
— Grand Strand*), plus Airbnb pattern analysis and the current unwindvacations.com.

### 2.1 Airbnb — what to steal / what to skip

Airbnb is the benchmark for **guest search UX**, not for a manager website. Steal
interaction patterns, skip the marketplace complexity.

**Steal:**
- **Search is the hero.** The entire above-the-fold experience is "Where / When / Who"
  → one big search action. Nothing competes with it.
- **Price + rating on every card.** No card ships without a nightly price and a star
  rating with review count. This is the #1 gap on Unwind's current cards.
- **Card anatomy** (copy this exactly): photo carousel (4:3, swipeable on mobile) →
  location/title line → key attribute line → price line ("$X night · $Y total") →
  star + review count, top-right. Optional badge top-left ("Guest favorite").
- **Sticky mobile booking bar** on property detail: price + dates + "Reserve" pinned
  to the bottom of the viewport at all times.
- **Filters as chips/modal**, not a form: tap "Filters" → modal with checkboxes,
  instant result-count feedback ("Show 23 homes").
- **Map/list toggle** on mobile; split map+list on desktop.

**Skip:**
- Category rows ("Amazing pools", "Beachfront") — needs thousands of listings to work;
  with 54 properties it looks thin. Use 3–4 curated collections instead.
- Wishlist/accounts, instant-book complexity, host-profile layers — OwnerRez handles
  booking; don't rebuild marketplace machinery.

### 2.2 Vacasa — what to steal / what to skip

**Observed live:** headline "Find a vacation rental" + seasonal subhead, search
immediately below; guest-first nav with management pitched further down; footer split
into FOR GUESTS / FOR HOMEOWNERS columns; owner case studies with hard numbers
("1,286 nights booked," "$623,155 rental revenue"); clean blue/white, heavy whitespace.

**Steal:**
- **One promise + search** above the fold. No carousel. (Their entire hero is a
  headline, a subhead, and a search box.)
- **Footer as the dual-audience map:** FOR GUESTS / FOR HOMEOWNERS link columns. This
  is the cheapest possible way to serve two audiences without cluttering the top nav.
- **Owner case studies with real numbers.** Specific beats general: "$623,155 rental
  revenue" converts owners better than "we maximize your income." Unwind has real
  numbers ($1.7M managed revenue, 50 properties, occupancy/ADR from OwnerRez) — use them.
- **Service bullets as trust:** "24/7 guest service · Professional cleaning" — short,
  concrete, scannable.
- **Whitespace discipline:** one idea per section, generous padding, max ~2 typefaces.

**Skip:**
- Corporate blandness — Vacasa reads like an airline site. Unwind's warmth and local
  face is the differentiator; keep the structure, not the personality.
- National-scale destination grid (632 rentals in 30A). At 54 properties, lead with
  **areas** (N. Myrtle, Myrtle, Murrells Inlet, Little River) instead.
- **Their weakness is our pitch:** Vacasa's owner reputation is "call-center
  management." The owner page should position Unwind explicitly against that (without
  naming them): *"Your property gets a local team, not a ticket queue."*

### 2.3 Sea Star Realty — the boutique comp in our own market

**Observed live:** video hero with two CTAs; deep nav nesting (by type/area/amenity);
"Why Book with Us" section that names Airbnb/Vrbo fees; Best Price Guarantee as lead
value prop; cards show name/beds/baths/sleeps + location descriptor ("Walk to Beach,"
"Second Row") but **no prices**; ratings on only some cards; "thousands of five-star
reviews" asserted but not linked; owner pitch buried under a quiet "Owners" nav item
with a "Free Rental Projection" CTA.

**Steal:**
- **"Book direct, skip the fees" messaging** — explicitly comparing to Airbnb/Vrbo is
  standard practice in our market; guests respond to it. Pair with a Best Price
  Guarantee (costs nothing — direct is already cheaper than OTA + guest fee).
- **Location descriptors on cards:** "Oceanfront," "Walk to Beach," "2nd Row" — Grand
  Strand guests think in these terms. Unwind's amenity data already supports this.
- **"Free Rental Projection" as the owner CTA.** Concrete and low-commitment — much
  stronger than "Contact us." Unwind can fulfill this with OwnerRez + Beyond Pricing
  comps in under a day.

**Skip / beat them on:**
- **No prices on cards** — their gap, our opening. Show real nightly rates.
- **Unverifiable review claims** — they assert "thousands of five-star reviews" with no
  link. Unwind should show *actual* review excerpts with property names, pulled from
  OwnerRez, linked to the property.
- **Video hero** — heavy, slow on mobile, and pushes search down. One fast image wins.
- **Nav overload** — their mega-menu nests everything. Keep Unwind's nav to ~5 items.
- **Owner pitch buried** — "Owners" as a quiet nav item wastes the growth engine. Unwind
  puts "Property Management" in the top nav AND an owner section on the homepage.

### 2.4 Pattern summary → design requirements

| Pattern | Source | Requirement for Unwind |
|---|---|---|
| Search-first hero, one promise, no carousel | Vacasa | R1: Hero = 1 image + headline + search bar |
| Price + rating on every card | Airbnb | R2: Cards show $/night + ★ + review count |
| Card anatomy (photo → title → attrs → price → rating) | Airbnb | R3: Adopt exact card structure |
| Sticky mobile booking bar | Airbnb | R4: On property detail pages |
| Filter modal with live result count | Airbnb | R5: Filters as chips/modal, not a form |
| Map + list view | Airbnb | R6: Map toggle (OwnerRez supports map widget) |
| FOR GUESTS / FOR HOMEOWNERS footer | Vacasa | R7: Dual-audience footer columns |
| Owner case study with hard numbers | Vacasa | R8: Real Unwind numbers on owner page |
| "Book direct, skip OTA fees" + price guarantee | Sea Star | R9: Why-book-direct strip on homepage |
| Location descriptors (Oceanfront, Walk to Beach) | Sea Star | R10: Badge on cards where applicable |
| "Free Rental Projection" owner CTA | Sea Star | R11: Primary owner CTA sitewide |
| Local-team-not-call-center positioning | anti-Vacasa | R12: Core owner-page messaging |
| Verifiable reviews (excerpts + property links) | anti-SeaStar | R13: Named review excerpts, not claims |

These R-numbers get referenced in Sections 3, 6, and 9 so every page spec traces back
to an observed, working pattern.

### Gaps remaining after Section 2
- Kozy Getaways (second boutique comp) not audited — optional; Sea Star covers the
  boutique/local archetype in-market. Revisit only if owner-page inspiration runs thin.

---

## Section 3 — Information Architecture + Sitemap

### 3.1 The core IA move
The current site has a **10-item nav** (Home, About, Properties, Map, Property
Management, Reviews, Activities, Owner Portal, Contact, Privacy Policy) where guests
and owners fight for attention. The redesign collapses to **5 items** and lets the
homepage act as a **router**: guests hit search immediately (R1); owners get a clearly
labeled lane that leads to one destination page.

### 3.2 Top navigation (5 items + CTA)
```
[Unwind logo]   Find a Rental   Areas   Property Management   About   ☎ (843) xxx-xxxx   [Book Direct & Save →]
```
- **Find a Rental** → /rentals (search + map; the Map page merges in here, R6)
- **Areas** → dropdown of the 4 markets (also reachable from homepage collections)
- **Property Management** → /property-management (the owner lane — top-level, never
  buried; this beats Sea Star's quiet "Owners" link)
- **About** → /about (the local-story trust page)
- **[Book Direct & Save]** button → /rentals (guest CTA, styled as the primary button)
- Reviews, Contact, Owner Portal, Activities, Privacy move to the **footer** (see 3.4).
  Reviews also get surfaced *inline* on every page (R13) instead of living only on a
  destination page.
- Mobile: logo + hamburger + a persistent **Search** icon. The hamburger opens a
  full-screen menu with the same 5 items, owner lane clearly separated at the bottom
  ("Own a rental property? →").

### 3.3 Sitemap / URL map
**Guest path (booking funnel):**
| URL | Page | Role |
|---|---|---|
| `/` | Homepage | Router: search hero (R1), why-book-direct strip (R9), area collections, owner strip, reviews strip |
| `/rentals` | Search + results | Cards w/ price+rating (R2/R3), filter modal (R5), map toggle (R6) |
| `/rentals/{property-slug}` | Property detail | Gallery, price, reviews, sticky mobile book bar (R4) |
| `/north-myrtle-beach`, `/myrtle-beach`, `/murrells-inlet`, `/little-river` | Area pages | Curated collection + area guide; local-SEO workhorses |
| `/book-direct` | Why book direct | The fee math vs Airbnb/Vrbo, Best Price Guarantee (R9) |
| `/things-to-do` | Guest guide | Migrate live Activities page as-is (renamed 2026-07-13); new CSS restyles it |
| `/reviews` | All reviews | Aggregated, filterable by property (R13) |

**Owner path (acquisition funnel):**
| URL | Page | Role |
|---|---|---|
| `/property-management` | Owner landing | The conversion page: local-team positioning (R12), real numbers (R8), FAQ |
| `/property-management/free-rental-projection` | Projection form | Primary CTA target (R11): address + beds + contact → John replies with OwnerRez/Beyond comps |
| `/property-management/thank-you` | Confirmation | Conversion-tracking event fires here |

**Shared/utility:** `/about`, `/contact`, `/owner-portal` (login link out to OwnerRez
portal), `/privacy-policy`.

### 3.4 Footer (the dual-audience map, R7)
Four columns, Vacasa-style:
- **FOR GUESTS:** Find a Rental · Book Direct & Save · Areas (4 links) · Activities · Reviews · Contact
- **FOR HOMEOWNERS:** Property Management · Free Rental Projection · Owner Portal · Owner FAQ
- **COMPANY:** About · Our Story · Contact · Privacy
- **CONTACT:** phone (tap-to-call), email, Facebook/Instagram, "Local office — Grand Strand, SC"

### 3.5 Cross-linking rules (so each audience finds its lane)
- Every **guest** page carries exactly ONE owner touchpoint (a slim strip near the
  footer: "Own a property on the Grand Strand? Get a free rental projection →").
  Never more — guests shouldn't feel sold to.
- Every **owner** page carries exactly ONE guest touchpoint (nav + "see how we present
  your home to guests → /rentals"). The owner lane otherwise stays distraction-free.
- Homepage order: search hero → book-direct strip → area collections → featured
  homes → reviews strip → owner strip → footer. Guests get everything first;
  the owner strip sits just above the footer where owner-intent visitors scroll to.
- **No page serves both audiences in its body copy.** Shared pages (About, Reviews)
  end with a split CTA block: "Book your stay" | "List your property." Owners get
  three doors — nav item, homepage strip, footer column — all to `/property-management`.

### 3.6 User-flow walkthroughs (acceptance test for the IA)
- **Guest, mobile, from Instagram:** lands on `/` → search above the fold → dates +
  guests → `/rentals` filtered → card shows $/night + ★ → property page → sticky Book
  bar → OwnerRez checkout. *Zero owner content en route.*
- **Owner, from a Vintory email or realtor referral:** lands on `/property-management`
  directly (that's the link every campaign uses) → local pitch + real numbers + named
  testimonials → projection form → `/thank-you`. *Zero guest content en route.*
- **Owner, organic, lands on homepage:** sees "Property Management" in the nav within
  1 second, or scrolls to the owner strip. Two clicks max to the form.
- **Guest comparison-shopping vs Airbnb:** homepage strip → `/book-direct` → sees the
  fee math → books direct.

---

## Section 4 — Platform Decision

### 4.1 The decision
**Build on the OwnerRez hosted website (Option A), pushed hard with CSS Magic,
custom header code, and custom pages.** WordPress (Option B) is documented below as
the escape hatch if we hit the design ceiling.

### 4.2 Why (at $0, for this builder, with this engine)
| Criterion | A: OwnerRez hosted + CSS/custom pages | B: GoDaddy WP + OwnerRez plugin |
|---|---|---|
| True cost | ✅ $0 — included in the OwnerRez subscription | ⚠️ $0 **only if** John's GoDaddy plan includes WordPress hosting — unconfirmed; likely a new hosting/plan cost |
| Listings/calendar/payments | ✅ Native — 54 properties, rates, reviews, booking all sync automatically | ⚠️ Via plugin widgets/shortcodes — works, but widget markup is less flexible than native pages |
| Search + map + filters | ✅ Built in (already live today) | ⚠️ Widget-based; map/filter UX is more limited inside WP |
| Design freedom | ⚠️ Bounded — restyle via CSS Magic + custom code injection + fully custom pages; header has per-device templates. Can't rewrite core listing-page markup | ✅ Unlimited on non-booking pages |
| Maintenance/security | ✅ Zero — OwnerRez hosts, SSL, updates | ❌ WP updates, plugins, backups, security = ongoing John-time |
| John publishes | ✅ One UI he already knows (OwnerRez settings) | ❌ Second CMS to learn + maintain |
| SEO migration risk | ✅ Minimal — same platform, URLs mostly stable | ❌ Full URL migration + redirects |
| Speed to launch | ✅ Weeks | ❌ Months |

The deciding facts: OwnerRez hosted sites accept **custom CSS snippets** (Theme &
Layout → CSS tab), **custom code in the site header**, **fully custom pages**
(perfect for /property-management, /book-direct, area pages), and **per-device
header/menu templates** ([CSS Magic](https://www.ownerrez.com/support/articles/hosted-website-css-magic),
[custom code](https://www.ownerrez.com/support/articles/how-to-add-custom-code),
[custom pages](https://www.ownerrez.com/support/articles/custom-page),
[headers & menus](https://www.ownerrez.com/support/articles/hosted-websites-editing-headers-and-menus)).
That covers ~90% of R1–R13 without taking on WordPress's maintenance tax or an
unconfirmed hosting cost.

### 4.3 Capability check against the R-requirements
| Req | Achievable on OwnerRez hosted? | How |
|---|---|---|
| R1 search-first hero | ✅ | Home page settings + hero image + search widget placement; CSS to kill carousel & style |
| R2/R3 price+rating cards | ⚠️ Mostly | OwnerRez search results support rates & reviews display; exact Airbnb card anatomy approximated via CSS Magic, not full markup control |
| R4 sticky mobile book bar | ⚠️ Partial | Property pages have a booking widget; stickiness via custom CSS/JS in header injection — test early (build step 1 risk item) |
| R5 filter modal | ⚠️ Partial | Native filters restyled via CSS; a true modal may not be possible — acceptable degradation |
| R6 map | ✅ | Native map widget/page |
| R7 dual footer | ✅ | Footer customization |
| R8/R11/R12 owner landing + projection CTA | ✅ | Custom pages + OwnerRez inquiry form (or embedded form) |
| R9 book-direct strip/page | ✅ | Custom page + homepage section |
| R10 location badges | ⚠️ Partial | Via property tags/amenity display; CSS styling |
| R13 review excerpts everywhere | ✅ | Native review widgets on pages; excerpts on custom pages |

**Early spike (do first in Section 9's build sequence):** verify R2 (price+rating on
cards) and R4 (sticky bar) on a staging hosted site before committing polish time. If
BOTH fail badly, revisit Option B.

### 4.4 Setup steps (staging-safe)
1. OwnerRez → **Settings → Hosted Websites** → create a **second** website (keeps the
   live site untouched) on a free `*.ownerreservations.com` staging subdomain.
2. **Theme & Layout → CSS tab** — this is where all Claude-produced CSS lands.
3. **Header** — pick the cleanest header template per device (desktop/tablet/phone);
   apply the 5-item nav from §3.2.
4. **Pages** — create custom pages: /property-management, /free-rental-projection,
   /book-direct, /about, 4 area pages. Claude supplies HTML blocks; John pastes.
5. **Home page settings** — single hero image + search widget; disable carousel.
6. Configure footer columns (§3.4), theming (Settings → Branding & Legal → Theming:
   logo, colors, phone).
7. Iterate on staging until Section 6 specs are met → then domain cutover (§10).

### 4.5 Escape hatch (Option B, documented for later)
If the hosted-site ceiling blocks R2/R4 *and* direct-booking growth justifies it:
GoDaddy WP (confirm hosting cost first) + [OwnerRez WordPress plugin](https://www.ownerrez.com/support/articles/wordpress-plugin)
for property widgets, keeping all Section 5–6 design assets (they port 1:1).

### Open question for John (Section 4)
- Does the current GoDaddy plan include WordPress hosting (matters only for the
  escape hatch)? Not a blocker for Option A.

### Gaps remaining after Section 4
- (resolved — Section 5 below)

---

## Section 5 — Design System

Everything here is deliberately **CSS-first** because the whole system ships through
OwnerRez's Theme & Layout → CSS tab plus custom-page HTML. No build tools, no
frameworks. Vacasa gives us the discipline (few colors, lots of air); the boutique
warmth comes from a serif display face and sand/coral tones Vacasa would never use.

### 5.1 Palette (coastal, warm, boutique — NOT corporate blue)
| Token | Hex | Use |
|---|---|---|
| `--uw-navy` | `#123B4F` | Headings, footer bg, primary text on light |
| `--uw-teal` | `#0E7C86` | Links, secondary buttons, active filter chips |
| `--uw-coral` | `#E76F51` | THE action color: Book/Reserve/Get Projection CTAs only |
| `--uw-coral-dark` | `#D45A3D` | CTA hover |
| `--uw-sand` | `#F6F1E7` | Alternating section backgrounds (replaces gray) |
| `--uw-white` | `#FFFFFF` | Cards, page bg |
| `--uw-ink` | `#1F2937` | Body text |
| `--uw-gray` | `#6B7280` | Secondary text (beds/baths line, captions) |
| `--uw-line` | `#E5E7EB` | Borders, dividers |
| `--uw-gold` | `#E8A33D` | Review stars only |

Rule: **coral appears exactly once per viewport** — it's reserved for the one action
we want. If everything is coral, nothing is.

### 5.2 Typography (2 Google Fonts, both free)
- **Headings: Fraunces** (serif, warm, a little beachy-editorial — instantly
  de-corporates the template). Weights 600/700.
- **Body & UI: Inter.** Weights 400/500/600. Cards, buttons, nav, forms.
- Load via one `<link>` in the site header (custom code injection):
  `https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Inter:wght@400;500;600&display=swap`

Type scale (desktop / mobile):
| Element | Size | Notes |
|---|---|---|
| H1 (hero) | 44px / 32px, Fraunces 700 | One per page |
| H2 (section) | 32px / 26px, Fraunces 600 | |
| H3 (card title) | 18px, Inter 600 | |
| Body | 16px, Inter 400, line-height 1.6 | Never below 16px on mobile (form zoom!) |
| Caption/attrs | 14px, Inter 400, `--uw-gray` | |
| Price line | 16px, Inter 600, `--uw-ink` | "$285 night" |

### 5.3 Spacing & shape
- Base unit **4px**; common steps 8/12/16/24/32/48/64/96.
- Section vertical padding: 96px desktop / 48px mobile; alternate `--uw-white` and
  `--uw-sand` backgrounds so the page reads in calm bands (Vacasa trick).
- Cards: radius **12px**, border `1px solid --uw-line`, shadow only on hover
  (`0 4px 16px rgba(18,59,79,.10)`), photo aspect ratio **4:3**.
- Buttons: radius **8px**, padding 14px 24px, Inter 600 16px. Primary = coral;
  Secondary = white bg, `--uw-teal` border+text; Ghost = navy text + underline.
- Tap targets ≥ 44px; content max-width 1200px, gutter 24px/16px.

### 5.4 Core CSS (paste-ready starter for the OwnerRez CSS tab)
```css
:root{
  --uw-navy:#123B4F; --uw-teal:#0E7C86; --uw-coral:#E76F51; --uw-coral-dark:#D45A3D;
  --uw-sand:#F6F1E7; --uw-ink:#1F2937; --uw-gray:#6B7280; --uw-line:#E5E7EB; --uw-gold:#E8A33D;
}
body{font-family:'Inter',system-ui,sans-serif;color:var(--uw-ink);font-size:16px;line-height:1.6}
h1,h2{font-family:'Fraunces',Georgia,serif;color:var(--uw-navy)}
h1{font-size:44px;line-height:1.15}h2{font-size:32px}
@media(max-width:767px){h1{font-size:32px}h2{font-size:26px}}
.uw-btn-primary{background:var(--uw-coral);color:#fff;border-radius:8px;padding:14px 24px;
  font-weight:600;border:0;display:inline-block;text-decoration:none}
.uw-btn-primary:hover{background:var(--uw-coral-dark)}
.uw-btn-secondary{background:#fff;color:var(--uw-teal);border:1.5px solid var(--uw-teal);
  border-radius:8px;padding:13px 24px;font-weight:600;display:inline-block;text-decoration:none}
.uw-section-sand{background:var(--uw-sand)}
.uw-card{background:#fff;border:1px solid var(--uw-line);border-radius:12px;overflow:hidden;
  transition:box-shadow .15s}
.uw-card:hover{box-shadow:0 4px 16px rgba(18,59,79,.10)}
.uw-badge{display:inline-block;background:var(--uw-sand);color:var(--uw-navy);
  border-radius:999px;padding:4px 12px;font-size:13px;font-weight:500}
.uw-stars{color:var(--uw-gold);font-size:14px}
```
(Selectors for OwnerRez's own widgets — search results, booking widget — get captured
during the Section 9 spike with browser dev tools, then restyled to match `.uw-card`.)

### 5.5 Property card spec (R2/R3, the Airbnb anatomy)
```
┌────────────────────────┐
│ photo 4:3   [Oceanfront]│  ← badge top-left (R10); dots/swipe if gallery
├────────────────────────┤
│ Sea Glass Cottage      ★ 4.9 (38)   ← title 18px + gold stars top-right
│ North Myrtle Beach · Sleeps 8 · 3 BR · 2 BA   ← 14px gray
│ $285 night                           ← 16px semibold
└────────────────────────┘
```
Grid: 3-up desktop / 2-up tablet / 1-up mobile, 24px gaps.

### 5.6 Imagery rules ($0 budget)
- Use **real Unwind property photos only** — no stock. Boutique = real.
- Hero: one wide, bright, uncluttered beach/porch shot; text overlaid on a
  `rgba(18,59,79,.35)` navy scrim for contrast.
- Owner page: photos of the actual team + real properties (anti-call-center proof, R12).
- Compress everything ≤ 300KB (free: squoosh.app) before upload — template sites die
  by 4MB photos.

### Gaps remaining after Section 5
- OwnerRez widget selector names unknown until the staging spike (Section 9, step 1).

---

## Section 6 — Page-by-Page Specs + Copy

Copy rules: Unwind voice = boutique, coastal, carefree, plain-spoken. Short sentences.
No "nestled," no "hidden gem," no exclamation points. Facts only — anything marked
`[CONFIRM]` needs John's sign-off before publishing. Sub-part **6a = guest pages**
(this iteration); **6b = owner pages + about/reviews** (next).

### 6.1 Homepage `/` (R1, R9)

**Wireframe (top → bottom):**
1. **Hero** — full-width photo (bright beach/porch shot, navy scrim). H1 + subhead +
   search widget ON the image. No carousel. Nothing else above the fold.
2. **Book-direct strip** (sand bg) — 3 icons + one line each.
3. **Browse by area** — 4 photo cards (N. Myrtle, Myrtle, Murrells Inlet, Little River).
4. **Featured homes** — 6 property cards (R2/R3 anatomy), "See all 54 homes →".
5. **Reviews strip** — 3 real review excerpts w/ property names (R13).
6. **Owner strip** (navy bg, the ONE owner touchpoint) — headline + projection CTA.
7. Footer (R7).

**Copy:**
- H1: `Your week at the beach starts here.`
- Subhead: `54 handpicked vacation homes across the Grand Strand — cared for by a local team that actually lives here.`
- Search labels: `Where · Check-in · Check-out · Guests` → button: `Search homes`
- Book-direct strip: **Best rate, guaranteed** — `Booking direct always beats the Airbnb price. Same home, no service fees.` · **A real local team** — `Our office is on the Grand Strand. Text us — a person answers.` · **Handpicked homes** — `We manage every home we list. No surprises at check-in.`
- Area section H2: `Where do you want to unwind?`
- Featured H2: `Homes guests come back to`
- Reviews H2: `Don't take our word for it`
- Owner strip H2: `Own a rental on the Grand Strand?` Body: `See what your property could earn with a local team on your side. Free, no-pressure projection — real numbers from real bookings.` CTA: `Get my free rental projection`

### 6.2 Search / results `/rentals` (R2, R3, R5, R6)

**Wireframe:** slim search bar pinned at top (dates/guests editable inline) → filter
chips row (`Oceanfront · Private pool · Hot tub · Pets · Game room · More filters`) →
result count (`23 homes for your dates`) → card grid 3/2/1-up → map toggle button
(desktop: split list+map if the widget allows; mobile: full-screen map toggle, R6).
Sort: Featured / Price / Bedrooms.

**Card spec:** per §5.5 — badge (R10: `Oceanfront`, `Walk to beach`, `2nd row`),
title, ★ + review count, area · sleeps · BR · BA, `$X night`. **Prices and ratings
ON, always** — this beats every boutique competitor in market (Sea Star shows none).

**Empty state:** `No homes match those filters for your dates. Try dropping a filter — or text us at [PHONE] and we'll find you something close.`

### 6.3 Property detail `/rentals/{slug}` (R4, R13)

**Wireframe:** gallery (grid hero: 1 large + 4 thumbs, "See all photos") → title row
(H1 name, ★ 4.9 (38 reviews) anchor-linked to reviews, area badge) → attribute line →
**booking widget right rail** (desktop) with nightly rate, date picker, total incl.
fees before any click, `Book direct — best rate` button → description → amenity grid →
reviews (all, newest first, R13) → map → "similar homes" 3 cards → **mobile: sticky
bottom bar** (R4): `$285 night · ★4.9` + `Check availability` button.

**Copy patterns:** rewrite property descriptions to lead with the *experience*, not
the spec sheet: first line = the one thing you'd text a friend (`The porch faces the
ocean, and the coffee pot is 10 feet away.`). Keep OwnerRez's structured amenity data
for the grid. Booking reassurance under button: `Free cancellation for 48 hours [CONFIRM policy] · No booking fees · Local support, 7 days a week`.

### 6.4 Book direct `/book-direct` (R9)

**Wireframe:** H1 → fee-math table → guarantee block → 3 FAQ items → CTA to /rentals.

**Copy:**
- H1: `Same home. Better price. That's booking direct.`
- Intro: `Every home on this site is also on Airbnb and Vrbo — but those platforms add a service fee on top of your rent. Book here and it disappears.`
- Fee-math table (illustrative, `[CONFIRM real example from OwnerRez]`):
  | | Airbnb | Direct with Unwind |
  |---|---|---|
  | 4 nights at $285 | $1,140 | $1,140 |
  | Guest service fee | ~$160 | $0 |
  | **You pay** | **~$1,300** | **$1,140** |
- Guarantee: `**Our Best Rate Guarantee.** Find the same home, same dates cheaper on another site and we'll match it — then take another 5% off. [CONFIRM John approves the 5%]`
- FAQs: is it secure (yes — same payment processing, real local company, [X] years on the Grand Strand `[CONFIRM years]`) · what if plans change (cancellation policy) · who do I call (a real person at our local office — number).

### Gaps remaining after 6a
- `[CONFIRM]` items: cancellation window, best-rate-guarantee sweetener, years in
  business, real fee-math example.

### 6.5 Owner landing `/property-management` (R8, R11, R12) — THE growth page

**Audience mindset:** an owner comparing Unwind vs a national brand (Vacasa-type) vs
their current manager vs self-managing. They arrive from a realtor referral, Vintory
outreach, or a Google search — the page's job is to make the **free rental projection**
feel like the obvious, zero-risk next step.

**Wireframe (top → bottom):**
1. **Hero** (photo: real team member at a real property, not stock): H1 + subhead +
   coral CTA + phone number.
2. **Proof bar** — 4 stats in a row (R8).
3. **"The difference" section** — 3 columns: national brand vs self-managing vs Unwind (R12).
4. **What we handle** — 6-item grid (pricing, marketing, guest messaging 7 days/wk,
   cleaning & inspections, maintenance coordination, owner portal & monthly statements).
5. **How switching works** — 3 steps (`Tell us about your property → Get your projection → We handle the switch, usually inside 30 days [CONFIRM]`).
6. **Owner testimonial(s)** — 1–2 real quotes `[CONFIRM which owners will go on record]`.
7. **Projection form** (see below) + "prefer to talk?" phone/text line.
8. **Owner FAQ** — fees `[CONFIRM whether % is published]`, contract length, owner
   stays/blocking dates, onboarding time, how payouts work.

**Copy:**
- H1: `Your beach property deserves better than a call center.`
- Subhead: `Unwind manages 50+ vacation homes across the Grand Strand — with a local team you can meet for coffee, not a ticket queue. See what your property could really earn.`
- CTA: `Get my free rental projection`
- Proof bar **(DECIDED 2026-07-14, John):** `Locally owned & operated` · `Airbnb SuperHost` · `★ 4.9 · 950+ reviews` · `Data-driven results` — NO revenue number published; "realtor-referred since day one" woven into copy. Fee % NOT published (discuss on call). Onboarding promise: **within 7 days**. 24/7 guest support published sitewide. Full page HTML shipped in build-assets Block 5.
- "The difference" framing: **The big brands** — `Your home is a unit number. Guest problems route through a national call center.` **Going it alone** — `Weekend texts, pricing guesswork, cleaner no-shows — a second job you didn't ask for.` **Unwind** — `A boutique local team, professional pricing tools, and a manager who's seen your actual living room.`
- Anti-big-brand line (use once, no naming): `We're not trying to manage 40,000 homes. We're trying to be the best manager on the Grand Strand.`

**Projection form `/property-management/free-rental-projection` (R11):**
Fields (keep to 6 — every extra field costs conversions): Name · Email · Phone ·
Property address (or building/complex name) · Bedrooms · Anything we should know
(optional textarea). Button: `Send me my projection`. Under-button reassurance:
`Real numbers from comparable homes we already manage — in your inbox within one business day. No spam, no pressure, no obligation.`
→ Fulfillment: John/team builds the projection from OwnerRez comps + Beyond Pricing.
→ Submit lands on `/property-management/thank-you` (conversion event, §10).

### 6.6 About `/about`

**DECISION 2026-07-13 (John):** keep the EXISTING live about page as the base — its
structure (local-roots story → 5 values → differentiators → CTA) and "we live where
we work" positioning are strong. Migrate via `<>` source-copy from the live site's
page editor, then make three surgical upgrades: (1) team section with real names,
roles, photos `[CONFIRM who appears]`; (2) replace placeholder testimonials with 2–3
real guest reviews; (3) end with the split CTA ("Book your stay" | "List your
property"). Draft copy below stays available as backup/remix material.

**Also decided:** live **Activities page migrates as-is** (it's excellent — filters,
maps links, "New for 2026") → renamed **"Things To Do"**, slug `/things-to-do`;
Phase 5 area pages will cross-link into its sections. **Owner Portal** becomes a
direct footer/menu link to secure.ownerrez.com/login — no page.

**Original wireframe (superseded, kept for reference):** H1 + founding story (3 short
paragraphs) → team photo grid with names & roles → values strip (2–3 EOS core values,
plain-English) → dual CTA (find a rental / own a property).

**Story copy (draft, `[CONFIRM details]`):** `Unwind started with a simple frustration: beach property owners deserved better than being unit #4,000 at a national chain, and guests deserved homes that actually looked like the photos. Today we manage 50+ properties across the Grand Strand — still local, still picking up the phone. We live here. We check on your home after storms. We know which buildings have elevator quirks and where guests should get shrimp on a Tuesday. That's the whole model: stay boutique, stay local, sweat the details.`

### 6.7 Reviews `/reviews` (R13)

Aggregated review stream (OwnerRez review widget), filterable by property; header
shows sitewide average + total count, auto-updated. H1: `What guests say when we're
not in the room.` Each review links to its property page. No hand-picked-only wall —
volume + recency is the trust signal (beats Sea Star's unverifiable "thousands of
five-star reviews" claim).

### 6.8 Area page template (`/north-myrtle-beach` etc.)

H1 pattern: `North Myrtle Beach vacation rentals` → 2-paragraph area intro (who it's
for, what it's near — written for humans, does double duty for local SEO) → live
property grid filtered to that area → 3 "know before you go" tips → cross-links to
other areas. Claude drafts all 4 intros in the build phase.

### Gaps remaining after Section 6 (complete)
- All `[CONFIRM]` items compiled in Section 9's pre-build checklist.

---

## Section 7 — Mobile-First Requirements

Assume **65–75% of guest traffic is mobile** (typical for STR direct sites; verify
with GA4 once installed, §10). Every design decision gets checked on a phone first.

### 7.1 The current template's mobile leaks (worst first)
1. **Carousel hero + search below the fold** — on a phone, guests see a slow photo
   slider and must scroll to search. Fix: hero image + search visible in the first
   viewport (R1).
2. **Heavy images** — template sites routinely ship multi-MB photos; on cellular this
   is 5–10s of white screen. Fix: every uploaded image ≤300KB (§5.6).
3. **No sticky booking action** on property pages — guest scrolls a long page, the
   Book button is gone. Fix: sticky bottom bar (R4).
4. **Desktop-sized tap targets and text** — nav links and filter controls too small;
   sub-16px inputs trigger iOS auto-zoom. Fix: ≥44px targets, ≥16px inputs (§5.3).
5. **No tap-to-call** — phone number as plain text. Fix: every phone mention is
   `tel:` linked; mobile nav shows a call icon.

### 7.2 Mobile requirements checklist (acceptance criteria for every page)
- [ ] First viewport contains: brand, H1 promise, and the primary action (search or CTA)
- [ ] Search widget usable with thumbs — date picker and guest stepper full-width
- [ ] Cards 1-up, full-width, swipeable photos; price + rating visible without tapping
- [ ] Property page: sticky bottom bar with price + `Check availability` (R4 spike)
- [ ] Filter UI opens as full-screen sheet, applies with one tap, shows result count
- [ ] Map view: full-screen toggle with pin prices if the widget supports it (R6)
- [ ] Owner page: projection form fields stack 1-per-row; submit button full-width
- [ ] All `tel:` + `sms:` links live; footer has tap-to-call and tap-to-text buttons
- [ ] Test matrix: iPhone Safari + Android Chrome, on cellular, before every publish
- [ ] PageSpeed Insights (free) mobile score ≥80 at launch; re-test monthly

### 7.3 Testing ritual (build phase)
After each publish John loads the staging site on his own phone + one kid's Android
(free device lab). 30-second test: *can you find a house, see its price, and start
booking within 3 taps from the homepage?* If no → that iteration isn't done.

---

## Section 8 — Trust & Social-Proof Plan

Trust is the whole ballgame for a direct-booking site: guests must trust an
unfamiliar website with $1,500, and owners must trust it with a $400k asset.

### 8.1 Guest-side trust (layered, per page)
| Layer | Where | What |
|---|---|---|
| Reviews (R13) | Every property card, property page, homepage strip, /reviews | Real OwnerRez-synced reviews, counts + excerpts; never hand-picked-only |
| Price honesty | Booking widget | Total incl. fees shown BEFORE checkout starts — the anti-OTA move |
| Real humans | Sitewide footer + contact | Team names/photo, local office line, `Text us: [number]` |
| Response signal | Contact + property pages | `We answer 7 days a week, [X]am–[X]pm [CONFIRM hours]` — publish it, then beat it |
| Secure booking | Checkout vicinity | `Secure checkout · Powered by OwnerRez` + card logos |
| Policy clarity | Property page + /book-direct | Cancellation window in plain English, one sentence |

### 8.2 Owner-side trust
- Proof bar numbers (§6.5) — real, current, `[CONFIRM]` before publish.
- 1–2 named owner testimonials with property type (`— Susan, 3BR oceanfront, Windy Hill`); ask the 2–3 happiest owners this month `[JOHN ACTION]`.
- "How switching works" removes the fear of a messy transition (§6.5).
- The projection promise (`in your inbox within one business day`) is itself a trust
  test — it demonstrates response speed before any contract. Never miss it.
- Realtor-referral heritage line on /about: local pros already trust us with their
  clients.

### 8.3 The review-capture flywheel (feeds the whole plan)
1. Post-stay email (OwnerRez trigger) asks for the review — already standard; verify
   it's on for direct bookings, not just OTA stays.
2. Reviews sync to the site automatically (OwnerRez review widget) → every new stay
   compounds the site's trust.
3. Quarterly: pull the 3 best new quotes into homepage strip + owner page.
4. Respond publicly to any ≤3★ review within 48h — the response is read by 100×
   more future guests than the review itself.

### 8.4 What we will NOT do
No fake urgency ("3 people are looking at this home!"), no stock-photo "guests," no
unverifiable superlatives. Boutique trust = verifiable specifics, stated calmly.

---

## Section 9 — Step-by-Step Build Sequence

Rule of the build: **Claude produces, John clicks.** Each task names its owner.
Estimated total John-time: **10–15 hours spread over 3–4 weeks.** Nothing here blocks
daily operations; the live site stays untouched until Phase 7 cutover.

### Phase 0 — Decisions & baselines (John, ~2 hrs, do once)
The compiled `[CONFIRM]` / `[JOHN ACTION]` list from Sections 6–8:
1. [ ] Cancellation window in plain English (§6.3, §8.1)
2. [ ] Approve/adjust Best Rate Guarantee + "extra 5% off" sweetener (§6.4)
3. [ ] Years in business for /book-direct and /about (§6.4, §6.6)
4. [ ] One real fee-math example from OwnerRez (a recent booking's OTA vs direct price) (§6.4)
5. [ ] Which proof-bar numbers go public: 50+ homes / $1.7M+ bookings / ★4.8+ (§6.5)
6. [ ] "Onboarding inside 30 days" claim — true? (§6.5)
7. [ ] Ask 2–3 happiest owners for an on-record testimonial (§6.5, §8.2)
8. [ ] Publish management fee % on owner FAQ — yes/no (§6.5)
9. [ ] About-page story details + who appears in team photos (§6.6)
10. [ ] Response hours to publish (`7 days a week, Xam–Xpm`) (§8.1)
11. [ ] Is GA4 (or any analytics) on the current site? If yes, export 90-day baseline; if no, note it — we install in Phase 6 (§1, §10)
12. [ ] Pull direct-vs-OTA booking baseline from OwnerRez (Claude can do this via the OwnerRez MCP) (§1)
13. [ ] Check whether the GoDaddy plan includes WordPress hosting (escape hatch info only) (§4)
14. [ ] Verify post-stay review emails fire for DIRECT bookings in OwnerRez (§8.3)
15. [ ] Collect best 20–30 property/team photos into a folder; compress at squoosh.app (§5.6)

### Phase 1 — Staging site + the two spikes ✅ PASSED 2026-07-06
- [x] John: staging site created → `https://unwind-vacations-1.hosted.ownerrez.com/`
- [x] Claude: markup inspected, selectors captured (Bootstrap-based; `.thumbnail`,
  `.media-object`, `h2/h3.media-heading`, `.amenity-summary-*`, `.btn-default`,
  `.ownerrez-widget[data-widget-type]`)
- [x] **R2 price: PASS natively** — cards already render `$524/night` in `h3.media-heading`
- [x] **R2 rating: partial→better** — no per-card stars in markup, but site JSON-LD
  exposes **★4.996 / 977 reviews** sitewide → use a rating band above the grid instead
- [x] **R4 sticky bar: PASS** — booking widget targetable; slim sticky bar built via
  header JS (see build-assets doc)
- [x] **Gate: PASSED — platform choice confirmed.** Bonus finds: real cancellation
  policy already published (100% less $100 fee >30d; 50% >7d; none <7d) → Phase 0
  item 1 resolved; phone (843) 438-9992 already tel:-linked.
- 📄 Paste-ready assets → `website-redesign-build-assets.md` (same folder)

### Phase 2 — Global shell ✅ LIVE on staging 2026-07-11
- [x] Claude: v1 CSS bundle + fonts/sticky-bar head code (build-assets doc)
- [x] John: CSS tab + Head tab + Fonts & Colors all saved (after one blank-site
  incident: a missing `</script>` — fixed with Head block v1.1)
- [x] Bonus: GA4 already installed on the site (G-96L4KV3KEJ) → Phase 0 item 11 done
- [ ] Still open from Phase 2: 5-item nav labels (§3.2) + footer columns (§3.4) —
  do alongside Phase 3

### Phase 3 — Guest pages (John 2–3 hrs)
- [ ] Claude: homepage section HTML (hero copy, book-direct strip, area cards, owner strip) per §6.1
- [ ] John: configure home page (single hero + search, kill carousel), paste sections
- [ ] Claude: /book-direct full page HTML (§6.4, with Phase-0 real numbers)
- [ ] John: create custom page, paste
- [ ] Both: restyle /rentals + property detail via CSS; verify card anatomy §5.5, empty state §6.2, sticky bar §6.3

### Phase 4 — Owner funnel (John 1–2 hrs) — highest ROI
- [ ] Claude: /property-management full HTML (§6.5) + projection form + /thank-you copy
- [ ] John: create the 3 custom pages; wire form (OwnerRez inquiry form or embedded free form) so submissions email John + create a Vintory/GHL contact `[decide]`
- [ ] Both: end-to-end test — submit form on a phone, confirm email arrives, thank-you page loads

### Phase 5 — Content & trust (John 2–3 hrs, can trickle)
- [ ] Claude: 4 area-page intros (§6.8), /about story final (§6.6), review-strip excerpts picked from real reviews
- [ ] John: create area pages + about; upload compressed photos; place review widgets (§6.7)

### Phase 6 — QA + analytics (John ~1 hr)
- [ ] Both: run §7.2 mobile checklist on every page (John's phone + one Android)
- [ ] Claude: GA4 snippet + thank-you-page conversion event code
- [ ] John: create free GA4 property, paste snippet in header custom code
- [ ] John: PageSpeed Insights mobile ≥80; fix heaviest images if not

### Phase 7 — Launch (≈1 hr, see §10)

---

## Section 10 — Launch + Migration Plan

### 10.1 Pre-cutover
- [ ] Claude: crawl the CURRENT live site and list every indexed URL (properties, pages) → map each to its new-site equivalent. Keep property slugs identical wherever possible — same OwnerRez property records should mean same/similar URLs, making most "redirects" unnecessary.
- [ ] John: full staging walkthrough as a guest (search → book to payment screen) and as an owner (projection form) on phone + desktop
- [ ] Optional soft check: text the staging link to 2–3 friends/repeat guests — "which site would you book from?"

### 10.2 Cutover (low-drama version)
Because both old and new sites live in OwnerRez, cutover = **reassigning the custom
domain** unwindvacations.com from the old hosted site to the new one inside OwnerRez
(Settings → Hosted Websites → Domain). GoDaddy DNS records already point at OwnerRez
and likely need **no change**; John only touches GoDaddy if OwnerRez support docs say
the record target differs. Do it on a low-traffic morning (Tue–Wed); old site stays
intact in OwnerRez as instant rollback (reassign the domain back).

### 10.3 SEO protection
- [ ] Verify domain in **Google Search Console** (free) BEFORE cutover; export current queries/rankings as baseline
- [ ] After cutover: submit new sitemap; spot-check the top 10 ranking URLs resolve (no 404s); add redirects/matching slugs for any casualties
- [ ] Keep page titles/H1s keyword-consistent with what ranks today (`Myrtle Beach vacation rentals`, etc.) — the area pages (§6.8) strengthen this
- [ ] Watch Search Console weekly for 4 weeks; a temporary wobble is normal, a cliff is not (rollback available)

### 10.4 Measurement (30/60/90 days, vs §1 metrics)
- **Day 0:** fill every TBD baseline in §1 (GA4 export, OwnerRez direct-booking share, Search Console rankings)
- **30 days:** homepage bounce, mobile conversion funnel, projection-form fills (GA4 thank-you event), PageSpeed re-test
- **60 days:** direct bookings vs baseline; owner-lead count → follow-up quality check (is the 1-business-day projection promise being kept?)
- **90 days:** full review against §1 targets; decide next investment (photography? paid traffic to /property-management? blog for SEO?) — with data, not vibes
- Cadence: add a 10-minute "website numbers" line to the existing weekly L10/scorecard rhythm `[JOHN ACTION: add to scorecard]`

### 10.5 Open items ledger
- GoDaddy WordPress hosting question — informational only (escape hatch §4.5)
- Projection-form → Vintory/GHL wiring decision (Phase 4)
- Photography refresh — the one future spend most worth considering (not required for launch)

