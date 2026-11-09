# Top menu layout — unwindvacations.com

OwnerRez ▸ Hosted Websites ▸ Unwind Vacations ▸ **Menu Layout** (`/settings/hostedsites/573931745/menulayoutedit`).
OwnerRez is the source of truth; this file records the intended order.

As of **2026-11-09**:

1. Home
2. About
3. Properties ▾ (All Properties, Oceanfront, Pet-Friendly, Large Groups 4+ BR, North Myrtle Beach & Cherry Grove, Myrtle Beach, Surfside Beach, Murrells Inlet, Little River)
4. Resorts ▾ (Grande Cayman, Ocean Reef, Prince Resort, Kingston Plantation, North Beach Plantation)
5. Property Management
6. Snowbird Rentals
7. Reviews
8. Activities
9. Owner Portal
10. Map
11. **Long Term Rentals**: OwnerRez *Menu Item* (Create Menu) linking to `https://rentals.unwindvacations.com`, same tab

The "Contact" button sits to the left of the menu and comes from the theme, not from Menu Layout.

## Width fix (2026-11-09)

With 11 top-level items, the desktop menu ran off the right edge of the screen. This is why Resorts was never visible before.
The fix is `nav-fit.css.html`, appended to Theme & Layout ▸ HEAD:
- the header row can be up to 1480px wide
- the menu text scales with screen width, `clamp(11px, 1.02vw, 16px)`

Checked that the menu fits on one row at 1728, 1512, 1470, 1440 and 1280px wide.
Below about 1200px the theme switches to its mobile hamburger menu.
If more top-level items are added, recheck at 1280px or group items into dropdowns.
