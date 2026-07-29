# Unwind Vacations — Website

Version-controlled backup of the custom code and strategy behind
**unwindvacations.com** (an OwnerRez *hosted website*).

> **Live source of truth is OwnerRez, not this repo.** OwnerRez does not deploy
> from GitHub. This repo is a **backup + version history + developer-ready
> reference**. When code changes here, it must also be pasted into OwnerRez (and
> vice-versa). Paths to each OwnerRez destination are in the file headers.

## What's here

```
unwind-website/
├── live/                       # The custom code, as pasted into OwnerRez
│   ├── head-custom.html        # Google Fonts + bedroom quick-filter script  → Theme & Layout ▸ HEAD tab
│   ├── site-custom.css         # Chip + rating-strip styling                 → Theme & Layout ▸ CSS tab (appended)
│   └── homepage-intro.html     # Guest-rating + host-badge strip             → Home page ▸ Content ▸ Intro
├── docs/                       # Strategy + build notes (from the Obsidian vault)
│   ├── website-redesign-strategy.md
│   └── website-redesign-build-assets.md
├── snapshots/                  # Raw HTML of the live pages (reference only)
│   ├── homepage.html
│   └── properties.html
└── README.md
```

## The two OwnerRez sites

| Name | Purpose | URL |
|------|---------|-----|
| **Unwind Vacations** (id 573931745) | **LIVE** | https://www.unwindvacations.com |
| Unwind Vacations v2 | Staging / redesign sandbox | https://unwind-vacations-1.hosted.ownerrez.com |

## Features live on the site (built 2026-07)

- **Beach hero** — single static image (search + chips overlaid), ~281 KB.
- **Premium-first ordering** — biggest oceanfront homes first (Properties ▸ Display
  Order ▸ External); applies to the homepage and `/properties`.
- **One-tap bedroom filter** — "1 / 2 / 3 / 4+ Bedrooms" chips. 1–3 do *exact*-match
  filtering (OwnerRez's native filter is "N or more"); the script fetches every
  result page in parallel and shows only exact matches. See `live/head-custom.html`.
- **Prices on every card** — OwnerRez "Show range for min and max" (was hidden).
- **Guest-rating trust strip** — real cross-platform 4.86 ★ / 1,723 reviews, plus
  Airbnb Superhost · Vrbo Premier Host · Booking.com Preferred Plus badges.

## Gotchas (learned the hard way — see build-assets doc)

- The CSS/Head tabs are **ACE code editors**; the HEAD tab must end with `</script>`
  or the whole site goes blank.
- `/properties` **ignores URL query params** (POST-only filtering), which is why the
  bedroom filter drives the form and fetches pages client-side.
- OwnerRez auto-generates SEO structured data with its own (higher) internal rating;
  it is separate from the visible 4.86 strip.

## Not stored here

- The pre-existing **Facebook Messenger** plugin in the HEAD tab (separate integration).
- Pre-existing OwnerRez custom CSS (hero/logo/property-item sizing) that predates this work.
