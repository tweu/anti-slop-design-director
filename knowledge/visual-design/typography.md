# Typography

Type carries information, hierarchy and voice. On most interfaces it does more for the identity than colour.

## Roles before fonts
Define the roles the interface needs (typically display, heading, body, label, metadata and
data/code) and how they differ. Use the fewest families that make the hierarchy unmistakable:
one family is often right for Operate, and two (display plus text) for Persuade/Read/Experience. Add a
second family only for a role that it alone can perform.

## Choosing faces
- Match the face to the direction's world, not to a category habit. Ask what the letterforms say:
  institutional, handmade, technical, literary, luxurious or blunt.
- **Operate:** a well-tuned neutral UI face or the system stack is legitimate. The quality shows in
  the scale, weights and numerals.
- **Persuade/Experience display:** choose a face with character, self-hosted or loaded properly.
  The closest installed font is a fallback, not a choice.
- Avoid using defaults as identity: Inter, Roboto or the system UI font as a *display voice*, and the
  "geometric sans plus mono labels" AI pairing.
- Check licensing (Google Fonts are OFL; commercial fonts need licences) and weight availability.
  Pairings: `references/typography-pairs.md`. UI/UX Pro Max `--domain typography` /
  `--domain google-fonts` if installed.

## Scale
- Use a ratio-based scale (1.2–1.25 for dense UI, 1.25–1.333 for balanced, 1.414–1.618 for expressive
  display). Adjacent roles must differ visibly, because two sizes 2px apart do different jobs badly.
- Use size, weight, case, spacing and colour together. Don't ask size to do everything.
- Display tops out around 6rem on desktop. Use `clamp()` for fluid display sizes on marketing surfaces
  and keep product and reading surfaces at fixed role sizes.
- Keep heading tracking slightly negative for large sizes (−0.01 to −0.03em) and no tighter than −0.04em.
  Small all-caps labels need positive tracking (+0.04 to +0.08em).

## Reading
- Body is at least 16px on reading and marketing surfaces. Dense Operate data may use 13–14px with high
  contrast. Mobile inputs are at least 16px.
- Measure: 45–75 characters for prose (`max-width: 65ch` is a good default).
- Line height: about 1.5–1.7 for body, 1.1–1.25 for display. Wider measures need more leading.
- Light text on dark grounds needs a little more line height, slightly more tracking and sometimes one
  weight step heavier.
- Use either paragraph spacing or a first-line indent, not both.
- Add `text-wrap: balance` to headings and `text-wrap: pretty` to body copy. Check manual line breaks at
  every width.

## Details that signal craft
- `font-variant-numeric: tabular-nums` in tables, prices, timers and any compared numbers.
- Real quotes and apostrophes (“ ” ’), en dashes for ranges and an ellipsis character.
- Avoid widows in headlines. Avoid all-caps paragraphs. Avoid underlines that aren't links.
- Load only the weights you use. Use `font-display: swap` with a metric-adjusted fallback (`size-adjust`) to
  limit layout shift.
- Respect zoom, user font settings and Dynamic Type on native.

## Editorial typography (load when the direction is editorial or Read-heavy)
- Contrast a display face with a text face (for example a high-contrast serif display with a sturdy
  text serif or a humanist sans).
- Use a column grid with deliberate measure. Pull quotes, drop caps or run-in heads are allowed
  as one device each, used rarely.
- Rules (hairlines) and whitespace separate content better than boxes.
- Captions, bylines and datelines form a consistent metadata role.

## Verify
- Roles are recognisable without reading the words.
- There is no overflow, clipping or awkward wrap at 320, 390, 768 and 1440 with real copy and long names.
- There is no invisible text while loading and no large reflow when fonts swap.
