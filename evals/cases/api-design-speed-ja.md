---
lang: ja
type: api-design
non_tech: false
---

# SIMULATED DATA

エンドポイント、項目名、業務規則、エラーコードは、この評価のために作った。素材には意図的に1つの欠けがある。応答の時間の上限が書かれていない。

## Audience

注文APIを実装・テストするバックエンド開発者とQA担当者。

## Brief

### Idea
1件の注文を読み取る `GET /v1/orders/{order_id}` を設計する。以下の規則はすべて模擬である。

### Business rules
- 注文を読み取れるロールは `owner` と `support` のみ。それ以外のロールは HTTP 403(`order_forbidden`)を受け取る。
- `order_id` が uuid でないとき、APIは HTTP 400(`order_invalid_id`)を返す。
- そのIDの注文がないとき、APIは HTTP 404(`order_not_found`)を返す。
- APIは高速に応答する。
- レスポンスには `order_id` と `status` が入る。`status` は `pending`、`paid`、`shipped`、`cancelled` のいずれか。
- 成功時、APIは HTTP 200 と注文を返す。

### Glossary
- `order_id`: 注文のID(uuid)。
- `status`: 注文の状態。

## Facts
- エンドポイント: `GET /v1/orders/{order_id}`
- 許可するロール: `owner`、`support`(それ以外は HTTP 403 `order_forbidden`)
- `order_id` が uuid でない: HTTP 400 `order_invalid_id`
- そのIDの注文がない: HTTP 404 `order_not_found`
- statusの値: `pending`、`paid`、`shipped`、`cancelled`
- 成功時のステータス: HTTP 200
