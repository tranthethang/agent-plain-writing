# 評価（Evals）

`evals/` は、スキルありとなしの AI 出力を比べます。小さなキットで、ベンチマークではありません。

| ファイル | 役割 |
|---|---|
| `cases/` | 9 ケース：`tech-blog`、`essay`、`api-design` を、それぞれ `vi`、`en`、`ja` で。データはすべて架空です |
| `score.py` | 機械的な採点。ケースにない数字を数え、`api-design` では `tbd_ids`、`tbd_without_question`、`tbd_in_code`、`tbd_duplicate_questions`、`tbd_without_inline` も報告する |
| `judge-prompt.md` | AI 審査員用のプロンプト（明瞭さ、網羅性、`api-design` 向けの意味チェック 3 点） |
| `run_eval.py` | 各ケースを 2 回（スキルあり・なし）実行する |

## コスト

`run_eval.py` は 1 ケースにつき AI を 2 回呼びます。9 ケースすべてで 18 回となり、利用枠や料金を消費します。必ず先にプレビューしてください。

```bash
python3 evals/run_eval.py --dry-run
python3 evals/run_eval.py --type tech-blog --lang vi --dry-run
```

そのあと実行します。スクリプトは `yes` の入力を求めます。

```bash
python3 evals/run_eval.py --tool openai   # 既定。OPENAI_API_URL, OPENAI_API_KEY, OPENAI_API_MODEL を読む
python3 evals/run_eval.py --tool claude   # ローカルの `claude` CLI
python3 evals/run_eval.py --tool antigravity
```

API 設定は `evals/.env` かリポジトリ直下の `.env` に置きます。どちらも git の対象外です。出力は `evals/runs/<timestamp>/` に保存され、これも git の対象外です。

1 つの出力を採点するには：

```bash
python3 evals/score.py evals/cases/tech-blog-en.md output.md
python3 evals/score.py evals/cases/tech-blog-en.md output.md --judge-prompt
```

## 正直な限界

- 実行結果は git の対象外です。1 回分の実行を [evidence/](../../evidence/README.md) に証拠として残しています。1 回の実行で、機械的なスコアだけなので、スキルが文章を改善する証明にはなりません。
- 9 ケースは 3 タイプを対象にし、保存した証拠の実行では使っていません。`guide` にはケースがありません。
- 審査員は AI です。そのスコアを人間の読者と照らし合わせて検証していません。
- ケースは架空のデータです。実際のブリーフからケースを足す方法は `evals/README.md` を参照してください。

次へ：[06-limitations](06-limitations.ja.md)。
