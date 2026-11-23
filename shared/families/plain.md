## Voice family

Numeric limits are per language and type. They live only in `languages/<lang>/profile.json`. The type section may relax or tighten a rule. See "Who owns what" for which part wins.

### `plain` (`tech-blog`, `api-design`, `user-guide`, `common`)

One voice: **short, concrete, understood on first read.**

- **Sentence length**: `sentence` in `profile.json`.
- **Paragraph length**: `paragraph` in `profile.json`, one idea.
- **Jargon (reader outside the field)**: `terms` or `non_tech_terms` in `profile.json`. Explain each term in one sentence, or replace it with an everyday word.
- **Examples and metaphors**: One example or story per section, and a section is one main point.
- **Evaluative adjectives** ("great", "powerful", "beautiful"): Replace with a number from the source or a visible detail. If the source has no number, add none.
- **Length**: `length` in `profile.json` is a ceiling, under the type's length policy. The checker warns only above it; a shorter text is fine. Never pad to reach it. Never more than 10% over.
- **Nothing added beyond the source**: keep human context, reasoning, and reactions grounded in the brief. In specs and guides, write `TBD-n <specific question>` or ask.
