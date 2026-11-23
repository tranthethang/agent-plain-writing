# Overview

`agent-plain-writing` is a set of six agent skills: a router and five sub-skills, one for each document type. They tell an AI to write short, concrete text in Vietnamese (`vi`), English (`en`) or Japanese (`ja`).

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

- **A router skill,** `agent-plain-writing`. It picks the document type and the language, then hands off. It holds no writing rules.
- **Five sub-skills,** `agent-plain-writing-<type>`. Each has the core rules and workflow (6 shared rules plus rules per voice family, draft then edit) and the voice, structure and length of its type.
- **Five document types in two voice families:** `plain` (`tech-blog`, `api-design`, `user-guide`, `common`) and `creative` (`essay`). Each type has a file in `shared/doc-types/`.
- **Three language folders** with the unit, numeric limits, banned phrases, jargon list and examples.
- **A checker script**, `check_style.py` (Python 3.15+, standard library only). Each sub-skill holds its own copy.
- **An eval kit** in `evals/` (see [05-evals](05-evals.en.md)).

`prose`, `poetry`, and `screen-design` are out of scope for now.

## Who owns which rule

Each fact has one owner file in `shared/`. Other files point to it. The `SKILL.md` of each sub-skill is generated from `shared/` and is never edited.

| Fact | Owner |
|---|---|
| Workflow and core rules | `shared/skill-core.md` |
| Voice family | `shared/families/<family>.md` |
| Voice, structure, length policy, rhythm | `shared/doc-types/<type>.md` |
| Unit and numeric limits | `shared/languages/<lang>/profile.json` |
| Banned phrases | `shared/languages/<lang>/banned.txt` (checker list), `banned-guide.md` (what the agent reads) |
| Grammar traps, pronoun and level words | `shared/languages/<lang>/profile.md` |
| Jargon list | `shared/languages/<lang>/terms.txt` |
| Routing between sub-skills | `skills/agent-plain-writing/SKILL.md` |

On limits and structure, `doc-types` wins over `skill-core.md`. On words and grammar, `languages` wins over `doc-types`. On how much a text may add beyond the source, the voice family and `doc-types` win over the core rules; the facts in core rule 5 never change. The full table is in `AGENTS.md`.

## Repository layout

```
.
├── README.md
├── AGENTS.md                 # rules for editing this repo
├── docs/{en,vi,ja}/          # this documentation
├── evals/                    # cases, smoke prompts, scorer, judge prompt
├── scripts/sync_shared.py    # builds skills/ from shared/
├── shared/                   # the only place to edit skill content
│   ├── skill-core.md
│   ├── families/             # plain.md, creative.md
│   ├── doc-types/            # tech-blog, essay, api-design, user-guide, common
│   ├── languages/{vi,en,ja}/ # profile.json, profile.md, banned.txt, banned-guide.md,
│   │                         # terms.txt, examples/
│   ├── templates/PLAIN-WRITING.example.md
│   └── scripts/check_style.py
└── skills/                   # generated, except the router
    ├── agent-plain-writing/              # router: SKILL.md only
    └── agent-plain-writing-<type>/       # SKILL.md, languages/, scripts/, templates/
```

Next: [01-install](01-install.en.md).
