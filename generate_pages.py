# generate_pages.py
# Run this to create many unique Androbeet pages

variations = [
    "writer", "feminist", "atheist", "philosophy", "creator",
    "thinker", "essayist", "critic", "voice", "mind",
    "ideas", "thoughts", "analysis", "perspective", "view"
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Androbeet {title}</title>
<meta name="description" content="Androbeet is a feminist atheist writer and creator focused on {desc}.">
<meta name="keywords" content="androbeet, androbeet {slug}, feminist atheist writer">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Androbeet",
  "description": "Feminist atheist writer and creator"
}}
</script>
</head>
<body>
<h1>Androbeet – {title}</h1>
<p>Androbeet is a feminist atheist writer and creator. Exploring philosophy, critical thinking, atheism and feminism.</p>
<p>Contact: androbeetz@gmail.com</p>
</body>
</html>
"""

for v in variations:
    title = v.title()
    content = template.format(title=title, desc=v, slug=v)
    with open(f"androbeet-{v}.html", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: androbeet-{v}.html")

print("\\nAll pages generated successfully!")