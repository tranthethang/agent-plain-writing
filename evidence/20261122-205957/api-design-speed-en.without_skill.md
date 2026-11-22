# `GET /v1/orders/{order_id}`

Retrieves one order.

## Request

**Path parameter**

| Name | Description |
|---|---|
| `order_id` | UUID of the order to retrieve. |

## Authorization

Only users with the `owner` or `support` role may read an order. Other roles receive **HTTP 403** with error code `order_forbidden`.

## Success response

**HTTP 200**

The response contains the order:

```json
{
  "order_id": "…",
  "status": "pending"
}
```

`status` is one of `pending`, `paid`, `shipped`, or `cancelled`.

## Errors

| Condition | HTTP status | Error code |
|---|---:|---|
| `order_id` is not a UUID | 400 | `order_invalid_id` |
| No order exists with that ID | 404 | `order_not_found` |
| Caller’s role is not `owner` or `support` | 403 | `order_forbidden` |

The brief does not specify an error response body or the order in which errors take precedence if multiple conditions apply.

## Response time

The API should respond quickly. No specific time limit or latency target is defined.