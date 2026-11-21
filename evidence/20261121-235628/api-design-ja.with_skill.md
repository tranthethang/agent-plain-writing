## 識別情報

- メソッドとパス: `POST /wp/v2/posts`
- 目的: 投稿を1件作成する。
- 認可: ロール `editor` と `author` は投稿を作成できる。`status` を `publish` にできるのは `editor` のみ。`author` は `status` に `publish` を指定してはならない。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `title` | リクエスト | string | 条件付き（`content` がない場合） | 最大長 `TBD-1` |
| `content` | リクエスト | string | 条件付き（`title` がない場合） | — |
| `status` | リクエスト | enum<string> | 任意 | `publish`、`future`、`draft`、`pending`、`private` |
| `slug` | リクエスト | string | 任意 | — |
| `date` | リクエスト | `TBD-3` | 条件付き（`status` が `future` の場合） | 現在時刻より後 |
| `categories` | リクエスト | integer[] | 任意 | 各IDが存在すること |
| 保存した投稿 | レスポンス | `TBD-4` | — | — |

## エンドポイント

リクエスト:

```json
{"title": "投稿タイトル"}
```

成功ステータス: HTTP 201

## 処理

- `status` がない場合、システムは `draft` を設定する。
- `slug` がない場合、システムは `title` から作成する。`title` もない場合の動作: `TBD-5`。
- 同じスラッグがすでにある場合、システムは数字の接尾辞を付ける。接尾辞の決め方: `TBD-6`。
- 処理順: `TBD-8`。
- エラーの優先順: `TBD-9`。

## エラー

| HTTP | コード | 条件 |
|---|---|---|
| 403 | `rest_cannot_create` | 呼び出し元のロールが `editor` と `author` 以外 |
| 403 | `rest_cannot_publish` | 呼び出し元が `author` で、`status` が `publish` |
| 400 | `rest_empty_post` | `title` と `content` の両方がない |
| 400 | `rest_invalid_date` | `status` が `future` で、`date` が現在時刻より後でない |
| 400 | `rest_invalid_term` | `categories` に存在しないIDがある |
| `TBD-2` | `TBD-2` | `title` が `TBD-1` の最大長を超える |
| `TBD-7` | `TBD-7` | `status` が許可された値に含まれない |

## 副作用

なし

## 未決事項

- `TBD-1`: `title` の最大長は何文字か。
- `TBD-2`: `title` が最大長を超えた場合のHTTPステータスとエラーコードは何か。
- `TBD-3`: `date` の型は何か。
- `TBD-4`: 成功レスポンスに含める投稿のフィールドと型は何か。
- `TBD-5`: `title` と `slug` の両方がない場合、システムはどう動作するか。
- `TBD-6`: 既存のスラッグと重複した場合、数字の接尾辞をどう決めるか。
- `TBD-7`: `status` が許可された値に含まれない場合のHTTPステータスとエラーコードは何か。
- `TBD-8`: 処理の実行順は何か。
- `TBD-9`: 複数のエラー条件に該当した場合、どのエラーを優先するか。