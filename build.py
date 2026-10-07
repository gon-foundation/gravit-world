"""Build gravit.world (DE / FR / IT / EN) into dist/.

    python build.py               # preview: PENDING texts highlighted, banner shown
    python build.py --production  # refuses to build while any PENDING text remains
    python build.py --base /preview

Standard library only. Content: src/content/site.py and statuten_de.json
(the statutes text is exported from the Foundation's legal package).
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from content import site as C  # noqa: E402

DIST = ROOT / "dist"
TPL = ROOT / "src" / "templates"

SOCIAL = [
    ("LinkedIn", "https://linkedin.com/company/gravit-open-network",
     "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"),
    ("X", "https://x.com/GravitNet",
     "M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"),
    ("Substack", "https://substack.com/@gravitopennetworkfoundation",
     "M22.539 8.242H1.46V5.406h21.08v2.836zM1.46 10.812V24L12 18.11 22.54 24V10.812H1.46zM22.54 0H1.46v2.836h21.08V0z"),
]


def page_langs(slug: str) -> list[str]:
    return C.PAGES[slug].get("langs", C.LANGS)


def href(root: str, lang: str, slug: str | None) -> str:
    if slug and lang not in page_langs(slug):
        lang = "de"  # e.g. the English "Legal notice" link points to the German Impressum
    return f"{root}/{lang}/" + (f"{slug}/" if slug else "")


def nav(root, lang, current):
    return "\n".join(
        f'        <li><a href="{href(root, lang, s)}"{" aria-current=\"page\"" if s == current else ""}>{C.LABELS[s][lang]}</a></li>'
        for s in C.NAV)


def lang_switch(root, lang, slug):
    langs = page_langs(slug) if slug else C.LANGS
    return " ".join(
        f'<a href="{href(root, l, slug)}" hreflang="{l}" lang="{l}" title="{C.LANG_NAMES[l]}"'
        f'{" aria-current=\"true\"" if l == lang else ""}>{l}</a>' for l in langs)


def footer(root, lang):
    links = " ".join(f'<a href="{href(root, lang, s)}">{C.LABELS[s][lang]}</a>' for s in C.FOOTER_NAV)
    social = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><svg viewBox="0 0 24 24"><path d="{p}"/></svg></a>'
        for n, u, p in SOCIAL)
    return f"""  <footer>
    <nav class="footer-links" aria-label="Legal">{links}</nav>
    <p class="footer-copy">{C.COMMON["copyright"][lang]}</p>
    <div class="footer-socials">{social}</div>
    <div class="footer-origin"><span>{C.COMMON["from"][lang]}</span><span class="flag-ch" aria-label="Schweiz"></span><span>{C.COMMON["to_world"][lang]}</span></div>
  </footer>"""


def board_html(root, lang):
    cards = []
    for slug, name, roles in C.BOARD:
        img = f"{root}/assets/img/people/{slug}"
        cards.append(f"""<div class="person">
  <img src="{img}-240.webp" srcset="{img}-240.webp 1x, {img}-480.webp 2x" width="120" height="120" alt="{name}" loading="lazy" decoding="async" />
  <div class="name">{name}</div><div class="role">{roles[lang]}</div></div>""")
    return '<div class="people">' + "\n".join(cards) + "</div>"


def statutes_html(lang):
    data = json.loads((ROOT / "src" / "content" / "statuten_de.json").read_text(encoding="utf-8"))
    out = []
    if C.COMMON["german_prevails"][lang]:
        out.append(f'<p class="note">{C.COMMON["german_prevails"][lang]}</p>')
    out.append(f'<p>{C.PENDING("Datum der Vereinsversammlung eintragen, an der diese Neufassung angenommen wurde. Bis dahin gelten die Statuten vom 12. Februar 2023.")}</p>')
    out.append('<div class="statute" lang="de">')
    for i, (title, body) in enumerate(data["articles"], 1):
        out.append(f"<h3>Artikel {i} – {html.escape(title)}</h3>")
        for b in body:
            if isinstance(b, list):
                out.append("<ol>" + "".join(f"<li>{html.escape(x)}</li>" for x in b) + "</ol>")
            else:
                out.append(f"<p>{html.escape(b)}</p>")
    out.append("</div>")
    return "\n".join(out)


def news_html(lang, limit=None):
    items = C.NEWS[:limit] if limit else C.NEWS
    return '<ul class="entries">' + "".join(
        f'<li><div class="date">{d}</div><div class="title">{t[lang]}</div><div>{x[lang]}</div></li>'
        for d, t, x in items) + "</ul>"


def shell(root, lang, slug, title, description, main, draft):
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{C.SITE_URL}{href("", l, slug)}" />'
        for l in (page_langs(slug) if slug else C.LANGS))
    banner = ('<div style="background:#3a2a00;color:#ffd27a;text-align:center;font-size:12px;padding:6px;letter-spacing:.05em">'
              'PREVIEW — highlighted texts await confirmation</div>') if draft else ""
    pending_css = "<style>.pending{background:#5a4100;color:#ffe6a6;padding:2px 6px;border-radius:4px}</style>" if draft else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:image" content="{C.SITE_URL}/assets/img/og.webp" />
  <meta property="og:type" content="website" />
{alternates}
  <link rel="icon" type="image/png" sizes="512x512" href="{root}/android-chrome-512x512.png" />
  <link rel="stylesheet" href="{root}/assets/site.css" />
  {pending_css}
</head>
<body>
{(TPL / "orbital.html").read_text(encoding="utf-8")}
<div class="page">
  {banner}
  <header>
    <a class="logo" href="{href(root, lang, None)}">Gravit Open Network Foundation</a>
    <div class="header-right">
      <nav aria-label="Main"><ul>
{nav(root, lang, slug)}
      </ul></nav>
      <div class="lang-switch">{lang_switch(root, lang, slug)}</div>
    </div>
  </header>
{main}
{footer(root, lang)}
</div>
</body>
</html>
"""


def home(root, lang, draft):
    tiles = "".join(
        f'<a class="tile" href="{href(root, lang, s)}"><h2>{C.LABELS[s][lang]}</h2><p>{t[lang]}</p></a>'
        for s, t in C.HOME["tiles"])
    main = f"""  <main class="page-main" style="flex-direction:column;align-items:center">
    <section class="hero">
      <h1>Gravit Open Network Foundation</h1>
      <div class="tagline">{C.COMMON["legal_form"][lang]}</div>
      <p>{C.HOME["intro"][lang]}</p>
    </section>
    <div class="tiles">{tiles}</div>
    <section class="content" style="margin-top:28px">
      <h2 style="margin-top:0">{C.LABELS["news"][lang]}</h2>
      {news_html(lang, 3)}
    </section>
  </main>"""
    return shell(root, lang, None, "Gravit Open Network Foundation", C.HOME["intro"][lang], main, draft)


def inner(root, lang, slug, draft):
    p = C.PAGES[slug]
    body = p["body"][lang]
    body = (body.replace("{board}", board_html(root, lang))
                .replace("{statutes}", statutes_html(lang) if "{statutes}" in body else "")
                .replace("{news}", news_html(lang)))
    title = p["title"][lang]
    main = f"""  <main class="page-main">
    <article class="content">
      <div class="eyebrow">Gravit Open Network Foundation</div>
      <h1>{html.escape(title)}</h1>
      <div class="tagline">{p["tagline"][lang]}</div>
{body}
    </article>
  </main>"""
    return shell(root, lang, slug, f"{title} · Gravit Open Network Foundation", f"{title} — Gravit Open Network Foundation", main, draft)


ROOT_INDEX = """<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Gravit Open Network Foundation</title>
<link rel="stylesheet" href="{root}/assets/site.css" />
<script>
(function(){{var l=(navigator.languages||[navigator.language||"de"]).map(function(x){{return x.slice(0,2)}});
var ok=["de","fr","it","en"];for(var i=0;i<l.length;i++){{if(ok.indexOf(l[i])>=0){{location.replace("{root}/"+l[i]+"/");return}}}}
location.replace("{root}/de/");}})();
</script></head>
<body><main class="page-main"><div class="content" style="text-align:center">
<h1>Gravit Open Network Foundation</h1>
<p><a href="{root}/de/">Deutsch</a> · <a href="{root}/fr/">Français</a> · <a href="{root}/it/">Italiano</a> · <a href="{root}/en/">English</a></p>
</div></main></body></html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--production", action="store_true")
    ap.add_argument("--base", default="")
    a = ap.parse_args()
    draft = not a.production
    root = a.base.rstrip("/")

    out = {"index.html": ROOT_INDEX.format(root=root)}
    for lang in C.LANGS:
        out[f"{lang}/index.html"] = home(root, lang, draft)
        for slug in C.PAGES:
            if lang in page_langs(slug):
                out[f"{lang}/{slug}/index.html"] = inner(root, lang, slug, draft)

    pending = sorted({n for n, t in out.items() if 'data-pending="1"' in t})
    if a.production and pending:
        print("Refusing production build; PENDING text remains in: " + ", ".join(pending), file=sys.stderr)
        return 1

    # only now touch dist/: a refused build leaves the previous output intact
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "assets", DIST / "assets")
    shutil.copytree(ROOT / "static", DIST, dirs_exist_ok=True)
    for name, text in out.items():
        p = DIST / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    refs = {m for t in out.values() for m in re.findall(r'(?:src|href|srcset)="' + re.escape(root) + r'(/[^"# ]+)', t)}
    missing = sorted(r for r in refs if not (DIST / r.lstrip("/")).exists() and not (DIST / r.lstrip("/") / "index.html").exists())
    if missing:
        print("Broken internal links/assets: " + ", ".join(missing), file=sys.stderr)
        return 1
    print(f"built {len(out)} pages ({'production' if a.production else 'preview'}), {len(pending)} with pending text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
