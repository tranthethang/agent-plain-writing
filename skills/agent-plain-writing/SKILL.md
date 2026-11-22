---
name: agent-plain-writing
description: "Plain-language writing standard with measurable limits, for Vietnamese (vi), English (en) and Japanese (ja). Use when writing, rewriting or shortening text such as tech blogs, personal essays, API design and user guides. Also use when the user says AI writing is wordy, hard to understand or too technical. Do not use for prose, poetry or screen-design. Viết, viết lại, rút gọn văn bản tiếng Việt, Anh, Nhật (blog kỹ thuật, tản văn, tài liệu API, hướng dẫn). 文章の作成・書き直し・簡潔化 (技術ブログ、エッセイ、設計書、マニュアル)."
---

# Plain writing

Works in Vietnamese (`vi`), English (`en`) and Japanese (`ja`), grouped into two voice families: `plain` and `creative`.

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
- On how much a text may add beyond the source (reasoning, reactions, inner thoughts), the voice family below and `doc-types/<type>.md` win over the core rules. The facts in core rule 5 never change.
- Every limit that has a key in `profile.json` comes from `profile.json`. No other file repeats it.

## Workflow

0. **Check for `PLAIN-WRITING.md`** in the project root (template: `templates/PLAIN-WRITING.example.md`). If `PLAIN-WRITING.md` exists, read it and let it win on voice and terms. Use `default_lang` and `default_type` to skip the questions in steps 1 and 2.
1. **Pick the output language** (`vi`, `en` or `ja`). It is the language of the text you produce, not the language of the prompt. A Vietnamese brief that asks for a Japanese manual means `ja`. If unclear, ask one question. Then read `languages/<lang>/profile.json` (the limits for your type) and `languages/<lang>/profile.md`.
2. **Pick the document type** (table below). Read the structure file from the type table (`doc-types/<type>.md`; `common` has none) and `languages/<lang>/examples/<type>.md` (`guide` uses `examples/user-guide.md`). Also read `languages/<lang>/banned.txt` and `banned-guide.md`. Read `languages/<lang>/terms.txt` only when the type is `guide` or `--non-tech` applies. Read only these.
3. **Know the reader**: who they are, what they already know, what they must do after reading. If missing, ask one question. If you cannot ask, state your assumption outside the document (or mark `TBD-n` inline in specs).
4. **Outline** (one line per idea) for any text longer than about 400 words. Write only ideas that are in the outline. In the `creative` family, the outline fixes the scenes, not every sentence.
5. **Draft** with the core rules and the type's voice, structure and rhythm. Write normal paragraphs—never put every sentence on its own line.
6. **Edit** in a separate pass: cut, run the checklist, run the script. Fix until clean. When Python cannot run, apply the final checklist by hand and say in the report that the script did not run.
7. **Report** two things outside the generated text: the result, and what you had to guess. Never prepend or append `Result:`, `Guesses:`, or `**推測したこと:**` lines inside the document. Send the report as a second message when you can. Otherwise end the document, add one line `<!-- report -->`, then the report, and keep it out of the file that the checker reads. When you guessed nothing and added nothing, write no report and no marker. Never write a report that only says so, such as "I did not add facts beyond the brief." In specs, mark missing details inline with `TBD-n`. The script flags the labels in `banned.txt`, section `[report]`, on any line outside code blocks.

Draft and edit are two passes. Do not try to get it right in the first pass.

## Choose the document type

| Type | Family | Structure file | `--type` | Typical reader |
|---|---|---|---|---|
| Tech blog (sharing technical experience) | `plain` | `doc-types/tech-blog.md` | `tech-blog` | Peers |
| Essay (personal, reflective) | `creative` | `doc-types/essay.md` | `essay` | General readers |
| API design (one endpoint) | `plain` | `doc-types/api-design.md` | `api-design` | Developers, QA |
| User guide, manual | `plain` | `doc-types/user-guide.md` | `guide` | General users |
| Anything else | `plain` | none (`languages/<lang>/examples/common.md`) | `common` | Varies |

Always read `languages/<lang>/banned-guide.md` too (banned phrases and what replaces them).

## Core rules (both families, all languages)

These rules hold for every document type:

| # | Rule | Limit |
|---|---|---|
| 1 | One idea per sentence | In `plain`, two subordinate clauses means split. In `creative`, the type file sets sentence rhythm |
| 2 | Concrete verbs, active voice | "send", not "perform the sending of" |
| 3 | Banned phrases | Zero hits from `banned.txt` (`[all]` plus the type section) |
| 4 | Opening and closing | Opening: at most 2 sentences, straight to the point. No recap, no empty thanks |
| 5 | No invention | Add no number, event, person, place, technical spec, or outcome that is not in the source. Do not place two numbers with different units or time periods next to each other as a comparison; keep both numbers and narrow the claim to what they support. How much else a text may add (reasoning, reactions, inner thoughts) is set by its voice family |
| 6 | Consistency | One concept, one name. One register for the whole text |

## Voice families

Numeric limits are per language and type. They live only in `languages/<lang>/profile.json`. A type file may relax or tighten a rule. See "Who owns what" for which file wins.

### `plain` (`tech-blog`, `api-design`, `guide`, `common`)

One voice: **short, concrete, understood on first read.**

- **Sentence length**: `sentence` in `profile.json`.
- **Paragraph length**: `paragraph` in `profile.json`, one idea.
- **Jargon (reader outside the field)**: `terms` or `non_tech_terms` in `profile.json`. Explain each term in one sentence, or replace it with an everyday word.
- **Examples and metaphors**: One example or story per section, and a section is one main point.
- **Evaluative adjectives** ("great", "powerful", "beautiful"): Replace with a number or a visible detail.
- **Length**: `length` in `profile.json` is a ceiling, under the type's length policy. Do not pad to reach it. Never more than 10% over.
- **Nothing added beyond the source**: keep human context, reasoning, and reactions grounded in the brief. In specs and guides, write `TBD-n <specific question>` or ask.
- **`common` voice, no first person**: write about the subject, not about yourself.
- **`common` voice, no opening recap**: start with the content.
- **`common` voice, no closing summary**: end when the content ends.

### `creative` (`essay`)

- **Sentence length**: `sentence` in `profile.json`.
- **Paragraph length**: `paragraph` in `profile.json`, one idea.
- **Rhythm and imagery**: Owned by `doc-types/essay.md`.
- **Evaluative adjectives**: None without a visible detail.
- **Inner voice**: the facts stay fixed (core rule 5), but the narrator may think, remember and doubt. Use the inner material the brief gives first. When the brief gives none, `doc-types/essay.md` sets how much you may add. Report each added thought outside the text (Workflow step 7).

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

For `tech-blog` and `essay`, keep human context, reasoning, and tension instead of cutting down to a bare fact list. In `essay`, also keep the narrator's inner thoughts and the sensory detail each scene needs.

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
- [ ] Every number, event and outcome appears in the user's source. In `essay`, every inner thought that the brief does not give is reported outside the text.
- [ ] Register is consistent.
- [ ] Guesses are reported outside the generated document (or marked `TBD-n` inline in specs).

## Check with the script

`<skill-dir>` is the folder that holds `SKILL.md`.

```
python3 <skill-dir>/scripts/check_style.py draft.md --lang en --type tech-blog
python3 <skill-dir>/scripts/check_style.py spec.md  --lang ja --type api-design
python3 <skill-dir>/scripts/check_style.py guide.md --lang vi --type guide
python3 <skill-dir>/scripts/check_style.py post.md  --lang en --type tech-blog --non-tech
```

- `--lang`: `vi`, `en`, `ja` (optional if `default_lang` is set in `PLAIN-WRITING.md`). `--type`: `tech-blog`, `essay`, `api-design`, `guide`, `common` (`user-guide` also works; defaults to `default_type` in `PLAIN-WRITING.md` or `common`).
- `--short-brief`: use `length_short` for a type that has it (for example `tech-blog`).
- `--config <path>`: path to a `PLAIN-WRITING.md` config file. By default, the script reads `PLAIN-WRITING.md` from the current directory if present.
- Units differ by language: Vietnamese counts syllables (tiếng), English counts words, Japanese counts characters (字). The unit is set in `profile.json`.
- The script checks sentence length, paragraph length, banned phrases, jargon count and text length. Text length outside the range is a warning, not a violation. It does **not** judge whether the voice is good.
- Edit `banned.txt` and `terms.txt` in the language folder to fit your needs.

## Extend the skill

Whenever the AI writes a sentence you dislike:

1. Rewrite it the way you want.
2. Add the pair "bad → good" to the section "Your own samples" in the matching `examples/<type>.md` of that language.
3. If one phrase keeps coming back, add it to that language's `banned.txt` and `banned-guide.md`.

Real samples written by you always outweigh samples written by AI.

**Add a language:** create `languages/<code>/` with `profile.md`, `profile.json`, `banned.txt`, `terms.txt`, `banned-guide.md` and `examples/`. The script supports three units (`syllable`, `word`, `char`). No code change is needed.
