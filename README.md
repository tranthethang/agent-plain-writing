# agent-plain-writing

An agent skill that makes AI write **short, concrete, plain text** in Vietnamese, English and Japanese.

It sets limits you can count (sentence length, paragraph length, banned phrases, jargon), gives the AI many bad → good examples for each language and document type, and includes a script that checks a draft against those limits.

## Why

AI drafts tend to have the same faults:

- Wordy and hard to follow.
- Heavy with technical terms.
- When asked to write for non-technical readers, the AI "translates" every technical detail instead of choosing what the reader needs. The result is longer, not clearer.

Adjectives such as "clear" or "friendly" in a prompt do not fix this. Limits that can be counted, examples that can be copied, and a separate edit pass do.

## What it does

- **One owner per rule:** `SKILL.md` owns the workflow and core rules. `doc-types/<type>.md` owns voice, structure, length policy and rhythm. `languages/<lang>/` owns the unit, numeric limits, banned phrases, grammar and examples. On limits and structure, `doc-types` wins over `SKILL.md`. On words and grammar, `languages` wins over `doc-types`.

- **One skill, three languages:** Vietnamese (`vi`), English (`en`), Japanese (`ja`). The language of the output text selects the language folder.
- **Five document types:** blog post, prose, poetry, detail design (API specs), user guide.
- **Measurable rules:** sentence length, paragraph length, banned phrases, jargon count, text length. Limits are set per language and per document type.
- **Few-shot examples:** bad → good pairs and one complete sample for each language and type.
- **A two-pass workflow:** draft first, then edit against a checklist and the checker script.
- **A checker script:** Python 3, standard library only.

### Example

| | |
|---|---|
| Bad | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Good | The system saves results it has already computed. Next time, it answers faster. |

## Repository layout

```
.
├── README.md
├── AGENTS.md                         # instructions for AI agents that edit this repo
├── evals/
│   ├── README.md                     # eval structure and cost warning
│   ├── cases/                        # 6 simulated cases (blog and design x vi, en, ja)
│   ├── judge-prompt.md               # AI judge prompt (clarity and coverage)
│   ├── score.py                      # mechanical scorer and judge-prompt builder
│   └── run_eval.py                   # user-confirmed runner (antigravity or claude)
└── skills/
    └── agent-plain-writing/          # the skill (copy this folder into your agent)
        ├── SKILL.md                  # workflow, 12 core rules, language and type routing
        ├── doc-types/                # type rules: voice, structure, length policy, rhythm (language-neutral)
        │   ├── blog.md
        │   ├── prose.md
        │   ├── poetry.md
        │   ├── detail-design.md
        │   └── user-guide.md
        ├── languages/
        │   ├── vi/  en/  ja/         # the same file set in each language folder:
        │   │   ├── profile.json      #   unit and numeric limits per document type
        │   │   ├── profile.md        #   unit, register, grammar traps, pronoun and level words
        │   │   ├── banned.txt        #   the actual banned phrases (machine-readable)
        │   │   ├── banned-guide.md   #   the same phrases with replacements
        │   │   ├── terms.txt         #   jargon list for the jargon count
        │   │   └── examples/         #   common, blog, prose, poetry, detail-design, user-guide
        ├── templates/
        │   └── PLAIN-WRITING.example.md
        └── scripts/
            └── check_style.py
```

## Install

Copy `skills/agent-plain-writing/` into the skills folder of your agent. Keep the folder name equal to the `name` in `SKILL.md`.

- **Claude Code:** project skills go in `.claude/skills/`, personal skills in `~/.claude/skills/`.
- **Other tools that read `SKILL.md`:** check the tool's documentation for the skills location.
- **Claude apps:** if your plan supports custom skills, zip the `agent-plain-writing/` folder and upload it in the skills settings.

The exact steps differ between tools and versions. Check your tool's current documentation.

## Use

Ask for the task in plain words and give the AI a good brief. Examples:

```
Use agent-plain-writing to write a user guide in Japanese from these notes: ...
Rewrite this API detail design in English. Fill the template only. Mark missing facts as TBD.
Shorten this blog post. My own paragraph is attached as the model for rhythm.
```

Each file in `doc-types/` lists the **brief** the AI needs for that document type (summary, main points, reader, a sample of your own writing, words to use or avoid). The more of it you provide, the less the AI has to guess.

### The workflow the skill follows

1. Pick the output language (`vi`, `en`, `ja`).
2. Pick the document type. Read only that type's structure file and that language's examples.
3. Identify the reader. Ask one question if it is unclear.
4. Outline (for longer texts).
5. Draft.
6. Edit in a separate pass: cut, check the checklist, run the script.
7. Report the result and what had to be guessed.

## Check a draft

```bash
python3 skills/agent-plain-writing/scripts/check_style.py draft.md --lang en --type blog
python3 skills/agent-plain-writing/scripts/check_style.py spec.md  --lang ja --type design
python3 skills/agent-plain-writing/scripts/check_style.py guide.md --lang vi --type guide
python3 skills/agent-plain-writing/scripts/check_style.py post.md  --lang en --type blog --non-tech
```

| Option | Values |
|---|---|
| `--lang` | `vi`, `en`, `ja` (optional if `default_lang` is in `PLAIN-WRITING.md`) |
| `--type` | `blog`, `prose`, `poetry`, `design`, `guide` (`detail-design` and `user-guide` also work) |
| `--non-tech` | Limit jargon to 3 terms (for readers outside the field). The `guide` type always applies this limit. |
| `--config` | Path to a `PLAIN-WRITING.md` file (default: `./PLAIN-WRITING.md` if present). |

Exit codes: `0` clean, `1` violations found, `2` usage error.

The script checks sentence length, paragraph length, banned phrases, jargon count and text length. It skips code blocks, tables and headings. Requires Python 3.7 or later. No packages to install.

### Units

| Language | Unit counted | Sentence limit for `blog` (starting value) |
|---|---|---|
| `vi` | syllables (*tiếng*) | 28 (about 20 words) |
| `en` | words | 20 |
| `ja` | characters (字), punctuation and spaces excluded | 60 |

The numbers for every type are only in each language's `profile.json`. `profile.md` and `doc-types/` point to them and do not repeat them.

## Customize

- **Add a project config.** Copy `skills/agent-plain-writing/templates/PLAIN-WRITING.example.md` to `PLAIN-WRITING.md` in your project root to set `default_lang`, `default_type`, project voice, extra terms, extra banned phrases and numeric limits.
- **Add your own samples.** Each `examples/*.md` file ends with a "Your own samples" section. Paste sentences the AI wrote badly together with your rewrite. Samples written by you matter more than samples written by AI.
- **Add banned phrases.** Add the phrase to `banned.txt` and to `banned-guide.md` in the same language folder.
- **Tune the limits.** Edit `profile.json`. Update the "Units" table above if the `blog` sentence limit changes.
- **Add a language.** Create `languages/<code>/` with `profile.json`, `profile.md`, `banned.txt`, `banned-guide.md`, `terms.txt` and `examples/`. The script supports three units: `syllable`, `word`, `char`. No code change is needed.

## Limitations

- **The script is mechanical.** It does not judge voice, and it does not check rhyme or meter. For haiku and other fixed forms, count by hand.
- **The numeric limits are starting estimates.** Run the script on real texts from your team and adjust them.
- **The Japanese content was improved by an AI and has no native review yet.** Register conventions (です・ます調 or である調 by document type), requirement words and the example pairs should be reviewed before real use.
- **Stories and numbers in the examples are illustrations.** In real work, use the author's own facts, or write `TBD`.
- **There is no automated test suite yet.** See `AGENTS.md` for the manual checks.

## Contributing

Read `AGENTS.md` before changing anything. It lists the rules that keep the three language folders consistent.

## License

GNU GPL v3, see `LICENSE`.
