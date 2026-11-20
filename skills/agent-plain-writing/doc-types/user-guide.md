# User guide (manual)

Use for guides written for general users who are not technical.

## Overrides to the core rules

- Short sentences (see profile). Each step is one action.
- At most 7 steps per procedure.
- Jargon stays within `terms` in `profile.json`. Replace each term with an everyday word, or explain it in one sentence.
- Address the reader directly ("you" or the language's equivalent).
- Button and menu names use the exact label on the screen, in bold.

## Principles

1. **The title is the thing the user wants to do**: "Change your password", not "Password management feature".
2. **One action per step**: verb + object + where to click.
3. **State the result after important steps**: "You will see the message 'Saved'".
4. **Say what the user gets. Drop the internal mechanism.** Never explain how the system works inside.
5. **Use the exact words on the screen.** If the button says "Save", write **Save**, not "confirm and save".
6. **Warnings take one line**, placed right before the risky step.
7. **End with "If something goes wrong"**, as a table: what you see → what to do.

## Structure of each guide

1. **Title**: the task.
2. **Goal** (one sentence): when to use it and what you get.
3. **Before you start** (if needed, at most 3 lines).
4. **Steps** (numbered, at most 7).
5. **If something goes wrong** (table).

## Brief the AI needs

1. The feature name and its purpose (1 or 2 lines).
2. The real steps, in order, with the exact button labels.
3. Who the user is and what they already know.
4. Common errors and the messages shown on screen.
5. Internal mechanism, **if any**: say which parts the user does not need. The AI will drop them.

## Checklist

- [ ] The title is a task.
- [ ] One action per step, within the sentence limit.
- [ ] Button names match the screen, in bold.
- [ ] No internal mechanism and no unreplaced jargon.
- [ ] There is an "If something goes wrong" section.
- [ ] `python3 scripts/check_style.py guide.md --lang <lang> --type guide`
