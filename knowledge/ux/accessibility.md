# Accessibility

The target is WCAG 2.2 AA. Accessibility sits above aesthetics in the decision hierarchy, and an
aesthetic preference never justifies a failure.

## Checklist (run on every build, and in full on audits)
**Perceivable**
- Text contrast is at least 4.5:1, large text at least 3:1, and UI components and focus indicators at least 3:1. Check every state and theme.
- Colour is never the only carrier of meaning (status, errors, required fields, chart series, links in body text).
- Informative images have meaningful `alt`. Decorative images get `alt=""` or `aria-hidden="true"`.
- Video has captions and audio has a transcript. Nothing autoplays with sound.
- Content reflows at 320px CSS width and at 200% zoom without horizontal scroll (data tables excepted).
- Text spacing overrides (line height 1.5, letter spacing 0.12em) don't break the layout.

**Operable**
- Everything works by keyboard, in a logical order, with a visible focus indicator that is never hidden under sticky headers.
- A skip link is the first focusable element on pages with navigation.
- There are no keyboard traps. Modals trap focus intentionally and release it on close.
- Targets are at least 24×24px (AA minimum) and at least 44×44px on touch-first interfaces.
- No time limits without a way to extend. Anything moving for more than 5s can be paused.
- No content flashes more than three times per second.
- Dragging has a single-pointer alternative.

**Understandable**
- `lang` is set on `<html>`. Labels and instructions are visible.
- Errors are identified in text, linked to their field (`aria-describedby`) and suggest fixes.
- Navigation and naming are consistent across pages.

**Robust**
- Use native elements before ARIA. A `<button>` beats `div role="button"`.
- Every control has an accessible name. Icon-only buttons get `aria-label`.
- Toggles expose state (`aria-pressed` or `aria-expanded`). Live updates (toasts, counts, validation) use `aria-live`.
- Headings go in order without skipping levels. Use landmark regions (`header`, `nav`, `main`, `footer`).

## Motion and accessibility
- Honour `prefers-reduced-motion`: remove parallax, scroll-linked movement, auto-playing loops and large transforms.
  Keep fades under 200ms or remove them.
- Content must never depend on an animation finishing to become visible.

## Common design-level failures
- Light grey "muted" text on white (often about 2.8:1).
- Placeholder text used as the label.
- Focus rings removed for aesthetics.
- Low-contrast text on photographs or gradients (add a scrim or a solid panel).
- Status shown only as red or green dots.
- Custom selects and checkboxes without keyboard support.

## How to verify
- Compute contrast from the actual token values (`scripts/slop_scan.py --contrast FG BG` gives a quick ratio).
- Tab through the whole page. Check the order, visibility and traps.
- Zoom to 200%, then view at 320px.
- Toggle reduced motion and check that everything is still visible and usable.
- If available, run axe or Lighthouse. Report automated results as partial coverage, because they catch about 30–40% of issues.
