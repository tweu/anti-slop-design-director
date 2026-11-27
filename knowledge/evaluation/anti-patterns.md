# Anti-pattern detection

How to find slop in code and renders. `core/anti-ui-slop.md` explains *what* each pattern is and why it matters. This file
explains how to *detect* each one and how to decide whether it's justified.

## Mechanical signals (scan the code)
`python <skill>/scripts/slop_scan.py <path>` reports these. You can also grep for them by hand:

| Signal | Grep for | Judge |
|---|---|---|
| Gradient text | `background-clip:\s*text`, `bg-clip-text` | Almost always replace with weight or size |
| Purple/violet gradients | `from-(purple\|violet\|indigo\|fuchsia)`, `linear-gradient(` with violet hues | Justified only by brand or request |
| Glass / blur | `backdrop-filter`, `backdrop-blur` | Justified only over real content that must stay visible |
| Pill shapes | `rounded-full`, `border-radius:\s*(9999px\|999px\|50vh)` on non-avatar elements | Check against the `pills` setting |
| Shadow everywhere | count of `shadow-` / `box-shadow` | More than a handful of distinct uses usually means decoration |
| Hard offset shadow | `box-shadow:\s*\d+px\s+\d+px\s+0` | Brutalist direction only |
| Nested cards | card-like classes (`card`, `rounded-xl border`, `shadow`) inside each other in JSX/HTML | Check against the `containers` setting |
| Emoji as icons | emoji characters in headings, buttons, list items | Replace with an icon set |
| Eyebrow labels | small uppercase tracked text right before an `h1`/`h2` | Remove unless it carries information |
| Scroll reveal everywhere | `whileInView`, `data-aos`, `IntersectionObserver` + opacity 0 on many sections | Keep one authored moment |
| Raw values | hex/px literals inside component files | Move to tokens |
| Placeholder copy | `lorem`, `Acme`, `John Doe`, `TODO`, `[Your` | Replace with real or clearly labelled sample content |
| Generic CTA | `Get started`, `Learn more` repeated | Verb + object |

## Visual signals (look at the render)
- **Uniform grid:** three or more same-size boxes with an icon, heading and text, repeated in two or more sections.
- **Template hero:** a centred pill, an H1, a subline, two buttons and a gradient or blob, with nothing product-specific.
- **Box soup:** containers inside containers, each with a border and padding, so content gets narrow and noisy.
- **Accent confetti:** the accent colour on many unrelated elements, so nothing stands out.
- **Equal rhythm:** the same gap between everything, giving no grouping.
- **Fake data:** round numbers, "10k+ users" or "99.9% uptime" with no source.
- **Interchangeable:** nothing that could only belong to this product.

## Deciding whether a pattern is justified
For each finding, ask:
1. Did the user or brand ask for it? (Then keep it and build it well.)
2. Does it carry information or affordance here? (A status pill on an invoice row: yes. A pill over a hero heading: no.)
3. Does the direction call for it? (A hard offset shadow in a brutalist direction: yes.)
4. Does it respect the settings?
If none of these apply, fix it. **Replace it structurally, not cosmetically.** Turning cards into bordered rows is the
same slop in a different shape. Fix the hierarchy, the content or the composition.

## Reporting
List each finding with its location, why it reads as generic in *this* context and the structural fix. Mark findings you
decided to keep as "kept: <reason>" so that the reasoning is visible.
