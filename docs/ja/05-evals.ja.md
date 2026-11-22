# 評価（Evals）

`evals/` は、スキルありとなしの AI 出力を比べます。小さなキットで、ベンチマークではありません。

| ファイル | 役割 |
|---|---|
| `cases/` | 15 ケース：`tech-blog`、`essay`、`api-design`、`guide`、`common` を、それぞれ `vi`、`en`、`ja` で。データはすべて架空です |
| `score.py` | 機械的な採点。ケースにない数字を数え、`api-design` では `tbd_ids`、`tbd_without_question`、`tbd_in_code`、`tbd_duplicate_questions`、`tbd_without_inline` も報告する |
| `judge-prompt.md` | AI 審査員用のプロンプト（明瞭さ、網羅性、`api-design`・`tech-blog`・`essay`・`guide`・`common` ごとの意味チェック） |
| `run_eval.py` | 各ケースを 2 回（スキルあり・なし）実行する |

## コスト

`run_eval.py` は 1 ケースにつき AI を 2 回呼びます。15 ケースすべてで 30 回となり、利用枠や料金を消費します。必ず先にプレビューしてください。

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

API 設定は `evals/.env` かリポジトリ直下の `.env` に置きます。どちらも git の対象外です。出力は `evidence/<timestamp>/` に保存され、git で管理されます。

1 つの出力を採点するには：

```bash
python3 evals/score.py evals/cases/tech-blog-en.md output.md
python3 evals/score.py evals/cases/tech-blog-en.md output.md --judge-prompt
python3 evals/run_eval.py --judge-prompts 20261122-181452
```

`--judge-prompts <run>` は `evidence/` 内の実行フォルダにある `with_skill` 出力すべてについて、審査員プロンプトを作ります。出力先は `judge-prompts/<run>/<case>.judge.md` で、AI は呼びません。値を省略すると、新しい実行の後に同じ処理をします。

## 正直な限界

- 実行結果は `evidence/` に保存され、git で管理されます。実行ごとの要約は [evidence/](../../evidence/README.md) にあります。どちらも 1 回の実行で、機械的なスコアだけなので、スキルが文章を改善する証明にはなりません。
- `evals/cases/` のケースはすべての文書タイプを対象にします。各実行がどのケースを扱ったかは、その実行の `README.md` に書いてあります。
- 審査員は AI です。そのスコアを人間の読者と照らし合わせて検証していません。
- ケースは架空のデータです。実際のブリーフからケースを足す方法は `evals/README.md` を参照してください。

次へ：[06-limitations](06-limitations.ja.md)。
