# 投稿作成 API 設計

## 概要

1件の投稿を作成するAPIです。

| 項目 | 内容 |
|---|---|
| メソッド | `POST` |
| エンドポイント | `/wp/v2/posts` |

## 権限

投稿を作成できるロールは `editor` と `author` です。それ以外のロールからのリクエストには、HTTP `403` とエラーコード `rest_cannot_create` を返します。

`status` を `publish` にできるのは `editor` のみです。`author` が `publish` を指定した場合は、HTTP `403` とエラーコード `rest_cannot_publish` を返します。

## リクエスト項目

| 項目 | 説明・制約 |
|---|---|
| `title` | 投稿のタイトル。`content` と合わせて、少なくともどちらか一方が必要です。最大長は `TBD` です。 |
| `content` | 投稿の本文。`title` と合わせて、少なくともどちらか一方が必要です。 |
| `status` | 投稿の公開状態。`publish`、`future`、`draft`、`pending`、`private` のいずれか。省略時の既定値は `draft` です。 |
| `date` | `status` が `future` の場合、現在時刻より後の日時を指定します。 |
| `slug` | 投稿に固有のURLの部分。省略時は `title` から作成されます。同じスラッグがすでにある場合は、数字の接尾辞が付与されます。 |
| `categories` | カテゴリIDの一覧。各IDが存在する必要があります。 |

`title` と `content` の両方がない場合は、HTTP `400` とエラーコード `rest_empty_post` を返します。

`status` が `future` で、`date` が現在時刻より後でない場合は、HTTP `400` とエラーコード `rest_invalid_date` を返します。

`categories` に存在しないIDが含まれる場合は、HTTP `400` とエラーコード `rest_invalid_term` を返します。

## 成功レスポンス

投稿の作成に成功した場合は、HTTP `201` と保存した投稿を返します。レスポンスの項目構成はここでは規定しません。