#!/usr/bin/env python3
"""Mirror what is LIVE on unwindvacations.com into unwind-website/mirror/.

OwnerRez is the only home for page content edited in its ACE editor, so this
pulls the rendered public pages and pulls out the parts we wrote:
  mirror/pages/<slug>.html   full rendered page (as served)
  mirror/content/<slug>.html custom IntroHtml block (between page header and footer)
  mirror/site-custom.css     Theme > CSS (site-wide <style> in <head>)
  mirror/head-custom.html    Theme > Head (everything after the canonical link)
Note: OwnerRez strips HTML comments on render, so annotated sources in live/ stay
the readable copy; mirror/ is the exact-as-live copy. Re-run after any site edit:
  python3 unwind-website/scripts/mirror_live_site.py
"""
import pathlib, re, urllib.request, time

BASE = "https://www.unwindvacations.com"
OUT = pathlib.Path(__file__).resolve().parent.parent / "mirror"
UA = {"User-Agent": "Mozilla/5.0 (unwind-mirror)"}


def get(path):
    req = urllib.request.Request(f"{BASE}{path}?v={int(time.time())}", headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def custom_content(html):
    i = html.index('class="body-content"')
    i = html.index(">", i) + 1
    m = re.search(r'<h1 class="page-header">.*?</h1>\s*</div>\s*</div>', html[i:i + 800], re.S)
    if m:
        i += m.end()
    body = html[i:html.index("<footer>", i)].rstrip()
    return re.sub(r"(\s*</div>\s*){1,3}$", "", body).strip() + "\n"


def main():
    # Custom pages = sitemap entries that aren't property listings (-orp...x)
    sitemap = get("/sitemap.xml")
    paths = [u.replace(BASE, "") or "/" for u in re.findall(r"<loc>([^<]+)", sitemap) if "-orp" not in u]
    (OUT / "pages").mkdir(parents=True, exist_ok=True)
    (OUT / "content").mkdir(parents=True, exist_ok=True)
    for p in paths:
        slug = p.strip("/") or "homepage"
        html = get(p)
        html = re.sub(r"\?v=\d+", "", html)  # keep diffs clean
        (OUT / "pages" / f"{slug}.html").write_text(html)
        (OUT / "content" / f"{slug}.html").write_text(custom_content(html))
        print(f"{slug:45} {len(html):>7}")
        if slug == "homepage":
            head = html[:html.index("</head>")]
            styles = re.findall(r"<style>(.*?)</style>", head, re.S)
            (OUT / "site-custom.css").write_text(max(styles, key=len).strip() + "\n")
            canon = head.index('rel="canonical"')
            (OUT / "head-custom.html").write_text(head[head.index("\n", canon) + 1:].strip() + "\n")


if __name__ == "__main__":
    main()
