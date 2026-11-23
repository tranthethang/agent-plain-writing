# AGENTS.md

Use this guide when you edit this project.
The skill rules themselves live in `skills/*/SKILL.md`.
Edit `shared/` instead of those generated files.

## What this project is

This project holds six skills.
One router (`agent-plain-writing`) picks the type and language.
Five sub-skills (`agent-plain-writing-<type>`) hold the writing rules.

They help AI write plain text.
Supported languages are Vietnamese (`vi`), English (`en`), and Japanese (`ja`).
See `README.md` for an overview.

## Layout

```
shared/                   # the only place to edit skill content
├── skill-core.md         # workflow, core rules, checklist (English)
├── families/             # plain.md, creative.md: voice families (English)
├── doc-types/<type>.md   # sub-skill frontmatter, voice, structure, length policy (English)
├── languages/<lang>/     # profile.json, profile.md, banned.txt, banned-guide.md,
│                         # terms.txt, examples/
├── templates/            # PLAIN-WRITING.example.md
└── scripts/check_style.py

scripts/sync_shared.py    # builds skills/ from shared/ (--check compares)
.githooks/pre-commit      # runs sync_shared.py --check

skills/                   # generated, except the router. Never edit by hand
├── agent-plain-writing/               # router: SKILL.md only, edited by hand
└── agent-plain-writing-<type>/        # tech-blog, essay, api-design, user-guide, common
    ├── SKILL.md          # generated
    ├── languages/        # copy of shared/languages/ (only examples/<type>.md)
    ├── scripts/          # copy of shared/scripts/check_style.py
    └── templates/        # copy of shared/templates/

evals/                    # cases/, smoke-prompts.md, score.py, judge-prompt.md
evidence/<run>/           # outputs and results.json from real-agent runs (tracked)
tests/                    # unittest, standard library only
```

Run `git config core.hooksPath .githooks` once after you clone.
After you edit `shared/`, run `python3 scripts/sync_shared.py`.
Then commit the generated files.

## Rules for editing

### General

- Support `vi`, `en`, and `ja` in full. Update all three languages when you change a document type.
- Leave `prose`, `poetry`, and `screen-design` out of scope. Their plans live in `.agent-relay/`.
- Keep changes small and focused. Do not reformat unchanged files.
- Write `shared/skill-core.md`, `shared/families/`, `shared/doc-types/`, and the router `SKILL.md` in **English**.
- Write examples in `languages/<lang>/examples/` in that language. Keep labels (Bad, Good, Fault, Fix) in English.
- Do not invent facts. Stories and numbers in examples are illustrations. Keep the note at the top of the file.
- Match each skill folder name, frontmatter `name`, and `README.md` path (`agent-plain-writing`, `agent-plain-writing-<type>`).
- The frontmatter `description` controls when a skill triggers. Keep it one quoted line under 1,024 characters. Avoid double quotes inside. Keep trigger words for all three languages. Match the router `description` only to unclear requests. Put each sub-skill `description` at the top of `shared/doc-types/<type>.md`.
- Use `user-guide` everywhere for the user guide type. Do not use a `guide` alias.

### The three language folders stay parallel

- Every language folder in `shared/` has the **same file set**. Add new files to all three folders, or explain why not.
- Every `shared/languages/<lang>/examples/` folder has five files: `common.md`, `tech-blog.md`, `essay.md`, `api-design.md`, and `user-guide.md`. Each `skills/` folder keeps only its own `examples/<type>.md`.
- End each examples file with a "Your own samples" section.

### Single sources of truth

Each fact has one owner.
Other files point to the owner without restating the fact.
This table matches the "Who owns what" section in each generated `SKILL.md`.

Edit only the owner in `shared/`.
Never edit generated `SKILL.md` files or copies in `skills/*/`.

| Fact | Owner | Mirror (update both) |
|---|---|---|
| Workflow and core rules for every type and language | `shared/skill-core.md` | none |
| Voice family text | `shared/families/<family>.md` | none |
| Voice, structure, length policy, sentence rhythm | `shared/doc-types/<type>.md` | none |
| Kinds of phrases to ban for a type (for example meta-report openings) | `shared/doc-types/<type>.md` | none |
| Routing between sub-skills | `skills/agent-plain-writing/SKILL.md` | none |
| Units and numeric limits | `shared/languages/<lang>/profile.json` | the "Units" table in `README.md` only. `profile.md` and `doc-types/` point to the key and do not repeat the number |
| Actual banned phrases | `shared/languages/<lang>/banned.txt` | `banned-guide.md` (the same phrases with their replacements, no rule prose) |
| Grammar traps, pronoun and level words | `shared/languages/<lang>/profile.md` | none |
| Jargon list | `shared/languages/<lang>/terms.txt` | none |
| CLI options | `shared/scripts/check_style.py` | `shared/skill-core.md` and `README.md` |

**Precedence when two owners disagree:**

- On limits and structure, `shared/doc-types/<type>.md` beats `shared/skill-core.md`.
- On words and grammar, `shared/languages/<lang>/` beats `shared/doc-types/<type>.md`.
- On extra content (reasoning, reactions, thoughts), voice rules beat core rules. Core rule 5 facts never change.
- `limits` in `PLAIN-WRITING.md` override `profile.json` for that project. The checker warns above 1.5 times the profile value.

### Example pairs

- Format pairs as `**Bad:**`, `**Good:**`, then `**Fault:**` and `**Fix:**` when useful.
- Every "Good" example must pass the skill rules. It must contain no banned phrase for its language and type.
- Complete samples in each examples file must pass the checker.
- Add pairs from real failures instead of inventing new ones.

### Japanese content

- If you are unsure a Japanese sentence is natural, say so. Do not guess.
- Count Japanese text in characters (`char`), not words.

### Vietnamese content

- Count sentence length in syllables (*tiếng*, split by spaces). One word is about 1.4 syllables.
- Keep Vietnamese diacritics intact. Never convert files to ASCII.

### The script (`shared/scripts/check_style.py`)

- Use Python 3.15+ with built-in modules only. Do not add dependencies.
- Keep exit codes: `0` clean, `1` violations, `2` usage error.
- Read limits and word lists from `languages/<lang>/` next to the script. Do not hard-code them.
- When you change an option, update `shared/skill-core.md` and `README.md` together. Then run `sync_shared.py`.
- Keep the script mechanical. Never judge voice, rhyme, or meter.

## Verify your change

Automated tests live in `tests/` and use built-in Python modules only.
They cover:

- `TBD-n` statistics and short-brief length range in `evals/score.py`
- Document-type set and checker default type
- Table-cell, report-label, and `--short-brief` checks
- "Units" tables in `README.md` and `docs/vi/README.md`
- Shipped samples in `examples/` (`tests/test_examples_samples.py`)
- Report marker in `evals/score.py`
- Time and date token count
- `PLAIN-WRITING.md` search from a subfolder
- Length warning above the upper limit only
- `doc-types/` file for every type (`tests/test_doc_types.py`)
- Parity of generated sub-skills with `shared/` (`tests/test_shared_sync.py`)

Run them from the project root:

```bash
python3 -m unittest discover -s tests
python3 scripts/sync_shared.py --check
```

GitHub Actions (`.github/workflows/test.yml`) runs both commands on `main`.
It uses Python 3.15.2 for pushes and pull requests.

Run these manual checks for everything else:

1. **Bad and good samples.** Write one bad paragraph and one good paragraph per language. The bad one must exit `1`. The good one must exit `0`:

   ```bash
   python3 shared/scripts/check_style.py bad.md  --lang en --type api-design
   python3 shared/scripts/check_style.py good.md --lang en --type api-design
   ```

2. **Shipped samples.** `tests/test_examples_samples.py` covers these. As a fallback, test the last fenced block of each examples file. Use its matching type and expect zero violations.
3. **Parallel folders.** Compare file lists in `shared/languages/vi`, `en`, and `ja`. They must match.
4. **Generated files.** Run `python3 scripts/sync_shared.py --check`. It exits `0` when all sub-skills match `shared/`.
5. **Mirrors.** If you changed `profile.json`, check the "Units" table in `README.md`. If you changed `banned.txt`, check `banned-guide.md` for matching phrases.

Put new automated tests under `tests/`.
Update this section and `README.md` if the run command changes.

## Do not

- Do not edit a generated `SKILL.md` or copied file in `skills/agent-plain-writing-<type>/`.
- Never add a language, type, or core rule in one place. Update `shared/`, the router, `README.md`, and the owner table.
- Do not put secrets, personal data, or real customer content in examples.
- Do not delete the "Your own samples" sections.
- Never claim you tested something you did not run.
