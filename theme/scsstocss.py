import subprocess
from pathlib import Path

import requests

# URLs des fichiers SCSS Reveal.js à télécharger
reveal_scss_files = {
    "theme/template/exposer.scss": "https://raw.githubusercontent.com/hakimel/reveal.js/refs/tags/5.2.1/css/theme/template/exposer.scss",
    "theme/template/mixins.scss": "https://raw.githubusercontent.com/hakimel/reveal.js/refs/tags/5.2.1/css/theme/template/mixins.scss",
    "theme/template/settings.scss": "https://raw.githubusercontent.com/hakimel/reveal.js/refs/tags/5.2.1/css/theme/template/settings.scss",
    "theme/template/theme.scss": "https://raw.githubusercontent.com/hakimel/reveal.js/refs/tags/5.2.1/css/theme/template/theme.scss",
}

# sources du thème Geotribu
src_geotribu_scss = Path("theme/slides/geotribu.scss")


# Télécharger les fichiers SCSS nécessaires
for local_path, url in reveal_scss_files.items():
    local_file = Path(local_path)
    if local_file.exists():
        print(f"{local_file} existe déjà, pas besoin de le télécharger.")
        continue
    local_file.parent.mkdir(parents=True, exist_ok=True)
    print(f"Téléchargement de {url} vers {local_file}")
    response = requests.get(url)
    response.raise_for_status()
    local_file.write_text(response.text, encoding="utf-8")


subprocess.run(
    ["npx", "sass", str(src_geotribu_scss), str("theme/slides/geotribu.css")],
    check=True,
)
