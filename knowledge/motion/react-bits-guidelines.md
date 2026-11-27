# React Bits guidelines

React Bits (https://reactbits.dev, github.com/DavidHDev/react-bits) is a library of about 215 animated React
components. It is an **implementation resource**, not a design philosophy. Choose an effect because the
direction calls for it, never because it's impressive.

## Gate: use a React Bits component only if all of these hold
1. The project is React (React 18/19, Next.js, Vite, Remix or Astro with React islands). Don't port components to other
   frameworks: the licence forbids redistributing ported versions.
2. The effect serves a stated purpose in the motion plan (`motion-principles.md`).
3. The `animation` setting is `balanced` or `expressive` (feedback-type micro components may be used at
   `minimal` if they are restrained). `implementation` isn't `conservative`, unless the user asked for the component.
4. The mode and product fit: Backgrounds, cursor effects and WebGL are for tech, software, gaming and Experience
   surfaces, never on Operate, Read, local businesses or services. See `core/decision-hierarchy.md` #9–10.
5. Settings fit: no `PillNav` or `VoicePill`-style shapes under `pills=off`, and no `MagicBento` or card-stack effects
   under `containers=none`.
6. Its dependencies are acceptable (see below).
Use at most one background or shader effect per page and one or two text or animation effects. Micro components count
as ordinary components.

## Installing (four flavours: JS/TS × CSS/Tailwind)
Pick the flavour matching the project (TypeScript? Tailwind?):
```bash
npx shadcn@latest add @react-bits/<Name>-<JS|TS>-<CSS|TW>
# or
npx jsrepo@latest add https://reactbits.dev/r/<Name>-<JS|TS>-<CSS|TW>
```
For shadcn, add the registry to `components.json`: `"registries": {"@react-bits": "https://reactbits.dev/r/{name}.json"}`.
Manual: copy from the component's Code tab on reactbits.dev.

**Before installing, inspect** `https://reactbits.dev/r/<Name>-<flavour>.json`. It lists `dependencies` and the file
contents. Read the file's imports too, because the declared list can be incomplete. Ask the user before installing under
`balanced`, and state the package names under `ambitious`.

## Typical dependencies by family (verify per component)
| Family | Often needs | Cost |
|---|---|---|
| Text animations (SplitText, ScrollReveal, …) | `gsap`, `@gsap/react`, or `motion` | Low–medium |
| Backgrounds (Aurora, Silk, Particles, …) | raw WebGL, `ogl`, or `three` / `@react-three/fiber` | Medium–high GPU |
| 3D components (Lanyard, ModelViewer, FluidGlass) | `three`, `@react-three/*`, `@react-three/rapier`, `meshline` | High |
| Physics (FallingText, Ballpit) | `matter-js` or `three` | Medium–high |
| Micro / Components | Usually none, `motion` or `gsap` | Low |

## Integration checklist
- **SSR / Next.js App Router:** add `"use client"` to the component, and dynamically import WebGL components with
  `ssr: false`. Guard `window`/`document` access.
- **Reduced motion:** most components do not handle it themselves. Wrap them so that `prefers-reduced-motion`
  renders a static fallback (a still frame, plain text, or a CSS gradient).
- **Accessibility:** text effects must leave the real text in the DOM, readable by screen readers (split letters
  need an `aria-label` on the parent and `aria-hidden` on fragments). Cursor effects are decorative and get
  `aria-hidden`. Interactive components must support the keyboard. Add it if missing.
- **Performance:** at most one live WebGL context per viewport (four per page at most), pause when off-screen
  (IntersectionObserver), cap DPR at 2, use a static fallback on low-power devices and mobile, and keep any loop past 5s pausable.
- **Theming:** replace the demo's default colours with the project's tokens. A React Bits default palette dropped
  into a page is slop too.
- **Text over effects:** never place body text over an animated background without a solid or scrim backing that
  passes contrast.

## Licence
MIT + Commons Clause: free to use in applications, websites and products, including commercial ones.
**Do not** sell or redistribute the components themselves (alone, in a bundle or as a port). This skill therefore names
components and points to the official source, and never bundles their code. Keep the copyright notice in the
component's file header if one is present.

Catalogue of names and purposes: `references/component-resources.md`.
