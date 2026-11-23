# Evidence

Outputs and scores from eval runs of `agent-plain-writing`. The runs up to `20261122-201235` compare an AI with the skill against the same AI without it, on simulated cases. New runs use a real agent with the skills installed and have only `with_skill` outputs. Read each run's own `README.md`. Numbers from different runs are **not comparable** unless a run says so: the skill, the checker and the baseline prompt changed between runs.

## Folder layout

```
evidence/<run>/
├── README.md                          # summary of the run: table, what it shows, limits
├── <type>-<lang>.with_skill.md        # raw output with the skill
├── <type>-<lang>.without_skill.md     # raw output without the skill (old runs only)
├── results.json                       # mechanical scores from evals/score.py
└── run-meta.json                      # tool, model, commit, start time (not in the oldest runs)
```

In a new run, the agent writes the `with_skill` outputs and you save `results.json` with `evals/score.py` (see `evals/README.md`). Old runs also have `run-meta.json`, written by the deleted API runner. After a run, write its `README.md` from `results.json`: use only numbers from `results.json`, and state which rules of the checker and prompt applied.

## Runs

- [`20261122-201235/`](20261122-201235/README.md): 15 cases (`api-design`, `common`, `essay`, `guide`, `tech-blog`), model `gpt-6-luna`. With the skill, 12 of 15 outputs pass the checker; without it, 9 of 15.
- [`20261122-181452/`](20261122-181452/): 15 cases, model `gpt-6-luna`, commit `3246fef`. No summary yet; read `results.json`.
- [`20261122-154249/`](20261122-154249/README.md): 9 cases (`api-design`, `essay`, `tech-blog`). History.
- `20261121-235628/`: 9 cases, the earliest run. No `run-meta.json`, so the model is not recorded. With the skill, 7 of 9 outputs passed the checker, against 6 of 9 without it. History only; it used an older checker and an older baseline prompt.
