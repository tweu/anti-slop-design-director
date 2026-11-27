# Interaction design

Every control gives feedback, every action has a visible result and every error has a way out.

## Feedback
- **Hover** (pointer devices): a visible change on every interactive element, meaning a colour shift, underline or
  slight lift. Never rely on hover alone to reveal essential controls, because touch devices have no hover.
- **Press/active:** immediate (under 100ms) visual response.
- **Focus-visible:** a clear ring (at least 2px, at least 3:1 contrast, with offset) on every focusable element. Never use
  `outline: none` without a replacement.
- **Loading:** show progress for anything over about 300ms. Use skeletons that match the real layout for content and
  in-button spinners for actions (keep the button width stable and disable it to prevent a double submit).
- **Success:** confirm in place (an inline message or row highlight). Show a toast only for actions without an
  on-screen result. Confirm only after a real success response.
- **Optimistic UI** for low-risk, high-frequency actions (like, star, toggle), with rollback and a message on failure.

## Forms
- Use visible labels above the fields. Placeholders are examples, not labels.
- Group related fields and use a single column for most forms.
- Validate on blur or submit, not on every keystroke. Put errors next to the field, saying what is wrong and how to
  fix it. Add an error summary at the top for long forms, with links to the fields.
- Use the correct input `type`, `inputmode` and `autocomplete`. Mark required fields, or optional ones if fewer.
- Use helper text for format constraints *before* the user errs.
- Never wipe user input on error.
- Destructive actions need a clear verb ("Delete 3 posts"), friction proportional to the risk and an undo where possible
  (undo beats a confirmation dialog).

## States every screen considers
Default · loading · empty (first use, no results, cleared) · partial · error (recoverable, fatal,
offline) · success · disabled (explain why when it isn't obvious) · permission denied · very long content ·
very many items.

**Empty states** teach: what goes here, why it's empty and the one action that fills it. They are a
chance to show the product's voice, but they are not a place for a decorative illustration with no action.

## Copy in the interface
- Buttons are a verb plus an object ("Save draft", "Invite member"). Avoid "Submit", "OK" and "Click here".
- Error messages name the problem and the recovery, in the product's language, without blame.
- Use one term per concept across the product ("post" or "thread", not both).

## Overlays
- Use a modal only when the task needs interruption or protected focus. Trap focus, close on Esc, return focus to the
  trigger and never stack modals.
- Use popovers and menus for small choices, and drawers or side panels for detail views that keep context.
- Tooltips supplement and never hold essential information. They must be reachable by keyboard.

## Navigation flow
- Back behaviour is predictable, and URL state is deep-linkable (filters, tabs, pagination).
- Preserve scroll position and form state when returning.
- Long processes show progress and allow saving and resuming.

## Performance as interaction
- Reserve space for images and async content to avoid layout shift (CLS < 0.1).
- Debounce search input. Virtualise long lists (500+ rows).
- Keep the main thread responsive. Interactions should paint within about 200ms (INP).
