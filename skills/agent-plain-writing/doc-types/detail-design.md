# Detail design (API and function specs)

Use when filling a design template: API detail design, function descriptions, processing descriptions. Reader: developers and QA.

## Overrides to the core rules

- Sentence limit is a little looser (see profile).
- Jargon is allowed without limit, but **one concept gets one name**.
- No long prose. Use tables, bullets and numbered steps.
- **Fill the template only.** Do not add sections, do not remove sections.

## Principles

1. **Template only.** A section the template lacks is not added. A section with no information gets `TBD: <specific question>`.
2. **Never guess a number.** Timeout, limit, size: write it if the source has it, otherwise `TBD`.
3. **Name the actor.** "The system checks...", "The client sends...". Avoid the passive voice.
4. **Use requirement words consistently** (RFC 2119 style). One word per level, the same all through the document. The words for each language are in `profile.md`:
   - must: mandatory
   - must not: forbidden
   - should: recommended
   - may: optional
5. **Condition → result** is written "When <condition>, the system must <action>."
6. **Every error has three parts**: the condition, the HTTP status, the error code.
7. **No vague words**: "appropriate", "if necessary", "quickly", "etc." (see `banned-guide.md`).
8. **One concept, one name.** Pick "order" and never mix in "purchase" or "request" for the same thing.

## Brief the AI needs

1. The template (required).
2. The idea of the API: purpose, who calls it, when.
3. Business rules already decided.
4. One fully filled API as a model.
5. The glossary of agreed terms (if any).

If item 2 or 3 is missing, ask. Do not infer business rules.

## Checklist

- [ ] Every template section has content or `TBD`.
- [ ] No section was added outside the template.
- [ ] Every error has an HTTP status, a code and a condition.
- [ ] No number invented by the AI.
- [ ] No vague word.
- [ ] One concept, one name.
- [ ] `python3 scripts/check_style.py spec.md --lang <lang> --type design`
