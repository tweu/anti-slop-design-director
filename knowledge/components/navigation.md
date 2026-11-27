# Navigation

Navigation shows users where they are, what's possible and how to get back. It is also the
first element where generic defaults creep back into an otherwise considered design.

## Choose the pattern by structure
| Structure | Pattern |
|---|---|
| Marketing site, 3–6 pages | Top bar: logo left, links, one primary CTA right |
| Large marketing / product suite | Top bar with mega-menu grouped by job or audience |
| App with 5+ sections, desktop-first | Left sidebar (collapsible), with the page header holding title and actions |
| App with 3–5 sections, mobile-first | Bottom tab bar (5 items or fewer) with icon and label |
| Docs | Left section tree, right "on this page" outline, top search |
| Content platform / forum | Top bar with prominent search, category nav, user menu |
| Multi-audience institution | Audience switcher or audience-first sections ("Students", "Staff", "Applicants") |

## Rules
- Labels use the users' words and are short. Icons never stand alone in primary navigation unless they are universal (search, settings, profile).
- The active state is visible through more than colour (weight, indicator bar or background).
- Keep one primary CTA in the nav at most. Don't repeat it in every section below as well.
- The logo links home. A skip link comes before the nav.
- Mobile menu: a full-screen or drawer menu, a button with `aria-expanded`, focus moved into the menu, Esc to close and no body scroll behind it.
- Sticky headers stay short (56–64px), may shrink on scroll and never hide focused elements (use `scroll-padding-top`).
- Breadcrumbs for hierarchies three or more levels deep. Back behaviour stays predictable, and deep links work.
- Footers carry secondary navigation, legal links and contact. Don't make them a sitemap dump unless the site needs one.

## Pills and navigation
`pills=off` means no pill-shaped nav containers or pill-highlighted active states. Use underlines, weight
or an indicator line. `expressive` allows pill nav as an identity element.

## Slop signals
- A floating rounded glass nav bar detached from the top edge, with no reason.
- A hamburger menu on desktop for a site with four links.
- A "Get started" button in the nav, the hero, every section and the footer.
- Nav links that are vague nouns ("Solutions", "Resources", "Platform") with nothing specific behind them.
