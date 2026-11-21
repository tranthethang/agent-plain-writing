# API design

Use when you write the design of one API endpoint: purpose, fields, processing and errors. Reader: developers and QA.

## Overrides to the core rules

- Sentence limit is a little looser (see profile).
- Jargon is allowed without limit, but **one concept gets one name**.
- No long prose. Use tables, bullets and numbered steps.
- **Use the fixed template below.** Do not add sections, do not remove sections, do not reorder them.

## Principles

1. **The template owns the structure.** Write `TBD-n` (for example `TBD-1`, `TBD-2`) inline in a section or cell when information is missing. A bare `TBD` is not allowed, including in an example value. Each `TBD-n` matches one question under Open items.
2. **One owner for each fact.** Authorization is written in Identity only. Processing points to Identity and does not restate the role rule. Errors are written in the Errors table only. Other sections point to them and do not repeat them.
3. **Never guess a number, field type, required flag, or component.** Timeout, limit, size, type, required rule: write it if the source has it, otherwise `TBD-n`.
4. **Name the actor.** "The system checks...", "The client sends...". Avoid the passive voice.
5. **Use requirement words consistently** (RFC 2119 style). One word per level, the same all through the document. The words for each language are in `profile.md`:
   - must: mandatory
   - must not: forbidden
   - should: recommended
   - may: optional
6. **Condition → result** is written "When <condition>, the system must <action>."
7. **Every error has three parts**: the condition, the HTTP status, the error code. Every validation check in Processing must match one row in Errors, or mark its error status or code as `TBD-n`.
8. **No vague words**: no word that leaves a condition, an amount or a speed open. The words for each language are in `banned.txt`, section `[api-design]`, with replacements in `banned-guide.md`.
9. **One concept, one name.** Pick "order" and never mix in "purchase" or "request" for the same thing.
10. **No pointer to another API.** Do not write "same as the other endpoints". Write the rule here.

## Template

Write these sections in this order.

1. **Identity.** Method, path, purpose, caller, authorization (here only), idempotency.
2. **DTO and field mapping.** Request and response fields in a table with type, required (`Yes`, `No`, `Conditional (<rule>)`, or `TBD-n`), and constraint. Keep the labels `Yes`, `No`, and `Conditional` in English in every language.
3. **Endpoint.** One request example and one success response example with its status. Use `TBD-n` (never bare `TBD`) for any unknown example value.
4. **Processing.** Number the steps in execution order only when the brief states the order; otherwise list unnumbered rules and mark execution order or error precedence `TBD-n`. Point to Identity for authorization instead of restating role rules. Skip the Mermaid diagram when the execution order is `TBD-n` or fewer than three nodes carry meaning; write `TBD-n` in its place. Otherwise add one Mermaid sequence diagram or flowchart in a fenced code block using only actors and components named in the brief. Give each rule that has an empty or edge case its own step.
5. **Errors.** One table with condition, HTTP status and code. Errors appear nowhere else.
6. **Side effects.** Audit, events, cache, async jobs. Write `None` for a read-only call, or `TBD-n` when the brief is silent. Never repeat the main action of the API.
7. **Open items.** Every `TBD-n` with its question (write each question here once; keep inline cells to `TBD-n`). Open items hold spec questions only: do not ask for an example, ask one thing per question, and do not ask what the brief already answers.

The template excludes tech stack, convention, error contract, changelog and test links. The project convention lives outside the API file.

## Brief the AI needs

1. The idea of the API: purpose, who calls it, when.
2. Business rules already decided.
3. One fully filled API as a model.
4. The glossary of agreed terms (if any).

If item 1 or 2 is missing, ask. Do not infer business rules.

## Coverage checklist

Check that the spec covers or marks `TBD-n` for each of these gaps:

- Missing field of a conditional rule
- Empty array
- Field used to derive another field
- Value outside an enum
- Response body
- Error body

## Checklist

- [ ] Every template section has content or `TBD-n`, in the template order.
- [ ] Missing facts use `TBD-n` inline (no bare `TBD`, including in example values), with each `TBD-n` matched to one question in Open items.
- [ ] Open items hold spec questions only, one question per item, with no request for an example and no question the brief already answers.
- [ ] No section was added outside the template.
- [ ] Authorization appears in Identity only; Processing points to Identity.
- [ ] `Yes`, `No`, and `Conditional` stay in English.
- [ ] Every error is in the Errors table with an HTTP status, a code and a condition.
- [ ] Every validation check in Processing matches a row in Errors, or marks its error status or code as `TBD-n`.
- [ ] Processing is numbered only when the brief gives the order; otherwise unnumbered with precedence `TBD-n`.
- [ ] Mermaid diagram is skipped when execution order is `TBD-n` or fewer than three nodes carry meaning; otherwise it uses only actors and components named in the brief.
- [ ] All six coverage checklist gaps are addressed or marked `TBD-n`.
- [ ] No number, field type, required flag, or component invented by the AI.
- [ ] No vague word.
- [ ] One concept, one name.
- [ ] `python3 scripts/check_style.py spec.md --lang <lang> --type api-design`
