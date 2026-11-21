---
lang: ja
type: api-design
non_tech: false
---

# SIMULATED DATA

エンドポイントと項目名は、公開されているWordPress REST APIの投稿リファレンス(「Create a Post」)による。業務規則とエラーコードは、この評価のために作った。

## Audience

ブログAPIを実装・テストするバックエンド開発者とQA担当者。

## Brief

### Idea
1件の投稿を作成する `POST /wp/v2/posts` を設計する。情報源: WordPress REST APIの投稿リファレンス、エンドポイント「Create a Post」。項目名と許可される値を除き、以下の規則は模擬である。

### Business rules
- ロール `editor` と `author` のみが投稿を作成できる。それ以外のロールには HTTP 403 (`rest_cannot_create`) を返す。
- `title` か `content` のどちらかが必要である。両方ない場合は HTTP 400 (`rest_empty_post`) を返す。
- `status` は `publish`、`future`、`draft`、`pending`、`private` のいずれかとする。既定値は `draft` である。
- `status` を `publish` にできるのは `editor` のみである。`author` が `publish` を送ると HTTP 403 (`rest_cannot_publish`) を返す。
- `status` が `future` のとき、`date` は現在時刻より後でなければならない。そうでない場合は HTTP 400 (`rest_invalid_date`) を返す。
- `slug` がない場合、システムは `title` から作る。同じスラッグがすでにある場合は、数字の接尾辞を付ける。
- `categories` の各IDは存在しなければならない。存在しないIDには HTTP 400 (`rest_invalid_term`) を返す。
- 成功した場合は HTTP 201 と保存した投稿を返す。
- `title` の最大長は情報源にない。`TBD` とする。

### Glossary
- `title`: 投稿のタイトル。
- `content`: 投稿の本文。
- `status`: 投稿の公開状態。
- `slug`: 投稿に固有のURLの部分。
- `categories`: カテゴリIDの一覧(整数)。

## Facts
- エンドポイント: `POST /wp/v2/posts`
- 許可するロール: `editor`、`author`(それ以外は HTTP 403 `rest_cannot_create`)
- statusの値: `publish`、`future`、`draft`、`pending`、`private`。既定値は `draft`
- 公開できるのは `editor` のみ(違反は HTTP 403 `rest_cannot_publish`)
- `title` と `content` の両方がない: HTTP 400 `rest_empty_post`
- `future` は未来の `date` が必要(違反は HTTP 400 `rest_invalid_date`)
- 存在しないカテゴリID: HTTP 400 `rest_invalid_term`
- 成功時のステータス: HTTP 201
