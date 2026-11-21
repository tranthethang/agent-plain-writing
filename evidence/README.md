# Evidence

Outputs and scores from one eval run of `agent-plain-writing`. The run compares an AI with the skill against the same AI without it, on 9 simulated cases.

## Run 20261121-235628

Copied from `evals/runs/20261121-235628/` (that folder is ignored by git). Files:

- `<type>-<lang>.with_skill.md` and `<type>-<lang>.without_skill.md`: the 18 raw outputs.
- `results.json`: mechanical scores from `evals/score.py`. Absolute paths were made relative. Nothing else was changed.

Run it again with `python3 evals/run_eval.py` (see `docs/en/05-evals.en.md`).

### Results

Mechanical checker only. `viol` is the number of violations reported by `check_style.py` (warnings are separate; length outside the target range is a warning). Fewer is better.

| Case | Mode | Length | Avg sentence | viol | Warn | Jargon | TBD-n | Invented numbers |
|---|---|---|---|---|---|---|---|---|
| api-design en | with skill | 178 words | 8.5 | 0 | 0 | 1 | 8 | 0 |
| api-design en | without | 168 words | 9.9 | 0 | 0 | 2 | 0 | 0 |
| api-design ja | with skill | 379 字 | 15.8 | 0 | 0 | 1 | 9 | 0 |
| api-design ja | without | 264 字 | 26.4 | 0 | 0 | 2 | 0 | 0 |
| api-design vi | with skill | 184 tiếng | 8.8 | 0 | 0 | 1 | 8 | 0 |
| api-design vi | without | 322 tiếng | 12.4 | 2 | 0 | 2 | 0 | 0 |
| essay en | with skill | 124 words | 10.3 | 0 | 0 | 0 | 0 | 0 |
| essay en | without | 144 words | 11.1 | 0 | 0 | 0 | 0 | 0 |
| essay ja | with skill | 227 字 | 20.6 | 0 | 0 | 0 | 0 | 0 |
| essay ja | without | 272 字 | 22.7 | 0 | 0 | 0 | 0 | 0 |
| essay vi | with skill | 87 tiếng | 10.9 | 0 | 0 | 0 | 0 | 0 |
| essay vi | without | 157 tiếng | 11.2 | 0 | 0 | 0 | 0 | 0 |
| tech-blog en | with skill | 456 words | 14.7 | 7 | 1 | 0 | 0 | 0 |
| tech-blog en | without | 286 words | 12.4 | 3 | 1 | 1 | 0 | 0 |
| tech-blog ja | with skill | 753 字 | 29.0 | 2 | 1 | 4 | 0 | 0 |
| tech-blog ja | without | 648 字 | 30.9 | 2 | 1 | 3 | 0 | 0 |
| tech-blog vi | with skill | 612 tiếng | 15.3 | 0 | 1 | 3 | 0 | 0 |
| tech-blog vi | without | 414 tiếng | 15.9 | 0 | 2 | 3 | 0 | 0 |

Units: `en` words, `ja` characters, `vi` syllables (*tiếng*).

### What the numbers show

- **Clean runs:** with the skill, 7 of 9 outputs pass the checker (all 3 `api-design`, all 3 `essay`, and `tech-blog vi`). Without it, 6 of 9 pass (`api-design vi`, `tech-blog en`, and `tech-blog ja` fail).
- **Sentence length:** with the skill, the average sentence is shorter in 8 of 9 cases. The exception is `tech-blog en` (14.7 words with the skill against 12.4 without).
- **`api-design`:** all 3 skill outputs pass with 0 violations, cut jargon from 2 terms to 1, and carry 8 to 9 `TBD-n` markers, each tied to an `Open items` question (no missing, duplicate, or code-fenced `TBD-n`). The outputs without the skill have none, and `api-design vi` fails with 2 violations (one 33-syllable sentence and 2 instances of the banned phrase `"trong brief"`). The checker does not say whether each `TBD-n` marks a real gap; a reader must judge.
- **`essay`:** all 6 outputs pass with 0 violations and 0 warnings. With the skill, all 3 essays are shorter overall and have shorter average sentences.
- **`tech-blog`:** `tech-blog vi` passes with 0 violations in both modes (without the skill it also triggers an ambiguous-phrase warning for `"không chỉ"`). `tech-blog en` has more violations with the skill (7: 5 long sentences and 2 long paragraphs) than without (3). `tech-blog ja` has 2 paragraph-length violations in both modes. All 6 `tech-blog` outputs are shorter than the target length range (`600–800` words / `1500–2000` 字), which prints a warning.
- **Invented numbers:** none in any output, with or without the skill.

### Limits of this evidence

- **One run, 9 cases.** `api-design`, `essay`, and `tech-blog` are covered; `guide` has no eval case. Run-to-run variance is unknown.
- **Mechanical scores only.** This run has no AI-judge scores and no human review. The results do not measure clarity, voice, or coverage.
- **The model is not recorded** in `results.json`.
- **Simulated data.** All cases use made-up briefs.
- **`tech-blog` outputs are short** compared with the length target, with or without the skill.
