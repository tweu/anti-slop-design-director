# Quality control engine

This step judges the built result independently. Its job is to find what is wrong, not to confirm that the work is
done. Treat your own output as you would a stranger's pull request.

## The loop
1. **Render.** Run the app or open the page. Use the project's dev server, or a static server for plain HTML. Use a
   browser tool if one is available (an in-app browser, Chrome DevTools MCP or Playwright). Wait for fonts and images to load.
2. **Capture** at 1440 and 390 at minimum, plus 768 and 320 for layouts that reflow. Capture the important states:
   hover, focus, empty, error, loading and a long-content case.
3. **Scan mechanically:** `python <skill>/scripts/slop_scan.py <changed files or src dir>`. If installed, also run
   the Impeccable detector. Run the project's lint, type-check and tests.
4. **Audit visually** with `visual-audit.md`. Answer each question from the captures, not from memory of the code.
5. **Check against the contract:** the direction, the mode, the settings and the finish condition from the plan.
6. **Fix in one batch.** Group related problems, fix the root cause (a token or a component), not each instance.
7. **Look again** at the affected sizes and states. Stop once the contract is met. Don't invent more work. If a
   bounded second pass can't resolve something, report it rather than claiming a pass.

## Blocking defects (must fix before handing off)
- Contrast failures, missing focus states, keyboard traps, unlabeled controls.
- Horizontal scroll, overlap or clipped text at any tested width.
- Content invisible without JavaScript, animation or hover.
- Broken images, empty visual frames, placeholder text, lorem ipsum, `TODO` in the UI.
- Controls that do nothing. Missing loading, error or empty states on reachable paths.
- Invented testimonials, metrics, logos or claims.
- Violations of the user's settings (a nested card under `containers=none`, a decorative pill under `pills=off`).
- Regressions in existing functionality.

## Quality findings (fix when in scope, otherwise report)
- Generic patterns from `core/anti-ui-slop.md` with no justification.
- Weak hierarchy (fails the squint test), monotonous rhythm, inconsistent spacing.
- Weak or default typography for the direction.
- Unnecessary shadows, borders, gradients, glass or containers.
- Inconsistent tokens: raw values, near-duplicate colours, more than one radius or button style.
- Motion without a purpose, or missing reduced-motion handling.
- Browser defaults left untouched: selection colour, focus ring, scrollbar, tabular numerals.

## If you can't render
Say so plainly: "Verified by code reading only; not rendered." Then do the strongest checks available
(the scan, a token and contrast computation, a structural read of the markup) and list what still needs a visual check.
Never describe an unrendered result as visually verified.

## Report
Report what was rendered, at which sizes and states, what the scan found, what you fixed and what remains. Keep confirmed
issues separate from judgement calls and from checks that could not run.
