# 投稿作成 API 設計

## 概要

1件の投稿を作成するAPI。エンドポイントと項目名は、WordPress REST APIの投稿リファレンス「Create a Post」に基づく。以下の業務規則は本設計のための模擬規則である。

| 項目 | 内容 |
|---|---|
| HTTPメソッド | `POST` |
| パス | `/wp/v2/posts` |
| 成功時のHTTPステータス | `201 Created` |

## 権限

投稿を作成できるロールは `editor` と `author` のみ。その他のロールからのリクエストには、次のエラーを返す。

| HTTPステータス | エラーコード | 条件 |
|---|---|---|
| 403 | `rest_cannot_create` | ロールが `editor` または `author` ではない |

## リクエスト項目

| 項目 | 説明・規則 |
|---|---|
| `title` | 投稿のタイトル。最大長は `TBD`。 |
| `content` | 投稿の本文。 |
| `status` | 投稿の公開状態。指定できる値は `publish`、`future`、`draft`、`pending`、`private`。省略時は `draft`。 |
| `date` | `status` が `future` の場合、現在時刻より後の日時を指定する。 |
| `slug` | 投稿に固有のURLの部分。省略時は `title` から生成する。同じスラッグがすでにある場合は、数字の接尾辞を付ける。 |
| `categories` | カテゴリIDの一覧。各IDは整数で、存在するカテゴリを指定する。 |

`title` と `content` の少なくとも一方が必要。両方がない場合は、HTTP `400` とエラーコード `rest_empty_post` を返す。

## ステータスに関する規則

- `status` に指定できる値は `publish`、`future`、`draft`、`pending`、`private`。
- `publish` にできるのは `editor` のみ。`author` が `publish` を指定した場合は、HTTP `403` とエラーコード `rest_cannot_publish` を返す。
- `status` が `future` の場合、`date` は現在時刻より後でなければならない。条件を満たさない場合は、HTTP `400` とエラーコード `rest_invalid_date` を返す。

## カテゴリの検証

`categories` に存在しないカテゴリIDが含まれている場合は、HTTP `400` とエラーコード `rest_invalid_term` を返す。

## レスポンス

### 成功

投稿を保存し、HTTP `201 Created` と保存した投稿を返す。レスポンス本文の項目構成は本設計では定めない。

### エラー一覧

| HTTPステータス | エラーコード | 条件 |
|---|---|---|
| 403 | `rest_cannot_create` | 投稿を作成できないロールからのリクエスト |
| 403 | `rest_cannot_publish` | `author` が `publish` を指定 |
| 400 | `rest_empty_post` | `title` と `content` の両方がない |
| 400 | `rest_invalid_date` | `status` が `future` だが、`date` が現在時刻より後ではない |
| 400 | `rest_invalid_term` | `categories` に存在しないカテゴリIDが含まれる |