# Layer co-author tracker — Enterprise Agentic AI Adoption Compass 2026

Goal: every layer page featured by a practitioner startup founder. Status as of August 11, 2026 (report v1.2). Edit freely; the "Candidates" column is seeded from companies already on that page's market map.

| Page | Layer | Status | Co-author | Company | LinkedIn | Photo | Candidates to approach | Next step / notes |
|---|---|---|---|---|---|---|---|---|
| 11 | Models and inference | COMMITTED | TBD | Lyceum | | no | — | Get founder name, title, square headshot, company domain for logo |
| 13 | Orchestration and architecture | FILLED | Jakob Mayer | OSM Data | [/in/ja-may](https://www.linkedin.com/in/ja-may/) | yes | — | Confirm title: report says "Founder and CEO", LinkedIn says Co-Founder |
| 14 | Knowledge, context, and memory | FILLED | Justinas Zaliaduonis | fermisense | [/in/justinz](https://www.linkedin.com/in/justinz/) | yes | — | Authors' lab; disclosed on page 3 |
| 15 | Tools and actions | OPEN | — | — | — | — | Composio, Arcade, Smithery | |
| 16 | Computer use and reinforcement learning (deep dive) | FILLED | Ingmar Klein | Huzzle Labs | [/in/ingmar-klein](https://www.linkedin.com/in/ingmar-klein/) | yes | — | |
| 17 | Identity, permissions, and security | COMMITTED | TBD | Kontext | | no | — | Get founder name, title, square headshot, company domain for logo |
| 18 | Deployment and operations | OPEN | — | — | — | — | E2B, Modal, Daytona, Runloop | |
| 19 | Observability and cost | OPEN | — | — | — | — | Langfuse, Helicone, AgentOps, Vantage | |
| 20 | Evals and improvement | OPEN | — | — | — | — | Braintrust, Patronus AI, promptfoo | |
| 21 | People and operating model | OPEN | — | — | — | — | DX, Worklytics, Sana | |

Not tracked: page 12 (intelligence-ownership deep dive) is the authors' own fermisense work by design.

## Suggested status ladder

OPEN → APPROACHED (date) → COMMITTED (quote/photo promised) → FILLED (in the report)

## How a slot gets filled (mechanical)

1. Drop the headshot in `agentic-stack-report-2026-08-03/coauthors/` as `firstname-lastname.jpg` (square crop, 100px+).
2. Tell Claude the name, role, company, and page — the placeholder strip is swapped for the filled pattern and all three editions re-render; or edit `report-source*.html` yourself: replace the "Open slot" `.coauth` div on that page with the filled pattern used on pages 13/14/16, then run `render.sh`.
3. Optional per co-author: one practitioner quote or "the move" contribution on their page gives them real authorship beyond the credit strip.

## Pitch line that has worked

"Your company already appears on the market map of this page; the co-author strip adds your face and name as the practitioner voice of the layer. Takes one photo and one review pass of the page."
