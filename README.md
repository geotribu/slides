# Geotribu slides

[![🚀 Deployment](https://github.com/geotribu/slides/actions/workflows/deploy.yml/badge.svg)](https://github.com/geotribu/slides/actions/workflows/deploy.yml)

## How to add a slide

1. Create a markdown file under `slides` subfolder following the naming convention with the date as prefix
1. Write your slides using the reveal-md syntax
1. Push on the default branch (`main`) on `origin` (<https://github.com/geotribu/slides/>)
1. The CI/CD build and publish slides on the Github Pages website

----

## Build & serve

This project uses [MkSlides](https://github.com/MartenBE/mkslides/) to convert Markdown into  static HTML.

### Local setup

Requirements:

- Python >= 3.10

Install (typically on Ubuntu):

```sh
python3 -m venv .venv
# on Windows, it should be something like this:
# py -3 -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -U setuptools wheel
python -m pip install .
```

### Build

```sh
mkslides build slides/
```

The generated website is under `site` subfolder.

### Serve locally

```sh
mkslides serve slides/
```

The website is served on <http://localhost:8000> (you can customize the port with `-p` option in case of conflict) and autoreloaded when a file is changed.

----

## Export to PDF

### Print as PDF

By default, you can find an hyperlink on the index pages that generates an [HTML page ready to be print as PDF](https://revealjs.com/pdf-export/). It

### Using decktape

#### With Docker

Here comes an example (replace with your own slides URL and output filename):

```sh
docker run --name decktape --rm  -v "./:/slides" astefanutti/decktape https://geotribu.github.io/slides/2025-02-13_geotribu_introduction_en.html output.pdf
```

You can also specify author, title and subject:

```sh
docker run --name decktape --rm  -v "./:/slides" astefanutti/decktape --pdf-author "Julien Moura (Geotribu)" --pdf-title "Introducing the Geotribu project" --pdf-subject "Slides to introduce the project Geotribu." https://geotribu.github.io/slides/2025-02-13_geotribu_introduction_en.html output.pdf
```
