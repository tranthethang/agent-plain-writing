# 投稿作成API設計

## 概要

1件の投稿を作成するAPIです。項目名と `status` の許可値は、WordPress REST APIの投稿リファレンス「Create a Post」によります。本書に記載する業務規則は、この設計のためのものです。

| 項目 | 内容 |
|---|---|
| メソッド | `POST` |
| エンドポイント | `/wp/v2/posts` |
| 成功時 | HTTP `201`。保存した投稿を返す |

## 権限

投稿を作成できるロールは `editor` と `author` です。それ以外のロールからのリクエストには、HTTP `403` とコード `rest_cannot_create` を返します。

`status` に `publish` を指定して投稿できるのは `editor` のみです。`author` が `publish` を指定した場合は、HTTP `403` とコード `rest_cannot_publish` を返します。

## リクエスト項目

| 項目 | 説明・規則 |
|---|---|
| `title` | 投稿のタイトル。最大長は `TBD`。 |
| `content` | 投稿の本文。 |
| `status` | 投稿の公開状態。許可値は `publish`、`future`、`draft`、`pending`、`private`。省略時は `draft`。 |
| `date` | `status` が `future` の場合、現在時刻より後の日時を指定する必要があります。 |
| `slug` | 投稿に固有のURLの部分。省略時は `title` から作成します。同じスラッグがすでにある場合は、数字の接尾辞を付けます。 |
| `categories` | カテゴリIDの一覧（整数）。指定する各IDは存在している必要があります。 |

`title` と `content` は、少なくとも一方を指定してください。両方を指定しない場合は、HTTP `400` とコード `rest_empty_post` を返します。

## エラー応答

| 条件 | HTTPステータス | エラーコード |
|---|---:|---|
| 許可されていないロールが投稿を作成 | `403` | `rest_cannot_create` |
| `author` が `status: publish` を指定 | `403` | `rest_cannot_publish` |
| `title` と `content` の両方がない | `400` | `rest_empty_post` |
| `status: future` で、`date` が現在時刻より後ではない | `400` | `rest_invalid_date` |
| 存在しないカテゴリIDを指定 | `400` | `rest_invalid_term` |

## 未確定事項

- `title` の最大長は `TBD` です。
- エラー応答の本文形式、日時の形式、各項目の型（`categories` を除く）、およびエラーが複数該当する場合の優先順位は、この設計では定めていません。
- 許可値以外の `status` を指定した場合の応答は、この設計では定めていません。
- `slug` の数字の接尾辞の付け方、および `title` がない状態で `slug` も省略された場合の動作は、この設計では定めていません。