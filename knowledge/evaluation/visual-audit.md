# Visual audit

A structured critique for a rendered interface, whether your own build or an existing product the user wants
reviewed. Answer every question with evidence (a screenshot region, a selector, a computed value).

## 1. First impression (5 seconds, 1440 and 390)
- What is this, who is it for and what should I do? Can a stranger answer all three?
- Where does the eye land first, second and third? Is that the intended order?
- Could this belong to a different product with only the name changed? (If yes, the identity is missing.)

## 2. Hierarchy and composition
- Squint test: are the primary element, secondary element and groups distinguishable?
- Does one element clearly lead each region, or do several compete?
- Is the spacing rhythm deliberate (tight inside groups, generous between them) or uniform?
- Do sections vary in form when their content differs, or repeat one structure?
- Are edges aligned to a grid? Do any elements float off-grid without intent?

## 3. Typography
- Are the roles distinct? Is the scale coherent? Does the display face fit the direction?
- Is the measure 45–75ch for prose? Are the line heights tuned? Are there bad heading wraps or widows?
- Are numerals tabular where compared? Are quotes and dashes correct?

## 4. Colour
- Does every colour have a role? Does the accent mark the right things, and only those?
- Does contrast pass in all states and themes? Is colour never the only signal?
- Is any gradient, glow or tint there by default rather than by decision?

## 5. Components and surfaces
- Count the cards, nesting depth, pills, shadows and borders. Is each one justified? Do they match the settings?
- Is there one button family, one card style, one radius scale and one link style?
- Are icons from one consistent set? Are there emoji used as icons?
- Are the states complete (hover, focus, disabled, loading, empty, error)?

## 6. Content
- Is the copy real and specific? Do buttons use a verb plus an object? Are headings named things rather than moods?
- Is there invented proof, placeholder data presented as real or stock imagery posing as the product?

## 7. Responsive and interaction
- At 320, 390, 768 and 1440: is there overflow, overlap, clipping, unusable tables or hidden primary actions?
- Keyboard pass: does focus order match the visual order? Are focus rings visible and never hidden?
- Does motion have a purpose? Is it reduced-motion safe, with no content hidden behind it?

## 8. Performance signals
- Are there oversized images, layout shift when fonts or images load, or many WebGL contexts?

## Output format
```
## Verdict
<2–3 sentences: what works, the biggest problem, overall readiness>

## Findings (ordered by user impact)
1. [Blocking|Major|Minor] <screen/state> — <what is wrong, with evidence>
   Fix: <smallest concrete change>
...

## Not checked
<anything that couldn't be verified and why>
```
Separate defects (objective) from taste (say "judgement call" and why). Don't pad the list. If nothing
material is wrong, say so for the scope inspected.
