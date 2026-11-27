# Decision hierarchy and resolved conflicts

## Priority order
When two recommendations disagree, the higher one wins:

1. Explicit user requirements, including the settings.
2. Product requirements and real user needs.
3. Existing project architecture and constraints: stack, components, brand, DESIGN.md.
4. Usability, accessibility and performance.
5. The project-specific design system.
6. Context-dependent design recommendations (this knowledge base).
7. General aesthetic preferences, including your own habits.

A user requirement can override an aesthetic warning ("I want a purple gradient hero" means you
build a good one). It cannot quietly break accessibility. If a request would fail contrast or
keyboard access, implement the intent in the nearest accessible way and say what you changed.

## How to read rules in this knowledge base
Most rules are **warnings with a context**, not bans. Each says when it applies. Before you apply
one, check:
- **Mode:** a Persuade rule doesn't automatically apply to Operate.
- **Scope:** refine and extend inherit the existing world, while new work chooses one.
- **Settings:** containers, pills, animation and density override defaults.
- **Product:** does the reason behind the rule hold for this product?

A small set of things is **always a defect**, whatever the context: text below contrast minimums,
lost keyboard focus, content that is hidden without motion or JavaScript, horizontal scroll on
mobile, invented proof or data, broken states, and controls that do nothing.

## Resolved conflicts between the sources

| # | Conflict | Resolution |
|---|---|---|
| 1 | **Section height.** Taste wants every marketing section to be exactly one or two screens tall, while Impeccable/UIZZE say Operate and Read need predictable, content-sized structure. | One-section-per-screen is a *Persuade rhythm option* for full-page marketing sites. It never applies to dashboards, docs, forums or app UI. Even on Persuade pages, let content decide height. Avoid half-empty screens and sections that spill into the next one. |
| 2 | **Violet.** Taste bans violet outright; Impeccable says "the brief wins". | Violet/purple-blue *as a default* is a slop signal. A brand colour, a user request or a product reason makes it legitimate. Build it with care (OKLCH ramps, no neon-on-black by habit). |
| 3 | **Nested cards.** Impeccable calls nested cards "always wrong", while the user can set containers=normal. | The `containers` setting decides. The default `selective` allows nesting only where the inner box is a distinct object (such as a code block inside a doc card, or a row editor inside a settings panel). Decorative nesting is always flagged. |
| 4 | **Eyebrow labels over headings.** Impeccable bans them outright; other sources are silent. | Treat as a strong warning. A small kicker above every heading is a generic tell. Keep one only when it carries real information (a category in an article header, a step in a flow) or the brand uses it. Never use them as a section pattern. |
| 5 | **Motion amount.** Taste requires a hero entrance, a scroll moment and a hover layer on every page; Impeccable wants restraint on Operate surfaces. | The `animation` setting and the mode decide. Every interactive element still gives feedback (hover, press, focus) in every mode, because that is affordance, not decoration. Entrances and "moments" are for Persuade/Experience, at `balanced` or `expressive`. |
| 6 | **Choosing by random deal vs by judgment.** Taste deals palettes and heroes randomly to force variety. | Decide by the product. Use variety only to break ties between options that fit equally well. Never pick the same hero or palette as the previous project just because it is familiar. |
| 7 | **Body size.** UX Pro Max says 16px base and 1.5 line height; enterprise DESIGN.md examples use 14px body. | Prose and reading surfaces use 16px or more. Dense Operate surfaces (tables, sidebars, metadata) may use 13–14px when contrast is high and zoom works. Inputs are 16px on mobile to avoid iOS zoom. |
| 8 | **System font.** UIZZE says a system font fits product UI; Impeccable calls a system display face on an own-world page a failure. | Operate: a well-tuned system or neutral UI face is fine. Persuade/Experience display type: choose a face with character that matches the direction. |
| 9 | **Shader/WebGL backgrounds.** React Bits offers 60+; Taste restricts effects to tech, gaming and software. | Effects are reserved for products with a technical or experiential subject, at `animation≥balanced` and `implementation≥balanced`. Use at most one per page, never behind body text, and always with a static fallback. Local businesses, services and Operate surfaces get photographs, type and colour instead. |
| 10 | **Tilt, carousels, timed tabs.** Taste forbids them; React Bits ships TiltedCard and several carousels. | Rejected by default. A carousel is allowed only when browsing a set is the task (such as a product gallery), with visible controls and no autoplay. Tilt is allowed only with `animation=expressive` on Experience surfaces. |
| 11 | **Database recommendations.** UX Pro Max's design-system generator recommends styles such as glassmorphism and bento for many products. | Generator output is a candidate list. Run it through anti-ui-slop and the product test before adopting anything. |
| 12 | **DESIGN.md structure.** The brief's long section list conflicts with the Google DESIGN.md spec's fixed order of eight H2s. | Keep the spec's eight H2s in order so linters pass. Put detailed topics (buttons, forms, navigation, tables, pills, motion, responsive, accessibility, anti-patterns) as H3s under Components, Layout and Do's and Don'ts. See `systems/design-documentation.md`. |
| 13 | **Light vs dark.** Category habit says "dev tools are dark, wellness is light". | Pick light or dark from the scene of use: who uses it, where and in what light. Offer both when the product is used all day. |
| 14 | **Real photos vs drawn visuals.** Taste demands real photographs; other sources are neutral. | Show the real thing: product UI for software, photographs for places and physical goods. Use licensed stand-ins only when the client has none, and list them as stand-ins. Never use decorative illustration in place of missing substance. |
