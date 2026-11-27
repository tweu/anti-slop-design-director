# Visual density

Density is how much information each region carries. It must fit use frequency, decision complexity
and mode. Minimalism isn't automatically better than density, and more whitespace isn't always better.

## Choosing density
| Signal | Leans compact | Leans spacious |
|---|---|---|
| Use frequency | Daily, for hours | Occasional, first visit |
| User expertise | Expert, trained | Newcomer |
| Task | Compare, monitor, triage | Decide, feel, understand |
| Content | Many similar records | Few rich items |
| Mode | Operate | Persuade / Experience |

A product often mixes densities: a spacious marketing site, a compact app, and a balanced docs site.
Decide per surface.

## Scales by density setting
| | compact | balanced | spacious |
|---|---|---|---|
| Spacing range | 4–32px | 8–64px | 16–128px |
| Body / data text | 13–14px | 15–16px | 16–18px |
| Row height (tables/lists) | 32–36px | 40–48px | 56px+ |
| Control height | 28–32px | 36–40px | 44–48px |
| Section padding (marketing) | 48–64px | 80–112px | 120–200px |
Touch targets stay at least 44×44px on touch devices in every density. Make the hit area larger than the visible mark if needed.

## Dense done well (dashboards, admin, trading, forums)
- Remove chrome, not information: fewer borders and boxes, more alignment and typographic hierarchy.
- Use tables with right-aligned tabular numbers, sticky headers, zebra striping *or* row dividers (not
  both), and column sorting and filtering.
- Group with whitespace and subtle background bands rather than many cards.
- Use semantic colour sparingly so that the anomalies stand out.
- Use progressive disclosure for rare controls, but keep essential data visible without hovering.
- Let users choose density (compact or comfortable) when the audience is mixed.

## Spacious done well
- Space exists to give weight to something. Every large gap frames content.
- Use large type, generous measure and fewer items per viewport, but each viewport still makes a point.
- "Premium" comes from precision and material quality, not emptiness.

## Failure modes
- **Too sparse:** a three-word section filling a screen, giant padding around thin content, scrolling
  through emptiness.
- **Too dense:** no grouping, everything at equal weight, and tiny text used to fit more.
- **Inconsistent:** compact cards inside spacious sections, or random padding values.
