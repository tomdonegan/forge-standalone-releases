#!/usr/bin/env python3
"""Single source of truth for the website's top navigation.

Edit NAV below, run `python3 scripts/sync-nav.py`, commit the result.
`--check` exits 1 if any page is out of date (used by CI).
"""
import re, sys, pathlib

NAV = [  # (label, href, page file or None for anchors)
    ("Home", "/", "index.html"),
    ("Screens", "/#screens", None),
    ("Features", "/features.html", "features.html"),
    ("Download", "/download.html", "download.html"),
    ("Setup", "/setup.html", "setup.html"),
    ("Sports", "/sports.html", "sports.html"),
    ("How-to", "/how-to.html", "how-to.html"),
    ("FAQ", "/faq.html", "faq.html"),
    ("Feedback", "/feedback.html", "feedback.html"),
]
COFFEE = '<a class="bar-coffee" id="forge-bar-coffee" href="#" target="_blank" rel="noopener noreferrer" hidden>☕ Buy me a coffee</a>'
DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"
CSS = '<link rel="stylesheet" href="/site-nav.css">'
JS = '<script src="/site-config.js"></script>\n<script src="/site-nav.js" defer></script>'

def nav_html(page):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if f == page else "", l)
        for l, h, f in NAV)
    return '<nav aria-label="Main navigation">%s</nav>%s' % (links, COFFEE)

def sync(path):
    s = path.read_text()
    new = re.sub(r'<nav(?: aria-label="Main navigation")?>.*?</nav>(?:\s*<a class="bar-coffee"[^>]*>.*?</a>)?',
                 lambda m: nav_html(path.name), s, count=1, flags=re.S)
    if CSS not in new:
        new = new.replace("</head>", CSS + "\n</head>", 1)
    if "/site-nav.js" not in new:
        new = re.sub(r'<script src="/site-config.js"></script>\n?', "", new)
        new = new.replace("</body>", JS + "\n</body>", 1)
    return s, new

def main():
    stale = []
    for p in sorted(DOCS.glob("*.html")):
        if p.name == "feedback-thanks.html":
            continue
        old, new = sync(p)
        if old != new:
            stale.append(p.name)
            if "--check" not in sys.argv:
                p.write_text(new)
    if stale and "--check" in sys.argv:
        print("Navigation out of date in:", ", ".join(stale), "- run scripts/sync-nav.py")
        sys.exit(1)
    print("updated" if stale else "already in sync", *stale)

main()
