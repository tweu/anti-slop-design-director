# Cards and containers

A card says "this is a discrete object you can act on". When every block is a card, the signal is lost and
the page becomes a grid of equal boxes. This file applies the `containers` setting (see `core/settings.md`).

## When a card is right
- A **repeated, discrete, actionable object**: a product, a post in a masonry feed, a course tile, a
  draggable kanban item, a file.
- Content that **moves as a unit**: drag, reorder, dismiss, select.
- A **different object type** sitting on a page of another type (an embedded tweet, a code sample in prose).
- A grouped control panel in settings, **when** grouping by space alone is ambiguous.

## When a card is wrong
- A wrapper around a section that already has a heading and whitespace.
- Feature lists: use type, icons and space, or real UI imagery.
- A single item alone on a page.
- Rows in data lists: use table rows or list rows with dividers.
- A card used to "add some depth" to an empty-looking page. The page lacks content or hierarchy, and a card won't fix that.

## Nesting rules
| Setting | Allowed |
|---|---|
| none | Never a box in a box. Inner groups use spacing, a heading, a divider or a background band. |
| selective | Only when the inner element is a different object type (code block, media embed, editable row, an attachment in a post). Never box-in-box for decoration. |
| normal | Nesting allowed where it clarifies. Max two levels, and the inner level is visually lighter (no shadow, subtler border). |

Under every setting, never stack three treatments (border + tint + shadow) on nested elements.

## Alternatives to cards
- **Whitespace and a heading:** the default way to group.
- **Dividers:** hairline rules between list items or sections.
- **Background bands:** a full-width tonal shift marks a section without boxing it.
- **Columns with shared alignment:** content aligned to a grid reads as grouped.
- **Tables / list rows:** for anything compared or scanned.
- **Indentation or a leading rule:** for hierarchy inside threads or trees.

## When you do use cards
- One card style per project: one radius, one elevation approach (border *or* shadow *or* tint), one padding scale.
- The whole card is the link target if it links (with one clear primary link for screen readers). Don't put competing
  buttons inside a linked card.
- Content leads. Put the image or title first and the metadata quiet. Skip the icon-in-a-tinted-square unless icons carry meaning.
- In a grid, cards should be genuinely equivalent. If one item matters more, make it bigger or separate it.
- Hover (on pointer devices): a subtle lift (about 2px), a border or shadow change, or an image zoom of 1.02–1.03. Pick one.

## Surfaces, borders, radius, shadow
- **Elevation is information.** Use it for things above the page (menus, popovers, dialogs, sticky bars), not for
  everything on it.
- Shadows need an offset and a soft blur, tinted from the background hue rather than pure black. Use 2–3 levels at most.
- Radius scale: pick a small set (for example 4 / 8 / 12 plus full for avatars). Radius grows with element size, and nested
  radius equals the outer radius minus the padding. Sharp radii suit fintech, developer tools and editorial. Soft radii suit consumer products.
- Borders: 1px and low contrast for structure. Strong borders belong to brutalist or swiss directions.
