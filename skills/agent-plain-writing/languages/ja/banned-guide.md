# Banned phrases and what to use instead (Japanese)

The machine-readable list is `banned.txt` in this folder. This file explains the replacements. When you add a phrase in one place, add it in the other.

## Padding and "AI voice" (all types)

| Phrase | Use instead | Example |
|---|---|---|
| することができる / することができます | 〜できる / 〜できます | 「送信することができます」→「送信できます」 |
| 〜を行う / 〜を行います | the verb itself | 「確認を行う」→「確認する」 |
| 〜において *(warn)* | 〜で | 「本システムにおいて」→「本システムで」 |
| 〜に関して *(warn)* | 〜について | |
| させていただ(く) | 〜します (use it only when the situation truly needs humility) | 「報告させていただきます」→「報告します」 |
| 非常に、大変 *(warn: 大変)* | delete, or give a number | |
| 画期的、革新的、包括的、強力な、シームレス | say what it does, with a number | 「強力なツール」→「1秒に1万行を処理できるツール」 |

## Vague words in detail design

| Word | Use instead |
|---|---|
| 適切、適宜 | the exact condition |
| 必要に応じて | the exact condition, or `TBD` |
| 等、など | list everything, or point to an appendix |
| 迅速、容易に | a number (ms, number of steps) |
| 柔軟 | what can be configured, and how |
| 効率的、安全に | a measurable criterion |

## Words common in user guides

| Word | Use instead |
|---|---|
| 実施、〜を行う | a concrete verb: タップする、選ぶ、入力する |
| 設定を行う | 設定する |

## Phrases of blog

| Phrase | Use instead |
|---|---|
| この記事を書いた | open with the event or conclusion directly |
| 学んだこと：, 注意点： | weave the point into the paragraph, no label |
| と言えるでしょう / と言えます / ではないでしょうか | state the claim, or state the evidence (「重要と言えるでしょう」→ say why it matters) |

## Phrases of prose

| Phrase | Use instead |
|---|---|
| 胸が高鳴、時が止まっ、言葉にできない、心が張り裂け、瞳が輝 | one visible action or detail |
| と言えるでしょう / と言えます / ではないでしょうか | state the claim, or delete |

## General rules

- A banned phrase may stay when it is a **direct quote**, a proper name or a fixed label on a screen.
- Banning a phrase does not ban the idea. 「システムは速い」is still needed, with a number.
- 「など」 is legitimate in casual text. It is flagged only in detail design, where it hides an incomplete list.
