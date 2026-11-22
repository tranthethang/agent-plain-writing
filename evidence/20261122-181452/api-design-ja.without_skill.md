# 投稿作成API設計

## 概要

| 項目 | 内容 |
|---|---|
| メソッド | `POST` |
| エンドポイント | `/wp/v2/posts` |
| 成功時のHTTPステータス | `201 Created` |
| 成功時のレスポンス | 保存した投稿 |

## 認可

投稿を作成できるロールは `editor` と `author` です。それ以外のロールからのリクエストには、HTTP `403` とエラーコード `rest_cannot_create` を返します。

`status` を `publish` にできるのは `editor` のみです。`author` が `publish` を指定した場合は、HTTP `403` と `rest_cannot_publish` を返します。

## リクエスト項目

| 項目 | 説明・規則 |
|---|---|
| `title` | 投稿のタイトル。`content` とあわせて、どちらか一方は必要です。最大長は `TBD` です。 |
| `content` | 投稿の本文。`title` とあわせて、どちらか一方は必要です。 |
| `status` | 投稿の公開状態。`publish`、`future`、`draft`、`pending`、`private` のいずれか。省略時は `draft` です。 |
| `date` | `status` が `future` の場合、現在時刻より後の日時を指定します。 |
| `slug` | 投稿に固有のURLの部分。省略時は `title` から作成されます。同じスラッグがすでにある場合は、数字の接尾辞が付きます。 |
| `categories` | カテゴリIDの一覧（整数）。各IDは存在している必要があります。 |

## バリデーションとエラー

| 条件 | HTTPステータス | エラーコード |
|---|---:|---|
| 投稿を作成できないロールからのリクエスト | `403` | `rest_cannot_create` |
| `title` と `content` の両方がない | `400` | `rest_empty_post` |
| `author` が `status: publish` を指定 | `403` | `rest_cannot_publish` |
| `status: future` で、`date` が現在時刻より後でない | `400` | `rest_invalid_date` |
| 存在しないカテゴリIDを指定 | `400` | `rest_invalid_term` |

## 処理規則

1. 投稿作成を許可されたロールか確認します。
2. `title` または `content` の少なくとも一方があることを確認します。
3. `status` を検証します。省略時は `draft` とします。
4. `publish` の権限と、`future` の場合の日時を検証します。
5. `categories` の各IDが存在することを確認します。
6. `slug` が省略されている場合は `title` から作成し、重複時には数字の接尾辞を付けます。
7. 作成に成功した場合は、HTTP `201` と保存した投稿を返します。