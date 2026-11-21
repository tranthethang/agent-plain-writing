# AGENTS.md

Instructions for AI agents (and humans) working **on this repository**. They are not the instructions of the skill itself. The skill's instructions are in `skills/agent-plain-writing/SKILL.md`.

## What this repository is

A single agent skill, `agent-plain-writing`, that makes AI write short, concrete, plain text in Vietnamese (`vi`), English (`en`) and Japanese (`ja`). See `README.md` for the overview.

## Layout

```
skills/agent-plain-writing/
├── SKILL.md              # workflow, core rules, voice families, routing (English)
├── doc-types/            # voice, structure, length policy per type, language-neutral (English)
├── languages/<lang>/     # profile.json, profile.md, banned.txt, banned-guide.md,
│                         # terms.txt, examples/
├── templates/            # PLAIN-WRITING.example.md
└── scripts/check_style.py
```

## Rules for editing

### General

- The supported scope for now is `vi`, `en` and `ja`, all in full. A change for one document type covers all three languages.
- `prose`, `poetry`, and `screen-design` are out of scope; their plans live in `.agent-relay/`.
- Keep changes small and focused. Do not reformat files you are not changing.
- `SKILL.md` and everything in `doc-types/` are written in **English**.
- Examples in `languages/<lang>/examples/` are written in that language. Labels (Bad, Good, Fault, Fix) stay in English.
- Do not invent facts. Stories and numbers in examples are illustrations. Keep the note that says so at the top of the file.
- Keep the skill folder name, the `name` field in the `SKILL.md` frontmatter and the paths in `README.md` identical (`agent-plain-writing`).
- The `description` in the frontmatter decides when the skill is triggered. Keep it a single quoted line, under 1,024 characters, with no double quotes inside. Keep trigger words for all three languages.

### The three language folders stay parallel

- Every language folder has the **same file set**. If you add a file in one, add it in the others (or open a note saying why not).
- Every `examples/` folder has the same five files: `common.md`, `tech-blog.md`, `essay.md`, `api-design.md`, `user-guide.md`.
- Each examples file ends with a "Your own samples" section. Keep it.

### Single sources of truth

Each fact has one owner. Other files point to the owner and do not restate the fact. This table matches the "Who owns what" section of `SKILL.md`.

| Fact | Owner | Mirror (update both) |
|---|---|---|
| Workflow and core rules for every type and language | `SKILL.md` | none |
| Voice, structure, length policy, sentence rhythm | `doc-types/<type>.md` | none |
| Kinds of phrases to ban for a type (for example meta-report openings) | `doc-types/<type>.md` | none |
| Units and numeric limits | `languages/<lang>/profile.json` | the "Units" table in `README.md` only. `profile.md` and `doc-types/` point to the key and do not repeat the number |
| Actual banned phrases | `languages/<lang>/banned.txt` | `banned-guide.md` (the same phrases with their replacements, no rule prose) |
| Grammar traps, pronoun and level words | `languages/<lang>/profile.md` | none |
| Jargon list | `languages/<lang>/terms.txt` | none |
| CLI options | `scripts/check_style.py` | `SKILL.md` and `README.md` |

**Precedence when two owners disagree:**

- On limits and structure, `doc-types/<type>.md` wins over `SKILL.md`.
- On words and grammar, `languages/<lang>/` wins over `doc-types/<type>.md`.
- On how much a text may add beyond the source (reasoning, reactions, inner thoughts), the voice family in `SKILL.md` and `doc-types/<type>.md` win over the core rules. The facts in core rule 5 never change.

### Example pairs

- Format: `**Bad:**`, `**Good:**`, then `**Fault:**` and `**Fix:**` where useful.
- A "Good" example must pass the rules of the skill. In particular, it must contain no banned phrase for its language and type.
- Complete samples (the fenced blocks near the end of each examples file) must pass the checker for their type.
- Prefer adding a pair that came from a real failure over inventing a new one.

### Japanese content

- The agent may change `ja` content, but must state that it changed `ja` and record "no native review yet".
- If you are not sure a Japanese sentence is natural, say so in your reply instead of guessing.
- Do not count Japanese text by words. The unit is characters (`char`).

### Vietnamese content

- Sentence length is counted in syllables (*tiếng*, split by spaces). One word is about 1.4 syllables.
- Keep Vietnamese diacritics intact. Do not convert files to ASCII.

### The script (`scripts/check_style.py`)

- Python 3.7+, **standard library only**. Do not add dependencies.
- Keep the exit codes: `0` clean, `1` violations, `2` usage error.
- Limits and word lists must be read from `languages/<lang>/`. Do not hard-code them.
- If you add or rename an option, update `SKILL.md` and `README.md` in the same change.
- Keep the script mechanical. It must not try to judge voice, rhyme or meter.

## Verify your change

Automated tests live in `tests/` and use the standard library only. They cover the `TBD-n` statistics and the short-brief length range in `evals/score.py`, the document-type set, the checker default type, and the "Units" table in `README.md`. Run them from the repository root:

```bash
python3 -m unittest discover -s tests
```

Run these checks by hand for the rest.

1. **Bad and good samples.** For each language you touched, write one bad paragraph (long sentence, banned phrases) and one good paragraph. The bad one must exit with `1`, the good one with `0`:

   ```bash
   python3 skills/agent-plain-writing/scripts/check_style.py bad.md  --lang en --type api-design
   python3 skills/agent-plain-writing/scripts/check_style.py good.md --lang en --type api-design
   ```

2. **Shipped samples.** Extract the last fenced block of each examples file and run the checker with the matching type (`tech-blog`, `essay`, `api-design`, `guide`). Expect no violations.
3. **Parallel folders.** Compare the file lists of `languages/vi`, `languages/en` and `languages/ja`. They must match.
4. **Mirrors.** If you changed `profile.json`, check the "Units" table in `README.md`. If you changed `banned.txt`, check that `banned-guide.md` lists the same phrases.

If you add more automated tests, put them under `tests/` and update this section and `README.md` when the run command changes.

## Do not

- Do not add a language, a document type or a core rule without updating `SKILL.md`, `README.md` and the files listed in the table above.
- Do not put secrets, personal data or real customer content in examples.
- Do not delete the "Your own samples" sections.
- Do not state that something was tested if you did not run it.
