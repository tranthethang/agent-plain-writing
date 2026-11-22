## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author` のみが投稿を作成できる。`status` を `publish` にできるのは `editor` のみである。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `title` | リクエスト | string | 条件付き（`content` がない場合は必須） | 最大長: `TBD-1` |
| `content` | リクエスト | string | 条件付き（`title` がない場合は必須） | — |
| `status` | リクエスト | enum | 任意 | `publish`、`future`、`draft`、`pending`、`private` |
| `date` | リクエスト | datetime | 任意 | — |
| `slug` | リクエスト | string | 任意 | — |
| `categories` | リクエスト | integerの配列 | 任意 | — |
| 投稿 | レスポンス | `TBD-2` | — | — |

## エンドポイント

リクエスト:

```json
{"title": "投稿タイトル", "status": "draft"}
```

成功時のHTTPステータス: `201`

## 処理

`status` がない場合、システムは `draft` を設定する。

`slug` がない場合、システムは `title` から `slug` を作成する。作成する `title` がない場合の動作は `TBD-3`。同じ `slug` がすでにある場合、システムは数字の接尾辞を付ける。

処理順: `TBD-4`

複数のエラー条件に該当する場合の優先順: `TBD-5`

## エラー

| 条件 | HTTPステータス | コード |
|---|---:|---|
| 呼び出し元のロールが `editor` または `author` ではない | 403 | `rest_cannot_create` |
| 呼び出し元が `author` で、`status` が `publish` である | 403 | `rest_cannot_publish` |
| `title` と `content` が両方ない | 400 | `rest_empty_post` |
| `status` が許可された値ではない | `TBD-6` | `TBD-6` |
| `status` が `future` で、`date` が現在時刻より後ではない | 400 | `rest_invalid_date` |
| `categories` に存在しないIDが含まれる | 400 | `rest_invalid_term` |

## 副作用

なし

## 未決事項

- `TBD-1`: `title` の最大長はいくつか。
- `TBD-2`: 成功レスポンスに含めるフィールドと各フィールドの型は何か。
- `TBD-3`: `title` がない場合、システムは `slug` をどう作成するか。
- `TBD-4`: 処理の実行順は何か。
- `TBD-5`: 複数のエラー条件に該当する場合、どのエラーを優先するか。
- `TBD-6`: 許可されていない `status` の値に対するHTTPステータスとエラーコードは何か。

<!-- report -->

固定テンプレートに沿って作成しました。業務ルールについて追加の推測はしていません。