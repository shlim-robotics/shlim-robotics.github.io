"""Package the buildless site into dist/ using only the Python standard library."""
from pathlib import Path
from html import escape
import json
import os
import re
import shutil

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)
for name in ("styles.css", "script.js", ".nojekyll"):
    shutil.copy2(ROOT / name, OUT / name)
shutil.copytree(ROOT / "assets", OUT / "assets", dirs_exist_ok=True)

# Images are optional. A row only gains an image column when a file exists.
image_metadata = json.loads((ROOT / "publication-images.json").read_text())
image_count = 0

def add_publication_image(match):
    global image_count
    key, body = match.group("key", "body")
    metadata = image_metadata.get(key, {})
    image_path = next((ROOT / "assets" / "publications" / f"{key}{suffix}"
                       for suffix in (".webp", ".png", ".jpg", ".jpeg", ".gif")
                       if (ROOT / "assets" / "publications" / f"{key}{suffix}").is_file()), None)
    if image_path is None:
        return match.group(0)

    image_count += 1
    src = escape(image_path.relative_to(ROOT).as_posix(), quote=True)
    alt = escape(metadata.get("alt", f"Research figure for {key}"), quote=True)
    caption = escape(metadata.get("caption", "Research figure"))
    source = metadata.get("source")
    if source:
        caption = (f'<a href="{escape(source, quote=True)}" target="_blank" '
                   f'rel="noopener noreferrer">{caption}</a>')
    figure = f'''            <figure class="paper-figure">
              <a class="paper-image-link" href="{src}" target="_blank" rel="noopener noreferrer" aria-label="Enlarge image: {alt}">
                <img src="{src}" alt="{alt}" loading="lazy" decoding="async">
              </a>
              <figcaption>{caption}<span aria-hidden="true"> ↗</span></figcaption>
            </figure>
'''
    return f'<article class="paper paper-with-figure" data-paper="{key}">{body.rstrip()}\n{figure}          </article>'

html = re.sub(
    r'<article class="paper" data-paper="(?P<key>[a-z0-9-]+)">(?P<body>.*?)</article>',
    add_publication_image,
    (ROOT / "index.html").read_text(),
    flags=re.DOTALL,
)

# GitHub Pages supplies its actual URL, including any custom domain or base path.
site_url = os.environ.get("SITE_URL", "").strip().rstrip("/")
if site_url:
    image_url = escape(f"{site_url}/assets/seonghyeon-lim.jpg", quote=True)
    html = re.sub(
        r'(<meta property="og:image" content=")[^"]*(">)',
        lambda match: f"{match[1]}{image_url}{match[2]}",
        html,
    )

(OUT / "index.html").write_text(html)
print(f"Site ready: {OUT / 'index.html'}")
print(f"Publication images: {image_count}")
