# Colour palettes

Starting palettes grouped by world. Each lists canvas, surface, text, muted text, action and one supporting
colour. Text, muted text and action colours all pass AA (4.5:1) on both canvas and surface, and white text passes
on each light palette's action colour (checked with the bundled script; verify again after any change with
`python <skill>/scripts/slop_scan.py --contrast <fg> <bg>`). Adapt the hue to the brand. Don't ship these unchanged.

| Name | Canvas | Surface | Text | Muted | Action | Support | Fits |
|---|---|---|---|---|---|---|---|
| Seminar paper | #F7F4EE | #FFFFFF | #1C2230 | #59606E | #2348B8 | #B5651D | Universities, forums, docs |
| Newsprint | #F4F1EA | #FBFAF6 | #161514 | #5C5852 | #B3261E | #1F4E79 | Editorial, media |
| Calm terminal (dark) | #0F1216 | #171B21 | #E6E8EB | #9BA3AE | #5AA9E6 | #E0B252 | Dev tools, monitoring |
| Ledger | #FAFAF8 | #FFFFFF | #111418 | #545B66 | #0B6E4F | #A23B2A | Fintech, accounting |
| Clinic | #F5F8F8 | #FFFFFF | #13292E | #4D6166 | #0F6E7A | #C2563A | Health, care services |
| Bakery morning | #FBF5EC | #FFFDF8 | #2B1D14 | #6B5646 | #A4471C | #3F6B3A | Cafés, food, local shops |
| Gallery white | #FFFFFF | #F6F6F4 | #0D0D0D | #5E5E5A | #0D0D0D | #C8102E | Portfolios, galleries, premium |
| Night gallery (dark) | #0B0B0C | #151517 | #F2F1EE | #A3A19B | #F2F1EE | #D9A441 | Luxury, photography, film |
| Workshop | #F2F0EB | #FAF9F6 | #1E1F1C | #57594F | #B23F18 | #2E5E8C | Hardware, craft, manufacturing |
| Field green | #F3F5EF | #FFFFFF | #18211A | #4F5B51 | #2F6B3B | #B9772B | Outdoors, sustainability, agriculture |
| Swiss signal | #FFFFFF | #F2F2F2 | #111111 | #555555 | #D00511 | #111111 | Swiss/structured, transit, studios |
| Soft brutal | #FFF8E7 | #FFFFFF | #111111 | #4A4A4A | #1D4ED8 | #FF6B35 | Playful consumer, creator tools |

## Semantic colours (adapt per palette)
success #1F7A4D · warning #A15C00 · danger #B42318 · info #1F5FAD, used as text on light canvases. For tints, mix
about 8–12% of the hue into the surface.

## Notes
- **Action colour = brand colour** in most products. Add a separate brand accent only when the brand colour fails as
  an action colour (for example yellow on white).
- Dark palettes: lower the saturation of large accent areas. Muted text is about #9BA3AE or lighter on #0F1216.
- Check the palette against the product's photography. A warm palette with cold photographs fights.
- The purple-blue gradient isn't in this list on purpose. Use it only when the brand calls for it.
If installed, UI/UX Pro Max `--domain color` has 194 product-specific palettes. Treat them as candidates.
