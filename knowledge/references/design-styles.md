# Design styles

This is vocabulary for directions. Each style lists what defines it, where it fits, where it fails and its slop version
(how it degrades when applied without a decision). A style is a starting point to adapt to the product, never
a template.

| Style | Defining traits | Fits | Fails on | Slop version |
|---|---|---|---|---|
| **Editorial** | Display serif or strong grotesque, columns, rules, pull quotes, generous measure | Media, publishing, research, culture, long-form brands | Dense tools | Serif headline on a SaaS template |
| **Swiss / International** | Strict grid, flush-left grotesque, asymmetry, colour as signal, lots of structure | Institutions, transit, architecture, design studios, data | Warm consumer brands | Helvetica plus random red bar |
| **Minimal (precise)** | Few elements, strong type scale, restrained palette, perfect spacing | Premium products, tools, portfolios | Content-heavy sites (becomes sparse) | Empty white page with a centered sentence |
| **Brutalist** | Exposed structure, raw borders, system/mono type, hard shadows, clashing colour | Art, music, independent media, dev culture | Trust-critical products (banking, health) | Hard offset shadows on a normal SaaS page |
| **Neo-brutalist (soft)** | Thick outlines, flat bright fills, offset shadows, playful | Consumer apps, creator tools, education for young people | Enterprise, luxury | Same, used for every "fun" brief |
| **Premium / luxury** | Restraint, photography, refined serif or wide grotesque, slow motion, low saturation | Fashion, hospitality, high-end goods, real estate | Utilitarian tools | Black page, gold text, thin serif |
| **Utilitarian / dense** | System or neutral UI type, compact tables, minimal chrome, keyboard-first | Admin, dev tools, trading, ops consoles | Persuade pages | Grey everything with no hierarchy |
| **Warm / human** | Soft natural palette, humanist type, real photographs, rounded but not bubbly | Local businesses, health, wellness, education, non-profits | Technical B2B | Beige plus generic stock smiles |
| **Technical / engineered** | Precise grid, mono for data only, schematics, real product output | Hardware, infrastructure, developer tools | Lifestyle brands | Dark neon grid with fake terminal text |
| **Playful / expressive** | Bold colour, custom illustration, bouncy motion, characterful type | Consumer apps, games, kids, creative tools | Serious or regulated services | Random 3D blobs and emoji |
| **Retro / era-specific** | A committed period reference (70s print, 90s web, Y2K, Bauhaus) | Campaigns, culture, brands with heritage | Products needing timelessness | Pastiche without craft |
| **Glass / layered** | Translucent layers over rich content, depth, blur | OS-like surfaces, media overlays, spatial UI | Text-heavy pages; low-end devices | Frosted cards on a gradient for no reason |
| **Bento / modular** | Varied tile sizes encoding importance | Feature overviews with genuinely varied content, personal dashboards | Pages where all items are equal | Random tile sizes, all cards |
| **Experimental** | Concept-first rules: unusual type, layout or interaction | Portfolios, campaigns, art, launches | Anything task-critical | Chaos without a concept |

## Combining
Pick **one** primary style and at most one secondary influence ("Swiss structure with warm photography").
Never mix more than two. That is how trend collages happen.

## From the user's `visual-direction` setting
The setting names a style. Apply its defining traits, then adapt them to the product. "Editorial" for a SaaS
docs site means editorial type and structure, not a magazine layout.

If installed, UI/UX Pro Max `--domain style` has more than 80 more style entries with CSS keywords. Treat them as candidates.
