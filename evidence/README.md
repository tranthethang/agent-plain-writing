# Evidence

Outputs and scores from one eval run of `agent-plain-writing`. The run compares an AI with the skill against the same AI without it, on 6 simulated cases.

## Run 20261121-171734

Copied from `evals/runs/20261121-171734/` (that folder is ignored by git). Files:

- `<type>-<lang>.with_skill.md` and `<type>-<lang>.without_skill.md`: the 12 raw outputs.
- `results.json`: mechanical scores from `evals/score.py`. Absolute paths were made relative. Nothing else was changed.

Run it again with `python3 evals/run_eval.py` (see `docs/en/05-evals.en.md`).

### Results

Mechanical checker only. `viol` is the number of violations reported by `check_style.py`. Fewer is better.

| Case | Mode | Length | Avg sentence | viol | Jargon | TBD-n | Invented numbers |
|---|---|---|---|---|---|---|---|
| api-design en | with skill | 265 words | 8.3 | 0 | 2 | 11 | 0 |
| api-design en | without | 193 words | 10.7 | 0 | 3 | 0 | 0 |
| api-design ja | with skill | 572 字 | 16.8 | 0 | 1 | 10 | 0 |
| api-design ja | without | 200 字 | 28.6 | 1 | 2 | 0 | 0 |
| api-design vi | with skill | 286 tiếng | 8.9 | 0 | 2 | 10 | 0 |
| api-design vi | without | 185 tiếng | 10.3 | 0 | 2 | 0 | 0 |
| blog en | with skill | 344 words | 15.6 | 7 | 1 | 0 | 0 |
| blog en | without | 175 words | 15.9 | 3 | 0 | 0 | 0 |
| blog ja | with skill | 592 字 | 31.2 | 1 | 1 | 0 | 0 |
| blog ja | without | 376 字 | 31.3 | 1 | 1 | 0 | 0 |
| blog vi | with skill | 256 tiếng | 15.1 | 1 | 2 | 0 | 0 |
| blog vi | without | 330 tiếng | 16.5 | 1 | 2 | 0 | 0 |

Units: `en` words, `ja` characters, `vi` syllables (*tiếng*).

### What the numbers show

- **Clean runs:** with the skill, 3 of 6 outputs pass the checker (all `api-design`). Without it, 2 of 6 pass.
- **Sentence length:** with the skill, the average sentence is shorter in all 6 cases. For `blog-ja` the gap is 0.1 (31.2 against 31.3). For `api-design` the skill outputs are split into more, shorter sentences.
- **`api-design`:** the skill outputs are longer and carry 10 to 11 `TBD-n` markers, each tied to a question. The outputs without the skill have none and use no numbered markers. The checker does not say which is better. A reader must judge whether each `TBD-n` marks a real gap.
- **`blog`:** the skill did not make the checker pass. All three blog outputs with the skill still fail, and the `en` one has more violations (7) than without the skill (3). For `vi` and `ja` the only violation is length (the target is 600 to 800 words, or 1,500 to 2,000 字, and the outputs are shorter). The `en` output has 6 sentence or paragraph violations on top of length, so it is the one real failure of the rules.
- **Invented numbers:** none in any output, with or without the skill.

### Limits of this evidence

- **One run, 6 cases.** Only `blog` and `api-design` are covered. Run-to-run variance is unknown.
- **Mechanical scores only.** This run has no AI-judge scores and no human review. The results do not measure clarity or coverage.
- **The model is not recorded** in `results.json`.
- **Simulated data.** All cases use made-up briefs.
- **Blog outputs are short** compared with the length target, with or without the skill.
