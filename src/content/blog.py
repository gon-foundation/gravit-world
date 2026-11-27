"""Blog: the full texts we publish (Substack, LinkedIn, longer X threads).

One Markdown file per post in src/content/blog/, named YYYY-MM-DD-slug.md:
a header (date, slug, title, summary), a line '---', then the text.
Supported: '## ' headings, paragraphs, '- ' lists, **bold**, bare URLs.
Posts are in English; the other language versions say so.
"""
import html
import re
from pathlib import Path

DIR = Path(__file__).parent / "blog"


def _inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"(https?://[^\s<]+[^\s<.,;:)])", r'<a href="\1">\1</a>', t)


def to_html(md):
    out, para, items = [], [], []

    def flush():
        if para:
            out.append("<p>" + "<br>\n".join(_inline(l) for l in para) + "</p>")
            para.clear()
        if items:
            out.append("<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    for line in md.splitlines():
        s = line.rstrip()
        if not s:
            flush()
        elif s.startswith("## "):
            flush()
            out.append(f"<h2>{_inline(s[3:])}</h2>")
        elif s.startswith("- "):
            if para:
                flush()
            items.append(s[2:])
        else:
            if items:
                flush()
            para.append(s)
    flush()
    return "\n".join(out)


def load():
    posts = []
    for f in sorted(DIR.glob("*.md"), reverse=True):
        head, body = f.read_text(encoding="utf-8").split("\n---\n", 1)
        meta = dict(l.split(": ", 1) for l in head.strip().splitlines())
        meta["html"] = to_html(body)
        posts.append(meta)
    return posts


POSTS = load()
