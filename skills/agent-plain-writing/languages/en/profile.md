# Language profile: English (en)

The numbers live in `profile.json`. This file explains how to use them.

## Unit

- The script counts **words** (letters and digits, with internal hyphens and apostrophes).
- Blog length is counted in words.

## Limits by document type

| Type | Max sentence (words) | Max paragraph (sentences) | Length | Jargon |
|---|---|---|---|---|
| blog | 20 | 3 | 600–800 words | unlimited (3 with `--non-tech`) |
| prose | 30 | 6 | any | unlimited |
| poetry | n/a | n/a | any | unlimited |
| design | 18 | 3 | per template | unlimited |
| guide | 12 | 3 | any | at most 3 |

These are starting points. Run the script on real texts, then adjust `profile.json`.

## Voice and register

- Blog: "I" and "you". Contractions are fine ("don't", "it's").
- Guide: "you". Plain imperative verbs ("Click", "Select", "Enter"). Contractions are fine.
- Design: name the actor ("The system...", "The client..."). No "I", no "you". No contractions.
- Prose: follow the chosen point of view. Past tense by default unless the brief says otherwise.

## Requirement words (detail design)

| Level | Use |
|---|---|
| Mandatory | must |
| Forbidden | must not |
| Recommended | should |
| Optional | may |

One word per level, all through the document. Do not use "shall", "needs to", "is required to" for the same level.

## Jargon

- Reader is a developer: keep the technical name (API, token, cache). One concept, one name.
- Reader is outside the field: use the replacement table in `examples/user-guide.md`.

## Common traps in English

- Nominalizations: "perform an analysis of" → "analyze".
- Stacked prepositions and "of" chains: "the configuration of the settings of the module".
- Empty openers: "There is a...", "It is important to note that...".
- Hedging stacks: "may potentially be able to".
- Passive voice with no actor: "Errors are logged." → "The system logs errors."
- Punctuation: keep one style for the Oxford comma. Limit em dashes to one per paragraph.
