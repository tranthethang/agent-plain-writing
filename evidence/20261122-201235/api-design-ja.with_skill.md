## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author` のみ。`status` を `publish` にできるのは `editor` のみ。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `title` | リクエスト | string | 条件付き（`content` がない場合に必要） | 最大長は `TBD-1` |
| `content` | リクエスト | string | 条件付き（`title` がない場合に必要） | — |
| `status` | リクエスト | enum<string> | 任意 | `publish`、`future`、`draft`、`pending`、`private` |
| `slug` | リクエスト | string | 任意 | — |
| `categories` | リクエスト | integerの配列 | `TBD-4` | 各IDが存在すること |
| `date` | リクエスト | `TBD-3` | 条件付き（`status` が `future` の場合に必要） | 現在時刻より後であること |
| 保存した投稿 | レスポンス | `TBD-5` | — | — |

## エンドポイント

リクエスト例:

```json
{"title": "Example post", "status": "draft"}
```

成功ステータス: HTTP 201

## 処理

システムは、`status` がない場合に `draft` を使う。

リクエストに `slug` がない場合、システムは `title` から `slug` を作る。`title` もない場合の動作は `TBD-8`。

同じ `slug` がすでにある場合、システムは数字の接尾辞を付ける。接尾辞の決め方は `TBD-9`。

実行順序: `TBD-6`

エラー優先順位: `TBD-7`

## エラー

| 条件 | HTTP | コード |
|---|---:|---|
| 呼び出し元のロールが `editor` または `author` 以外 | 403 | `rest_cannot_create` |
| 呼び出し元が `author` で、`status` が `publish` | 403 | `rest_cannot_publish` |
| `title` と `content` の両方がない | 400 | `rest_empty_post` |
| `status` が `future` で、`date` が現在時刻より後ではない | 400 | `rest_invalid_date` |
| `categories` のIDが存在しない | 400 | `rest_invalid_term` |
| `title` が最大長を超える | `TBD-2` | `TBD-2` |

## 副作用

—

## 未決事項

- `TBD-1`: `title` の最大長は何文字か。
- `TBD-2`: `title` が最大長を超えた場合のHTTPステータスとエラーコードは何か。
- `TBD-3`: `date` の型と形式は何か。
- `TBD-4`: `categories` は必須か、任意か。
- `TBD-5`: レスポンスに含むフィールド名と各型は何か。
- `TBD-6`: 処理の実行順序は何か。
- `TBD-7`: 複数のエラー条件が成立した場合、どのエラーを優先するか。
- `TBD-8`: `slug` と `title` の両方がない場合、システムはどう動作するか。
- `TBD-9`: 既存の `slug` と重複した場合、数字の接尾辞をどう決めるか。