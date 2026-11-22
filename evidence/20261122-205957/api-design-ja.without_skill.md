# 投稿作成 API 設計

## 概要

1件の投稿を作成する。エンドポイントと項目名は、WordPress REST API の投稿リファレンス「Create a Post」に基づく。以下の業務規則は本仕様で定める模擬ルールである。

## エンドポイント

| 項目 | 内容 |
|---|---|
| メソッド | `POST` |
| パス | `/wp/v2/posts` |

## 実行権限

投稿を作成できるロールは `editor` と `author` のみ。それ以外のロールからのリクエストには、HTTP `403` とエラーコード `rest_cannot_create` を返す。

## リクエスト項目

| 項目 | 説明・規則 |
|---|---|
| `title` | 投稿のタイトル。最大長は `TBD`。 |
| `content` | 投稿の本文。 |
| `status` | 投稿の公開状態。指定できる値は `publish`、`future`、`draft`、`pending`、`private`。省略時は `draft`。 |
| `date` | `status` が `future` の場合、現在時刻より後の日時を指定する。 |
| `slug` | 投稿に固有のURLの部分。省略時は `title` から作成する。同じスラッグがすでにある場合は数字の接尾辞を付ける。 |
| `categories` | カテゴリIDの一覧（整数）。各IDは存在しなければならない。 |

### 必須条件

`title` または `content` の少なくとも一方を指定する。両方がない場合は HTTP `400`、エラーコード `rest_empty_post` を返す。

### ステータス別の条件

- `author` が `status: publish` を指定した場合は、HTTP `403`、エラーコード `rest_cannot_publish` を返す。`publish` にできるのは `editor` のみ。
- `status: future` の場合、`date` は現在時刻より後でなければならない。条件を満たさない場合は HTTP `400`、エラーコード `rest_invalid_date` を返す。

### カテゴリの条件

`categories` に存在しないIDが含まれる場合は、HTTP `400`、エラーコード `rest_invalid_term` を返す。

## 成功レスポンス

投稿の作成に成功した場合は、HTTP `201` と保存した投稿を返す。

## 未確定事項

- `title` の最大長は `TBD`。
- `title` を指定せず、かつ `slug` も省略した場合のスラッグ生成方法は未定義。