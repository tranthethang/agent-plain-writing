# Language profile: Japanese (ja)

The numbers live in `profile.json`. This file explains how to use them.

**All limits below are starting estimates, not verified standards.** Run the script on real texts from your team and adjust `profile.json`.

## Unit

- The script counts **characters (字)**: every character except punctuation, spaces and control characters.
- Sentences are split at `。` `！` `？`.
- Blog length is counted in characters (about 1,500–2,000 字, the rough equivalent of 600–800 English words).

## Limits by document type

| Type | Max sentence (字) | Max paragraph (sentences) | Length | Jargon |
|---|---|---|---|---|
| blog | 60 | 3 | 1,500–2,000 字 | unlimited (3 with `--non-tech`) |
| prose | 80 | 6 | any | unlimited |
| poetry | n/a | n/a | any | unlimited |
| design | 55 | 3 | per template | unlimited |
| guide | 40 | 3 | any | at most 3 |

## Register (文体)

Choose one register per document and never mix them. Mixing is the most visible mistake in Japanese text.

| Type | Register | Notes |
|---|---|---|
| blog | です・ます調 | Friendly but direct |
| guide | です・ます調 | Steps end in 「〜します」. Instructions use 「〜してください」 sparingly (one per section at most) |
| design | である調 / 常体 | Plain form: 「〜する。」「〜しない。」. Table cells may end in a noun (体言止め) |
| prose | 常体 (だ・た) | Past tense by default |
| poetry | free | Follow the form |

Teams differ. Before writing a design document or a manual for a Japanese team or customer, confirm their register convention and follow it.

## Requirement words (detail design)

| Level | Use |
|---|---|
| Mandatory | 〜しなければならない |
| Forbidden | 〜してはならない |
| Recommended | 〜することが望ましい |
| Optional | 〜してもよい |

Many Japanese design documents state default behaviour with plain 「〜する」. Use the requirement words only where the strength of the requirement matters, and keep one form per level. Confirm the team convention.

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
