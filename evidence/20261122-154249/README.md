# Run 20261122-154249

History note: this run used an older skill, checker and prompt. Its numbers are not comparable with later runs. Copied from `evals/runs/20261122-154249/` (that folder is ignored by git). Files:

- `<type>-<lang>.with_skill.md` and `<type>-<lang>.without_skill.md`: the 18 raw outputs.
- `results.json`: mechanical scores from `evals/score.py`. Absolute paths were made relative. Nothing else was changed.
- `run-meta.json`: tool `openai`, model `gpt-6-luna`, commit `29259c5`, start time.

Run it again with `python3 evals/run_eval.py` (see `docs/en/05-evals.en.md`).

## Results

Mechanical checker only. `viol` is the number of violations reported by `check_style.py` (warnings are separate; length outside the target range is a warning). Fewer is better. Scoring covers the document only: `score.py` drops any report after the last horizontal rule.

| Case | Mode | Length | Avg sentence | viol | Warn | Jargon | TBD-n | Invented numbers |
|---|---|---|---|---|---|---|---|---|
| api-design en | with skill | 300 words | 3.6 | 1 | 0 | 1 | 8 | 0 |
| api-design en | without | 221 words | 4.3 | 0 | 0 | 2 | 0 | 0 |
| api-design ja | with skill | 638 字 | 7.8 | 2 | 0 | 1 | 8 | 0 |
| api-design ja | without | 660 字 | 11.0 | 1 | 0 | 2 | 0 | 0 |
| api-design vi | with skill | 358 tiếng | 4.4 | 0 | 0 | 2 | 8 | 0 |
| api-design vi | without | 443 tiếng | 4.8 | 0 | 0 | 3 | 0 | 0 |
| essay en | with skill | 107 words | 9.7 | 0 | 0 | 0 | 0 | 0 |
| essay en | without | 154 words | 10.3 | 0 | 0 | 0 | 0 | 0 |
| essay ja | with skill | 228 字 | 20.7 | 0 | 0 | 0 | 0 | 0 |
| essay ja | without | 297 字 | 27.0 | 0 | 0 | 0 | 0 | 0 |
| essay vi | with skill | 99 tiếng | 11.0 | 0 | 0 | 0 | 0 | 0 |
| essay vi | without | 174 tiếng | 11.6 | 0 | 0 | 0 | 0 | 0 |
| tech-blog en | with skill | 233 words | 12.3 | 2 | 1 | 0 | 0 | 0 |
| tech-blog en | without | 304 words | 12.2 | 5 | 1 | 1 | 0 | 1 |
| tech-blog ja | with skill | 475 字 | 29.7 | 0 | 1 | 3 | 0 | 0 |
| tech-blog ja | without | 699 字 | 31.8 | 1 | 1 | 3 | 0 | 0 |
| tech-blog vi | with skill | 283 tiếng | 14.2 | 0 | 1 | 3 | 0 | 0 |
| tech-blog vi | without | 406 tiếng | 15.0 | 1 | 2 | 3 | 0 | 0 |

Units: `en` words, `ja` characters, `vi` syllables (*tiếng*). The `api-design` averages are small because the checker now counts table cells as sentences.

## What the numbers show

- **Clean runs:** with the skill, 6 of 9 outputs pass the checker (`api-design vi`, all 3 `essay`, `tech-blog ja`, `tech-blog vi`). Without it, 5 of 9 pass (`api-design en`, `api-design vi`, all 3 `essay`). A warning does not fail an output.
- **Sentence length:** with the skill, the average sentence is shorter in 8 of 9 cases. The exception is `tech-blog en` (12.3 words against 12.2, a tie in practice).
- **`api-design`:** each skill output carries 8 `TBD-n` markers, each tied to an `Open items` question (no missing, duplicate, or code-fenced `TBD-n`). The outputs without the skill have none. Jargon drops by 1 term in each language. The skill outputs have 3 violations in total: `api-design en` has one 20-word sentence (max 18), and `api-design ja` has a 4-sentence paragraph and trailing-space line breaks. Without the skill, `api-design ja` has one 58-character sentence (max 55). The checker does not say whether each `TBD-n` marks a real gap; a reader must judge.
- **`essay`:** all 6 outputs pass with 0 violations and 0 warnings. With the skill, all 3 essays are shorter overall and have shorter average sentences.
- **`tech-blog`:** with the skill, `tech-blog vi` and `tech-blog ja` have 0 violations and `tech-blog en` has 2 (one 25-word sentence and one 4-sentence paragraph). Without the skill, they have 1, 1 and 5. All 6 outputs are shorter than the target length (`600–800` words / `1500–2000` 字), which prints a warning. The skill outputs are shorter than the baseline in all 3 languages, so the skill does not pad to reach the ceiling.
- **Invented numbers:** none with the skill. One without it (`tech-blog en`, the number `16`).

## Limits of this evidence

- **One run, 9 cases.** `api-design`, `essay`, and `tech-blog` are covered; `guide` and `common` have no eval case. Run-to-run variance is unknown, and a difference of one violation is within noise.
- **Mechanical scores only.** This run has no AI-judge scores and no human review. The results do not measure clarity, voice, or coverage.
- **Simulated data.** All cases use made-up briefs.
- **Short outputs.** All `tech-blog` outputs are far below the length target, with or without the skill. The cases do not set `short_brief`, so the length warning is expected.
- **`ja` content:** Japanese outputs were scored mechanically; no native review of them was done.
