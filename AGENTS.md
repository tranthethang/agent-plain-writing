# AGENTS.md

Instructions for AI agents (and humans) working **on this repository**. They are not the instructions of the skill itself. The skills' instructions are in the generated `skills/*/SKILL.md` files. You edit `shared/`, not those files.

## What this repository is

A set of six agent skills: a router, `agent-plain-writing`, and five sub-skills, one for each document type (`agent-plain-writing-<type>`). They make AI write short, concrete, plain text in Vietnamese (`vi`), English (`en`) and Japanese (`ja`). See `README.md` for the overview.

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

Run `git config core.hooksPath .githooks` once after you clone. After you edit `shared/`, run `python3 scripts/sync_shared.py` and commit the generated files.


## Rules for editing

### General

- The supported scope for now is `vi`, `en` and `ja`, all in full. A change for one document type covers all three languages.
- `prose`, `poetry`, and `screen-design` are out of scope; their plans live in `.agent-relay/`.
- Keep changes small and focused. Do not reformat files you are not changing.
- `shared/skill-core.md`, `shared/families/`, `shared/doc-types/` and the router `SKILL.md` are written in **English**.
- Examples in `languages/<lang>/examples/` are written in that language. Labels (Bad, Good, Fault, Fix) stay in English.
- Do not invent facts. Stories and numbers in examples are illustrations. Keep the note that says so at the top of the file.
- Keep each skill folder name, the `name` field in its `SKILL.md` frontmatter and the paths in `README.md` identical (`agent-plain-writing`, `agent-plain-writing-<type>`).
- The `description` in the frontmatter decides when a skill is triggered. Keep it a single quoted line, under 1,024 characters, with no double quotes inside. Keep trigger words for all three languages. The router `description` matches only a general request with an unclear type. Write each sub-skill `description` at the top of `shared/doc-types/<type>.md`.
- The type name for the user guide is `user-guide` everywhere. There is no `guide` alias.

### The three language folders stay parallel

- Every language folder in `shared/` has the **same file set**. If you add a file in one, add it in the others (or open a note saying why not).
- Every `shared/languages/<lang>/examples/` folder has the same five files: `common.md`, `tech-blog.md`, `essay.md`, `api-design.md`, `user-guide.md`. Each generated folder in `skills/` holds only its own `examples/<type>.md`.
- Each examples file ends with a "Your own samples" section. Keep it.

### Single sources of truth

Each fact has one owner. Other files point to the owner and do not restate the fact. This table matches the "Who owns what" section of each generated `SKILL.md`. Edit the owner in `shared/`. Generated `SKILL.md` files and the copies in `skills/*/` are never edited.

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

- On limits and structure, `shared/doc-types/<type>.md` wins over `shared/skill-core.md`.
- On words and grammar, `shared/languages/<lang>/` wins over `shared/doc-types/<type>.md`.
- On how much a text may add beyond the source (reasoning, reactions, inner thoughts), the voice family in `shared/families/` and `shared/doc-types/<type>.md` win over the core rules. The facts in core rule 5 never change.
- `limits` in `PLAIN-WRITING.md` override `profile.json` for that project. The checker warns above 1.5 times the profile value.

### Example pairs

- Format: `**Bad:**`, `**Good:**`, then `**Fault:**` and `**Fix:**` where useful.
- A "Good" example must pass the rules of the skill. In particular, it must contain no banned phrase for its language and type.
- Complete samples (the fenced blocks near the end of each examples file) must pass the checker for their type.
- Prefer adding a pair that came from a real failure over inventing a new one.

### Japanese content

- If you are not sure a Japanese sentence is natural, say so in your reply instead of guessing.
- Do not count Japanese text by words. The unit is characters (`char`).

### Vietnamese content

- Sentence length is counted in syllables (*tiếng*, split by spaces). One word is about 1.4 syllables.
- Keep Vietnamese diacritics intact. Do not convert files to ASCII.

### The script (`shared/scripts/check_style.py`)

- Python 3.7+, **standard library only**. Do not add dependencies.
- Keep the exit codes: `0` clean, `1` violations, `2` usage error.
- Limits and word lists must be read from `languages/<lang>/` next to the script. Do not hard-code them.
- If you add or rename an option, update `shared/skill-core.md` and `README.md` in the same change, then run `sync_shared.py`.
- Keep the script mechanical. It must not try to judge voice, rhyme or meter.

## Verify your change

Automated tests live in `tests/` and use the standard library only. They cover the `TBD-n` statistics and the short-brief length range in `evals/score.py`, the document-type set, the checker default type, the checker's table-cell, report-label and `--short-brief` checks, the "Units" tables in `README.md` and `docs/vi/README.md`, the shipped samples in `examples/` (`tests/test_examples_samples.py`), the report marker in `evals/score.py`, the time and date token count, the `PLAIN-WRITING.md` search from a subfolder, the length warning above the upper limit only, the `doc-types/` file for every type (`tests/test_doc_types.py`), and the parity of the generated sub-skills with `shared/` (`tests/test_shared_sync.py`). Run them from the repository root:

```bash
python3 -m unittest discover -s tests
python3 scripts/sync_shared.py --check
```

GitHub Actions (`.github/workflows/test.yml`) runs both commands on push and pull request to `main` across Python 3.7 and 3.x.

Run these checks by hand for the rest.

1. **Bad and good samples.** For each language you touched, write one bad paragraph (long sentence, banned phrases) and one good paragraph. The bad one must exit with `1`, the good one with `0`:

   ```bash
   python3 shared/scripts/check_style.py bad.md  --lang en --type api-design
   python3 shared/scripts/check_style.py good.md --lang en --type api-design
   ```

2. **Shipped samples.** Covered by `tests/test_examples_samples.py`. As a manual fallback, extract the last fenced block of each examples file and run the checker with the matching type (`tech-blog`, `essay`, `api-design`, `user-guide`, `common`). Expect no violations.
3. **Parallel folders.** Compare the file lists of `shared/languages/vi`, `shared/languages/en` and `shared/languages/ja`. They must match.
4. **Generated files.** Run `python3 scripts/sync_shared.py --check`. It exits `0` when every sub-skill matches `shared/`.
5. **Mirrors.** If you changed `profile.json`, check the "Units" table in `README.md`. If you changed `banned.txt`, check that `banned-guide.md` lists the same phrases.

If you add more automated tests, put them under `tests/` and update this section and `README.md` when the run command changes.

## Do not

- Do not edit a generated `SKILL.md` or a copied file in `skills/agent-plain-writing-<type>/`.
- Do not add a language, a document type or a core rule without updating `shared/`, the router, `README.md` and the files listed in the table above.
- Do not put secrets, personal data or real customer content in examples.
- Do not delete the "Your own samples" sections.
- Do not state that something was tested if you did not run it.
