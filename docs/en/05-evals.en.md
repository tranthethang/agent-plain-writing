# Evals

`evals/` compares AI output with and without the skill. It is a small kit, not a benchmark.

| File | Role |
|---|---|
| `cases/` | 9 cases: `tech-blog`, `essay` and `api-design`, each in `vi`, `en`, `ja`. All data is simulated |
| `score.py` | Mechanical scorer. Counts numbers not found in the case, and for `api-design` also reports `tbd_ids`, `tbd_without_question`, `tbd_in_code`, `tbd_duplicate_questions`, and `tbd_without_inline` |
| `judge-prompt.md` | Prompt for an AI judge (clarity, coverage, and per-type semantic checks for `api-design`, `tech-blog`, and `essay`) |
| `run_eval.py` | Runs each case twice (with and without the skill) |

## Cost

`run_eval.py` makes 2 AI calls per case. All 9 cases mean 18 calls and use quota or credits. Always preview first:

```bash
python3 evals/run_eval.py --dry-run
python3 evals/run_eval.py --type tech-blog --lang vi --dry-run
```

Then run it. The script asks you to type `yes`.

```bash
python3 evals/run_eval.py --tool openai   # default; reads OPENAI_API_URL, OPENAI_API_KEY, OPENAI_API_MODEL
python3 evals/run_eval.py --tool claude   # local `claude` CLI
python3 evals/run_eval.py --tool antigravity
```

Put API settings in `evals/.env` or the repo root `.env`. Both are ignored by git. Outputs go to `evals/runs/<timestamp>/`, also ignored by git.

Score one output:

```bash
python3 evals/score.py evals/cases/tech-blog-en.md output.md
python3 evals/score.py evals/cases/tech-blog-en.md output.md --judge-prompt
```

## Honest limits

- Run outputs are ignored by git. One run is kept as evidence in [evidence/](../../evidence/README.md). It is a single run with mechanical scores only, so it does not prove that the skill improves writing.
- Nine cases cover three types, and none of them ran in the kept evidence run. `guide` has no case.
- The judge is an AI. Its scores are not verified against human readers.
- Cases use simulated data. To add a case from a real brief, see `evals/README.md`.

Next: [06-limitations](06-limitations.en.md).
