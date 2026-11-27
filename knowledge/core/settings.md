# User-controlled settings

Settings are the user's explicit preferences (priority 1 in the decision hierarchy). Apply them to
every surface you touch, and record project-wide choices in DESIGN.md (see below).

## containers (nested cards)
- **none**: never put a box inside a box. Separate content with whitespace, type scale, dividers,
  background bands, alignment and full-bleed sections. A page may still use single-level cards
  for genuinely repeated, clickable objects (products, posts). If even that feels wrong, list rows
  with dividers work.
- **selective** (default): cards exist when they represent a discrete object the user acts on, or
  when they group controls that move together. Nesting is allowed only when the inner element is a
  distinct object type (a code block, a media embed, an editable row). Decorative nesting is never allowed.
- **normal**: standard card usage, with nesting where appropriate. Still check hierarchy and avoid
  an all-cards page.

## pills
- **off**: no pill shapes for labels. Use text labels, small caps, coloured text, dots plus text, or
  standard controls (selects, segmented controls with modest radius). Buttons are not pill-shaped.
- **functional-only** (default): pills only for meaningful status, filters, categories, tags and
  input chips. Never decorative ("New!", "✨ AI-powered" above a heading). Keep it to one pill style.
- **expressive**: pills may be part of the identity (pill buttons, pill nav). Use one shape
  language consistently, chosen on purpose.

## visual-direction
- **adaptive** (default): derive the direction from the product (`visual-design/art-direction.md`).
- **minimal**: few elements, a strong type scale, a restrained palette, and precision over decoration.
  This is not "empty": every screen still needs a clear point and real content.
- **editorial**: type-led, with a strong display face, column structures, pull quotes, rules and
  generous measure. It reads like a well-made publication.
- **brutalist**: exposed structure, raw grids, system or grotesque type, hard edges and visible
  borders. Hard offset shadows are allowed here and only here. Usability stays intact.
- **swiss**: a strict grid, flush-left grotesque type, asymmetric balance and colour as signal.
- **premium**: restraint, material quality, precise spacing, refined serif or grotesque type,
  photography-led, low saturation and slow motion.
- **experimental**: unconventional composition, type or interaction. It needs a clear concept, still
  has to be usable, and works best on Experience/Persuade surfaces.
A direction the user names overrides the mode's defaults on aesthetics, but not on usability.

## animation
- **minimal**: state feedback only (hover, press, focus, open/close), 100–200 ms, with no entrances
  and no scroll effects.
- **balanced** (default; Operate surfaces drop to minimal unless the user asked): feedback plus
  one hero entrance on Persuade pages and purposeful transitions between states. One authored
  moment at most.
- **expressive**: an authored motion language, a signature moment or two, and React Bits effects
  when justified. Still respect reduced motion and performance budgets.

## density
- **compact**: an 8–32px spacing range, 13–14px secondary text, tables over cards. Good for
  expert tools and dashboards.
- **balanced**: a 16–64px range.
- **spacious**: a 24–128px range, large type and few items per viewport. Good for premium and editorial
  marketing pages. Spacious doesn't mean sparse; every screen still carries content.
If unset, use compact or balanced for Operate, balanced for Read and balanced or spacious for Persuade and Experience.

## implementation
- **conservative**: no new dependencies, minimal file churn, reuse existing components, and CSS-only
  motion.
- **balanced** (default): small, justified dependencies after checking compatibility. New
  components where the system needs them.
- **ambitious**: custom components, WebGL or React Bits effects and bigger structural changes when
  they serve the direction. Still state each dependency and its cost.

## references
- **auto** (default): use real-product references or style libraries when they would change a
  decision, and skip them otherwise.
- **user-only**: use only what the user supplied. Don't fetch or browse libraries.
- **library**: actively consult the installed style or DESIGN.md libraries and UI/UX Pro Max
  data before choosing the direction.

## Persistence
After a DESIGN.md exists, record the project's standing settings as one line in its Overview
section, for example:

`Director settings: containers=none · pills=functional-only · visual-direction=editorial · animation=minimal · density=balanced`

Read that line at the start of later tasks. Settings given in a request apply to that task. Update
the line only when the user says the change is permanent ("from now on…") or when you are creating
or redesigning the system.
