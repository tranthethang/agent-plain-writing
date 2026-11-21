# Language profile: English (en)

The numbers live in `profile.json`. This file explains how to use them.

## Unit

- The script counts **words** (letters and digits, with internal hyphens and apostrophes).
- `length` in `profile.json` is counted in words.

## Limits and voice

Every number (sentence, paragraph, length, jargon) lives in `profile.json`. This file does not repeat them.
Voice, speaker and structure are set by `doc-types/<type>.md`. The language adds only its forms:

- Pronouns: "I" and "you". Contractions ("don't", "it's") are a register choice that the type file makes.
- Plain imperative verbs for steps ("Click", "Select", "Enter"). Button names in bold, exactly as on screen.

## Requirement words (API design)

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
