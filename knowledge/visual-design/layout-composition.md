# Layout and composition

Layout turns product priority into reading order, grouping, rhythm and usable space. Diagnose the
structural problem before moving boxes around.

## The spatial thesis (state it before editing)
- The primary reading or task path.
- What belongs together and what must separate.
- Which element leads and which ones support it.
- The intended density and spacing rhythm.
- How the structure changes across viewports and content extremes.

## Principles
- **Group by meaning, using proximity first.** Add containers only when proximity and alignment can't do the job.
- **Rhythm is contrast between tight and generous intervals.** One spacing value repeated everywhere
  gives everything equal weight. Put more space above a heading than below it.
- **Use a spacing scale** on a 4px base (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). No one-off values.
- **Hierarchy follows product priority,** not framework defaults. The most important thing is the
  biggest, the first or the most contrasting. Pick one of those per element, not all three.
- **Share edges.** Keep content edges consistent (equal left and right margins on marketing pages)
  and align blocks to grid columns. An off-grid element must look deliberate, not accidental.
- **Topology matches content.** Repeated equal tiles are only for genuinely equivalent items. A
  comparison is a table. A sequence is a list or steps. A story is a column.
- **Variation is not a goal.** Change the form when the content or its priority changes, and keep it
  the same when it doesn't.

## Grids and widths
- Marketing: a 12-column grid, with content max-width around 1120–1280px and full-bleed bands for media.
- Reading: a single column at about 65ch, with optional side margins for notes, a table of contents or metadata.
- Operate: an app shell (sidebar or top bar) with fluid content. Tables can use the full width. Forms are
  about 480–640px wide.
- Asymmetric splits (for example 5/7 or 4/8) read as more composed than 6/6 for text-plus-media.

## Composing a Persuade page
- **First viewport:** say what it is, for whom, with one hard fact and an obvious next action.
  Show the real thing (product UI, photograph or the work), not an abstract blob.
- **Sequence of sections by the reader's questions:** What is it? → Does it do what I need? →
  Can I trust it? → What does it cost? → How do I start? Cut sections that answer no question.
- Each section has one idea, its heading names that idea, and the section is sized to its content.
  Avoid sections that are half empty or that spill a neighbour's heading into a full-screen view. A
  rhythm of roughly one or two screens per section works well for long marketing pages, but treat
  that as rhythm, not a rule.
- Change composition between neighbouring sections: media left or right, full-bleed versus contained, type-led
  versus image-led, a tonal background band.
- One primary action per screen. At most two actions in the hero.

## Composing Operate screens
- Predictable structure is an affordance. Users learn where things are.
- Put the primary task's controls where the eye lands first, and secondary actions in overflow menus.
- Prefer tables and lists over card grids for scanning and comparing.
- Use sticky headers and toolbars when long content needs persistent context.
- See `ux/information-architecture.md` and `visual-density.md`.

## Composing Read screens
- Wayfinding first: breadcrumbs, a table of contents, previous and next links.
- Comfortable measure, strong heading hierarchy, and code or figure blocks that break the column.

## Verify
- The squint test shows primary, secondary and groups in order.
- Long text, empty states, localisation (+30% text length) and zoom don't break the structure.
- DOM and focus order match the visual order.
- Nothing scrolls sideways at 320px.
