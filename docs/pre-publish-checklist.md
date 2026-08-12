# Pre-publish checklist: Enterprise Agentic AI Adoption Compass 2026

Compiled 2026-08-04, from all research passes in this project. Work top to bottom; A blocks publishing, B-D are judgment calls.

## Round 3 (2026-08-10, v15 "Version 1.1"): publish-readiness pass

Closed this round, each verified against a live source on 2026-08-10:
1. arXiv identifiers: all three fetched and title-matched (Kaplan 2001.08361; Gao 2312.10997; Zheng 2306.05685).
2. METR chart: anchors re-verified (GPT-2 2s, doubling ~7 months per metr.org); o3 corrected from ~2h to ~1.5h ("nearly two hours" / 1h30 in METR's GPT-5 comparison), GPT-5 at 2h17 (August 2025) added as a real published point. Deep links now go to metr.org/time-horizons.
3. Timeline dates: NVIDIA $5T close Oct 29, 2025 (TechCrunch); GPT-5 Aug 7, 2025; Gemini 1.5 Feb 15, 2024; IMO gold Jul 2025 (DeepMind and OpenAI); Cursor $2B ARR Feb 2026 (Bloomberg via press). All match the printed timeline.
4. Benchmark spot-check: Fable 5 at 95% SWE-bench Verified and HLE ~53% confirmed across model-card coverage; HLE explainer now notes the text-only vs tool-augmented config difference.
5. Gartner exposure reduced: cover no longer brands "Gartner's first Hype Cycle"; the figure is cited neutrally as (Gartner, 2026). Full rights confirmation still Fabian's call if the stat should stay.
6. Cover credibility line changed to "Research affiliations of the authors" (was "Written by AI researchers from").
7. References: HAI deep links to the 2026/2025 report pages; own-work marked with an asterisk and legend; "links live as of August 10, 2026" note added.
8. About: data-availability sentence added; version bumped to 1.1 (August 10, 2026).
9. New closing CTA on the sequence page with contact address.
10. NDA scan re-run: zero hits for client or interviewee names.

Design v15 (all three editions): cover gradient top bar, radial glow and gradient cells; journey road carries a progress gradient; timeline 2026 dots, dumbbell endpoints, and spark endpoints carry glow rings; all line charts are smooth curves; at-a-glance feature tiles have gradient depth.

Remaining sign-offs that only Fabian can give: (a) Gartner quote rights if the cover stat stays; (b) swap favicon logos for press-kit vectors if the PDF goes to print; (c) freeze the fermisense numbers against the live blog post. Everything else on this list is closed.

## Round 2 review (2026-08-05, after v14: 24 pages, references apparatus)

Fixed in v14:
1. Renaming artifact "Levels Level 0 through Level 3" on the adoption-reality page corrected to "Levels 0 through 3". This was the only surviving text defect found by the sweep (no duplicated words, no double spaces, no placeholders, zero emdashes).
2. The report now has an HAI-style source apparatus: 35 numbered references on a dedicated page 23 (three groups: surveys, academic and technical, standards and leaderboards), 69 superscript citation markers across every exhibit source line, the stat rails, and the moveboxes, clickable links (36 live URL annotations verified inside the violet PDF), a "How to cite this report" block, and a Version 1.0 stamp on the About page.

Still open, blocking before any external send (in priority order):
1. **Gartner citation policy.** The cover quotes Gartner Hype Cycle figures (17 percent deployed, 42 percent planning). Gartner enforces a strict quote policy for non-clients; either confirm usage rights, swap the cover stat for a non-Gartner source, or soften the wording to "industry hype-cycle research". Highest legal-exposure item in the report.
2. **Benchmark spot-check.** SWE-bench Verified 95.0 and HLE 53.3 (Claude Fable 5) come from aggregators (llm-stats.com, benchlm.ai, felloai, cross-checked 2026-08-05); verify once against the lab model card before print.
3. **METR mid-points.** The time-horizon chart's anchor points (GPT-2 2s, o3 ~2h, Opus 4.6 ~12h, both doubling rates) are search-verified; the mid-points (GPT-3 9s, GPT-4 ~5min, o1 ~39min) are from the published METR figure as remembered. Two minutes against metr.org's chart.
4. **arXiv and working-paper identifiers.** References 16, 19, 20 carry arXiv IDs (2001.08361, 2312.10997, 2306.05685) and reference 18 carries HBS WP 24-013; all four from memory with high confidence, unverifiable from the build sandbox. Click each once.
5. **Deep links.** By design, reference URLs point at domains, not documents (avoids inventing paths). Before publishing, upgrade the ten most-cited entries (1, 3, 6, 7, 8, 16-18, 21, 28) to exact document URLs.
6. Existing round-1 blockers remain: timeline date spot-checks (A1-A2), fermisense freeze (A3), logo rights and the "Written by AI researchers from" endorsement wording (A5), final NDA scan (A6), McKinsey disclaimer comfort (A7).

Structural gaps an academic reviewer would still raise (not blocking, worth deciding):
1. No per-figure data availability note: HAI publishes underlying data; we could add one line to About ("underlying event list and level estimates available on request").
2. Self-published references (21, this report's own fermisense post) carry the same weight as peer-reviewed work in the list; consider marking authors' own work with an asterisk.
3. The benchmark page mixes access-dated leaderboard scores with April 2026 AI Index scores; the footnote says so, but a reviewer may still ask for one consistent as-of date.
4. The exhibit numbering is consulting style (Exhibit 1-22 continuous); HAI numbers per chapter. Fine as a hybrid, but it is a visible style choice, not an oversight.

## A. Verify before publishing (facts, rights, claims)

1. **Timeline dates spot-check.** Four entries added from general knowledge rather than this project's verified pool: NVIDIA $5T (Oct 2025), IMO gold (Jul 2025), GPT-5 (Aug 2025), Gemini 1.5 1M context (Feb 2024). Two minutes each against primary announcements.
2. **Cursor $2B run rate (Feb 2026)** came from our verified margins research; re-confirm the number and date once against the original TechCrunch reporting before print.
3. **fermisense numbers freeze.** The intelligence-ownership page mirrors the blog (87.3 / 76.9 / 40x / 68x / 340x / $500 / 2.2x Ramp). If the blog post gets edited, the report must follow; decide which is canonical.
4. **Anthropic report citation.** We quote page 3, 8, and 44 figures; the PDF is a public marketing report, quoting stats with attribution is fine, but confirm you are comfortable citing it while it brands "Claude" prominently.
5. **Logo rights pass.** Favicon-based logos are fine internally; for a public PDF replace the top ~20 with official press-kit vectors (most vendors host brand pages), or add "logos via public favicons" to the disclaimer. Institution logos (Stanford, TUM, HEC, WU, CDTM) on the cover imply endorsement to some readers; consider "Research affiliations of the authors" as the label instead of "Written by AI researchers from".
6. **NDA scan.** Confirmed clean of Ravensburger and person-level quotes, but run one final search for "Ravensburger", client names, and interviewee names before any external send.
7. **McKinsey-style disclaimer.** Present on cover and About page of the navy edition; keep it in the violet edition too (it inherited it). Legal comfort check if the report goes truly public.
8. **"Median enterprise" and level-distribution estimates** are authors' synthesis; they are labeled as such, keep the labels if you edit.
9. **Self-report vs neutral framing.** The evidence page deliberately contrasts Anthropic 80% ROI with AI Index single-digit scale; read it once as an Anthropic partner would, confirm the tone is fair.
10. **Emdash and Level-naming sweep** after any manual edit (the build scripts enforce both; manual edits will not).

## B. Questions executive readers will ask that the report does not yet answer

1. **"How much should this cost me?"** No spend benchmarks per level or company size. Even a band ("typical Level 3 org: $1-5M across 3+ vendors") would be the most-used number in the report.
2. **"What return, by when?"** No payback windows. Candidate anchors: Anthropic 80% self-reported ROI, J&J 10-15% of use cases drive 80% of value, specialist-model unit economics.
3. **"Where do I start on Monday?"** The 90-day plan says how; a use-case selection filter is missing (structured, measurable, high-volume, low blast radius, data accessible).
4. **"Build or buy?"** The stack pages list vendors without a decision rule; the Anthropic 47% hybrid stat is the seed for a half-page rule per layer.
5. **"What does this mean for my people?"** Headcount, reskilling, hiring: touched in Layer 9, never answered. The AI Index entry-level data (-20% young developers) is the sharp edge here; decide if you want it in.
6. **"How do we compare to peers in our industry?"** No industry cuts. This is the benchmark-flywheel gap and also your GTM hook: "take the assessment".
7. **"What happens if we do nothing?"** No cost-of-inaction page; the Ramp 2.2x vs 15% revenue split is the strongest available anchor and is already in the report, just not framed as inaction cost.
8. **"When should we NOT use AI?"** A short negative-space list would add more credibility than any additional bull case.
9. **"Who should own this?"** Named owner per agent is in; C-level ownership and operating cadence (who chairs the AI council, what the monthly review looks like) is not.

## C. Trending exhibits and data you are currently not using

1. **Anthropic Economic Index automation-vs-augmentation shift** (27% to 39% directive in 8 months; first time automation exceeds augmentation): one-line chart, very current, fits the journey or evidence page.
2. **KPMG quarterly agent-deployment line** (11% to 53% in five quarters, then plateau; orchestration doubling 9% to 18%): the only longitudinal agent series anywhere; natural for the adoption-reality page.
3. **Inference price-collapse curve** (280x in 2 years, AI Index 2025): the most viral AI-economics chart of the period; currently only text in the laws sidebar.
4. **Incident curve** (AI Incident Database 362 in 2025, +55%; response confidence falling 28% to 18%): strengthens the identity layer with a trend, not a snapshot.
5. **Adoption S-curve 55/78/88%** (AI Index): the canonical backdrop chart; currently cited in text only.
6. **Productivity jaggedness table** (+55% accountants, +26% developers, -19% experienced open-source devs; gains "largest in structured, measurable work"): the by-function ROI evidence, pairs perfectly with your jagged pages.
7. **Energy per prompt** (5-23 Wh per medium prompt, AI Index 2026): sustainability question is rising in EU boardrooms; one stat inoculates the report.
8. **RAI maturity 2.3 of 4 global average** (AI Index/McKinsey): a sister maturity scale, good About-page crosswalk.
9. **"Workslop" and verification-burden research** (low-quality AI output shifting work to reviewers): very current discourse; a candidate for the evals layer.
10. **Forward-deployed engineering** as the adoption motion (OpenAI and the labs embedding engineers with customers): one paragraph in the sequence section; it is also literally your design-partner model.

## D. Distribution polish

1. One-page social teaser: the journey graphic plus three stats, exported separately.
2. German edition decision (DACH pipeline vs maintenance cost of two languages).
3. Real Bower-alternative licensed fonts if the navy edition goes to print; the violet edition already stands on Charter and Avenir Next.
4. Pick the lead edition: navy for consulting-adjacent audiences, violet for founders, press, and community; do not circulate both to the same list.
5. Version stamp and changelog line on the About page once external (v1.0, date, contact).

## Round 4 (2026-08-10, v16): de-AI editorial pass
Applied with the frontend-design skill as guide (the requested "impeccable" skill is not installed in this environment). Colon-pattern titles cut from nine to two; the "X, not Y" construction thinned from twelve to the seven strongest; "is no longer X. It is Y" and "highest-leverage" rewritten; cover gradient accent bar removed (glow and gradient cells stay); one italic analyst aside added under the level-distribution exhibit. No figures, sources, or page counts changed; still 24 pages, three editions, Version 1.1.
