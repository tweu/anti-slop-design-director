# Anti-UI-slop engine

"Slop" is what comes out when no decision was made: the statistically average interface. These
patterns are **warnings, not bans**. Each one is fine when the product, the brief or a setting
justifies it. Your job is to notice when you reach for one without a reason.

## The test for any pattern
1. **What does it communicate or enable here?** "Looks modern" or "fills space" isn't an answer.
2. **Would this product's real users miss it?**
3. **Is it here because I chose it, or because it's the default?**
If it fails, don't replace it with the *next* default (cards become identical bordered rows, and
those become identical numbered steps). Fix the underlying problem: missing content, weak hierarchy
or no direction.

## Generic layouts
| Pattern | Why it reads as slop | Usually better |
|---|---|---|
| Three-column icon + title + text feature grid | Equal weight says nothing is more important | Lead with the one feature that matters, shown big as real UI; list the rest compactly |
| Bento grid with no reason for its tile sizes | Tile size must encode importance; random sizes encode nothing | Size by priority, or a simple list |
| Centered hero with a pill, H1, subline, two buttons and a gradient blob | The single most common AI hero | A composition built from the product: the UI itself, a photograph, a type-led statement, an asymmetric split |
| Every section with the same structure (heading, sub, grid) | Monotony; the page has no rhythm | Vary form when content changes: a full-bleed image, a table, a quote, a long-form block |
| Hero-metric template (big number, label, three supporting stats) | Invented-looking proof | Real numbers with sources, inside the context they prove |
| Floating decorative elements, orbs, blobs | Noise with no meaning | Delete, or replace with real content |
| Excessive empty space | Mistakes "premium" for "sparse" | Space sized to grouping: tight within groups, generous between |
| Logo strip, testimonial carousel and FAQ accordion by reflex | Template sections | Include only with real logos, real quotes and real questions |

## Generic aesthetics
- Purple-to-blue (or teal-to-violet) gradients as the default accent. **Gradient text** for emphasis
  (use weight or size instead).
- Glassmorphism and backdrop blur as decoration rather than as a specific layered effect.
- A soft drop shadow on everything. Zero-offset coloured glows. Hard offset shadows outside a
  brutalist direction.
- A border on every container *plus* a background tint *plus* a shadow (three signals where one would do).
- Default font stacks used as an identity (Inter or the system UI font for a Persuade display voice),
  or the "AI pairing" of a geometric sans with a mono label for everything.
- Monospace as a "technical" costume rather than for code, data or measurement.
- Random accent colours, more than one accent with no role, and saturated colour on large areas without intent.
- Large radii on everything (24px+ on cards, inputs and buttons alike) and pill-shaped everything.
- Dark mode with neon accents chosen because the product is "tech".
- Emoji or Unicode glyphs standing in for an icon system.
- "Futuristic" grids, scanlines and particles with no product reason.
- A coloured bar down one side of a rounded box as an accent.

## Component overuse
- Cards inside cards (governed by `containers`), and pages built entirely of cards.
- Badge or pill confetti: "New", "Beta", "AI", "Popular" on many items (governed by `pills`).
- An eyebrow label above every heading. Section numbers (01/02/03) when order carries no meaning.
- An icon in a tinted rounded square before every heading or list item.
- Floating action buttons, chat bubbles, "back to top" squares and toasts nobody triggered.
- Controls that do nothing (decorative tabs, fake toggles, play buttons with no media).
- Sparklines, progress rings and charts with no real data behind them.
- Modals for tasks that need neither interruption nor protected focus.

## Copy slop (it affects design as much as visuals)
- Headlines that describe a mood instead of the product ("Unlock your potential").
- Buttons that say "Get started" or "Learn more" everywhere. A button should be a verb plus an object
  ("Book a table", "Compare plans").
- Invented testimonials, customer logos, user counts and uptime figures.
- Filler sublines that restate the headline.

## Structural replacements to reach for
When you remove a slop pattern, separate and emphasise content with:
**typography** (scale, weight, case, a second face for one role) · **space** (rhythm between
tight and generous) · **alignment and grid** (shared edges, asymmetric columns) · **rules and
dividers** · **background bands** (a tonal shift between sections) · **real media** (product UI,
photographs) · **tables and lists** for comparable items · **position** (what comes first matters most).

## Signals that a whole page is slop
- You could swap in another product's name and nothing would look wrong.
- The squint test shows a uniform grid of equal blobs.
- Every section enters with the same fade-up animation.
- The only colour on the page is the gradient.
- No element on the page could only belong to this product.
Detection procedure: `evaluation/anti-patterns.md`. Mechanical scan: `scripts/slop_scan.py`.
