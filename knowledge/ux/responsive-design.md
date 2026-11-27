# Responsive design

Responsive decisions are structural. Decide what stacks, collapses, scrolls, hides behind
disclosure or stays fixed, based on what remains important at each size.

## Widths to design and test
320 (minimum) · 390 (phone) · 768 / 820 (tablet portrait) · 1024 (tablet landscape, small laptop) ·
1280–1440 (desktop) · 1920+ (wide; cap the content width, don't stretch the text).

## Strategy
- Start from the content. Breakpoints go where the layout breaks, not at device names. Mobile-first CSS
  usually produces simpler overrides.
- Prefer intrinsic layouts (`grid-template-columns: repeat(auto-fit, minmax(…))`, `clamp()`,
  `min()`) and **container queries** for components used in several contexts.
- Fluid type for display (`clamp(2.5rem, 5vw + 1rem, 5.5rem)`). Use fixed role sizes for UI and body text.
- Never fix a container width in pixels without a `max-width: 100%` escape.

## Patterns by component
- **Navigation:** horizontal links collapse into a menu button with a full-screen or drawer menu on mobile.
  App sidebars become a bottom bar (5 items or fewer) or a drawer.
- **Text and media splits:** stack with text first, unless the media *is* the message (a product photo, the work).
- **Tables:** on narrow screens, either scroll horizontally inside a labelled container with a sticky first column,
  or reflow into stacked label and value rows. Don't hide columns silently.
- **Card grids:** go from 3–4 columns to 2 and then 1. Check that the cards still make sense at full width.
- **Forms:** one column, inputs at least 16px font size (to prevent iOS zoom), full-width primary button on phones.
- **Hero:** keep the first viewport's message and primary action visible on a phone without scrolling.
- **Sticky elements:** at most one sticky bar per edge on mobile. Account for safe-area insets (`env(safe-area-inset-*)`).

## Input modes
- Use `@media (hover: hover)` for hover-only enhancements, and make tap targets at least 44px on `pointer: coarse`.
- Don't depend on hover tooltips or hover-revealed controls on touch devices.

## Viewport units
- Use `svh`/`lvh`/`dvh` deliberately. `100vh` on mobile includes browser chrome. `dvh` can cause layout jumps
  as the URL bar moves, so prefer `svh` for full-height sections.

## Verify
At every test width: no horizontal scroll, no overlap, no clipped text, the primary action reachable,
images not distorted or overly upscaled, focus order still logical, and long localised strings (+30%) still fit.
