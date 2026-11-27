# Design system generation

Every project gets its own coherent system. Never reuse one universal system across sites.

## When to create, update or leave alone
| Situation | Action |
|---|---|
| New project or approved redesign | Create DESIGN.md after the direction is chosen, before building screens |
| Existing project with no DESIGN.md, but a working visual language | Derive DESIGN.md **from the shipped code** (tokens, CSS, components) when the user asks for one, or when you are about to make system-level changes. Document what exists rather than what you would prefer |
| Existing DESIGN.md, extending it | Follow it. Add tokens or components you introduced, without rewriting the rest |
| Existing DESIGN.md, small fix | Leave it alone |
| Redesign | Replace it. Don't merge old and new |
Ask before overwriting an existing DESIGN.md that you didn't create in this session.

## Generation procedure
1. **Direction:** the paragraph from `visual-design/art-direction.md` becomes the Overview.
2. **Colour roles** (`visual-design/color-systems.md`): primitives plus semantic roles, with contrast checked.
3. **Type roles** (`visual-design/typography.md`): 8–12 levels with family, size, weight, line height and tracking.
4. **Spacing scale** (4px base) and **content widths** for each layout type.
5. **Shape:** a radius scale, border use and an elevation approach.
6. **Components:** buttons, inputs, navigation, cards/containers, tables, pills/badges, and the states for each.
7. **Motion:** durations, easings, what moves and the reduced-motion policy.
8. **Responsive rules and accessibility commitments.**
9. **Anti-patterns:** product-specific don'ts, including the settings (for example "no nested cards"), plus the
   one or two slop patterns most likely for this category.
10. **Director settings line** in the Overview.
Then implement the tokens in code (`design-tokens.md`) so that the document and the code agree.

## Deriving from existing code
- Collect the actual values in use (colours, font sizes, spacing, radii, shadows) by grepping CSS, the Tailwind config and theme files.
- Cluster near-duplicates (`#1f2937` and `#1e293b` doing the same job), and propose consolidation as a *recommendation*
  without silently changing anything.
- Describe the system as it is. Note inconsistencies in Do's and Don'ts or as a follow-up list.

## Using library references
With `references=auto|library`, an example DESIGN.md (from albemala's design-md-library, a brand library or
UI/UX Pro Max `--design-system --persist`) can show depth and token naming. Use it for **structure**. Take values
from this product's direction. Never adopt a brand's identity (name, logo, signature palette) for a different product.

## Validating
- Check every colour pair the document claims for contrast.
- Every token named in YAML is mentioned in the prose, and every `{reference}` resolves.
- If Node is available and the user agrees, `npx @google/design.md lint DESIGN.md` validates the format.
  Running it downloads a package, so treat it as optional.
Format details: `design-documentation.md`. Token implementation: `design-tokens.md`.
