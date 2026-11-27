# Source map

The research behind this knowledge base, recorded so it can be re-verified and updated. The knowledge files are an
original synthesis. No source file was copied wholesale. Paraphrased principles are attributed here.

Research date: **2026-11-28**.

## Sources inspected

| Source | Licence | Version inspected | Files actually read | Unique contribution |
|---|---|---|---|---|
| **UIZZE** (github.com/uizze/uizze) | MIT (repo); its `anti-ui-slop`/`ui-design` skills are Apache-2.0 adaptations of Impeccable | plugin 1.3.1; repo HEAD `fc401e9` | `skills/anti-ui-slop/SKILL.md`, `reference/{craft,distill,polish,audit,new-work}.md`, `skills/ui-radar/SKILL.md`, `skills/uizze-ui/SKILL.md`, NOTICE | Work-from-the-product stance; "warnings not bans" framing of habitual patterns; design contract; finish loop with honest verification; real-screen evidence (0–3 references, structural lesson, untrusted data) |
| **Impeccable** (github.com/pbakaus/impeccable) | Apache-2.0 | plugin 4.11.0; repo HEAD `2fc5e14` | `SKILL.md`, `reference/{craft-floor,layout,typeset,colorize,foundations}.md`; command table for the rest | Surface modes (Persuade/Operate/Read/Experience); "brief wins"; refinement vs redesign; craft floor (contrast, depth, spacing, type limits, browser surfaces); two-assessment method (judgement + mechanical scan); colour roles with OKLCH; typography line-break and optical rules |
| **Taste Skill** (github.com/Leonxlnx/taste-skill) | MIT | 2.5.1; repo HEAD `952435f` | `SKILL.md`, `references/{layout-v4,motion,copy}.md` (opening sections); reference index | Business kind decides the visual vocabulary; effects only where the trade is technical; the three motion layers (entrance, one moment, hover), with every motion having a purpose; copy rules (h1 names the category, verb + object buttons, nothing invented); real photographs and real product UI; anti-repetition across projects |
| **UI/UX Pro Max** (github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | 2.15.0; repo HEAD `11ca2b3`; data verified 2026-11-04 | `.claude/skills/ui-ux-pro-max/SKILL.md`, `data/catalog-summary.json`, data and reference listings | Priority-ordered rule categories (a11y → touch → perf → style → layout → type/colour → motion → forms → nav → charts); query contract (one intent, 2–5 terms, retry once, never fabricate a 0-result search); density/variance/motion dials; searchable database (80 styles, 194 palettes, 74 pairings, 141 UX rules, 25 charts, 22 stacks), used as an optional instrument and not duplicated |
| **Design.md Library** (github.com/albemala/design-md-library) | MIT | repo HEAD `b77c816` | README, `design-md-spec/spec.md`, `.agents/skills/lint-and-fix-design-md/SKILL.md`, `design-md/enterprise-saas/DESIGN.md`, directory listing (14 systems) | DESIGN.md format (YAML tokens + eight ordered H2 sections, `{token.path}` references, `npx @google/design.md lint`); structural examples per product category |
| **React Bits** (github.com/DavidHDev/react-bits) | MIT + Commons Clause | repo HEAD `a30a9da` (2026-11-26) | README, LICENSE.md, `package.json`, `src/content/*` listing (component names), registry JSON for SplitText, Aurora and SpotlightCard | Catalogue of about 215 animated components in 5 categories; install via shadcn/jsrepo in 4 flavours; registry JSON exposes dependencies; licence forbids redistributing the components |

Not inspected in depth: Impeccable's other ~40 reference files, Taste Skill's remaining references and asset kits,
UI/UX Pro Max's CSV contents, the other 13 DESIGN.md examples and React Bits component source beyond three registry
entries. Rules here don't claim to reproduce those files.

## Topic → contributing sources
| Knowledge file | Main sources |
|---|---|
| core/design-philosophy | Impeccable (modes, brief wins, refine vs redesign), UIZZE (work from product, verify), Taste (real material) |
| core/anti-ui-slop | Impeccable craft-floor "Refuse" list, UIZZE "habitual design", Taste "Never" list, copy rules |
| core/decision-hierarchy | Original synthesis. Conflicts drawn from all six |
| core/settings | User brief (settings spec), UI/UX Pro Max dials (density/motion) |
| core/implementation | UIZZE uizze-ui build steps, UI/UX Pro Max stack detection, Impeccable browser surfaces |
| visual-design/* | Impeccable (typeset, colorize, layout), Taste (layout rhythm, sections), UI/UX Pro Max (priorities) |
| ux/* | UI/UX Pro Max (UX categories), UIZZE (states, audit), Impeccable (operate/read) |
| components/* | Impeccable (cards, depth, radius), Taste (one system, hover layer), user brief (settings) |
| motion/* | Taste (three layers, purposes, never-list), Impeccable (one authored moment, easing), React Bits (catalogue, install) |
| systems/* | Design.md Library (format, lint), Impeccable (document from code), UI/UX Pro Max (master + overrides, tokens) |
| evaluation/* | Impeccable (two assessments, detector), UIZZE (audit, finish loop), Taste (checklist, honest gate) |
| references/* | Original curation. React Bits names from its repo. Fonts from Google Fonts |

## Updating
Re-check each repo's HEAD and licence, read the changed core files and update only the principles that changed.
Keep this table's versions current.
