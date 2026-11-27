# Design tokens

Tokens are the contract between the design decisions and the code. If a value isn't a token, it's a one-off that
will drift.

## Layers
1. **Primitives:** raw values (`blue-600`, `space-4`, `radius-2`). These are never used directly in components.
2. **Semantic:** purpose (`color-action`, `color-text-muted`, `surface-raised`, `space-section`,
   `radius-control`). Components use these.
3. **Component (optional):** `button-primary-bg`, used only when a component diverges from the semantic layer.
Themes (light/dark, brand variants) remap the semantic layer. Primitives stay the same.

## Naming
- Name by purpose: `--color-text-muted`, not `--gray-500-text`.
- Keep the vocabulary small and consistent (`canvas / surface / raised / overlay`, `text / muted / subtle / inverse`).
- Use the same names in DESIGN.md, CSS and the Tailwind config.

## Implementations
**CSS custom properties** (universal):
```css
:root {
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px;
  --space-8: 32px; --space-12: 48px; --space-16: 64px; --space-24: 96px;
  --radius-control: 6px; --radius-card: 10px;
  --font-display: "Fraunces", Georgia, serif;
  --font-body: "Source Sans 3", system-ui, sans-serif;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1); --dur-fast: 150ms; --dur-base: 250ms;
}
[data-theme="dark"] { /* remap semantic colours only */ }
```
**Tailwind v4:** declare tokens in `@theme { --color-action: …; }` in the main CSS. They become utilities
(`bg-action`). **Tailwind v3:** extend `theme` in `tailwind.config` with `var(--…)` references.
**CSS-in-JS / component libraries:** put tokens in the theme object (MUI `createTheme`, Chakra `defineConfig`,
styled-components `ThemeProvider`). shadcn/ui maps to its CSS variables (`--primary`, `--background`, …), so
set those rather than adding a parallel system.
**Native:** SwiftUI asset catalog colours and `Font` extensions. Compose `MaterialTheme` / custom `CompositionLocal`.

## Interchange
DESIGN.md frontmatter tokens (`colors`, `typography`, `rounded`, `spacing`, `components`) convert to and from
W3C DTCG `tokens.json`, Figma variables and Tailwind themes. Keep DESIGN.md as the human-readable source and the code
tokens as the executable source, and update both together.

## Hygiene
- Avoid raw hex values, px values or durations in components (search for `#[0-9a-f]{3,8}` in component files).
- Keep one spacing scale with no in-between values. If you need 20px, the scale is wrong, or you don't need it.
- Avoid unused tokens and duplicate tokens with the same value and purpose.
- Contrast-check every semantic text/surface pair, in each theme.
