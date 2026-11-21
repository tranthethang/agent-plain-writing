# 投稿作成 API 設計

## 概要

| 項目 | 内容 |
|---|---|
| メソッド | `POST` |
| エンドポイント | `/wp/v2/posts` |
| 用途 | 投稿を1件作成する |

## 利用条件

投稿を作成できるロールは `editor` と `author` です。それ以外のロールからのリクエストには、HTTP `403` とエラーコード `rest_cannot_create` を返します。

## リクエスト項目

| 項目 | 説明・規則 |
|---|---|
| `title` | 投稿のタイトル。最大長は `TBD`。 |
| `content` | 投稿の本文。 |
| `status` | 投稿の公開状態。指定できる値は `publish`、`future`、`draft`、`pending`、`private`。省略時は `draft`。`publish` にできるのは `editor` のみです。 |
| `date` | `status` が `future` の場合、現在時刻より後の日時を指定します。 |
| `slug` | 投稿に固有のURLの部分。省略時は `title` から作成されます。同じスラッグがすでにある場合は、数字の接尾辞が付与されます。 |
| `categories` | カテゴリIDの一覧（整数）。各IDは存在する必要があります。 |

`title` と `content` の少なくとも一方を指定してください。両方ともない場合は、HTTP `400` とエラーコード `rest_empty_post` を返します。

## エラー

| 条件 | HTTPステータス | エラーコード |
|---|---:|---|
| 投稿を作成できないロールからのリクエスト | `403` | `rest_cannot_create` |
| `title` と `content` の両方がない | `400` | `rest_empty_post` |
| `author` が `status: publish` を指定 | `403` | `rest_cannot_publish` |
| `status: future` で、`date` が現在時刻より後ではない | `400` | `rest_invalid_date` |
| 存在しないカテゴリIDが指定された | `400` | `rest_invalid_term` |

## 成功時のレスポンス

投稿の作成に成功した場合は、HTTP `201` と保存した投稿を返します。

## 未確定事項

エラー時のレスポンス本文、成功レスポンスの具体的な項目構成、`date` の形式、スラッグに付ける数字の具体的な規則は、この仕様では定めません。`title` の最大長も `TBD` です。