#!/usr/bin/env python3
"""
Androbeet site builder.

Reads data/site.json, data/lexicon.json, data/essays.json, data/posts.json
and regenerates every HTML page from the templates defined in this file.

Run manually:
    python3 scripts/build.py

Runs automatically via .github/workflows/build.yml on every push that
touches anything under data/.

To add content, don't edit HTML by hand — edit the JSON files in data/,
or use tools/add-content.html to generate the JSON snippet to paste in.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = json.loads((DATA / "site.json").read_text())
LEXICON = json.loads((DATA / "lexicon.json").read_text())
ESSAYS = json.loads((DATA / "essays.json").read_text())
POSTS = json.loads((DATA / "posts.json").read_text())

# giscus (visitor comments) config — fill these in once you've set up
# giscus.app on the repo, then this block auto-appears on every essay
# and lexicon page. Leave repo_id/category_id blank to hide comments.
GISCUS = {
    "repo": "Androbeet/androbeet.github.io",
    "repo_id": "",
    "category": "Comments",
    "category_id": "",
    "theme": "preferred_color_scheme",
}

NAV = [
    ("/", "Home"),
    ("/essays/", "Essays"),
    ("/lexicon/", "Lexicon"),
    ("/posts/", "Posts"),
    ("/about.html", "About"),
]


def esc(s):
    return html.escape(s or "")


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return s[:60].strip("-")


def nav_html(active_path):
    links = []
    for href, label in NAV:
        cls = ' class="active"' if href == active_path else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(links)


def giscus_html():
    if not GISCUS["repo_id"] or not GISCUS["category_id"]:
        return ""
    return f"""
    <div class="comments-block">
      <h2>Comments</h2>
      <script src="https://giscus.app/client.js"
        data-repo="{GISCUS['repo']}"
        data-repo-id="{GISCUS['repo_id']}"
        data-category="{GISCUS['category']}"
        data-category-id="{GISCUS['category_id']}"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-theme="{GISCUS['theme']}"
        crossorigin="anonymous"
        async>
      </script>
    </div>"""


SITE_URL = "https://androbeet.github.io"


def layout(title, description, active_path, body, canonical_path="", json_ld=None, og_type="website"):
    canonical = f"{SITE_URL}{canonical_path}" if canonical_path else ""
    canonical_tag = f'<link rel="canonical" href="{canonical}">' if canonical else ""
    og_image = f"{SITE_URL}/{SITE['banner']}"
    ld_tag = ""
    if json_ld:
        ld_tag = f'<script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{canonical_tag}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical or SITE_URL}">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_image}">
<meta name="author" content="{esc(SITE['real_name'])} ({esc(SITE['name'])})">
<link rel="icon" href="data:,">
<link rel="stylesheet" href="/assets/css/style.css">
{ld_tag}
<script>
  (function(){{try{{var t=localStorage.getItem('androbeet-theme');
  if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();
</script>
</head>
<body>
<header class="site-header">
  <div class="top">
    <a class="brand" href="/">{esc(SITE['name'])}</a>
    <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">Dark</button>
  </div>
  <nav class="site-nav">
      {nav_html(active_path)}
  </nav>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p>© {esc(SITE['name'])} · {esc(SITE['real_name'])} · <a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a></p>
  </div>
</footer>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- home ----
def build_home():
    latest_essays = ESSAYS[:3]
    latest_words = LEXICON[:5]
    latest_posts = POSTS[:2]

    essay_cards = "\n".join(
        f"""      <a class="card" href="/essays/{e['slug']}.html">
        <h3>{esc(e['title'])}</h3>
        <p>{esc(e['description'])}</p>
        <div class="tags">{''.join(f'<span class="tag">{esc(t)}</span>' for t in e['tags'])}</div>
      </a>"""
        for e in latest_essays
    )

    word_cards = "\n".join(
        f"""      <a class="card" href="/lexicon/{w['slug']}.html">
        <div class="cat">{esc(w['category'])}</div>
        <h3>{esc(w['word'])}</h3>
        <p>{esc(w['definition'][:110])}{'…' if len(w['definition']) > 110 else ''}</p>
      </a>"""
        for w in latest_words
    )

    posts_section = ""
    if latest_posts:
        post_cards = "\n".join(
            f"""      <a class="card" href="/posts/">
        <h3>{esc(p.get('caption','')[:60])}</h3>
      </a>"""
            for p in latest_posts
        )
        posts_section = f"""
    <section class="section wrap">
      <div class="section-head"><h2>Latest posts</h2><a class="see-all" href="/posts/">See all →</a></div>
      <div class="grid">
{post_cards}
      </div>
    </section>"""

    body = f"""
    <section class="hero wrap">
      <h1>{esc(SITE['name'])}</h1>
      <p>{esc(SITE['tagline'])}</p>
    </section>

    <section class="section wrap">
      <div class="section-head"><h2>Latest essays</h2><a class="see-all" href="/essays/">See all →</a></div>
      <div class="grid">
{essay_cards}
      </div>
    </section>

    <section class="section wrap">
      <div class="section-head"><h2>From the Lexicon</h2><a class="see-all" href="/lexicon/">See all →</a></div>
      <div class="grid">
{word_cards}
      </div>
    </section>
{posts_section}
"""
    (ROOT / "index.html").write_text(
        layout(f"{SITE['name']} — {SITE['tagline']}", SITE["tagline"], "/", body, "/")
    )


# ------------------------------------------------------------- lexicon ----
def build_lexicon():
    by_cat = {}
    for w in LEXICON:
        by_cat.setdefault(w["category"], []).append(w)

    sections = []
    for cat, ws in by_cat.items():
        cards = "\n".join(
            f"""        <a class="card" href="/lexicon/{w['slug']}.html">
          <h3>{esc(w['word'])}</h3>
          <p>{esc(w['definition'][:110])}{'…' if len(w['definition']) > 110 else ''}</p>
        </a>"""
            for w in ws
        )
        sections.append(f"""
    <section class="section wrap">
      <div class="section-head"><h2>{esc(cat)}</h2></div>
      <div class="grid">
{cards}
      </div>
    </section>""")

    body = f"""
    <section class="hero wrap">
      <h1>Lexicon</h1>
      <p>{len(LEXICON)} original words for realities that never had names. Coined and defined by {esc(SITE['real_name'])}.</p>
    </section>
{''.join(sections)}
"""
    termset_ld = {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "name": "Androbeet Lexicon",
        "description": f"{len(LEXICON)} original words coined by {SITE['real_name']} for realities without names.",
        "url": f"{SITE_URL}/lexicon/",
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "name": w["word"], "url": f"{SITE_URL}/lexicon/{w['slug']}.html"}
            for w in LEXICON
        ],
    }
    (ROOT / "lexicon" / "index.html").write_text(
        layout("Lexicon — Androbeet", f"{len(LEXICON)} original words coined by {SITE['real_name']} for realities without names.",
               "/lexicon/", body, "/lexicon/", json_ld=termset_ld)
    )

    for w in LEXICON:
        sub_bits = []
        if w.get("pronunciation"):
            sub_bits.append(esc(w["pronunciation"]))
        if w.get("etymology"):
            sub_bits.append(esc(w["etymology"]))
        etym = f'<p class="etymology">{" · ".join(sub_bits)}</p>' if sub_bits else ""

        short_note = ""
        if w.get("short"):
            short_note = '<p class="hint-note">Quick definition — a full essay expanding on this word is on the way.</p>'

        related = [o for o in LEXICON if o["category"] == w["category"] and o["slug"] != w["slug"]][:4]
        related_html = ""
        if related:
            related_links = "\n".join(
                f'<a class="card" href="/lexicon/{r["slug"]}.html"><h3>{esc(r["word"])}</h3></a>'
                for r in related
            )
            related_html = f"""
      <div class="section" style="border-top:1px solid var(--border); margin-top:28px;">
        <div class="section-head"><h2>More in {esc(w['category'])}</h2></div>
        <div class="grid">
{related_links}
        </div>
      </div>"""

        term_ld = {
            "@context": "https://schema.org",
            "@type": "DefinedTerm",
            "name": w["word"],
            "description": w["definition"],
            "inDefinedTermSet": f"{SITE_URL}/lexicon/",
            "url": f"{SITE_URL}/lexicon/{w['slug']}.html",
        }

        page_body = f"""
    <div class="wrap">
      <div class="page-header">
        <div class="eyebrow">{esc(w['category'])}</div>
        <h1>{esc(w['word'])}</h1>
        {etym}
      </div>
      <p class="definition">{esc(w['definition'])}</p>
      {short_note}
      <a class="back-link" href="/lexicon/">← Back to the Lexicon</a>
      {related_html}
      {giscus_html()}
    </div>
"""
        (ROOT / "lexicon" / f"{w['slug']}.html").write_text(
            layout(f"{w['word']} — Androbeet Lexicon", w["definition"][:150],
                   "/lexicon/", page_body, f"/lexicon/{w['slug']}.html", json_ld=term_ld, og_type="article")
        )


# -------------------------------------------------------------- essays ----
def build_essays():
    cards = "\n".join(
        f"""      <a class="card" href="/essays/{e['slug']}.html">
        <h3>{esc(e['title'])}</h3>
        <p>{esc(e['description'])}</p>
        <div class="tags">{''.join(f'<span class="tag">{esc(t)}</span>' for t in e['tags'])}</div>
      </a>"""
        for e in ESSAYS
    )
    body = f"""
    <section class="hero wrap">
      <h1>Essays</h1>
      <p>Writing on philosophy, atheism, feminism, and the psychology of belief.</p>
    </section>
    <section class="section wrap">
      <div class="grid">
{cards}
      </div>
    </section>
"""
    (ROOT / "essays" / "index.html").write_text(
        layout("Essays — Androbeet", "Essays on philosophy, atheism, feminism, and psychology.",
               "/essays/", body, "/essays/")
    )

    for e in ESSAYS:
        tags_html = "".join(f'<span class="tag">{esc(t)}</span>' for t in e["tags"])
        if e.get("body_html"):
            content = f'<div class="article-body">{e["body_html"]}</div>'
        else:
            content = f"""
      <div class="external-note">
        <p>This essay is published in full on Medium.</p>
        <a class="btn" href="{esc(e['external_url'])}" target="_blank" rel="noopener">Read the full essay on Medium →</a>
      </div>"""
        page_body = f"""
    <div class="wrap">
      <div class="page-header">
        <div class="eyebrow">{esc(', '.join(e['tags']))}</div>
        <h1>{esc(e['title'])}</h1>
      </div>
      <p class="definition">{esc(e['description'])}</p>
      {content}
      <a class="back-link" href="/essays/">← Back to Essays</a>
      {giscus_html()}
    </div>
"""
        article_ld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": e["title"],
            "description": e["description"],
            "keywords": ", ".join(e["tags"]),
            "datePublished": e.get("date", ""),
            "url": f"{SITE_URL}/essays/{e['slug']}.html",
            "author": {"@type": "Person", "name": SITE["real_name"], "alternateName": SITE["name"]},
            "publisher": {"@type": "Person", "name": SITE["real_name"], "alternateName": SITE["name"]},
        }
        (ROOT / "essays" / f"{e['slug']}.html").write_text(
            layout(f"{e['title']} — Androbeet", e["description"], "/essays/", page_body,
                   f"/essays/{e['slug']}.html", json_ld=article_ld, og_type="article")
        )


# --------------------------------------------------------------- posts ----
def build_posts():
    if POSTS:
        items = "\n".join(
            f"""      <div class="post">
        {'<img src="' + esc(p['image']) + '" alt="">' if p.get('image') else ''}
        <p>{esc(p.get('caption',''))}</p>
        <div class="date">{esc(p.get('date',''))}</div>
      </div>"""
            for p in POSTS
        )
    else:
        items = '<div class="empty-state">No posts yet — check back soon.</div>'

    body = f"""
    <section class="hero wrap">
      <h1>Posts</h1>
      <p>Photos and short updates, outside the essays and the Lexicon.</p>
    </section>
    <section class="section wrap">
{items}
    </section>
"""
    (ROOT / "posts" / "index.html").write_text(
        layout("Posts — Androbeet", "Photos and short updates from Androbeet.", "/posts/", body, "/posts/")
    )


# --------------------------------------------------------------- about ----
def build_about():
    sections = "\n".join(
        f"""    <section class="about-section wrap">
      <h2>{esc(s['heading'])}</h2>
      <p>{esc(s['body'])}</p>
    </section>"""
        for s in SITE["about_sections"]
    )
    social_links = "\n      ".join(
        f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(name.capitalize())}</a>'
        for name, url in SITE["socials"].items()
    )
    body = f"""
    <img class="banner" src="/{SITE['banner']}" alt="">
    <div class="about-head wrap">
      <img class="pfp" src="/{SITE['pfp']}" alt="{esc(SITE['name'])}">
      <h1>{esc(SITE['name'])}</h1>
      <div class="handle">{esc(SITE['real_name'])} · writer & philosopher</div>
      <div class="social-row">
      {social_links}
      </div>
    </div>
{sections}
"""
    person_ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": SITE["real_name"],
        "alternateName": SITE["name"],
        "url": f"{SITE_URL}/about.html",
        "image": f"{SITE_URL}/{SITE['pfp']}",
        "jobTitle": "Writer, philosopher, content creator",
        "description": SITE["tagline"],
        "email": SITE["email"],
        "sameAs": list(SITE["socials"].values()),
    }
    (ROOT / "about.html").write_text(
        layout(f"About — {SITE['name']} ({SITE['real_name']})", SITE["tagline"], "/about.html", body,
               "/about.html", json_ld=person_ld, og_type="profile")
    )


# ------------------------------------------------------------ sitemap -----
def build_sitemap():
    urls = ["/", "/about.html", "/essays/", "/lexicon/", "/posts/"]
    urls += [f"/essays/{e['slug']}.html" for e in ESSAYS]
    urls += [f"/lexicon/{w['slug']}.html" for w in LEXICON]
    body = "\n".join(
        f"  <url><loc>{SITE_URL}{u}</loc></url>" for u in urls
    )
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'
    (ROOT / "sitemap.xml").write_text(xml)
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


# ------------------------------------------------------------- llms.txt ---
def build_llms_txt():
    word_list = ", ".join(w["word"] for w in LEXICON[:15])
    essay_list = "\n".join(f"- {e['title']}: {e['description']} ({SITE_URL}/essays/{e['slug']}.html)" for e in ESSAYS)
    text = f"""# {SITE['name']} ({SITE['real_name']})

> {SITE['tagline']}

{SITE['real_name']} ({SITE['name']}) is a self-taught writer, philosopher, and content
creator publishing essays and original terminology on philosophy, atheism, feminism,
and the psychology of belief.

## Lexicon
{SITE_URL}/lexicon/ — {len(LEXICON)} original terms coined by {SITE['real_name']},
each with its own page. See data/lexicon.json in the repo for the full structured
list. A sample: {word_list}, and more.

## Essays
{SITE_URL}/essays/
{essay_list}

## About
{SITE_URL}/about.html

## Contact
{SITE['email']}
"""
    (ROOT / "llms.txt").write_text(text)


def main():
    build_home()
    build_lexicon()
    build_essays()
    build_posts()
    build_about()
    build_sitemap()
    build_llms_txt()
    print(f"Built: 1 home, 1 about, {len(LEXICON)+1} lexicon pages, {len(ESSAYS)+1} essay pages, 1 posts page.")


if __name__ == "__main__":
    main()
