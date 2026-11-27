# Pills, badges, chips and tags

Small rounded labels are useful for status, filters and tags, but they multiply easily. When there are too many,
every item shouts and none stands out. This file applies the `pills` setting.

## Uses by function
| Function | Example | Pill OK under functional-only? |
|---|---|---|
| Status | Paid / Overdue, Solved, Draft | Yes (text plus colour, never colour alone) |
| Filter / selected facet | "Week 3 ✕" | Yes (removable chip, keyboard-accessible) |
| Category / tag | #algorithms | Yes, when tags are a navigation feature |
| Input token | email recipients | Yes |
| Count | 3 unread | Yes, as a small numeric badge |
| Decoration | "✨ New", "AI-powered" over a heading | No |
| Eyebrow above a section heading | "FEATURES" | No |
| Marketing claims | "#1 rated" | No |

## Settings
- **off:** replace pills with plain text labels (`Solved` in the semantic colour, perhaps with an icon),
  small caps metadata, dot plus text (`● Overdue`), or standard controls (select, checkbox list, segmented
  control with a modest radius). Filter chips become a filter bar with checkboxes or selects plus a
  "Clear filters" link. Buttons use the project's normal radius, not fully rounded.
- **functional-only** (default): pills only for the rows marked Yes above. One shape and size family.
  Status colours are semantic tokens. At most about 2 pills per list item. If a row needs more, the information
  belongs in columns or metadata text.
- **expressive:** pill buttons, pill navigation and tag clouds can be part of the identity. Commit to it consistently
  (all buttons pill-shaped, not half of them) and still keep decorative pills meaningful.

## Craft
- Height of about 20–24px for badges and 28–32px for interactive chips, with a hit area of at least 24px (44px on touch for removable chips).
- Text at least 12px with medium weight. Contrast of 4.5:1 against the pill's own background, not against the page.
- Use tinted backgrounds with darker same-hue text rather than saturated fills with white text, unless the status is critical.
- Never truncate the only meaningful word. Long tags wrap or the list scrolls.
- Removable chips use a real `<button>` with `aria-label="Remove filter: Week 3"`.
- For counts, `aria-live` when they update and a cap at "99+".

## Smells
- Every card has 2–4 coloured pills.
- Pills in five unrelated colours with no legend.
- A pill as the only thing in the hero apart from the headline.
- A status shown as a pill *and* a coloured dot *and* coloured text at once.
