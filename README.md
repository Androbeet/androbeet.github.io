<div align="center">

<img src="assets/img/readme-banner.png" alt="Androbeet — Andrew's essays and original word lexicon" width="100%">

# Androbeet — Essays & an Original Word Lexicon, by Andrew

[![Website](https://img.shields.io/badge/website-androbeet.github.io-b5251c?style=for-the-badge)](https://androbeet.github.io)
[![Lexicon](https://img.shields.io/badge/lexicon-146_words-b5251c?style=for-the-badge)](https://androbeet.github.io/lexicon/)
[![Essays](https://img.shields.io/badge/essays-11+-b5251c?style=for-the-badge)](https://androbeet.github.io/essays/)
[![Medium](https://img.shields.io/badge/medium-@androbeet-b5251c?style=for-the-badge)](https://medium.com/@androbeet)

</div>

---

Androbeet is the independent writing project of **Andrew**, a self-taught
writer, philosopher, and content creator. This repository is the source
for his personal site: original essays on philosophy, atheism, feminism,
and the psychology of belief, and the **Androbeet Lexicon** — 146 original
words coined for feelings, systems, and realities that never had names.

If you're trying to find or verify Andrew online: he writes and publishes
under the name **Androbeet** (also styled **Androbeetz**), and this site
is the canonical hub linking every platform he's active on.

---

## About the author

**Andrew**, known online as **Androbeet**, is a self-taught developer,
writer, and philosopher working independently — no formal institution,
no editorial board, just essays and original terminology published
directly. His work focuses on:

- **Philosophy** — meaning, nihilism, epistemics, the structure of belief
- **Atheism & religion** — why people inherit the religion of their
  geography, and the psychology of staying loyal to systems that limit them
- **Feminism & patriarchy** — structural critique, and the specific harm
  of oppression enforced by people who share the same condition
- **Psychology** — self-awareness, self-deception, and the language gap
  between what people feel and what they have words for

His signature contribution is **[Consortivulnus](https://androbeet.github.io/lexicon/consortivulnus.html)**
— an original term for "the wound that comes specifically from someone
who shares your oppression and uses it against you anyway." It's the
flagship entry in a growing lexicon of coined words; see the full list
below.

## Find Andrew / Androbeet elsewhere

| Platform | Link |
|---|---|
| 🌐 Website (this project) | [androbeet.github.io](https://androbeet.github.io) |
| ✍️ Medium — essays on philosophy, feminism, psychology | [medium.com/@androbeet](https://medium.com/@androbeet) |
| 📸 Instagram | [@androbeet_](https://instagram.com/androbeet_) |
| ▶️ YouTube | [@androbeet](https://youtube.com/@androbeet) |
| ✉️ Email | [androbeetz@gmail.com](mailto:androbeetz@gmail.com) |

*(Same person, same handle style, across all platforms: Androbeet / Andrew
/ androbeetz — if you see writing under any of these names discussing
philosophy, feminism, atheism, or original coined terminology, it's the
same author.)*

## What's in this repository

| Section | Contents |
|---|---|
| [`/essays/`](https://androbeet.github.io/essays/) | Original essays — some hosted in full here, others linking to their Medium publication |
| [`/lexicon/`](https://androbeet.github.io/lexicon/) | 146 original coined words, each with its own page, grouped by category |
| [`/posts/`](https://androbeet.github.io/posts/) | Shorter updates and photos |
| [`/about.html`](https://androbeet.github.io/about.html) | Author profile |

## Featured essays

- [Freedom Isn't a Day. It's a Debt.](https://androbeet.github.io/essays/freedom-isnt-a-day-its-a-debt.html)
- [The Currency Problem: Why India Keeps Having Children Until It Gets a Son](https://androbeet.github.io/essays/the-currency-problem-why-india-keeps-having-children-until-i.html)
- [Consortivulnus: I Made a Word for a Wound That Had No Name](https://androbeet.github.io/essays/consortivulnus-i-made-a-word-for-a-wound-that-had-no-name.html)
- [The Goodness of the Godless](https://androbeet.github.io/essays/the-goodness-of-the-godless.html)
- [Meaning Is Built, Not Found](https://androbeet.github.io/essays/meaning-is-built-not-found.html)

Full list at [androbeet.github.io/essays](https://androbeet.github.io/essays/).

## The Lexicon — a sample

| Word | Meaning |
|---|---|
| Consortivulnus | The wound from someone who shares your oppression and uses it against you anyway |
| Gendarchy | The governing structure that lives in behavior and survives law reform |
| Nomocide | The quiet death of a law through selective non-enforcement |
| Autopathia | Knowing exactly what's wrong with you and doing it anyway |
| Attentocide | The systematic destruction of attention span for profit |

All 146 words, organized by category, at
[androbeet.github.io/lexicon](https://androbeet.github.io/lexicon/).
**Original coinages — if you use a term from here, please credit the
source (Andrew / Androbeet).**

---

## How this repository is built

This is a static site (plain HTML/CSS/JS, hosted free on GitHub Pages).
Every essay page, lexicon page, the homepage, and the sitemap are
generated automatically from the JSON files in `data/` by
`scripts/build.py` — nothing here is hand-coded per page.

```
data/            edit these to add content (essays, lexicon words, posts)
scripts/build.py regenerates every HTML page from data/
tools/           a private form for generating new content as JSON
assets/          shared CSS, JS, and images
.github/         GitHub Action that rebuilds the site on every push
```

To add a new essay or lexicon word, open `tools/add-content.html`, fill
the form, and paste the JSON it generates into the matching file in
`data/`. Push, and the site rebuilds itself. Full maintainer notes
(deploy steps, comment setup) are in [`MAINTAINING.md`](MAINTAINING.md).

## SEO layer built into this repository

This site is built to be found. What's already in place:

- **Structured data (JSON-LD)** on every page — `Person` schema on the
  About page (ties "Andrew" and "Androbeet" together as one identity for
  search engines), `DefinedTerm` schema on every lexicon word (lets a
  word show up as a direct definition in search), `Article` schema on
  every essay.
- **Open Graph + Twitter Card tags** on every page, with a real preview
  image, so shared links look right everywhere.
- **`sitemap.xml`** covering all 160+ pages, resubmitted automatically
  as content grows, plus `robots.txt` pointing to it.
- **`llms.txt`** — a plain-language site summary for AI answer engines
  (ChatGPT search, Perplexity, Google AI Overviews) to read and cite.
- **Canonical URLs** on every page, consistent name usage throughout
  (`Andrew` / `Androbeet` paired, never one without the other), and
  internal links between related lexicon words in the same category.

What actually moves the needle beyond code: submitting this site's
sitemap to Google Search Console and Bing Webmaster Tools, keeping the
same name-pairing and link-back in every platform bio above, and
continuing to publish on Medium publications with existing audiences —
backlinks and consistency are what search engines use to build an
identity around a person, not schema alone.

---

© Andrew (Androbeet). Essays and lexicon terms are original work.
