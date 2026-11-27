# Colour systems

Colour is hierarchy, meaning and atmosphere. Build roles, not a bag of swatches.

## Roles
- **Canvas and surfaces:** background plus 1–3 elevation levels.
- **Text:** primary, secondary and muted (the muted role must still pass contrast for its use).
- **Action:** primary action, hover, pressed, focus ring, selection.
- **Borders and separators:** subtle and strong.
- **Semantic:** success, warning, error and info, each with a text-safe and a tint variant.
- **Data:** categorical and sequential scales when charts exist.
- **Brand accent:** only if it differs from action. Often action *is* the brand colour.

## Strategy
Decide before choosing hues:
- **Temperature:** warm, cool or neutral, from the direction's world.
- **Dominant relationship:** ink on paper, light on dark, colour-blocked regions, or photography-led
  with neutral UI.
- **Dosage:** in Operate and Read, the accent is rare so that it has force (action, selection, unread).
  In Persuade and Experience, colour may own large regions when the world calls for it.
- Choose hue from product meaning and brand, never from category habit ("finance is blue, eco is green").

## Building the palette
- For new web palettes, prefer **OKLCH**, where lightness and chroma behave predictably. Build ramps by
  stepping lightness and reducing chroma near white and black.
- Neutrals: tint them toward the brand hue only when that creates cohesion. Pure neutral grey is
  also valid.
- On coloured surfaces, derive secondary text from the surface's hue, not a washed-out generic grey.
- Prefer explicit colours over stacks of translucent overlays, whose contrast changes with context.
- Light and dark themes are each composed. Don't invert mechanically. In dark themes, express elevation
  with lighter surfaces rather than shadows, and lower the saturation of large accents.
- Choose light or dark from the scene of use, not the category.

## Contrast (always, all states, both themes)
| Content | WCAG AA |
|---|---|
| Body text, placeholders that convey info | 4.5:1 |
| Large text (≥24px, or ≥18.66px bold) | 3:1 |
| UI components, icons, focus indicators | 3:1 against adjacent colours |
Check hover, disabled (exempt, but it should still be legible), text on images and overlays. Colour
is never the only signal: add text, icons, shape or position. For data, vary lightness as well as hue.

## Slop signals in colour
Purple-blue gradients by default · gradient text · neon on black for "tech" · several unrelated
accents · saturated colour on large areas without intent · grey text on coloured backgrounds ·
pure #000 on pure #FFF across large reading areas (slightly soften one or both).

## Quick token shape
```css
:root {
  --color-canvas: oklch(98.5% 0.005 85);
  --color-surface: oklch(100% 0 0);
  --color-text: oklch(22% 0.02 260);
  --color-text-muted: oklch(45% 0.02 260);   /* verify ≥4.5:1 on canvas */
  --color-border: oklch(90% 0.01 260);
  --color-action: oklch(48% 0.16 255);
  --color-action-hover: oklch(42% 0.16 255);
  --color-focus: var(--color-action);
  --color-danger: oklch(52% 0.19 27);
}
```
The values are illustrative. Derive real ones from the direction. Palette starting points are in
`references/color-palettes.md`. If installed, UI/UX Pro Max has `--domain color`.
