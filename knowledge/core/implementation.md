# Implementation engine

Turns the decisions into working UI. Good CSS doesn't automatically mean good design. This file
covers how to build without losing the direction.

## Before writing code
- **Detect the stack** from package.json, framework configs, pubspec, Package.swift or composer.json.
  Never assume React or Tailwind. Find the styling method (CSS modules, Tailwind, CSS-in-JS,
  vanilla CSS, a component library such as shadcn/MUI/Chakra) and **build in it**.
- **Inventory what exists:** tokens or theme files, base components (Button, Input, Card), layout
  primitives, icon library and fonts. Reuse these first. A new component must justify why an existing
  one doesn't fit.
- **Find the data contracts.** Don't invent backend behaviour. Wire UI to the real props, state and API
  shapes. Where data doesn't exist yet, use clearly labelled fixtures.

## Tokens first
- Put every colour, type role, spacing step, radius, shadow and duration in tokens: CSS custom
  properties, the Tailwind theme or the theme object. Components reference roles (`--color-action`,
  `--space-4`), never raw hex values or one-off pixels.
- Use semantic names that describe purpose (`surface-raised`, `text-muted`, `action-primary`),
  layered on primitives (`blue-600`). Themes remap the semantic layer.
- If the project already has a token system, extend it. Don't create a second one beside it.

## Building
- Semantic HTML first: real `<button>`, `<a>`, `<nav>`, `<main>`, `<label>`, headings in order.
- Layout with flex and grid using `gap`. Use container queries where a component lives in several
  contexts. Make structural responsive decisions (what stacks, collapses, scrolls or stays).
- Implement the states that can actually occur: hover, focus-visible, active, disabled, loading,
  empty, error, success. Errors say what happened and how to recover.
- Images: correct aspect ratio, `width`/`height` or `aspect-ratio` set, modern formats, lazy below the
  fold, meaningful `alt`. Fonts: load only the weights you use, `font-display: swap`, metric-compatible fallbacks.
- Theme the browser's own surfaces: `::selection`, `caret-color`, `accent-color`, focus rings,
  scrollbar colours where appropriate, `text-underline-offset` and tabular numerals in data.
  These details are a cheap but reliable sign that a page was built with care rather than assembled.

## Dependencies
- Under `conservative`, add no new dependency without asking. Under `balanced`, a small dependency is
  fine when it replaces substantial hand-written code. Under `ambitious`, allow more but still name each one.
- Before adding anything, check that it supports the framework version (React 19, Next App Router,
  SSR/`"use client"`), the bundle cost, whether it is maintained, and that its licence allows your use.
- Never add a dependency for something CSS can do: fades, transforms, hover states or simple
  scroll-driven effects with `animation-timeline` where supported.

## Motion in code
- Animate `transform` and `opacity` by default. `filter`, `clip-path` and masks are fine when they stay
  smooth. Avoid animating layout properties (width, height, top, left).
- Always add a `prefers-reduced-motion: reduce` path that keeps content visible and static.
- Content must be fully readable before any entrance runs. Never start content at `opacity: 0` with
  no fallback.

## Preserve function
- Don't break routes, handlers, forms, i18n or analytics while restyling. Run the project's
  type-check, lint and tests after changes.
- Keep diffs focused: restyle what is in scope and leave working areas alone.

## Handing off
Run `evaluation/quality-control.md` before reporting. Generate or update DESIGN.md when the
system was created or changed (`systems/design-system-generation.md`).
