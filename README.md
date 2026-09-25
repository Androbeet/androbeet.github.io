# androbeet.github.io

The merged Lexicon + Essays + Posts + About site. Everything is generated
from JSON files in `data/` by `scripts/build.py` — you never hand-edit
the HTML pages.

## How to deploy this

1. In your existing `androbeet.github.io` repo, delete everything and
   copy in every file from this folder (keep the `.github` folder too —
   it's hidden, don't skip it).
2. Replace the placeholder images with your real ones:
   - `assets/img/pfp.jpg` — your profile photo
   - `assets/img/banner.jpg` — your about-page banner (about 1600×400px)
3. Commit and push. GitHub Pages will serve it at `androbeet.github.io`.
4. Retire the old `androbeet-archive` repo (or leave it, unused — either
   is fine, it's no longer linked from anywhere).

## How to add new content (no coding each time)

Open `tools/add-content.html` in your browser (locally, or push it and
open it from the live site — it's marked `noindex` so it won't show up
in search). Fill in the form for an essay, a lexicon word, or a post.
It generates a JSON object — copy it, paste it into the matching array
at the **top** of `data/essays.json`, `data/lexicon.json`, or
`data/posts.json`, then commit and push.

GitHub Actions will automatically run `scripts/build.py` and commit the
regenerated pages — you don't need to run the build script yourself
unless you want to preview locally first:

```
python3 scripts/build.py
```

### New essays
Leave "Full body" blank to keep it as a Medium link-out (like your
current 11). Fill it in to host the essay natively on your own site,
comments and all.

### New lexicon words
Just word, etymology (optional), definition, category. A new page is
created automatically at `/lexicon/<word>.html`.

### New posts
Upload the image file into `assets/img/posts/` first, then reference
its path in the form.

## Turning on visitor comments (giscus)

Comments are wired in but switched off until you connect them:

1. Make sure the repo is public and **Discussions** is enabled
   (repo Settings → General → Features → Discussions).
2. Go to https://giscus.app, enter `Androbeet/androbeet.github.io`,
   and it will generate a `repo-id` and `category-id` for you.
3. Open `scripts/build.py`, find the `GISCUS = {...}` block near the
   top, and paste those two values in.
4. Run the build (or push — the Action will do it) and comments will
   appear on every essay and lexicon page automatically.

## Light / dark theme

Already working site-wide — the toggle button in the header remembers
each visitor's choice. No setup needed.

## Structure

```
index.html            home
about.html            profile page
lexicon/               index + one page per word
essays/                 index + one page per essay
posts/                 photo/update feed
data/                  the only files you normally edit
scripts/build.py       regenerates everything from data/
tools/add-content.html private helper — not linked in the nav
assets/                css, js, images
```
