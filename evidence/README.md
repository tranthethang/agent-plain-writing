# Evidence

Outputs and scores from real-agent eval runs of the `agent-plain-writing` skills. Read each run's own `README.md`. Numbers from different runs are **not comparable** unless a run says so: the skills and the checker can change between runs.

## Folder layout

```
evidence/<run>/
├── README.md                          # summary of the run: table, what it shows, limits
├── <case>.with_skill.md               # raw output of the agent with the skills installed
└── results.json                       # mechanical scores from evals/score.py
```

The agent writes the `with_skill` outputs, and you save `results.json` with `evals/score.py` (see `evals/README.md`). After a run, write its `README.md` from `results.json`: use only numbers from `results.json`, and state which rules of the checker applied.

## Runs

No run of the six-skill layout yet.
