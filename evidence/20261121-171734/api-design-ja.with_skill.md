## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author`。`status` を `publish` にできるのは `editor` のみ。

## DTOとフィールド対応

| 項目 | 型 | 必須 | 制約 |
|---|---|---|---|
| `title` | TBD-1 | 条件付き（`content` がない場合に必須） | 最大長はTBD-2 |
| `content` | TBD-3 | 条件付き（`title` がない場合に必須） | — |
| `status` | enum | 任意 | `publish`、`future`、`draft`、`pending`、`private`。既定値は `draft` |
| `date` | TBD-4 | 条件付き（`status` が `future` の場合） | 現在時刻より後 |
| `slug` | TBD-5 | 任意 | 未指定の場合は `title` から作成。同じスラッグがある場合は数字の接尾辞を付ける |
| `categories` | integerの一覧 | TBD-6 | 各IDが存在すること |

レスポンス: 保存した投稿。項目と型はTBD-7。

## エンドポイント

成功ステータス: HTTP 201。

## 処理

- システムは、呼び出し元のロールを確認する。条件に合わない場合は `rest_cannot_create` で止める。
- システムは、`title` と `content` の少なくとも一方があることを確認する。ない場合は `rest_empty_post` で止める。
- システムは、`status` が許可された値であることを確認する。許可されていない場合は `TBD-8` で止める。
- システムは、`status` に関するロール条件を確認する。条件に合わない場合は `rest_cannot_publish` で止める。
- `status` が `future` の場合、システムは `date` が現在時刻より後であることを確認する。そうでない場合は `rest_invalid_date` で止める。
- システムは、各 `categories` IDの存在を確認する。存在しない場合は `rest_invalid_term` で止める。
- `title` が最大長を超える場合の処理は `TBD-9`。
- 各処理の実行順と、複数の条件に該当した場合のエラー優先順位はTBD-10。

## エラー

| HTTP | コード | 条件 |
|---|---|---|
| 403 | `rest_cannot_create` | 呼び出し元のロールが `editor` または `author` ではない |
| 400 | `rest_empty_post` | `title` と `content` の両方がない |
| 403 | `rest_cannot_publish` | `author` が `status` に `publish` を指定した |
| 400 | `rest_invalid_date` | `status` が `future` で、`date` が現在時刻より後ではない |
| 400 | `rest_invalid_term` | `categories` に存在しないIDがある |
| TBD-8 | TBD-8 | `status` が許可された値ではない |
| TBD-9 | TBD-9 | `title` がTBD-2で定める最大長を超える |

## 副作用

システムは投稿を保存する。ほかの副作用はTBD。

## 未決事項

- TBD-1: `title` の型は何か。
- TBD-2: `title` の最大長は何か。
- TBD-3: `content` の型は何か。
- TBD-4: `date` の型は何か。
- TBD-5: `slug` の型は何か。
- TBD-6: `categories` は必須か、任意か。
- TBD-7: 保存した投稿のレスポンス項目と型は何か。
- TBD-8: 許可されていない `status` のHTTPステータスとエラーコードは何か。
- TBD-9: `title` が最大長を超えた場合のHTTPステータスとエラーコードは何か。
- TBD-10: 処理の実行順と、複数の条件に該当した場合のエラー優先順位は何か。
- 副作用として、投稿保存以外に何が発生するか。