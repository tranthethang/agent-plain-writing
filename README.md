# agent-plain-writing

An agent skill that tells an AI to write **short, concrete text** in Vietnamese (`vi`), English (`en`) and Japanese (`ja`).

The Vietnamese README is at [docs/vi/README.md](docs/vi/README.md).

It gives the AI limits it can count (sentence length, paragraph length, banned phrases, jargon), bad → good examples per language and document type, and a script that checks a draft against those limits.

| | |
|---|---|
| Bad | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Good | The system saves results it has already computed. Next time, it answers faster. |

![agent-plain-writing banner](assets/screenshot.png)


## Status

- Five document types in two voice families: `plain` (`tech-blog`, `api-design`, `guide`, `common`) and `creative` (`essay`). `prose`, `poetry`, and `screen-design` are out of scope for now.
- **Breaking change:** `--type blog` is now `--type tech-blog`. The default `--type` is `common`.
- The checker is mechanical. It counts. It does not judge voice. Text length outside the range prints a warning and does not fail the check.
- The numeric limits are starting estimates, not verified standards.
- The evidence is small: one eval run per version, 9 simulated cases, mechanical scores only. See [Evidence](#evidence).
- Automated tests cover the `TBD-n` statistics and the short-brief length range in `evals/score.py`, the document-type set, the checker default type, the checker's table-cell, report-label and `--short-brief` checks, the Units tables, and the shipped samples in `examples/`. Run them with `python3 -m unittest discover -s tests`. `AGENTS.md` lists the manual checks for the rest.

## Quick start

1. Install (needs Node.js; manual install is in [docs](docs/en/01-install.en.md)):

```bash
npx skills add tranthethang/agent-plain-writing -g
```

2. Ask: `Use agent-plain-writing to write a user guide in Japanese from these notes: ...`
3. Check a draft (Python 3.7+, no packages):

```bash
python3 skills/agent-plain-writing/scripts/check_style.py draft.md --lang en --type tech-blog
```

Exit codes: `0` clean, `1` violations, `2` usage error.

## Units

Mirrors `sentence` / `paragraph` limits in `skills/agent-plain-writing/languages/<lang>/profile.json`:

| Language | Unit | `tech-blog` | `essay` | `api-design` | `guide` | `common` |
|---|---|---|---|---|---|---|
| `vi` | syllables (*tiếng*) | 28 / 3 | 40 / 6 | 25 / 3 | 16 / 3 | 28 / 3 |
| `en` | words | 20 / 3 | 30 / 6 | 18 / 3 | 12 / 3 | 20 / 3 |
| `ja` | characters (字) | 60 / 3 | 80 / 6 | 55 / 3 | 40 / 3 | 60 / 3 |

`tech-blog` text length (`length` / `length_short` for a short brief): `vi` 600–800 / 300–500 words, `en` 600–800 / 300–500 words, `ja` 1500–2000 / 750–1250 字. Other types have no length range.

## Evidence

The latest eval run (`evidence/20261122-154249/`, model `gpt-6-luna`) compared the same AI with and without the skill on 9 simulated cases (`api-design`, `essay`, and `tech-blog`, in `vi`, `en`, `ja`). Checker results only, no AI judge or human review:

- 6 of 9 outputs with the skill pass the checker, against 5 of 9 without it.
- The average sentence is shorter with the skill in 8 of 9 cases (`tech-blog en` ties: 12.3 against 12.2 words).
- For `api-design`, each skill output carries 8 `TBD-n` markers tied to questions and cuts jargon by 1 term. Two skill outputs fail (`en`: one long sentence; `ja`: a long paragraph and trailing spaces), so only `api-design vi` passes. The checker cannot say if the markers are better.
- For `essay`, all 6 outputs pass with 0 violations; the skill outputs are shorter overall.
- For `tech-blog`, the skill outputs have 2, 0 and 0 violations (`en`, `ja`, `vi`) against 5, 1 and 1 without. All 6 are shorter than the length target (printed as a warning).
- One invented number without the skill (`tech-blog en`), none with it.

The earlier run (`20261121-235628`) is not comparable: the checker and the baseline prompt changed since. This is a small sample, not proof. Details, table and limits: [evidence/README.md](evidence/README.md).

## Documentation

Each topic has one file per language, in `docs/<lang>/`.

| # | Topic | English | Tiếng Việt | 日本語 |
|---|---|---|---|---|
| 00 | Overview | [en](docs/en/00-overview.en.md) | [vi](docs/vi/00-overview.vi.md) | [ja](docs/ja/00-overview.ja.md) |
| 01 | Install | [en](docs/en/01-install.en.md) | [vi](docs/vi/01-install.vi.md) | [ja](docs/ja/01-install.ja.md) |
| 02 | Usage | [en](docs/en/02-usage.en.md) | [vi](docs/vi/02-usage.vi.md) | [ja](docs/ja/02-usage.ja.md) |
| 03 | Checker | [en](docs/en/03-checker.en.md) | [vi](docs/vi/03-checker.vi.md) | [ja](docs/ja/03-checker.ja.md) |
| 04 | Customize | [en](docs/en/04-customize.en.md) | [vi](docs/vi/04-customize.vi.md) | [ja](docs/ja/04-customize.ja.md) |
| 05 | Evals | [en](docs/en/05-evals.en.md) | [vi](docs/vi/05-evals.vi.md) | [ja](docs/ja/05-evals.ja.md) |
| 06 | Limitations | [en](docs/en/06-limitations.en.md) | [vi](docs/vi/06-limitations.vi.md) | [ja](docs/ja/06-limitations.ja.md) |

## Contributing

Read [AGENTS.md](AGENTS.md) before changing anything. It keeps the three language folders parallel.

## License

GNU GPL v3. See [LICENSE](LICENSE).
