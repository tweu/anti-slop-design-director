# Anti-Slop Design Director

A Claude skill that acts as a design director for frontend work. It reads the product, chooses a visual direction
that fits it, writes a project-specific DESIGN.md, builds in the project's own stack and then reviews the rendered
result for generic "AI-made" patterns.

It combines what six design resources do best (UIZZE, Impeccable, Taste Skill, UI/UX Pro Max, the Design.md Library
and React Bits) into one curated knowledge base with a single decision-maker. It is not a merge of their files.

## Install
Copy this folder to `~/.claude/skills/anti-slop-design-director` (Claude Code), or upload the packaged `.skill`
file in Claude's skill settings. Start a new session and the skill appears as `/anti-slop-design-director`.

## Usage
```
/anti-slop-design-director redesign the course forum's thread list
/anti-slop-design-director containers=none pills=off build a landing page for our ceramics studio
/anti-slop-design-director visual-direction=editorial animation=minimal density=balanced
```
Or in plain language: "no cards inside cards, pills only for statuses, keep motion minimal."

| Setting | Values (default in bold) |
|---|---|
| containers | none · **selective** · normal |
| pills | off · **functional-only** · expressive |
| visual-direction | **adaptive** · minimal · editorial · brutalist · swiss · premium · experimental |
| animation | minimal · **balanced** · expressive |
| density | compact · balanced · spacious (inferred by default) |
| implementation | conservative · **balanced** · ambitious |
| references | **auto** · user-only · library |

Project-wide settings are saved as a `Director settings:` line in the project's DESIGN.md.

## Architecture
1. **Design Director** (`SKILL.md`): understand → analyze (mode and scope) → select knowledge → direction → rules →
   implement → review.
2. **Knowledge modules** (`knowledge/`): organised by design problem, loaded only when relevant.
3. **Design system engine** (`knowledge/systems/`): DESIGN.md generation in the open DESIGN.md format, plus tokens.
4. **Implementation engine** (`knowledge/core/implementation.md`, `motion/react-bits-guidelines.md`).
5. **Quality control** (`knowledge/evaluation/`, `scripts/slop_scan.py`): render, scan, audit, fix, re-check, with honest reporting.

## Optional companions
If UI/UX Pro Max, Impeccable, UIZZE or a DESIGN.md library is installed, the director uses it as an instrument
(search database, detector, real-screen references, structural examples). It works fully without any of them.

## Scanner
```
python scripts/slop_scan.py src/                 # flag generic patterns
python scripts/slop_scan.py --contrast "#59606E" "#F7F4EE"
python scripts/slop_scan.py --self-test
```
Python 3 standard library only.

## Tests
`evals/` holds three test cases (a forum redesign under `containers=none pills=off`, a new local-business site with
DESIGN.md, and a read-only dashboard audit) in the folder layout `claude plugin eval` reads.

## Licence
MIT (see `LICENSE`). Some principles are paraphrased from Apache-2.0 and MIT works; those portions also
remain under their original licences (`licenses/THIRD_PARTY_NOTICES.md`, `licenses/APACHE-2.0.txt`,
`knowledge/source-map.md`). No React Bits code is bundled.

## Disclaimers
- **No affiliation.** This project is independent. It is not affiliated with, sponsored by or endorsed by the
  authors or owners of UIZZE, Impeccable, Taste Skill, UI/UX Pro Max, the Design.md Library, React Bits, the DESIGN.md
  specification or any other project, product or company it names. All names and trademarks belong to their owners
  and are used only to credit sources.
- **Ideas, not copies.** The knowledge files are an original synthesis of design principles. No source file is
  reproduced. Attribution, versions and commits are listed in `knowledge/source-map.md`.
- **Third-party components and assets.** When the skill suggests React Bits components, fonts, icon sets or photographs,
  you install them from their official sources under their own licences. React Bits components may be used in your
  products but not resold or redistributed on their own (MIT + Commons Clause). Check font, image and icon licences
  before shipping.
- **Generated output.** The skill guides an AI model, and its output can contain mistakes. Review designs, code and
  accessibility before release. Example data, prices and copy the model produces are placeholders unless you supply them.
- **No warranty.** Provided "as is", without warranty of any kind (see `LICENSE`). Nothing here is legal advice.
