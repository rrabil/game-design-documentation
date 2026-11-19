# Calydon: High-Level Design Document

A docs-as-code web edition of my 2011 game design document for *Calydon*, an action-adventure RPG built on the Neverwinter Nights Aurora Toolset.

**Live site:** https://rrabil.github.io/game-design-documentation/

Built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme. Each section of the document is one Markdown file in `docs/`. The sidebar order is set in `mkdocs.yml`.

## How publishing works

Every push to `main` runs the GitHub Actions workflow in `.github/workflows/deploy.yml`. It installs MkDocs, builds the site with `mkdocs build --strict` (which fails on broken internal links), and publishes the result to GitHub Pages.

## Preview locally

```
pip install -r requirements.txt
mkdocs serve        # opens a live preview at http://127.0.0.1:8000
```

## Where the content came from

The section pages were first generated from the original Word document with [pandoc](https://pandoc.org/), using the scripts in `_source/` (`clean.lua` flattens table cells and strips Word formatting; `split.py` splits the document into one numbered page per section). After that first pass, the Markdown files are the source of truth and are edited by hand. The Word file stays local.

The activity diagrams in Section 6 were redrawn as [Mermaid](https://mermaid.js.org/) diagrams, so they live in the Markdown as text. Figure 4 is a crop of the original PDF, because its numbered callouts were drawn in Word on top of the screenshot.

## Notes

- Material for MkDocs has announced end of life on May 5, 2027. Its successor, [Zensical](https://zensical.org/), reads the same `mkdocs.yml`.
