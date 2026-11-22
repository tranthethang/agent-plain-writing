# Overview

`agent-plain-writing` is one agent skill. It tells an AI to write short, concrete text in Vietnamese (`vi`), English (`en`) or Japanese (`ja`).

## The problem

AI drafts often share the same faults:

- Long sentences that are hard to follow.
- Technical terms the reader does not know.
- For a non-technical reader, the AI explains every technical detail. The text gets longer, not clearer.

Words such as "clear" or "friendly" in a prompt do not fix this. The skill uses limits that can be counted, examples that can be copied, and a separate edit pass.

| | |
|---|---|
| Bad | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Good | The system saves results it has already computed. Next time, it answers faster. |

## What is in it

- **Core rules and workflow** in `SKILL.md` (6 shared rules plus rules per voice family, draft then edit).
- **Five document types in two voice families:** `plain` (`tech-blog`, `api-design`, `guide`, `common`) and `creative` (`essay`). Each has a file in `doc-types/` for voice, structure and length, except `common`, which has no file there.
- **Three language folders** with the unit, numeric limits, banned phrases, jargon list and examples.
- **A checker script**, `check_style.py` (Python 3.7+, standard library only).
- **An eval kit** in `evals/` (see [05-evals](05-evals.en.md)).

`prose`, `poetry`, and `screen-design` are out of scope for now.

## Who owns which rule

Each fact has one owner file. Other files point to it.

| Fact | Owner |
|---|---|
| Workflow and core rules | `SKILL.md` |
| Voice, structure, length policy, rhythm | `doc-types/<type>.md` |
| Unit and numeric limits | `languages/<lang>/profile.json` |
| Banned phrases | `languages/<lang>/banned.txt` |
| Grammar traps, pronoun and level words | `languages/<lang>/profile.md` |
| Jargon list | `languages/<lang>/terms.txt` |

On limits and structure, `doc-types` wins over `SKILL.md`. On words and grammar, `languages` wins over `doc-types`. On how much a text may add beyond the source, the voice family and `doc-types` win over the core rules; the facts in core rule 5 never change. The full table is in `AGENTS.md`.

## Repository layout

```
.
├── README.md
├── AGENTS.md                 # rules for editing this repo
├── docs/{en,vi,ja}/          # this documentation
├── evals/                    # cases, scorer, judge prompt, runner
└── skills/agent-plain-writing/
    ├── SKILL.md
    ├── doc-types/            # tech-blog, essay, api-design, user-guide
    ├── languages/{vi,en,ja}/ # profile.json, profile.md, banned.txt, banned-guide.md,
    │                         # terms.txt, examples/
    ├── templates/PLAIN-WRITING.example.md
    └── scripts/check_style.py
```

Next: [01-install](01-install.en.md).
