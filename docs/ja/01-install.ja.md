# インストール

ターミナルで次のコマンドを実行します。`npx` を使うため、Node.js が必要です。

```bash
npx skills add tranthethang/agent-plain-writing -g
```

- `tranthethang/agent-plain-writing` は、スキルを置いている GitHub リポジトリです。
- `-g` は、スキルをグローバル（ユーザー単位）にインストールします。1 つのプロジェクトだけではありません。`-g` を外すと、現在のプロジェクトにインストールします。

このコマンドは 6 つのスキルをまとめてインストールします。ルーターの `agent-plain-writing` と、5 つの `agent-plain-writing-<type>` サブスキルです。そのあと、エージェントに `agent-plain-writing`、またはいずれかのサブスキルを使うよう頼みます。[02-usage](02-usage.ja.md) を参照してください。

## 手動でインストールする

`npx` を使わない場合は、`skills/agent-plain-writing*/` の各フォルダを、エージェントのスキルフォルダにコピーします。6 つすべてをコピーします。各フォルダ名は、その `SKILL.md` の `name` と同じにします。

| ツール | 置き場所 |
|---|---|
| Claude Code | `.claude/skills/`（プロジェクト）または `~/.claude/skills/`（個人） |
| `SKILL.md` を読むほかのツール | そのツールのドキュメントを参照 |

## 注記

- Python 3.7 以上が必要なのは、チェックスクリプトを実行するときだけです（[03-checker](03-checker.ja.md)）。ほかの依存はありません。

次へ：[02-usage](02-usage.ja.md)。
