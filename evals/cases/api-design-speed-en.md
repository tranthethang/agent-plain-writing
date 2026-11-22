---
lang: en
type: api-design
non_tech: false
---

# SIMULATED DATA

The endpoint, the field names, the business rules and the error codes are invented for this eval. The brief has one gap on purpose: it gives no time limit for the response.

## Audience

Backend developers and QA engineers who implement and test an order API.

## Brief

### Idea
Design `GET /v1/orders/{order_id}` to read one order. All rules below are simulated.

### Business rules
- Only the roles `owner` and `support` may read an order. Other roles receive HTTP 403 (`order_forbidden`).
- When `order_id` is not a uuid, the API returns HTTP 400 (`order_invalid_id`).
- When no order has that id, the API returns HTTP 404 (`order_not_found`).
- The API responds quickly.
- The response holds `order_id` and `status`. `status` is one of `pending`, `paid`, `shipped`, `cancelled`.
- On success, the API returns HTTP 200 and the order.

### Glossary
- `order_id`: the id of the order (uuid).
- `status`: the state of the order.

## Facts
- Endpoint: `GET /v1/orders/{order_id}`
- Allowed roles: `owner`, `support` (others get HTTP 403 `order_forbidden`)
- `order_id` is not a uuid: HTTP 400 `order_invalid_id`
- No order with that id: HTTP 404 `order_not_found`
- Status values: `pending`, `paid`, `shipped`, `cancelled`
- Success status: HTTP 200
