# Unwind owner-postcard landing pages

Two QR landing pages for direct-mail campaigns to condo owners, both live on the
OwnerRez hosted site (website id `573931745`, "Unwind Vacations").

| Campaign | URL | OwnerRez page | Jotform |
|---|---|---|---|
| Grande Cayman Resort | https://unwindvacations.com/grandecayman | 574062202 | 262645949544067 |
| Ocean Reef Resort | https://unwindvacations.com/oceanreef | created 9/23 | 262654650147055 |

Both verified live: styles intact, form iframe loading with the resize handler
active, campaign `source` flowing through, the theme's duplicate page title
suppressed, no horizontal overflow at 375px.

---

## THE ONE THING STILL NOT DONE: notification emails

**Neither form emails anyone.** Submissions are captured and safe in Jotform, but
no alert goes out. I have now tested this four times across both forms.

The Jotform connector can build and style questions but **will not configure
email settings** - every attempt reports success and changes nothing. Your Chrome
isn't logged into Jotform either (the connector authenticates separately,
server-side), so I can't do it through the browser.

**This is a manual step, about a minute per form:**

1. Open the form builder:
   - Grande Cayman: https://www.jotform.com/build/262645949544067
   - Ocean Reef: https://www.jotform.com/build/262654650147055
2. **Settings** (top bar), then **Emails** (left)
3. **Add Email**, then choose **Notification Email** - NOT Autoresponder
4. **Recipients**, all four:
   - `jwatson@unwindvacations.com`
   - `jroy@unwindvacations.com`
   - `mmeetre@unwindvacations.com`
   - `hhorner@unwindvacations.com`
5. **Reply-To**: set to the form's **Email** field, so replying goes straight
   back to the owner
6. Save, then submit the live page once and confirm the email lands

Why this matters: the Grande Cayman form originally had an **Autoresponder**,
which emails a receipt to *whoever submitted* rather than alerting your team. I
removed it. If you want owners to get a confirmation too, add one back
deliberately - but the Notification is the one that tells you a lead came in.

### Test rows to delete

Four test submissions to clear before the mailers drop:

- Grande Cayman: **ZZ TEST / ZZ TEST2 / ZZ TEST3**, all "Delete Me"
- Ocean Reef: **ZZ TEST "Delete Me"**

---

## The two pages are deliberately different

They share a design system but not a pitch, because the mailers don't.

**Grande Cayman** leads with money: `$74,314` as the hero, "same resort, what is
your condo earning?" It names a number because the postcard does.

**Ocean Reef** leads with the upfit: "A fresh look. A stronger rental plan." It
carries **no revenue figure at all**, because that mailer deliberately omits one
and adds a disclaimer that Superhost status and review counts are portfolio-wide,
not results for any individual Ocean Reef condo. That disclaimer is reproduced in
the page footer. Don't add a number here without deciding that on purpose.

Ocean Reef asks one question Grande Cayman doesn't: **"Has your unit been through
the refresh yet?"** (finished / in progress / not scheduled / not sure). That
tells you where each owner sits in the renovation cycle, which is the whole hook.

---

## Working on the OwnerRez pages

**Settings > Hosted Websites > Unwind Vacations > Menu & Pages**, then click the
page, or **+ Create Page > Custom** for a new one.

The **Content** tab is an **ACE code editor** - there is no rich text editor and
no "Edit HTML Source" button, whatever the OwnerRez docs say. Paste HTML straight
in. Its form field is a hidden `textarea[name="IntroHtml"]`.

**Clipboard paste into ACE is unreliable.** The dependable way to set content:

```js
const html = "...";                                   // the page source
ace.edit(document.querySelector('.ace_editor')).setValue(html, -1);
document.getElementById('IntroHtml').value = html;    // the field that actually posts
```

Then click **Save and Close**. Always confirm afterwards by re-fetching the live
URL and checking the byte count changed - a failed save leaves the page
byte-identical and looks like success.

### Leave "Lead" blank

OwnerRez renders Lead text as a header above your content, and both pages carry
their own hero. Same for anything repeating the logo or title.

### The numeric slug suffix is fine

OwnerRez appends an id (`grandecayman-574062202`). That's **broken link
protection** and it does not affect the QR codes - the bare `/grandecayman` and
`/oceanreef` both resolve and return 200.

---

## Images

**Grande Cayman** embeds its logo and hero photo as data URIs - fully
self-contained, ~228 KB.

**Ocean Reef** references them from OwnerRez's own CDN instead, which is why it's
only ~17 KB:

- hero: `uc.orez.io/f/5859d7eb75c04bebb721201f64104db4` (Unwind's own Ocean Reef 3BR)
- logo: `uc.orez.io/f/a2de6297a16844d39af0e2eeb9081c0d` (the site's own logo)

The hero sits at 30% opacity behind a navy gradient, so if that photo is ever
removed from the media library the hero still reads correctly - it just loses the
texture. The logo is the one the site header uses, so it's safe.

---

## Campaign tracking

Both pages pass URL parameters through to the form's hidden fields:

```
unwindvacations.com/oceanreef?utm_source=postcard&utm_campaign=or-oct26
```

`source` defaults to `grande-cayman-postcard` / `ocean-reef-postcard`, so plain
QR scans are tagged without any parameters on the printed code.

---

## Grande Cayman's revenue figure

`$74,314.63` reconciles. OwnerRez **Reports > Booking Summary**, Grande Cayman
Resort #1253, Period **01 Jan - 31 Dec 2026**, Period Filter **Use departure
date**, with **Include owner bookings** and **Include canceled bookings** both
ticked.

One wording nit, unresolved: that report runs Jan-Dec on a departure basis, so it
includes ~$3,143 of December departures that haven't happened yet, plus canceled
and owner bookings. The page footnote describes the basis as "Jan. 1-Sep. 22,
2026," which isn't how the number was pulled. The figure stands; the footnote
wording could be tightened.

---

## Known limitations

- **"Powered by Jotform"** shows under both submit buttons. Removing it needs a
  paid Jotform plan.
- **The forms are iframes.** A hand-built form posting directly to Jotform gets
  rejected by their anti-spam CAPTCHA - which returns HTTP 200, so it would have
  looked fine while silently dropping every lead. The embed is their supported
  path.
- **Theme overrides.** Both pages hide `h1.page-header` and unpad
  `#content.container`. Those selectors are site-wide in form but ship inside
  each page's own `<style>` block, so they load only on that page.
- **The Ocean Reef postcard is a draft.** Copy on that page follows the
  2026-09-23 draft; update it when the final lands.

## Files

| File | What it is |
|---|---|
| `grandecayman-page.html` | Grande Cayman page, standalone (has `<title>`) |
| `grandecayman-PASTE.html` | Same, minus `<title>` - this is what's deployed |
| `oceanreef-page.html` | Ocean Reef page, standalone |
| `oceanreef-PASTE.html` | Same, minus `<title>` - this is what's deployed |
| `fallback-1-CSS-for-theme-tab.css` | OBSOLETE - contingency that proved unnecessary |
| `fallback-2-BODY-for-page-editor.html` | OBSOLETE - same |
