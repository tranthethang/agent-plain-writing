# API design

Use when you write the design of one API endpoint: purpose, fields, processing and errors. Reader: developers and QA.

## Overrides to the core rules

- Sentence limit is a little looser (see profile).
- Jargon is allowed without limit, but **one concept gets one name**.
- No long prose. Use tables, bullets and numbered steps.
- **Use the fixed template below.** Do not add sections, do not remove sections, do not reorder them.

## Principles

1. **The template owns the structure.** Write `TBD-n` (for example `TBD-1`, `TBD-2`) inline in a section or cell only for an open fact that the brief names, or for a fact without which a developer cannot implement the endpoint. Leave out a slot that the brief does not mention and that does not block implementation. A `TBD-n` is allowed when two rules in the brief conflict, or when a brief rule lacks its input (for example, `slug` comes from `title` and the brief has no `title` field). Do not open a `TBD-n` for a case that no brief rule touches. A `TBD-n` may ask for the error of a constraint that the brief states when the brief gives no code for its failure. A `TBD-n` asks for the missing decision (for example, the error when `date` is missing), not for a fact that a stated rule already implies. A bare `TBD` is not allowed. Each `TBD-n` matches one question under Open items, and two `TBD-n` must not ask the same question.
2. **One owner for each fact.** Identity owns every role rule, including a role rule on a field value (for example, only one role may set a field to a given value). Processing does not restate it. Errors are written in the Errors table only. Other sections point to them and do not repeat them. Processing lists no validation check and no role check: each check is one row in Errors (condition, HTTP status, code).
3. **Never guess a number, field type, required flag, or component.** Timeout, limit, size, type, required rule: write it if the source has it. A field type is known, not guessed, when any of these four sources gives it: the brief, the glossary, a list of allowed values (an enum of strings), or a list of ids that the glossary calls integers. A field counts as a `string` when its glossary entry describes text: a title, a body, a name, or a part of a URL. Write a known type directly in the table and do not open a `TBD-n` for it. When the source lacks a fact, write `TBD-n` only if the brief names the gap or the developer cannot implement without it; otherwise leave it out.
4. **Name the actor.** "The system checks...", "The client sends...". Avoid the passive voice.
5. **Use requirement words consistently** (RFC 2119 style). One word per level, the same all through the document. The words for each language are in `profile.md`:
   - must: mandatory
   - must not: forbidden
   - should: recommended
   - may: optional
6. **Condition → result** is written "When <condition>, the system must <action>."
7. **Every error has three parts**: the condition, the HTTP status, the error code. Every validation check and every role check is one row in Errors. The Errors table owns the HTTP status and the condition. When the code is an open fact, mark it `TBD-n`. No sentence only points to the Errors table.
8. **No vague words**: no word that leaves a condition, an amount or a speed open. The words for each language are in `banned.txt`, section `[api-design]`, with replacements in `banned-guide.md`.
9. **One concept, one name.** Pick "order" and never mix in "purchase" or "request" for the same thing.
10. **No pointer to another API.** Do not write "same as the other endpoints". Write the rule here.

## Template

Write these sections in this order.

1. **Identity.** Method, path, purpose, and every role rule (here only). Add caller and idempotency only when the brief states them or when the developer cannot implement without them.
2. **DTO and field mapping.** Request and response fields in one table with the columns Field, Direction, Type, Required, Constraint, in this order. Direction is `Request` or `Response` (labels in `profile.md`). Response fields are rows in the same table, not a line outside it. A response with unknown fields is one row with `TBD-n` as its type. Required uses the labels in `profile.md`, or `TBD-n`. Write a known field type (Principle 3) directly in the table with no `TBD-n`. Use `TBD-n` for a field type only when the type is not known and it blocks implementation. Write `—` in a cell that has no value. Do not leave a cell empty.
3. **Endpoint.** One request example and one success response example with its status. Write the success status here only. An example holds no `TBD-n`. Use only fields whose type the brief or the glossary gives. When no such field is known, leave out that example and write nothing in its place.
4. **Processing.** Number the steps in execution order only when the brief states the order; otherwise list unnumbered rules and mark execution order or error precedence `TBD-n`. Processing holds only behavior that no other section owns: generated values, defaults, the execution-order line and the error-precedence line. It lists no validation check and no role check; those live in Errors (and the role rule in Identity). When the section has nothing else, it holds only the order and precedence line. Skip the Mermaid diagram when the execution order is `TBD-n` or fewer than three nodes carry meaning, and write nothing in its place. Otherwise add one Mermaid sequence diagram or flowchart in a fenced code block using only actors and components named in the brief. Give each rule that has an empty or edge case its own step.
5. **Errors.** One table with condition, HTTP status and code. Errors appear nowhere else.
6. **Side effects.** Audit, events, cache, async jobs. When the brief states no side effect, or the call is read-only, the section text is exactly `None` (the label in `profile.md`), with no sentence around it. Add other effects only when the brief states them or when the developer cannot implement without them. Never repeat the main action of the API.
7. **Open items.** Every `TBD-n` with its question (write each question here once; keep inline cells to `TBD-n`; no duplicate question, see Principle 1). Open items hold spec questions only: do not ask for an example, ask one thing per question (the HTTP status and the code of one error row are one question), and do not ask what the brief already answers.

The template excludes tech stack, convention, error contract, changelog and test links. The project convention lives outside the API file.

## Brief the AI needs

1. The idea of the API: purpose, who calls it, when.
2. Business rules already decided.
3. One fully filled API as a model.
4. The glossary of agreed terms (if any).

If item 1 or 2 is missing, ask. Do not infer business rules.

## Checklist

- [ ] Every template section is present in the template order.
- [ ] `TBD-n` appears only for a gap the brief names or that blocks implementation, and never for a case that no brief rule touches (a rule conflict, a rule that lacks its input, and the error of a stated constraint with no code are allowed). A `TBD-n` asks for the missing decision, not for a fact a stated rule implies, with each `TBD-n` matched to one question in Open items. No bare `TBD`. No `TBD-n` in an example, and no example field whose type is unknown.
- [ ] Open items hold spec questions only, one question per item, with no request for an example and no question the brief already answers.
- [ ] No section was added outside the template.
- [ ] Every role rule, including one on a field value, appears in Identity only. Processing lists no role check.
- [ ] Required-flag labels follow `profile.md`.
- [ ] Every error is in the Errors table with an HTTP status, a code and a condition.
- [ ] Every validation check and role check is one row in Errors. Processing lists none of them.
- [ ] The DTO table has the columns Field, Direction, Type, Required, Constraint, with response fields as rows.
- [ ] Processing holds only generated values, defaults, the order line and the precedence line.
- [ ] No table cell is empty. The success status appears in Endpoint only.
- [ ] Side effects never repeat the main action. The section is exactly `None` when the call is read-only or the brief states no side effect.
- [ ] Processing is numbered only when the brief gives the order; otherwise unnumbered with precedence `TBD-n`.
- [ ] Mermaid diagram is skipped when execution order is `TBD-n` or fewer than three nodes carry meaning; otherwise it uses only actors and components named in the brief.
- [ ] No two `TBD-n` ask the same question.
- [ ] No number, field type, required flag, or component invented by the AI. A known field type (Principle 3) is written, not opened as `TBD-n`.
- [ ] No vague word.
- [ ] One concept, one name.
- [ ] `python3 scripts/check_style.py spec.md --lang <lang> --type api-design`
