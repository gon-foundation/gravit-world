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
PAGES = {"manifest": "manifest", "lessons/buttons": "lesson", "lessons/claims": "claim",
         "lessons/data": "data", "lessons/signature": "signature"}
LESSONS = ["lessons/buttons", "lessons/claims", "lessons/data", "lessons/signature"]
MODS = {"ru": "Все модули", "en": "All modules", "de": "Alle Module"}
LTITLE = {"ru": "Модули Gravit Education", "en": "Gravit Education modules", "de": "Module von Gravit Education"}
LLEAD = {"ru": "Уроки по 45 минут для школ. Свободны для использования.",
         "en": "45-minute lessons for schools. Free to use.",
         "de": "Unterrichtsstunden von 45 Minuten für Schulen. Frei verwendbar."}
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
.mono{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;word-break:break-all}
.sigdemo{max-width:none}.sigdemo textarea{display:block;width:100%;margin-top:4px;padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);font:15px/1.4 inherit;font-family:inherit}
.btn[role=button]{cursor:pointer;background:var(--card)}.btn[role=button]:hover{background:var(--acc);color:#fff;border-color:var(--acc)}
.item{border-bottom:1px solid var(--line);padding:8px 0}.item p{margin:0 0 6px}.item .btn.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.item .ok{color:#067647;font-weight:700}.item .no{color:var(--warn);font-weight:700}
.mods{display:grid;gap:14px;margin-top:20px}.mods a.card{display:block;text-decoration:none;color:var(--ink)}
.tbl{overflow-x:auto;margin:12px 0}table{border-collapse:collapse;width:100%;font-size:15px}
th,td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{font-weight:600}td:first-child{white-space:nowrap}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.9em}
footer{border-top:1px solid var(--line);margin-top:48px;padding-top:16px;color:var(--muted);font-size:14px}
"""

SORT_JS = """<script>(function(){var box=document.querySelector('.sort');if(!box)return;var h=document.getElementById('hint');
var ans=box.getAttribute('data-answers').split(',');var labels=document.getElementById('sort-labels').content.querySelectorAll('span');
var hints=document.getElementById('sort-hints').content.querySelectorAll('span');
box.querySelectorAll('.item').forEach(function(it,i){var row=document.createElement('p');labels.forEach(function(l){
var b=document.createElement('span');b.className='btn';b.setAttribute('role','button');b.tabIndex=0;b.textContent=l.textContent;
b.onclick=function(){row.querySelectorAll('.btn').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
var m=it.querySelector('.ok,.no');if(m)m.remove();var r=document.createElement('span');var good=l.getAttribute('data-v')===ans[i];
r.className=good?'ok':'no';r.textContent=good?' ✔':' ✘';row.appendChild(r);h.textContent=hints[i].textContent;};row.appendChild(b);});
it.appendChild(row);});})();</script>"""

SIG_JS = """<script>(function(){var d=document.getElementById('sigdemo');if(!d)return;var res=document.getElementById('sigres');
var t=document.getElementById('sigtext'),hs=document.getElementById('sighash'),ss=document.getElementById('sigsig');var keys=null,sig=null;
var C=window.crypto&&window.crypto.subtle;var al={name:'ECDSA',namedCurve:'P-256'},sa={name:'ECDSA',hash:'SHA-256'};
function hex(b){return Array.from(new Uint8Array(b)).map(function(x){return x.toString(16).padStart(2,'0')}).join('')}
function enc(){return new TextEncoder().encode(t.value)}
function fp(){C.digest('SHA-256',enc()).then(function(h){hs.textContent=hex(h).slice(0,32)+'…'})}
t.addEventListener('input',function(){if(C)fp()});
function act(a){if(!C){res.textContent=d.getAttribute('data-nosupport');return}
if(a==='keys'){C.generateKey(al,false,['sign','verify']).then(function(k){keys=k;sig=null;ss.textContent='…';res.textContent='✔ '+(document.documentElement.lang==='ru'?'Ключи созданы.':document.documentElement.lang==='de'?'Schlüssel erzeugt.':'Keys created.');fp()})}
else if(a==='sign'){if(!keys){res.textContent=d.getAttribute('data-need');return}C.sign(sa,keys.privateKey,enc()).then(function(s){sig=s;ss.textContent=hex(s).slice(0,48)+'…';fp();res.textContent='✔ '+(document.documentElement.lang==='ru'?'Текст подписан.':document.documentElement.lang==='de'?'Text signiert.':'Text signed.')})}
else if(a==='verify'){if(!keys||!sig){res.textContent=d.getAttribute('data-need');return}C.verify(sa,keys.publicKey,sig,enc()).then(function(ok){res.textContent=d.getAttribute(ok?'data-ok':'data-bad')})}}
d.querySelectorAll('[data-act]').forEach(function(b){b.addEventListener('click',function(){act(b.getAttribute('data-act'))});
b.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();act(b.getAttribute('data-act'))}})});})();</script>"""

JS = """<script>(function(){var h=document.getElementById('hint');if(!h)return;
document.querySelectorAll('.mock [data-hint]').forEach(function(el){el.addEventListener('click',function(e){
e.preventDefault();document.querySelectorAll('.mock .on').forEach(function(x){x.classList.remove('on')});
el.classList.add('on');h.textContent=el.getAttribute('data-hint');});});})();</script>"""


def page(slug, lang, body):
    more = ""
    if slug in LESSONS:
        more = f'<p class="next"><a href="/lessons/{lang}/">{MODS[lang]}</a> · <a href="/manifest/{lang}/">{TITLES["manifest"][lang]}</a></p>'
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
<main>{body}{more}</main>
<footer>{FOOT[lang]}<a href="{REPO}">GitHub</a></footer>
</div>{JS if 'data-hint' in body else ''}{SORT_JS if 'class="sort"' in body else ''}{SIG_JS if 'id="sigdemo"' in body else ''}</body></html>
"""


def chooser(slug):
    links = " · ".join(f'<a href="/{slug}/{l}/" lang="{l}">{LANG_NAMES[l]}</a>' for l in LANGS)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gravit Education</title><style>{CSS}</style>
<script>var l=(navigator.language||'en').slice(0,2);if(['ru','en','de'].indexOf(l)<0)l='en';location.replace('/{slug}/'+l+'/');</script>
</head><body><div class="wrap"><p class="kicker">Gravit Education</p><p>{links}</p></div></body></html>
"""


TITLES = {}


def title_of(name, lang):
    body = (ROOT / "content" / f"{name}_{lang}.html").read_text(encoding="utf-8")
    t = re.search(r"<h1>(.*?)</h1>", body).group(1)
    k = re.search(r'<p class="kicker">(.*?)</p>', body).group(1).split(" · ")
    return t, " · ".join(k[1:])


def lessons_index(lang):
    cards = "".join(f'<a class="card" href="/{s}/{lang}/"><b>{title_of(PAGES[s], lang)[0]}</b><p>{title_of(PAGES[s], lang)[1]}</p></a>'
                    for s in LESSONS)
    body = (f'<p class="kicker">Gravit Education</p><h1>{LTITLE[lang]}</h1><p class="lead">{LLEAD[lang]}</p>'
            f'<div class="mods">{cards}</div><p class="next"><a href="/manifest/{lang}/">{TITLES["manifest"][lang]}</a></p>')
    return page("lessons", lang, body)


def md_inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return re.sub(r"(https://[^\s|)<]+)", r'<a href="\1">\1</a>', t)


def md_to_html(md):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("# "):
            out.append(f"<h1>{md_inline(l[2:])}</h1>")
        elif l.startswith("## "):
            out.append(f"<h2>{md_inline(l[3:])}</h2>")
        elif l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| ]+\|$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            head = "".join(f"<th>{md_inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
            continue
        elif re.match(r"^\d+\. ", l):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append("<li>" + md_inline(re.sub(r"^\d+\. ", "", lines[i])) + "</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        elif l.strip():
            out.append(f"<p>{md_inline(l)}</p>")
        i += 1
    return "\n".join(out)


def history_page():
    body = md_to_html((ROOT / "history" / "REGISTER.md").read_text(encoding="utf-8"))
    body = body.replace("<h1>", '<p class="kicker">Gravit Education · History</p><h1>', 1)
    first_p = re.search(r"<p>(.*?)</p>", body).group(0)
    body = body.replace(first_p, first_p.replace("<p>", '<p class="lead">', 1), 1)
    body += ('<p class="note">Source: <a href="https://github.com/gon-foundation/gravit-world/blob/main/education/history/REGISTER.md">REGISTER.md</a>. '
             'First record of 9 November 2026 with an OpenTimestamps proof: '
             '<a href="https://github.com/gon-foundation/gravit-world/tree/main/education/history/evidence-2026-11-09">evidence-2026-11-09</a>.</p>'
             '<p class="next"><a href="/manifest/en/">Purpose, values, integrity</a> · <a href="/lessons/en/">All modules</a></p>')
    return page("history", "en", body).replace('<nav aria-label="Language">', '<nav aria-label="Language" hidden>')


if __name__ == "__main__":
    TITLES.update({s: {l: title_of(n, l)[0] for l in LANGS} for s, n in PAGES.items()})
    shutil.rmtree(OUT, ignore_errors=True)
    for slug, name in PAGES.items():
        for lang in LANGS:
            body = (ROOT / "content" / f"{name}_{lang}.html").read_text(encoding="utf-8")
            d = OUT / slug / lang
            d.mkdir(parents=True)
            (d / "index.html").write_text(page(slug, lang, body), encoding="utf-8")
        (OUT / slug / "index.html").write_text(chooser(slug), encoding="utf-8")
    for lang in LANGS:
        d = OUT / "lessons" / lang
        d.mkdir(parents=True)
        (d / "index.html").write_text(lessons_index(lang), encoding="utf-8")
    (OUT / "lessons" / "index.html").write_text(chooser("lessons"), encoding="utf-8")
    (OUT / "history").mkdir()
    (OUT / "history" / "index.html").write_text(history_page(), encoding="utf-8")
    print("\n".join(str(p.relative_to(OUT)) for p in sorted(OUT.rglob("index.html"))))
