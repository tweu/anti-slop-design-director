# Information architecture

For Operate and Read surfaces (dashboards, forums, admin, docs, university platforms), structure
matters more than styling. A beautiful screen with the wrong structure is still the wrong screen.

## Start from jobs, not pages
1. List the top 3–5 jobs users come to do, ranked by frequency × importance.
2. Map each job to the shortest path: entry point → screens → completion.
3. Give the most frequent job the most prominent position (often the default landing view).
4. Put rare jobs one level deeper. Don't delete them.

## Objects and views
- Identify the core objects (course, thread, post, user, invoice, deployment) and their relationships.
- Each object gets a consistent **list view** (scan and compare) and **detail view** (read and act), and if needed
  **create/edit** views.
- Use the same name, icon and colour for an object everywhere.

## Navigation structure
- Keep the global nav to 5–7 top-level items, ordered by job frequency. Use labels users would say (no internal jargon).
- Make the user's location visible at all times (active nav state, breadcrumbs for depth of 3 or more, page title).
- Put search where users expect it. For content-heavy products (forums, docs), search is primary navigation.
- Contextual actions live with their object, not in a global toolbar.

## Dashboards
- A dashboard answers "what needs my attention, and is everything OK?" Lead with exceptions and actions,
  not vanity totals.
- Choose one primary view, not twelve equal widgets. Group by decision rather than data source.
- Every number has context: compared to what (a target, the previous period), over what time and what unit.
- Charts must have real data, labelled axes and legends, and an accessible fallback (a table or summary). Choose the chart
  by the question asked (trend → line, comparison → bar, part-to-whole of 5 or fewer → stacked bar, distribution →
  histogram). Avoid pie charts with more than 5 slices, 3D charts and decorative sparklines. If installed, UI/UX Pro Max
  has `--domain chart`.
- Avoid the generic layout of four KPI cards on top, a line chart, a bar chart and a table. Use it only if those are
  really the user's first questions.

## Forums and community platforms
- Thread lists: title (strongest), author and time, reply count and last activity, unread state and tags (as quiet
  text or dots, under the pills setting). Use rows, not cards, so dozens can be scanned.
- Thread view: optimise reading (measure, a clear author block, quoted replies, visible nesting depth). Keep
  reply actions near content but visually quiet.
- Make status visible: pinned, solved/answered, locked and moderation state. Use text plus an icon, not colour alone.
- Make it easy to find old answers: search, filters by course, tag or date, and "solved" first.

## University and institutional platforms
- Mixed audiences (students, staff, applicants, public): route by audience early, then by task.
- Deadlines, schedules and announcements are time-critical, so put them where they are seen first.
- Accessibility and plain language are legal and ethical obligations.
- Keep the institutional brand restrained. Clarity and trust come before decoration.

## Docs and reading platforms
- Give a persistent table of contents, a page outline for long pages, previous and next links, a copy button on code
  blocks and visible version or last-updated information.

## Verify
Walk each top job end to end and count steps and decisions. Check every list with 0, 1 and 500+ items.
