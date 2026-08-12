# Enterprise Agentic AI Adoption Compass 2026

A 24-page executive report: seven adoption levels (0-6) by nine stack layers, with market maps, a benchmark map, and a 90-day crossing sequence. Version 1.2 (August 11, 2026). Authors: Fabian Hildesheim and Joel Hainzl, with layer co-authors.

## Editions

| File | Look | Audience |
|---|---|---|
| `dist/compass-2026-blue-violet.pdf` | Charter/Avenir, violet | founders, press, community (lead edition) |
| `dist/compass-2026-navy.pdf` | classic consulting grammar | consulting-adjacent readers |
| `dist/compass-2026-violet-gold.pdf` | violet with gold accents | experimental |

## How it works

- `src/report-navy.html` is the **master**. The violet and gold editions are **generated** from it - never edit them by hand.
- `render.sh` regenerates the editions, renders all three PDFs (needs Google Chrome on macOS), and runs the layout check.
- `tools/margin_scan.py` fails if any page's content intrudes into the bottom margin - run it after layout changes.
- Assets: `src/logos/` (vendor favicons), `src/inst/` (institution marks), `src/coauthors/` (co-author photos, 100px+, square).

## Collaborating

1. Text and data edits: edit `src/report-navy.html`, run `./render.sh`, commit source + PDFs.
2. Adding a layer co-author: photo into `src/coauthors/firstname-lastname.jpg`, replace the "Open slot" strip on that layer page with the filled pattern (see pages 13/14/16 in the source), re-render. Tracker: `docs/coauthor-tracker.md`.
3. Before any external send, work through `docs/pre-publish-checklist.md` - the open sign-offs are at the top.
4. House rules: no em dashes anywhere; every stat carries a source and date; levels are written "Level 0" through "Level 6"; run the margin scan before pushing layout changes.

## Docs

- `docs/pre-publish-checklist.md` - verification status and open sign-offs
- `docs/coauthor-tracker.md` - layer co-author recruitment status
- `docs/page-reviews-2026-08-10.md` - 24-agent per-page review (strengths / weaknesses / missing)
- `docs/changes.json`, `docs/maps-research.json` - review synthesis and market-map research

Private working repository. Statistics reproduced with source and date; company logos appear for identification only; the format follows the exhibit conventions of management-consulting publications and this document is not affiliated with or endorsed by McKinsey & Company.
