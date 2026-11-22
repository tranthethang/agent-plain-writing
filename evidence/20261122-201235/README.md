# Run 20261122-201235

Eval run of `agent-plain-writing` on 15 simulated cases (`api-design`, `common`, `essay`, `guide`, `tech-blog`, each in `en`, `ja`, `vi`). Each case has a with-skill output and a without-skill output: 30 rows.

From `run-meta.json`: tool `openai`, model `gpt-6-luna`, commit `2d8c9ab946aeabce951ff98dedc754cf57b46551`, started `2026-11-22T20:12:35`.

Files:

- `<type>-<lang>.with_skill.md` and `<type>-<lang>.without_skill.md`: the 30 raw outputs.
- `results.json`: mechanical scores from `evals/score.py`.
- `run-meta.json`: tool, model, commit, start time.

## Results

Mechanical checker only. `viol` is the number of violations from `check_style.py`. A warning is separate and does not fail an output. Fewer violations is better.

| Case | Mode | Length | Avg sentence | viol | Warn | Jargon | TBD-n | Invented numbers |
|---|---|---|---|---|---|---|---|---|
| api-design en | without | 275 words | 4.2 | 0 | 0 | 3 | 0 | 0 |
| api-design en | with skill | 311 words | 3.7 | 0 | 0 | 1 | 8 | 0 |
| api-design ja | without | 674 字 | 10.1 | 0 | 0 | 2 | 0 | 0 |
| api-design ja | with skill | 600 字 | 7.1 | 0 | 0 | 1 | 9 | 0 |
| api-design vi | without | 319 tiếng | 4.8 | 0 | 0 | 2 | 0 | 0 |
| api-design vi | with skill | 336 tiếng | 4.0 | 0 | 0 | 2 | 8 | 0 |
| common en | without | 46 words | 11.5 | 0 | 0 | 0 | 0 | 0 |
| common en | with skill | 49 words | 9.8 | 1 | 0 | 0 | 0 | 0 |
| common ja | without | 120 字 | 20.0 | 0 | 0 | 1 | 0 | 1 |
| common ja | with skill | 107 字 | 21.4 | 0 | 0 | 1 | 0 | 0 |
| common vi | without | 69 tiếng | 11.5 | 0 | 0 | 0 | 0 | 0 |
| common vi | with skill | 60 tiếng | 12.0 | 0 | 0 | 0 | 0 | 0 |
| essay en | without | 136 words | 9.7 | 0 | 0 | 0 | 0 | 0 |
| essay en | with skill | 90 words | 9.0 | 0 | 0 | 0 | 0 | 0 |
| essay ja | without | 254 字 | 25.4 | 0 | 0 | 0 | 0 | 0 |
| essay ja | with skill | 209 字 | 20.9 | 0 | 0 | 0 | 0 | 0 |
| essay vi | without | 117 tiếng | 10.6 | 0 | 0 | 0 | 0 | 0 |
| essay vi | with skill | 100 tiếng | 11.1 | 0 | 0 | 0 | 0 | 0 |
| guide en | without | 127 words | 11.5 | 4 | 0 | 0 | 0 | 0 |
| guide en | with skill | 74 words | 7.4 | 1 | 0 | 0 | 0 | 0 |
| guide ja | without | 314 字 | 20.9 | 2 | 0 | 0 | 0 | 0 |
| guide ja | with skill | 183 字 | 20.3 | 0 | 0 | 0 | 0 | 0 |
| guide vi | without | 115 tiếng | 11.5 | 2 | 0 | 0 | 0 | 0 |
| guide vi | with skill | 71 tiếng | 7.1 | 0 | 0 | 0 | 0 | 0 |
| tech-blog en | without | 289 words | 13.1 | 3 | 1 | 0 | 0 | 0 |
| tech-blog en | with skill | 235 words | 11.8 | 0 | 1 | 0 | 0 | 0 |
| tech-blog ja | without | 915 字 | 28.6 | 2 | 1 | 3 | 0 | 0 |
| tech-blog ja | with skill | 470 字 | 29.4 | 2 | 1 | 3 | 0 | 0 |
| tech-blog vi | without | 466 tiếng | 15.5 | 1 | 1 | 3 | 0 | 0 |
| tech-blog vi | with skill | 333 tiếng | 13.9 | 0 | 1 | 3 | 0 | 0 |

Units: `en` words, `ja` characters (字), `vi` syllables (*tiếng*).

## What the numbers show

- **Clean outputs:** with the skill, 12 of 15 pass the checker with 0 violations. Without it, 9 of 15 pass.
- **With the skill, the 3 outputs that fail:** `common en` (1 violation), `guide en` (1) and `tech-blog ja` (2).
- **Without the skill, the 6 outputs that fail:** `guide en` (4 violations), `guide ja` (2), `guide vi` (2), `tech-blog en` (3), `tech-blog ja` (2) and `tech-blog vi` (1). All 3 `guide` and all 3 `tech-blog` outputs fail.
- **`guide`:** with the skill, `guide ja` and `guide vi` pass and `guide en` has one 17-word sentence (max 12). Without it, none passes.
- **Invented numbers:** none with the skill. One without it (`common ja`, the number `08`).
- **`TBD-n`:** only the `api-design` outputs with the skill carry any (8, 9 and 8 for `en`, `ja`, `vi`). No other output has one.
- **Length:** all 6 `tech-blog` outputs get a length warning, with or without the skill. The with-skill outputs are shorter than the without-skill ones in `en`, `ja` and `vi`.

## Rules that changed after this run

- The length warnings follow the old rule from before T3 of the review-fixes run. The old rule warned below the lower limit. The checker now warns only above the upper limit, so these 6 warnings would not appear today.
- The one violation of `common en` (a 21-word first sentence) came from the time-token count. The first sentence has `2026-12-03` and `04:00`, and the old count split the time into 2 words. The checker now counts a time and an ISO date as one unit each, so the sentence has 20 words and passes.
- The with-skill prompt of this run included `banned.txt`. The prompt no longer sends it. This run's `common` with-skill prompt had no `doc-types/common.md`, which was added later.

## Limits of this evidence

- **One run.** Run-to-run variance is unknown, and a difference of one violation is within noise.
- **Mechanical scores only.** This run has no AI-judge scores and no human review. The results do not measure clarity, voice or coverage.
- **Simulated data.** All cases use made-up briefs.
- **Short outputs.** The `tech-blog` outputs are far below the old length target. The cases do not set `short_brief`.
- **`ja` content.** Japanese outputs were scored mechanically. No native review was done.
