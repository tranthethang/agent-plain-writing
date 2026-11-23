# チェックスクリプト

```bash
python3 skills/agent-plain-writing-tech-blog/scripts/check_style.py draft.md --lang en --type tech-blog
python3 skills/agent-plain-writing-api-design/scripts/check_style.py spec.md  --lang ja --type api-design
python3 skills/agent-plain-writing-user-guide/scripts/check_style.py guide.md --lang vi --type user-guide
python3 skills/agent-plain-writing-tech-blog/scripts/check_style.py post.md  --lang en --type tech-blog --non-tech
```

| オプション | 値 |
|---|---|
| `--lang` | `vi`、`en`、`ja`。`PLAIN-WRITING.md` に `default_lang` があれば省略可 |
| `--type` | `tech-blog`、`essay`、`api-design`、`user-guide`、`common`。既定は `default_type`、なければ `common` |
| `--non-tech` | 専門用語を 3 語までに制限する。`user-guide` タイプは常に用語の上限を適用する |
| `--config` | `PLAIN-WRITING.md` へのパス。既定は現在のフォルダから親フォルダへ順に探す（`.git` で停止） |
| `--short-brief` | `length_short` を持つタイプ（たとえば `tech-blog`）で、その範囲を使う |

終了コード：`0` 問題なし、`1` 違反あり、`2` 使い方の誤り。`--type blog` は廃止され終了コード `2` を返します。代わりに `--type tech-blog` を使ってください。

## チェックする内容

- 文の長さ、段落の長さ、禁止表現、専門用語の数、文章全体の長さ。文章全体の長さが上限を超えた場合だけ警告を出力し、終了コードは変わりません。上限より短い文章は問題ありません。長さを水増ししないでください。
- コードブロックの外で、行頭にある報告ラベル（`Result:` など）。
- 行末の空白による改行。
- `profile.json` で設定するパターンチェック：全角ダッシュや二分ダッシュ、中黒（`·`）、カーリークォート（`en` のみ有効）、段落冒頭の数え上げ開始、否定の対比表現、連続する疑問文。

コードブロック、表、見出しは対象外です。ただし `api-design` では、表の各セルの文の長さを調べます。リスト項目は文の長さだけを調べ、段落の長さは調べません。

## チェックしない内容

文体、事実、文が自然かどうか。スクリプトは機械的に数えるだけです。違反なしは、数の条件を満たしたという意味で、文章がよいという意味ではありません。

## カウント単位

| 言語 | 単位 | `tech-blog` の文の上限 |
|---|---|---|
| `vi` | 音節（*tiếng*） | 28（約 20 語） |
| `en` | 語 | 20 |
| `ja` | 文字（字）。句読点と空白は除く | 60 |

全タイプの上限は、各言語の `profile.json` だけにあります。上の表は `tech-blog` の行の写しです。

次へ：[04-customize](04-customize.ja.md)。
