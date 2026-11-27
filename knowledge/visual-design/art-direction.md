# Art direction

A direction is a decision about what world this product lives in, stated precisely enough that two
designers would build similar things from it. It comes before tokens, and tokens come before components.

## Inputs to a direction
- **Product truth:** what is sold or done, and the real material available (UI, photographs, data, copy).
- **Audience and scene:** who uses it, where, on what device, in what light, for how long, under what pressure.
- **Brand commitments:** logo, colours, fonts and voice that must stay.
- **Mode:** Persuade, Operate, Read or Experience (see SKILL.md).
- **Settings:** `visual-direction`, `density` and `animation`.

## Writing the direction (one paragraph)
Cover each of these concretely:
1. **World and references.** Name concrete materials, eras or objects, not adjectives: "a well-printed
   field guide", "a Swiss rail timetable", "a ceramic studio's price card on kraft paper", "a
   Bloomberg terminal made calm". Avoid "modern, clean, sleek". Those describe every AI page.
2. **Type character:** the voice of the display face and the job of the text face.
3. **Colour strategy:** temperature, the dominant relationship (ink on paper, light on dark,
   colour-blocked), what the accent marks and how much of it there is.
4. **Density and rhythm:** how much appears per screen and where the page breathes.
5. **Signature move:** one memorable decision (a typographic treatment, a photographic crop rule, a
   structural device, a single authored interaction). One only. Several signature moves cancel
   each other out.
6. **What it is not:** the nearest cliché to avoid ("not a dark neon dev-tool page").

### Example: a university course-discussion forum (Operate + Read)
"A well-run seminar room: calm off-white paper, ink-blue text, one university accent used only for
your own actions and unread state. A readable humanist sans for posts at 16–17px with a generous
measure; a compact grotesque for metadata. Threads are rows with rules, not cards; tags are plain
text links with a small coloured dot. The signature move is the thread view's margin of reply
indentation lines, which make the conversation's shape visible. Not a social feed, not a SaaS
dashboard."

## Offering directions
For an open-ended new identity, offer **2–3 directions that differ in kind**: different
worlds, type voices and densities, not the same layout in three colours. Give each a name, a
two-sentence description, its first viewport and its trade-off. When the user has already given a
direction or delegated the choice, don't offer. Commit.

## Committing
- Carry the direction through the details: nav, inputs, empty states, footer and error pages. Generic
  defaults usually creep back in at the edges.
- When torn between "refined" and "committed", choose committed on Persuade/Experience surfaces and
  refined on Operate/Read surfaces.
- Distinction can come from composition, content, type, imagery or interaction. It doesn't need
  unusual controls. Standard controls stay recognisable.

## Mapping product types to starting points
Use these as a first guess and then interrogate them. They are not templates.
| Product | Typical mode | Starting direction | Watch out for |
|---|---|---|---|
| B2B SaaS app | Operate | Precise, neutral surfaces, one action colour, compact tables | the KPI-card dashboard |
| SaaS marketing | Persuade | Lead with the product UI at true size; type-led | the purple gradient hero |
| Developer tool | Persuade/Operate | Code and real output as the hero; mono only for code | dark-neon cliché |
| Fintech / trading | Operate | Calm density, tabular numerals, semantic colour | red/green as the only cue |
| Editorial / media | Read | Display serif or strong grotesque, columns, rules | cards for articles |
| Portfolio / creative | Experience | The work leads full-bleed; interface recedes | over-animated chrome |
| E-commerce | Persuade/Operate | Photography-led, clear price and CTA, honest filters | badge confetti |
| Local business (cafe, studio, clinic) | Persuade | Real photographs, warm flat colour, address and hours early | shader effects, stock mood photos |
| University / institution | Read/Operate | Trustworthy, accessible, information architecture first | corporate blue template |
| Community forum | Operate/Read | Reading comfort, scannable threads, clear unread state | social-feed cards |
| Experimental | Experience | A concept-driven rule set | spectacle without usability |

For more starting vocabulary, see `references/design-styles.md`. If installed, UI/UX Pro Max's
`--domain product` and `--domain style` searches give more candidates.
