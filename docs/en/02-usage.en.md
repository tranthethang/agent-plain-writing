# Usage

Ask in plain words and give a good brief:

```
Use agent-plain-writing to write a user guide in Japanese from these notes: ...
Rewrite this API design in English. Use the api-design template. Mark missing facts as `TBD-n`.
Shorten this tech blog post. My own paragraph is attached as the model for rhythm.
```

Each file in `skills/agent-plain-writing/doc-types/` lists the brief the AI needs for that type: summary, main points, reader, a sample of your own writing, words to use or avoid. The less you give, the more the AI guesses.

## Workflow the skill follows

1. Pick the output language (`vi`, `en`, `ja`). It is the language of the text produced, not of the prompt.
2. Pick the document type. Read only that type's file and that language's examples.
3. Find the reader. Ask one question if unclear.
4. Outline, for texts longer than about 400 words.
5. Draft.
6. Edit in a separate pass: cut, check the checklist, run the checker.
7. Report the result and what had to be guessed. The report goes outside the document.

## Document types

| Type | Family | `--type` | Rules file |
|---|---|---|---|
| Tech blog | `plain` | `tech-blog` | `doc-types/tech-blog.md` |
| Essay (personal, reflective) | `creative` | `essay` | `doc-types/essay.md` |
| API design (one endpoint) | `plain` | `api-design` | `doc-types/api-design.md` |
| User guide | `plain` | `guide` | `doc-types/user-guide.md` |

Anything else falls back to `common` (`plain` family, `languages/<lang>/examples/common.md`).

For `api-design`, the AI uses a fixed template of seven sections. When the brief lacks a fact, it writes `TBD-n` only for a gap the brief names or one that blocks implementation. Known field types (from the brief, glossary, allowed-value enum, or id list) are written directly without `TBD-n`. Each `TBD-n` has one question under Open items, and no two `TBD-n` ask the same question.

Next: [03-checker](03-checker.en.md).
