# カスタマイズ

- **プロジェクト設定。** `skills/agent-plain-writing/templates/PLAIN-WRITING.example.md` を、プロジェクトのルートに `PLAIN-WRITING.md` としてコピーします。`default_lang`、`default_type`、文体、追加の用語、追加の禁止表現、上限を設定できます。スクリプトは JSON ブロックを読み、AI は Markdown の節を読みます。
- **自分のサンプル。** 各 `examples/*.md` の末尾に「Your own samples」の節があります。AI が下手に書いた文と、あなたの書き直しを貼ってください。自分で書いたサンプルは、AI が書いたサンプルより価値があります。
- **禁止表現。** 同じ言語フォルダの `banned.txt` と `banned-guide.md` の両方に追加します。`[tech-blog,essay]` のような見出しは、複数のタイプで 1 つの禁止リストを共有します。
- **上限。** `profile.json` を編集します。`tech-blog` の文の上限を変えたら、`README.md` と [03-checker](03-checker.ja.md) の単位の表も更新します。
- **新しい言語。** `languages/<code>/` を作り、`profile.json`、`profile.md`、`banned.txt`、`banned-guide.md`、`terms.txt`、`examples/` を置きます。スクリプトが対応する単位は `syllable`、`word`、`char` の 3 つです。`SKILL.md`、`README.md`、このドキュメントも更新します。`AGENTS.md` を参照してください。

次へ：[05-evals](05-evals.ja.md)。
