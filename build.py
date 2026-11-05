"""Package the buildless site into dist/ using only the Python standard library."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)
for name in ("index.html", "styles.css", "script.js", ".nojekyll"):
    shutil.copy2(ROOT / name, OUT / name)
shutil.copytree(ROOT / "assets", OUT / "assets", dirs_exist_ok=True)
print(f"Site ready: {OUT / 'index.html'}")
