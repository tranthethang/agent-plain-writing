# Evals

`evals/` tests the skills with a real agent. It is a small kit, not a benchmark.

| File | Role |
|---|---|
| `cases/` | 18 cases: `tech-blog`, `essay`, `api-design`, `user-guide`, and `common`, each in `vi`, `en`, `ja`, plus 3 extra `api-design-speed` cases. All data is simulated |
| `smoke-prompts.md` | The Smoke set: 5 prompts for a quick check after a change |
| `score.py` | Mechanical scorer. Counts numbers not found in the case, and for `api-design` also reports `tbd_ids`, `tbd_without_question`, `tbd_in_code`, `tbd_duplicate_questions`, and `tbd_without_inline` |
| `judge-prompt.md` | Prompt for an AI judge (clarity, coverage, and per-type semantic checks for `api-design`, `tech-blog`, `essay`, `user-guide`, and `common`) |

## Workflow

No script calls an API. A real agent writes each output.

1. Local gate: `python3 -m unittest discover -s tests` and `python3 scripts/sync_shared.py --check`.
2. Install all six skills: `npx skills add <repo>`.
3. Create `evidence/<run>/`.
4. Run the prompts in your agent. The Smoke set is `evals/smoke-prompts.md`. The Full set is every file in `evals/cases/`. Each prompt tells the agent to write its output to `evidence/<run>/<case>.with_skill.md`.
5. Score each output and save the results in `evidence/<run>/results.json`:

```bash
python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md
python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md --judge-prompt
```

`evals/README.md` has a short script that scores every output of a run into one `results.json`.

## Honest limits

- Run outputs are saved in `evidence/` and tracked by git. Each run has its own summary in [evidence/](../../evidence/README.md). The runs up to `20261122-201235` used an API runner that no longer exists. Each is a single run with mechanical scores only, so it does not prove that the skill improves writing.
- The cases in `evals/cases/` cover every document type. Which cases a run covered is in that run's `README.md`.
- The judge is an AI. Its scores are not verified against human readers.
- Cases use simulated data. To add a case from a real brief, see `evals/README.md`.

Next: [06-limitations](06-limitations.en.md).
