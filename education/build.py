"""Build the Gravit Education pages served on gravit.world (RU / EN / DE).

    python education/build.py        # writes education/dist/

Pages: /manifest/<lang>/ and /lessons/buttons/<lang>/, plus /manifest/ and
/lessons/buttons/ that pick a language. Every other path on gravit.world keeps
its 301 redirect to gravitopennetwork.org (see education/htaccess).
Standard library only. Content: education/content/*.html
"""
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
LANGS = ["ru", "en", "de"]
LANG_NAMES = {"ru": "Русский", "en": "English", "de": "Deutsch"}
PAGES = {"manifest": "manifest", "lessons/buttons": "lesson"}
FOOT = {
    "ru": "Gravit Open Network Foundation, Цюрих. Без трекинга. Исходный текст и история изменений: ",
    "en": "Gravit Open Network Foundation, Zurich. No tracking. Source and change history: ",
    "de": "Gravit Open Network Foundation, Zürich. Kein Tracking. Quelltext und Änderungsverlauf: ",
}
REPO = "https://github.com/gon-foundation/gravit-world/tree/main/education"

CSS = """
:root{--bg:#fbfaf7;--ink:#14161a;--muted:#5b6170;--line:#e4e1d8;--card:#fff;--acc:#0a62a8;--warn:#b42318}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#111315;--ink:#ecebe6;--muted:#a3a7b0;--line:#2a2d31;--card:#17191c;--acc:#6aaee8;--warn:#f97066}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:28px 16px 64px}a{color:var(--acc)}
header{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;font-size:15px}
header nav a{margin-left:10px;text-decoration:none}header nav a[aria-current]{font-weight:700;text-decoration:underline}
.kicker{color:var(--muted);font-size:14px;letter-spacing:.02em;margin:36px 0 4px}
h1{font:600 clamp(28px,6vw,40px)/1.15 Georgia,serif;margin:0 0 10px}
h2{font:600 24px/1.25 Georgia,serif;margin:40px 0 12px}
.lead{font-size:19px;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;margin:16px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;transition:transform .18s ease,box-shadow .18s ease}
.card:hover{transform:translateY(-4px);box-shadow:0 10px 24px rgba(0,0,0,.08)}
.card p{margin:6px 0 0;font-size:16px}
li{margin:6px 0}
.mock{background:var(--card);border:2px solid var(--line);border-radius:14px;padding:18px;max-width:440px;margin:16px 0}
.mock p{margin:8px 0}.mock [data-hint]{cursor:pointer;border-radius:6px}
.mock [data-hint]:hover,.mock [data-hint].on{outline:2px dashed var(--acc);outline-offset:3px}
.mock-title{font-weight:700;color:var(--warn)}.honest .mock-title{color:var(--ink)}
.mock-big{display:block;width:100%;margin:14px 0 6px;border:0;border-radius:999px;background:var(--warn);color:#fff;font-weight:700;font-size:17px;font-family:inherit;padding:13px}
.mock-small{font-size:12px;color:var(--muted)}
.btn{display:inline-block;border:1px solid var(--ink);border-radius:999px;padding:6px 12px;margin:4px 4px 0 0;font-size:14px}
.hint{min-height:2.6em;background:var(--card);border-left:4px solid var(--acc);padding:8px 12px;border-radius:6px}
.note{color:var(--muted);font-size:15px;margin-top:36px}.next{font-weight:600}
footer{border-top:1px solid var(--line);margin-top:48px;padding-top:16px;color:var(--muted);font-size:14px}
"""

JS = """<script>(function(){var h=document.getElementById('hint');if(!h)return;
document.querySelectorAll('.mock [data-hint]').forEach(function(el){el.addEventListener('click',function(e){
e.preventDefault();document.querySelectorAll('.mock .on').forEach(function(x){x.classList.remove('on')});
el.classList.add('on');h.textContent=el.getAttribute('data-hint');});});})();</script>"""


def page(slug, lang, body):
    title = re.search(r"<h1>(.*?)</h1>", body).group(1)
    desc = html.unescape(re.sub(r"<[^>]+>", "", re.search(r'<p class="lead">(.*?)</p>', body, re.S).group(1)))
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="https://gravit.world/{slug}/{l}/">' for l in LANGS)
    switch = " ".join(f'<a href="/{slug}/{l}/" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lang else "")
                      + f">{l.upper()}</a>" for l in LANGS)
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Gravit Education</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://gravit.world/{slug}/{lang}/">{alts}
<style>{CSS}</style></head><body><div class="wrap">
<header><a href="https://gravitopennetwork.org/">Gravit Open Network Foundation</a><nav aria-label="Language">{switch}</nav></header>
<main>{body}</main>
<footer>{FOOT[lang]}<a href="{REPO}">GitHub</a></footer>
</div>{JS if 'data-hint' in body else ''}</body></html>
"""


def chooser(slug):
    links = " · ".join(f'<a href="/{slug}/{l}/" lang="{l}">{LANG_NAMES[l]}</a>' for l in LANGS)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gravit Education</title><style>{CSS}</style>
<script>var l=(navigator.language||'en').slice(0,2);if(['ru','en','de'].indexOf(l)<0)l='en';location.replace('/{slug}/'+l+'/');</script>
</head><body><div class="wrap"><p class="kicker">Gravit Education</p><p>{links}</p></div></body></html>
"""


if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    for slug, name in PAGES.items():
        for lang in LANGS:
            body = (ROOT / "content" / f"{name}_{lang}.html").read_text(encoding="utf-8")
            d = OUT / slug / lang
            d.mkdir(parents=True)
            (d / "index.html").write_text(page(slug, lang, body), encoding="utf-8")
        (OUT / slug / "index.html").write_text(chooser(slug), encoding="utf-8")
    print("\n".join(str(p.relative_to(OUT)) for p in sorted(OUT.rglob("index.html"))))
