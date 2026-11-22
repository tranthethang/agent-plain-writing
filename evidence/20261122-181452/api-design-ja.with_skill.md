## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author` のみが投稿を作成できる。`status` を `publish` にできるのは `editor` のみである。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `title` | リクエスト | string | 条件付き（`title` または `content` が必要） | 最大長は `TBD-1` |
| `content` | リクエスト | string | 条件付き（`title` または `content` が必要） | — |
| `status` | リクエスト | enum | 任意 | `publish`、`future`、`draft`、`pending`、`private` |
| `slug` | リクエスト | string | 任意 | — |
| `date` | リクエスト | `TBD-2` | 条件付き（`status` が `future` の場合） | 現在時刻より後であること |
| `categories` | リクエスト | 整数の配列 | `TBD-3` | 各IDが存在すること |
| 保存した投稿のフィールド | レスポンス | `TBD-4` | — | — |

## エンドポイント

リクエスト:

```json
{"title": "投稿タイトル"}
```

成功ステータス: 201

## 処理

システムは、`status` が指定されていない場合、`draft` を使う。

システムは、`slug` が指定されていない場合、`title` から生成する。同じスラッグがすでにある場合、数字の接尾辞を付ける。接尾辞の形式は `TBD-7`。

実行順序: `TBD-8`

エラーの優先順位: `TBD-9`

## エラー

| 条件 | HTTP | コード |
|---|---:|---|
| 呼び出し元のロールが `editor` または `author` ではない | 403 | `rest_cannot_create` |
| 呼び出し元のロールが `author` で、`status` が `publish` である | 403 | `rest_cannot_publish` |
| `title` と `content` の両方がない | 400 | `rest_empty_post` |
| `status` が許可された値ではない | `TBD-5` | `TBD-5` |
| `status` が `future` で、`date` が現在時刻より後ではない | 400 | `rest_invalid_date` |
| `title` が最大長を超える | `TBD-6` | `TBD-6` |
| カテゴリIDが存在しない | 400 | `rest_invalid_term` |

## 副作用

`TBD-10`

## 未決事項

- `TBD-1`: `title` の最大長は何文字か。
- `TBD-2`: `date` の型は何か。
- `TBD-3`: `categories` は必須か。
- `TBD-4`: 成功レスポンスに含めるフィールドと各フィールドの型は何か。
- `TBD-5`: `status` が許可された値ではない場合のHTTPステータスとエラーコードは何か。
- `TBD-6`: `title` が最大長を超えた場合のHTTPステータスとエラーコードは何か。
- `TBD-7`: 重複した `slug` に付ける数字の接尾辞の形式は何か。
- `TBD-8`: 処理の実行順序は何か。
- `TBD-9`: 複数のエラー条件が同時に成立した場合、どのエラーを優先するか。
- `TBD-10`: 投稿の作成以外に発生させる副作用はあるか。