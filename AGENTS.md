# AGENTS.md

Instructions for AI agents (and humans) working **on this repository**. They are not the instructions of the skill itself. The skill's instructions are in `skills/agent-plain-writing/SKILL.md`.

## What this repository is

A single agent skill, `agent-plain-writing`, that makes AI write short, concrete, plain text in Vietnamese (`vi`), English (`en`) and Japanese (`ja`). See `README.md` for the overview.

## Layout

```
skills/agent-plain-writing/
├── SKILL.md              # workflow, 12 core rules, routing (English)
├── doc-types/            # structure per document type, language-neutral (English)
├── languages/<lang>/     # profile.json, profile.md, banned.txt, banned-guide.md,
│                         # terms.txt, examples/
├── templates/            # PLAIN-WRITING.example.md
└── scripts/check_style.py
```

## Rules for editing

### General

- Keep changes small and focused. Do not reformat files you are not changing.
- `SKILL.md` and everything in `doc-types/` are written in **English**.
- Examples in `languages/<lang>/examples/` are written in that language. Labels (Bad, Good, Fault, Fix) stay in English.
- Do not invent facts. Stories and numbers in examples are illustrations. Keep the note that says so at the top of the file.
- Keep the skill folder name, the `name` field in the `SKILL.md` frontmatter and the paths in `README.md` identical (`agent-plain-writing`).
- The `description` in the frontmatter decides when the skill is triggered. Keep it a single quoted line, under 1,024 characters, with no double quotes inside. Keep trigger words for all three languages.

### The three language folders stay parallel

- Every language folder has the **same file set**. If you add a file in one, add it in the others (or open a note saying why not).
- Every `examples/` folder has the same six files: `common.md`, `blog.md`, `prose.md`, `poetry.md`, `detail-design.md`, `user-guide.md`.
- Each examples file ends with a "Your own samples" section. Keep it.

### Single sources of truth

| Fact | Source | Mirror (update both) |
|---|---|---|
| Units and numeric limits | `languages/<lang>/profile.json` | the table in `profile.md`, and the "Units" table in `README.md` |
| Banned phrases | `languages/<lang>/banned.txt` | `banned-guide.md` (phrases and replacements) |
| Jargon list | `languages/<lang>/terms.txt` | none |
| Core rules | `SKILL.md` | `doc-types/*.md` only where a type overrides a rule |
| CLI options | `scripts/check_style.py` | `SKILL.md` and `README.md` |

### Example pairs

- Format: `**Bad:**`, `**Good:**`, then `**Fault:**` and `**Fix:**` where useful.
- A "Good" example must pass the rules of the skill. In particular, it must contain no banned phrase for its language and type.
- Complete samples (the fenced blocks near the end of each examples file) must pass the checker for their type, except for the length of `blog` samples, which are short on purpose.
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

There is no automated test suite yet. Run these checks by hand.

1. **Bad and good samples.** For each language you touched, write one bad paragraph (long sentence, banned phrases) and one good paragraph. The bad one must exit with `1`, the good one with `0`:

   ```bash
   python3 skills/agent-plain-writing/scripts/check_style.py bad.md  --lang en --type design
   python3 skills/agent-plain-writing/scripts/check_style.py good.md --lang en --type design
   ```

2. **Shipped samples.** Extract the last fenced block of each examples file and run the checker with the matching type (`blog`, `prose`, `design`, `guide`). Expect no violations, except length for `blog`.
3. **Parallel folders.** Compare the file lists of `languages/vi`, `languages/en` and `languages/ja`. They must match.
4. **Mirrors.** If you changed `profile.json` or `banned.txt`, check that `profile.md` and `banned-guide.md` say the same thing.

If you add automated tests, put them under `tests/` and document how to run them here and in `README.md`.

## Do not

- Do not add a language, a document type or a core rule without updating `SKILL.md`, `README.md` and the files listed in the table above.
- Do not put secrets, personal data or real customer content in examples.
- Do not delete the "Your own samples" sections.
- Do not state that something was tested if you did not run it.
