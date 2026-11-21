# agent-plain-writing

An agent skill that tells an AI to write **short, concrete text** in Vietnamese (`vi`), English (`en`) and Japanese (`ja`).

It gives the AI limits it can count (sentence length, paragraph length, banned phrases, jargon), bad → good examples per language and document type, and a script that checks a draft against those limits.

| | |
|---|---|
| Bad | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Good | The system saves results it has already computed. Next time, it answers faster. |

## Status

- Four document types in two voice families: `plain` (`tech-blog`, `api-design`, `guide`) and `creative` (`essay`). `prose`, `poetry`, and `screen-design` are out of scope for now.
- **Breaking change:** `--type blog` is now `--type tech-blog` (also the new default).
- The checker is mechanical. It counts. It does not judge voice.
- The numeric limits are starting estimates, not verified standards.
- The Japanese content has no native review yet.
- The evidence is small: one eval run, 6 simulated cases, mechanical scores only. See [Evidence](#evidence).
- Automated tests cover the `TBD-n` statistics in `evals/score.py`, the document-type set, the checker default type and the Units table. Run them with `python3 -m unittest discover -s tests`. `AGENTS.md` lists the manual checks for the rest.

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

| Language | Unit | `tech-blog` | `essay` | `api-design` | `guide` |
|---|---|---|---|---|---|
| `vi` | syllables (*tiếng*) | 28 / 3 | 40 / 6 | 25 / 3 | 16 / 3 |
| `en` | words | 20 / 3 | 30 / 6 | 18 / 3 | 12 / 3 |
| `ja` | characters (字) | 60 / 3 | 80 / 6 | 55 / 3 | 40 / 3 |

## Evidence

One eval run (`evidence/20261121-171734/`) compared the same AI with and without the skill on 6 simulated cases (`blog` and `api-design`, in `vi`, `en`, `ja`). Checker results only, no AI judge or human review:

- 3 of 6 outputs with the skill pass the checker, against 2 of 6 without it.
- The average sentence is shorter with the skill in all 6 cases (by 0.1 only for `blog-ja`).
- For `api-design`, the skill outputs are longer and carry 10 to 11 `TBD-n` markers. The checker cannot say if that is better.
- For `blog`, all three skill outputs still fail the checker. For `vi` and `ja` the only failure is length (before length became a warning). `blog-en` has more violations (7) than without the skill (3).
- No invented numbers in any output.

This is a small sample, not proof. Details, table and limits: [evidence/README.md](evidence/README.md).

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
