# 概要

`agent-plain-writing` は AI エージェント向けの 6 つのスキルのセットです。ルーター 1 つと、文書タイプごとのサブスキル 5 つからなります。ベトナム語（`vi`）、英語（`en`）、日本語（`ja`）で、短く具体的な文章を書くよう AI に指示します。

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

- **ルータースキル** `agent-plain-writing`：文書タイプと言語を選び、サブスキルに引き継ぎます。書き方のルールは持ちません。
- **サブスキル 5 つ** `agent-plain-writing-<type>`：それぞれ基本ルールと手順（共通ルール 6 つと文体ファミリーごとのルール、下書きのあとに推敲）と、そのタイプの文体、構成、長さを持ちます。
- **2 つの文体ファミリーに 5 つの文書タイプ**：`plain`（`tech-blog`、`api-design`、`user-guide`、`common`）と `creative`（`essay`）。各タイプに `shared/doc-types/` のファイルがあります。
- **3 つの言語フォルダ**：カウント単位、数値の上限、禁止表現、専門用語リスト、例文を収めます。
- **チェックスクリプト** `check_style.py`（Python 3.7 以上、標準ライブラリのみ）。各サブスキルが自分のコピーを持ちます。
- **評価キット**：`evals/`（[05-evals](05-evals.ja.md) を参照）。

`prose`、`poetry`、`screen-design` は現時点では対象外です。

## どのファイルがどのルールを持つか

各事実には、`shared/` の中に持ち主のファイルが 1 つあります。ほかのファイルはそこを指すだけです。各サブスキルの `SKILL.md` は `shared/` から生成され、手で編集しません。

| 事実 | 持ち主 |
|---|---|
| 手順と基本ルール | `shared/skill-core.md` |
| 文体ファミリー | `shared/families/<family>.md` |
| 文体、構成、長さの方針、文のリズム | `shared/doc-types/<type>.md` |
| カウント単位と数値の上限 | `shared/languages/<lang>/profile.json` |
| 禁止表現 | `shared/languages/<lang>/banned.txt`（チェッカー用の一覧）、`banned-guide.md`（AI が読むファイル） |
| 文法の落とし穴、人称と程度の語 | `shared/languages/<lang>/profile.md` |
| 専門用語リスト | `shared/languages/<lang>/terms.txt` |
| サブスキルへの振り分け | `skills/agent-plain-writing/SKILL.md` |

上限と構成では `doc-types` が `skill-core.md` に優先します。語句と文法では `languages` が `doc-types` に優先します。素材の外に何をどこまで足せるかでは、文体ファミリーと `doc-types` がコアルールに優先します。ただし、コアルール 5 の事実は変わりません。完全な表は `AGENTS.md` にあります。

## リポジトリの構成

```
.
├── README.md
├── AGENTS.md                 # このリポジトリを編集するときのルール
├── docs/{en,vi,ja}/          # このドキュメント
├── evals/                    # ケース、スモークプロンプト、採点、審査プロンプト
├── scripts/sync_shared.py    # shared/ から skills/ を生成する
├── shared/                   # スキルの内容を編集する唯一の場所
│   ├── skill-core.md
│   ├── families/             # plain.md, creative.md
│   ├── doc-types/            # tech-blog, essay, api-design, user-guide, common
│   ├── languages/{vi,en,ja}/ # profile.json, profile.md, banned.txt, banned-guide.md,
│   │                         # terms.txt, examples/
│   ├── templates/PLAIN-WRITING.example.md
│   └── scripts/check_style.py
└── skills/                   # ルーター以外は生成物
    ├── agent-plain-writing/              # ルーター：SKILL.md のみ
    └── agent-plain-writing-<type>/       # SKILL.md, languages/, scripts/, templates/
```

次へ：[01-install](01-install.ja.md)。
