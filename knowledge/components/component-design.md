# Component design

Components are where the system becomes real. Build a small, consistent set, and make each one complete.

## Principles
- **One of each:** one primary button style, one secondary, one tertiary or text style, one input style, one card style and
  one link style. Variants differ by role, not by whim.
- **Every state is designed:** default, hover, focus-visible, active, disabled, loading, error, selected, plus
  empty and overflow content.
- **Standard controls stay recognisable.** Express the identity through type, colour, radius and spacing, not by
  reinventing how a checkbox works.
- **Tokens only.** Components reference semantic tokens and never hard-code values.
- **Composition over configuration.** Prefer small composable parts over one component with 20 props.

## Buttons
- Hierarchy: one primary per view region. Secondary is outlined or tonal, and tertiary is text.
- The label is a verb plus an object. Icons go leading for recognisable actions and trailing for direction (→, external link).
- Height comes from the density scale, with a minimum hit area of 44px on touch. Keep the width stable when the loading state swaps in.
- Destructive buttons use the danger colour only at the confirmation step, not in every list.

## Inputs
- A visible label, optional helper text and an error slot that reserves space or animates in without shifting much.
- Clear focus, error, disabled and read-only states. Read-only isn't the same as disabled.
- Selects, comboboxes and date pickers: use native controls where possible, and if custom, support the full keyboard and ARIA pattern.

## Tables
- Left-align text, right-align numbers (tabular numerals) and use a consistent date format.
- Sticky header, sortable columns marked with direction, and row hover on pointer devices.
- Row actions are revealed on hover *and* reachable by keyboard, with an overflow menu for more than two.
- Empty, loading (skeleton rows) and error states. Pagination or virtualisation for long data.
- Wrap text or truncate with a full value available (tooltip or expand). Never silently lose data.

## Icons
- One library, one stroke weight, one size scale (16/20/24). Use a real icon set (Lucide, Phosphor, Heroicons,
  Tabler, Material Symbols) or authored SVG, never emoji.
- Icons support labels and don't replace them, except for universal actions with `aria-label`.
- Avoid putting every icon in a tinted rounded square. Do it only if the containers mean something (app icons, file types).
- Real third-party logos keep their own colours and shapes. Never draw a look-alike.

## Media
- Use real product UI, photographs of the actual thing and stand-ins only when necessary (and labelled as such in the handoff).
- A consistent crop and aspect-ratio rule per role (16:9 hero, 4:5 portrait, 1:1 avatar).
- Text on images needs a scrim or solid backing for contrast.

## Feedback components
- Toasts confirm background actions, auto-dismiss in 4–6s unless they contain an action, stack at most 3 and use `aria-live`.
- Inline alerts for page-level state (info, warning, error) dismiss only when appropriate.
- Skeletons match the real layout. Spinners are for small or unknown regions.

## Before creating a component
Check the project (and its component library) for an existing one. Extending is better than duplicating. If the
project uses shadcn/ui, MUI or Chakra, style through their theming APIs rather than overriding them with ad-hoc CSS.
