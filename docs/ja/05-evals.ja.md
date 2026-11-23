# 評価（Evals）

`evals/` は、実際のエージェントでスキルを試します。小さなキットで、ベンチマークではありません。

| ファイル | 役割 |
|---|---|
| `cases/` | 18 ケース：`tech-blog`、`essay`、`api-design`、`user-guide`、`common` を、それぞれ `vi`、`en`、`ja` で。さらに `api-design-speed` の 3 ケース。データはすべて架空です |
| `smoke-prompts.md` | スモークセット：変更後にすばやく確認するための 5 つのプロンプト |
| `score.py` | 機械的な採点。ケースにない数字を数え、`api-design` では `tbd_ids`、`tbd_without_question`、`tbd_in_code`、`tbd_duplicate_questions`、`tbd_without_inline` も報告する |
| `judge-prompt.md` | AI 審査員用のプロンプト（明瞭さ、網羅性、`api-design`・`tech-blog`・`essay`・`user-guide`・`common` ごとの意味チェック） |

## 手順

API を呼ぶスクリプトはありません。出力は実際のエージェントが書きます。

1. ローカルのゲート：`python3 -m unittest discover -s tests` と `python3 scripts/sync_shared.py --check`。
2. 6 つのスキルをすべてインストールします：`npx skills add tranthethang/agent-plain-writing -g`。
3. `evidence/<run>/` を作ります。
4. エージェントでプロンプトを実行します。スモークセットは `evals/smoke-prompts.md` です。フルセットは `evals/cases/` のすべてのファイルです。各プロンプトで、出力を `evidence/<run>/<case>.with_skill.md` に書くよう指示します。
5. 出力ごとに採点し、結果を `evidence/<run>/results.json` に保存します。

```bash
python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md
python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md --judge-prompt
```

`evals/README.md` に、1 回の実行のすべての出力を 1 つの `results.json` にまとめて採点する短いスクリプトがあります。

## 正直な限界

- 実行結果は `evidence/` に保存され、git で管理されます。実行ごとの要約は [evidence/](../../evidence/README.md) にあります。各実行には機械的なスコアしかないため、スキルが文章を改善する証明にはなりません。
- `evals/cases/` のケースはすべての文書タイプを対象にします。各実行がどのケースを扱ったかは、その実行の `README.md` に書いてあります。
- 審査員は AI です。そのスコアを人間の読者と照らし合わせて検証していません。
- ケースは架空のデータです。実際のブリーフからケースを足す方法は `evals/README.md` を参照してください。

次へ：[06-limitations](06-limitations.ja.md)。
