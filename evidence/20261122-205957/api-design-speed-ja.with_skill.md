## 識別情報

- メソッドとパス: `GET /v1/orders/{order_id}`
- 目的: 注文を1件読み取る。
- 認可: ロール `owner` と `support` のみ。

## DTOとフィールド対応

| 項目 | 方向 | 型 | 必須 | 制約 |
|---|---|---|---|---|
| `order_id` | リクエスト | uuid | 必須 | uuidであること |
| `order_id` | レスポンス | uuid | — | — |
| `status` | レスポンス | string | — | `pending`、`paid`、`shipped`、`cancelled` |

## エンドポイント

リクエスト:

    GET /v1/orders/{order_id}

レスポンス。ステータス200:

    {"order_id": "<uuid>", "status": "pending"}

## 処理

実行順とエラー優先順: `TBD-1`。

応答時間の上限: `TBD-2`。

## エラー

| HTTP | コード | 条件 |
|---|---|---|
| 403 | `order_forbidden` | 呼び出し元のロールが `owner` または `support` ではない |
| 400 | `order_invalid_id` | `order_id` がuuidではない |
| 404 | `order_not_found` | `order_id` の注文が存在しない |

## 副作用

なし

## 未決事項

- `TBD-1`: 実行順とエラー優先順は何か。
- `TBD-2`: 応答時間の上限はいくらか。