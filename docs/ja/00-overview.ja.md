# 概要

`agent-plain-writing` は AI エージェント向けのスキルです。ベトナム語（`vi`）、英語（`en`）、日本語（`ja`）で、短く具体的な文章を書くよう AI に指示します。

## 解決したい問題

AI の下書きには、次の欠点がよく出ます。

- 文が長く、読みにくい。
- 読者が知らない専門用語が多い。
- 専門外の読者向けでも、AI が技術的な細部をすべて説明する。文章は長くなり、分かりやすくはなりません。

プロンプトに「分かりやすく」「親しみやすく」と足しても直りません。このスキルは、数えられる上限、まねできる例、そして別工程の推敲を使います。

| | |
|---|---|
| 悪い例 | 本システムはキャッシュ機構を活用し、データ取得性能の最適化を図ります。 |
| 良い例 | システムは計算済みの結果を保存します。次回からは、すばやく答えます。 |

## 含まれるもの

- **基本ルールと手順**：`SKILL.md`（共通ルール 6 つと文体ファミリーごとのルール、下書きのあとに推敲）。(no native review yet)
- **2 つの文体ファミリーに 4 つの文書タイプ**：`plain`（`tech-blog`、`api-design`、`guide`）と `creative`（`essay`）。各タイプに `doc-types/` のファイルがあり、文体、構成、長さを定めます。
- **3 つの言語フォルダ**：カウント単位、数値の上限、禁止表現、専門用語リスト、例文を収めます。
- **チェックスクリプト** `check_style.py`（Python 3.7 以上、標準ライブラリのみ）。
- **評価キット**：`evals/`（[05-evals](05-evals.ja.md) を参照）。

`prose`、`poetry`、`screen-design` は現時点では対象外です。(no native review yet)

## どのファイルがどのルールを持つか

各事実には、持ち主のファイルが 1 つあります。ほかのファイルはそこを指すだけです。

| 事実 | 持ち主 |
|---|---|
| 手順と基本ルール | `SKILL.md` |
| 文体、構成、長さの方針、文のリズム | `doc-types/<type>.md` |
| カウント単位と数値の上限 | `languages/<lang>/profile.json` |
| 禁止表現 | `languages/<lang>/banned.txt` |
| 文法の落とし穴、人称と程度の語 | `languages/<lang>/profile.md` |
| 専門用語リスト | `languages/<lang>/terms.txt` |

上限と構成では `doc-types` が `SKILL.md` に優先します。語句と文法では `languages` が `doc-types` に優先します。素材の外に何をどこまで足せるかでは、文体ファミリーと `doc-types` がコアルールに優先します。ただし、コアルール 5 の事実は変わりません（no native review yet）。完全な表は `AGENTS.md` にあります。

## リポジトリの構成

```
.
├── README.md
├── AGENTS.md                 # このリポジトリを編集するときのルール
├── docs/{en,vi,ja}/          # このドキュメント
├── evals/                    # ケース、採点、審査プロンプト、実行スクリプト
└── skills/agent-plain-writing/
    ├── SKILL.md
    ├── doc-types/            # tech-blog, essay, api-design, user-guide
    ├── languages/{vi,en,ja}/ # profile.json, profile.md, banned.txt, banned-guide.md,
    │                         # terms.txt, examples/
    ├── templates/PLAIN-WRITING.example.md
    └── scripts/check_style.py
```

次へ：[01-install](01-install.ja.md)。
