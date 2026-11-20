---
lang: en
type: design
non_tech: false
---

# SIMULATED DATA

## Audience

Backend developers and QA engineers implementing and testing an internal API.

## Brief

### Template
```markdown
## <METHOD> <PATH>
### 1. Purpose
### 2. Input
### 3. Processing
### 4. Output
### 5. Errors
### 6. Notes
```

### Idea
Design `POST /v1/webhooks/endpoints` to register a webhook URL for a workspace so it receives event notifications.

### Business rules
- Only workspace `admin` users may create an endpoint. Other roles receive HTTP 403 (`FORBIDDEN`).
- The target URL must use `https://`. Plain `http://` URLs are rejected with HTTP 400 (`INVALID_URL`).
- Each workspace can register at most 5 active endpoints. Exceeding 5 returns HTTP 409 (`LIMIT_REACHED`).
- On success, the API generates a 32-byte signing secret, stores its hash, and returns the raw secret once in HTTP 201.
- Timeout for webhook delivery retries is not yet decided (mark as `TBD`).

### Glossary
- `url`: HTTPS callback URL (max 512 characters).
- `events`: non-empty list of event names (e.g. `order.created`, `order.paid`).
- `signing_secret`: 32-byte hex secret returned only on creation.

## Facts
- Endpoint: `POST /v1/webhooks/endpoints`
- Allowed role: `admin` (others get HTTP 403 `FORBIDDEN`)
- URL scheme: `https://` required (otherwise HTTP 400 `INVALID_URL`)
- Max URL length: 512 characters
- Max active endpoints per workspace: 5 (otherwise HTTP 409 `LIMIT_REACHED`)
- Signing secret size: 32 bytes
- Success status: HTTP 201
