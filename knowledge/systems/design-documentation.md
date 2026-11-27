# DESIGN.md format

DESIGN.md follows the open DESIGN.md format (google-labs-code/design.md, used by the design-md-library):
optional YAML front matter with tokens, then a markdown body with eight H2 sections **in this order**. Keep
the order so that linters and other tools can parse the file. The detailed topics this skill needs live as H3s inside them.

## Template
````markdown
---
version: alpha
name: <Project> Design System
description: <one line: the world and the mode>
colors:
  canvas: "#F7F4EE"
  surface: "#FFFFFF"
  text: "#1C2230"
  text-muted: "#59606E"
  action: "#2348B8"
  action-hover: "#1B3A99"
  border: "#E1DDD4"
  danger: "#B42318"
  success: "#1F7A4D"
typography:
  display:  { fontFamily: <Display>, fontSize: 56px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -0.02em }
  h1:       { fontFamily: <Display>, fontSize: 40px, fontWeight: 600, lineHeight: 1.1 }
  h2:       { fontFamily: <Display>, fontSize: 28px, fontWeight: 600, lineHeight: 1.2 }
  body:     { fontFamily: <Text>, fontSize: 16px, fontWeight: 400, lineHeight: 1.6 }
  label:    { fontFamily: <Text>, fontSize: 14px, fontWeight: 500, lineHeight: 1.4 }
  meta:     { fontFamily: <Text>, fontSize: 13px, fontWeight: 400, lineHeight: 1.4 }
rounded:
  sm: 4px
  md: 8px
  lg: 12px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  section: 96px
components:
  button-primary:
    background: "{colors.action}"
    text: "{colors.surface}"
    radius: "{rounded.md}"
    typography: "{typography.label}"
---

# <Project> Design System

## Overview
Design philosophy, brand personality and visual direction (the direction paragraph), mode(s) per surface,
audience and scene.
Director settings: containers=selective · pills=functional-only · visual-direction=adaptive · animation=balanced · density=balanced

## Colors
Each role, what it is for, and where it must not be used. Light/dark notes. Contrast pairs verified.

## Typography
Families and why. Role scale and use. Measure. Numerals. Loading strategy.

## Layout
### Spacing system
### Grid and content widths
### Responsive rules
Breakpoints, what reflows, mobile navigation, tables on narrow screens.

## Elevation & Depth
### Surfaces and backgrounds
### Shadows
What elevation means here and which elements get it.

## Shapes
### Borders and radius
### Iconography
Library, stroke, sizes, colour rules.

## Components
### Buttons
### Forms
### Navigation
### Cards and containers
Includes the nesting rule from the containers setting.
### Tables and data display
### Pills and badges
Includes the pills setting.
### Motion and interactions
Durations, easing, what moves, reduced motion.
### Accessibility
Commitments: contrast, focus, targets, keyboard, reduced motion.

## Do's and Don'ts
### Do
### Don't
### Anti-patterns for this product
Specific slop to avoid in this category, plus anything the settings forbid.
````

## Writing guidance
- Prose explains *why* and *when*, and tokens hold values. Name colours in prose descriptively and map them to tokens
  ("Seminar Ink (`text`)").
- Be specific: "Primary action colour is used only for the main action in a region and for the focus ring",
  not "use primary for important things".
- Only document what exists or is decided. A DESIGN.md full of generic advice is itself slop.
- Keep it short enough to read in five minutes. A small project might fill only half of the sections.
- Tokens must be valid: colours as `#hex`, dimensions with `px`/`em`/`rem`, references as `{group.token}`.
