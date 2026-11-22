## Identity

- Method and path: `GET /v1/orders/{order_id}`
- Purpose: read one order. Response-time limit: `TBD-1`.
- Authorization: only the roles `owner` and `support` may read an order.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `order_id` | Request | uuid | Yes | — |
| `order_id` | Response | uuid | — | — |
| `status` | Response | string | — | — |

## Endpoint

Request:

    GET /v1/orders/00000000-0000-4000-8000-000000000000

Response, status 200:

    {"order_id": "00000000-0000-4000-8000-000000000000", "status": "pending"}

## Processing

Execution order and error precedence: `TBD-2`.

## Errors

| Condition | HTTP status | Code |
|---|---:|---|
| The caller has a role other than `owner` or `support` | 403 | `order_forbidden` |
| `order_id` is not a UUID | 400 | `order_invalid_id` |
| No order has the requested ID | 404 | `order_not_found` |

## Side effects

None

## Open items

- `TBD-1`: What response-time limit defines “quickly”?
- `TBD-2`: In what order does the API apply authorization, UUID validation, and order lookup, and which error takes precedence when multiple conditions apply?