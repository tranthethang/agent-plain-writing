---
name: agent-plain-writing
description: "Plain-language writing standard with measurable limits, for Vietnamese (vi), English (en) and Japanese (ja). Use when writing, rewriting or shortening text such as blog posts, fiction and prose, poetry, detail design (API specs) and user guides. Also use when the user says AI writing is wordy, hard to understand or too technical. Viết, viết lại, rút gọn văn bản tiếng Việt, Anh, Nhật. 文章の作成・書き直し・簡潔化 (ブログ、設計書、マニュアル)."
---

# Plain writing

One voice: **short, concrete, understood on first read.**
Works in Vietnamese (`vi`), English (`en`) and Japanese (`ja`).

## Who owns what

Each rule has one owner. Read a rule in its owner file, not in a copy.

| Owner | Owns |
|---|---|
| `SKILL.md` (this file) | The workflow and the core rules that hold for every type and every language |
| `doc-types/<type>.md` | Everything that depends on the type: voice, structure, length policy, sentence rhythm, and the kinds of phrases to ban |
| `languages/<lang>/` | Everything that depends on the language: the unit, numeric limits (`profile.json`), the actual banned phrases (`banned.txt`, `banned-guide.md`), grammar traps, pronoun and level words, terms (`terms.txt`), and examples |

**When two owners disagree:**

- On limits and structure, `doc-types/<type>.md` wins over `SKILL.md`.
- On words and grammar, `languages/<lang>/` wins over `doc-types/<type>.md`.
- Every limit that has a key in `profile.json` comes from `profile.json`. No other file repeats it.

## Workflow

0. **Check for `PLAIN-WRITING.md`** in the project root (template: `templates/PLAIN-WRITING.example.md`). If `PLAIN-WRITING.md` exists, read it and let it win on voice and terms. Use `default_lang` and `default_type` to skip the questions in steps 1 and 2.
1. **Pick the output language** (`vi`, `en` or `ja`). It is the language of the text you produce, not the language of the prompt. A Vietnamese brief that asks for a Japanese manual means `ja`. If unclear, ask one question. Then read `languages/<lang>/profile.json` (the limits for your type) and `languages/<lang>/profile.md`.
2. **Pick the document type** (table below). Read `doc-types/<type>.md` and `languages/<lang>/examples/<type>.md`. Read only these.
3. **Know the reader**: who they are, what they already know, what they must do after reading. If missing, ask one question. If you cannot ask, state your assumption outside the document (or mark `TBD:` inline in specs).
4. **Outline** (one line per idea) for any text longer than about 400 words. Write only ideas that are in the outline.
5. **Draft** with the core rules and the type's voice, structure and rhythm. Write normal paragraphs—never put every sentence on its own line.
6. **Edit** in a separate pass: cut, run the checklist, run the script. Fix until clean.
7. **Report** two things outside the generated text: the result, and what you had to guess. Never prepend or append `Result:`, `Guesses:`, `---`, or `**推測したこと:**` lines inside the document. When your reply is the document itself and you have no other place for a note, leave the report out. In specs, mark missing details inline with `TBD:`. The script flags the labels in `banned.txt`, section `[report]`, on the first or last 3 lines.

Draft and edit are two passes. Do not try to get it right in the first pass.

## Choose the document type

| Type | Structure file | `--type` | Typical reader |
|---|---|---|---|
| Blog post (sharing experience) | `doc-types/blog.md` | `blog` | Peers |
| Fiction, essay, scene | `doc-types/prose.md` | `prose` | Readers of literature |
| Poetry | `doc-types/poetry.md` | `poetry` | Readers of poetry |
| Detail design (API, function specs) | `doc-types/detail-design.md` | `design` | Developers, QA |
| User guide, manual | `doc-types/user-guide.md` | `guide` | General users |
| Anything else | `languages/<lang>/examples/common.md` | `blog` | Varies |

Always read `languages/<lang>/banned-guide.md` too (banned phrases and what replaces them).

## Core rules (all languages)

Numeric limits are per language and type. They live only in `languages/<lang>/profile.json`.

| # | Rule | Limit |
|---|---|---|
| 1 | Sentence length | `sentence` in `profile.json` |
| 2 | Paragraph length | `paragraph` in `profile.json`, one idea |
| 3 | One idea per sentence | Two subordinate clauses means split |
| 4 | Concrete verbs, active voice | "send", not "perform the sending of" |
| 5 | Banned phrases | Zero hits from `banned.txt` (`[all]` plus the type section) |
| 6 | Jargon (reader outside the field) | `terms` or `non_tech_terms` in `profile.json`. Explain each term in one sentence, or replace it with an everyday word |
| 7 | Examples and metaphors | One example or story per section, and a section is one main point |
| 8 | Evaluative adjectives ("great", "powerful", "beautiful") | Replace with a number or a visible detail |
| 9 | Opening and closing | Opening: at most 2 sentences, straight to the point. No recap, no empty thanks |
| 10 | No invention | Add no number, technical spec, or outcome that is not in the source. In `blog` and `prose`, keep human context, reasoning, and reactions grounded in the brief; in specs and guides, write `TBD: <specific question>` or ask |
| 11 | Consistency | One concept, one name. One register for the whole text |
| 12 | Length | `length` in `profile.json`, under the type's length policy. Never more than 10% over |

A type file may relax or tighten a core rule (prose allows longer sentences, detail design allows more jargon). See "Who owns what" for which file wins.

**Paragraph form:** Write sentences continuously inside a paragraph—never split every sentence onto its own line (no trailing-space `  \n` line breaks). Sentence rhythm is set by the type file.

## When the reader is outside the field

Common failure: the AI "translates" every technical detail into plain words. The result is three times longer and still unclear. Do the opposite:

1. Pick **at most 3 ideas** the reader needs.
2. For each idea, say **what the reader gets or can do**. Drop the internal mechanism.
3. Test each sentence: if you delete it, will the reader fail at something or misunderstand something? If not, delete it.

## Cutting order for long drafts

1. Sentences that repeat an earlier idea.
2. Sentences that explain internal mechanism.
3. The second and later examples.
4. Adjectives and adverbs.
5. Empty opening and closing.

For `blog` and `prose`, keep human context, reasoning, and tension instead of cutting down to a bare fact list.

## When editing existing text

- Keep meaning, proper names, numbers, paths and code unchanged.
- Add no new information. List ambiguous spots at the end so the author can decide.
- Give a table "original → revised → reason" if the user wants to learn from the edit.

## Final checklist

- [ ] The script reports no violations.
- [ ] One idea per paragraph, one idea per sentence.
- [ ] No banned phrase. No empty adjective.
- [ ] Jargon is within the limit. Each term is explained or replaced.
- [ ] The type file's checklist passes.
- [ ] Every number and claim appears in the user's source.
- [ ] Register is consistent.
- [ ] Guesses are reported outside the generated document (or marked `TBD:` inline in specs).

## Check with the script

```
python3 scripts/check_style.py draft.md --lang en --type blog
python3 scripts/check_style.py spec.md  --lang ja --type design
python3 scripts/check_style.py guide.md --lang vi --type guide
python3 scripts/check_style.py post.md  --lang en --type blog --non-tech
```

- `--lang`: `vi`, `en`, `ja` (optional if `default_lang` is set in `PLAIN-WRITING.md`). `--type`: `blog`, `prose`, `poetry`, `design`, `guide` (`detail-design` and `user-guide` also work; defaults to `default_type` in `PLAIN-WRITING.md` or `blog`).
- `--config <path>`: path to a `PLAIN-WRITING.md` config file. By default, the script reads `PLAIN-WRITING.md` from the current directory if present.
- Units differ by language: Vietnamese counts syllables (tiếng), English counts words, Japanese counts characters (字). The unit is set in `profile.json`.
- The script checks sentence length, paragraph length, banned phrases, jargon count and text length. It does **not** judge whether the voice is good, and it does not check rhyme or meter.
- Edit `banned.txt` and `terms.txt` in the language folder to fit your needs.

## Extend the skill

Whenever the AI writes a sentence you dislike:

1. Rewrite it the way you want.
2. Add the pair "bad → good" to the section "Your own samples" in the matching `examples/<type>.md` of that language.
3. If one phrase keeps coming back, add it to that language's `banned.txt` and `banned-guide.md`.

Real samples written by you always outweigh samples written by AI.

**Add a language:** create `languages/<code>/` with `profile.md`, `profile.json`, `banned.txt`, `terms.txt`, `banned-guide.md` and `examples/`. The script supports three units (`syllable`, `word`, `char`). No code change is needed.
