# agent-plain-writing

AI models often write padded, abstract prose by default. I built six skills so AI writes short, concrete text in Vietnamese (`vi`), English (`en`), and Japanese (`ja`).

For Vietnamese, see [docs/vi/README.md](docs/vi/README.md).

| | |
|---|---|
| Bad | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Good | The system saves results it has already computed. Next time, it answers faster. |

![agent-plain-writing banner](assets/screenshot.png)

## Quick start

One router skill picks the document type, and five sub-skills enforce countable limits per language and type. Each sub-skill ships bad-to-good examples and a Python script that checks your draft against those limits.

1. Install all six skills together (requires Node.js; manual steps are in [docs](docs/en/01-install.en.md)):

```bash
npx skills add tranthethang/agent-plain-writing -g
```

> **Antigravity IDE:** Run `npx skills add tranthethang/agent-plain-writing -a antigravity -g`. Confirm all six skills sit in `~/.gemini/config/skills/` (global) or `.agents/skills/` (project), then reload the IDE or open a new chat.

2. Prompt the router or call one sub-skill directly:
   - `Use agent-plain-writing to shorten this text: ...` (router picks the type)
   - `Use agent-plain-writing-user-guide to write a user guide in Japanese from these notes: ...`

3. Run the checker on your draft (Python 3.15+, standard library only):

```bash
python3 skills/agent-plain-writing-tech-blog/scripts/check_style.py draft.md --lang en --type tech-blog
python3 skills/agent-plain-writing-user-guide/scripts/check_style.py guide.md --lang vi --type user-guide
```

Exit codes: `0` clean, `1` violations, `2` usage error.

## Units

This table mirrors the `sentence` / `paragraph` limits in `shared/languages/<lang>/profile.json`:

| Language | Unit | `tech-blog` | `essay` | `api-design` | `user-guide` | `common` |
|---|---|---|---|---|---|---|
| `vi` | syllables (*tiếng*) | 28 / 3 | 40 / 6 | 25 / 3 | 16 / 3 | 28 / 3 |
| `en` | words | 20 / 3 | 30 / 6 | 18 / 3 | 12 / 3 | 20 / 3 |
| `ja` | characters (字) | 60 / 3 | 80 / 6 | 55 / 3 | 40 / 3 | 60 / 3 |

For `tech-blog`, the length ceiling (`length` / `length_short`) is 600–800 / 300–500 words for `vi` and `en`. For `ja`, it is 1500–2000 / 750–1250 字; other types have no length range.

## Status and evidence

The five types sit in two voice families: `plain` (`tech-blog`, `api-design`, `user-guide`, `common`) and `creative` (`essay`). `prose`, `poetry`, and `screen-design` are out of scope for now.

Two things to know before you rely on the numbers:

- **Breaking change:** `--type blog` is now `--type tech-blog`, and the default `--type` is `common`.
- **Mechanical checks only:** The script counts tokens and flags banned phrases, without judging voice. It warns only above the upper length limit, never asks for padding, and never fails a run on length alone.

Our numeric limits are starting estimates, not verified standards. Each folder in [evidence/](evidence/README.md) holds raw outputs, `results.json`, and a summary. Each run uses one real agent on simulated cases (see [evals/README.md](evals/README.md)).

Those runs use checker scores without an AI judge or human review. Treat them as small samples, not proof.

Automated tests check `evals/score.py` stats, document types, default type, `--short-brief`, table cells, and report labels. They also check time/date counts, `PLAIN-WRITING.md` lookup, length warnings, `doc-types/`, Units tables, `examples/`, and `shared/` parity.

GitHub Actions runs `python3 -m unittest discover -s tests` and `python3 scripts/sync_shared.py --check` on Python 3.15.2. See `AGENTS.md` for manual checks.

## Documentation

Each topic has one file per language under `docs/<lang>/`:

| # | Topic | English | Tiếng Việt | 日本語 |
|---|---|---|---|---|
| 00 | Overview | [en](docs/en/00-overview.en.md) | [vi](docs/vi/00-overview.vi.md) | [ja](docs/ja/00-overview.ja.md) |
| 01 | Install | [en](docs/en/01-install.en.md) | [vi](docs/vi/01-install.vi.md) | [ja](docs/ja/01-install.ja.md) |
| 02 | Usage | [en](docs/en/02-usage.en.md) | [vi](docs/vi/02-usage.vi.md) | [ja](docs/ja/02-usage.ja.md) |
| 03 | Checker | [en](docs/en/03-checker.en.md) | [vi](docs/vi/03-checker.vi.md) | [ja](docs/ja/03-checker.ja.md) |
| 04 | Customize | [en](docs/en/04-customize.en.md) | [vi](docs/vi/04-customize.vi.md) | [ja](docs/ja/04-customize.ja.md) |
| 05 | Evals | [en](docs/en/05-evals.en.md) | [vi](docs/vi/05-evals.vi.md) | [ja](docs/ja/05-evals.ja.md) |
| 06 | Limitations | [en](docs/en/06-limitations.en.md) | [vi](docs/vi/06-limitations.vi.md) | [ja](docs/ja/06-limitations.ja.md) |

## Contributing and license

Read [AGENTS.md](AGENTS.md) before you edit anything so the three language folders stay parallel. Enable the `pre-commit` hook once after cloning so commits cannot leave `skills/` out of sync with `shared/`:

```bash
git config core.hooksPath .githooks
```

Licensed under GNU GPL v3; see [LICENSE](LICENSE).
