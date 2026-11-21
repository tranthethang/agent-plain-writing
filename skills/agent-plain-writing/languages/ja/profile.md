# Language profile: Japanese (ja)

The numbers live in `profile.json`. This file explains how to use them.

**All limits below are starting estimates, not verified standards.** Run the script on real texts from your team and adjust `profile.json`.

## Unit

- The script counts **characters (字)**: every character except punctuation, spaces and control characters.
- Sentences are split at `。` `！` `？`.
- `length` in `profile.json` is counted in characters.

## Limits and voice

Every number (sentence, paragraph, length, jargon) lives in `profile.json`. This file does not repeat them.
Voice, speaker and structure are set by `doc-types/<type>.md`. This file adds only the Japanese forms below.

## Register (文体)

The register is a Japanese form, so it is listed here. Choose one register per document and never mix them. Mixing is the most visible mistake in Japanese text.

| Type | Register | Notes |
|---|---|---|
| tech-blog | です・ます調 | Friendly but direct |
| essay | だ・である調 | Plain form by default (no native review yet) |
| guide | です・ます調 | Steps end in 「〜します」. Instructions use 「〜してください」 sparingly (one per section at most) |
| design | である調 / 常体 | Plain form: 「〜する。」「〜しない。」. Table cells may end in a noun (体言止め) |

Teams differ. Before writing a design document or a manual for a Japanese team or customer, confirm their register convention and follow it.

## Requirement words (API design)

| Level | Use |
|---|---|
| Mandatory | 〜しなければならない |
| Forbidden | 〜してはならない |
| Recommended | 〜することが望ましい |
| Optional | 〜してもよい |

Many Japanese design documents state default behaviour with plain 「〜する」. Use the requirement words only where the strength of the requirement matters, and keep one form per level. Confirm the team convention.

## Required-flag labels (API design)

Use in the field table of an API. The labels follow the document language. (no native review yet)

| Level | Label |
|---|---|
| Required | 必須 |
| Not required | 任意 |
| Depends on a rule | 条件付き（<条件>） |


## Jargon

- Reader is a developer: use the term the team already uses (for example サーバー or サーバ, never both). One concept, one term.
- Reader is outside the field: use the replacement table in `examples/user-guide.md`.

## Common traps in Japanese

- 「〜することができる」 → 「〜できる」.
- 「〜を行う」 (noun + を行う) → the verb itself: 「確認を行う」 → 「確認する」.
- 「〜において」「〜に関して」 → 「〜で」「〜について」.
- Overuse of 「〜させていただく」.
- Chains of の ("AのBのCのD"): split the sentence.
- Dropped subject in design documents: name the actor ("システムは...", "クライアントは...").
- Punctuation: use 、 and 。 in Japanese text. Use half-width digits. Keep one rule for spaces between Latin letters and Japanese, and follow the team rule.
