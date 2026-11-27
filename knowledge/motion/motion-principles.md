# Motion principles

Motion explains: where something came from, what changed and what responds. Motion without a purpose is noise,
and identical fade-ups on every section are a sign of a generic page.

## The three layers
1. **Feedback** (every mode, every `animation` setting): hover, press, focus, toggle, open/close and
   validation. 100–200ms. This is affordance, not decoration.
2. **Transitions** (`balanced`+): state and view changes such as panels, tabs, list reorder, route change and
   expand/collapse. 200–350ms. They preserve spatial continuity.
3. **Authored moments** (Persuade/Experience, `balanced` = 1 per page, `expressive` = 1–2): a hero
   entrance, one scroll-driven sequence in its own section, a signature interaction. 400–1200ms.

Write one line per motion in the plan: *what moves and why* ("hero: the headline arrives first, then the action").
Cut anything without a reason.

## Timing and easing
- Use exponential ease-out for entrances (`cubic-bezier(0.16, 1, 0.3, 1)`) and ease-in for exits. Exits run about 20–30% faster than entrances.
- Standard UI uses `cubic-bezier(0.2, 0, 0, 1)`. Use springs for direct manipulation (drag, toggle) when the library supports them.
- Don't use one duration everywhere. Small elements move faster and large surfaces slower.
- Stagger lists by 30–60ms per item, capped at about 6 items, and only on first load, not on scroll.

## What to animate
- Prefer `transform` and `opacity`. `filter: blur`, `clip-path`, masks and shadows are part of the palette when they
  stay at 60fps. Never animate width, height, top or left on large elements.
- Start from an **already-visible** default. Content is readable with JavaScript off, before hydration and under
  reduced motion. Never ship `opacity: 0` content that waits for an observer.

## Do not
- Fade or rise every section, card or row on scroll (stock reveals).
- Parallax on text, scroll-jacking or smooth-scroll hijacking libraries by default.
- Auto-advancing carousels, timed tabs, infinite marquees of logos without a pause control.
- Tilt-on-hover cards (unless `animation=expressive` on Experience surfaces).
- Cursor-following blobs or particles on Operate or Read surfaces.
- Loops running forever with no pause (anything moving for more than 5s needs a pause control).

## Reduced motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important; animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important; scroll-behavior: auto !important;
  }
}
```
Use this as a backstop, and also design an explicit reduced variant for authored moments (a static frame or a simple cross-fade).

## Implementation choice
- CSS transitions and keyframes first. CSS scroll-driven animations (`animation-timeline: view()`) with
  `@supports` for simple scroll effects.
- Use the project's existing library if it has one (Motion/Framer Motion, GSAP, React Spring).
- Add a library only when choreography, physics, layout animation or SVG morphing need it, and only under `balanced`+ implementation.
- WebGL or shaders only per the rules in `react-bits-guidelines.md` and `core/decision-hierarchy.md` (#9).

## Mode guide
| Mode | Default motion |
|---|---|
| Operate | Feedback plus quick transitions. No entrances. Respect users who repeat actions all day. |
| Read | Feedback plus subtle navigation transitions. Nothing competes with the text. |
| Persuade | Feedback, a hero entrance and one authored moment. |
| Experience | Can be motion-led. Still interruptible, reduced-motion-safe and performant. |

If installed, UI/UX Pro Max `--domain gsap` has GSAP presets.
