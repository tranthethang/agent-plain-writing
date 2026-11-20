---
lang: ja
type: design
non_tech: false
---

# SIMULATED DATA

## Audience

内部APIを実装・テストするバックエンド開発者とQA担当者。

## Brief

### Template
```markdown
## <METHOD> <PATH>
### 1. 目的
### 2. 入力
### 3. 処理
### 4. 出力
### 5. エラー
### 6. 備考
```

### Idea
ログイン済みユーザーがAPIトークンを1つ失効させる `DELETE /v1/tokens/{token_id}` を設計する。

### Business rules
- ユーザーは自分が所有するトークンのみ失効できる。他人のトークンを指定した場合は HTTP 403 (`FORBIDDEN`) を返す。
- すでに失効済みのトークンを指定した場合は HTTP 409 (`ALREADY_REVOKED`) を返す。
- 存在しない `token_id` の場合は HTTP 404 (`NOT_FOUND`) を返す。
- 失効に成功した場合、システムは現在時刻を `revoked_at` に記録し、HTTP 200 で `token_id` と `revoked_at` を返す。
- 失効後、キャッシュされたトークンが完全に無効になるまでの最大遅延時間は未定（`TBD` とする）。

### Glossary
- `token_id`: トークン識別子（UUID）。
- `revoked_at`: 失効日時（ISO 8601 UTC）。

## Facts
- エンドポイント: `DELETE /v1/tokens/{token_id}`
- 所有者以外の指定: HTTP 403 (`FORBIDDEN`)
- 失効済みの再指定: HTTP 409 (`ALREADY_REVOKED`)
- 未存在のID: HTTP 404 (`NOT_FOUND`)
- 成功時: HTTP 200 (`token_id`, `revoked_at`)
- 形式: `token_id` は UUID、`revoked_at` は ISO 8601 UTC
