# English examples: API design

Stories and numbers in these examples are illustrations, not facts.

Requirement words in this document: **must**, **must not**, **should**, **may**. One word per level.

## Bad → good pairs

### 1. Vague performance

**Bad:** The API returns results quickly.
**Good:** The API must respond within 500 ms at P95.
(If no figure is known: `TBD: P95 target for this API?`)

### 2. Vague error handling

**Bad:** The system handles out-of-stock errors appropriately.
**Good:** When an item is out of stock, the system returns 409 with the code `OUT_OF_STOCK` and does not create the order.

### 3. Vague authorization

**Bad:** Only users with appropriate permissions can perform this action.
**Good:** Only the roles `admin` and `staff` may call this API. Any other role receives 403.

### 4. Vague security

**Bad:** Data is stored securely.
**Good:** Passwords are stored as bcrypt hashes. The system must not store a plain-text password.

### 5. A process written as prose

**Bad:** First the system checks whether the cart is empty, and if it is not, it then proceeds to check the stock of each item, and if stock is sufficient, it creates the order and subsequently clears the cart.
**Good:**
1. The system checks that the cart is not empty.
2. The system checks stock for each line.
3. The system creates the order with status `PENDING`.
4. The system clears the cart.

### 6. Vague retry

**Bad:** If necessary, the system retries.
**Good:** When a call to the payment service fails, the system retries up to 3 times, 2 seconds apart. After the third failure, it returns 503.
(If the source gives no figure: `TBD: number of retries and delay?`)

### 7. Input written as prose

**Bad:** The API accepts the necessary information such as the cart ID, the payment method and an optional note.
**Good:**

| Field | Type | Required | Constraint |
|---|---|---|---|
| `cart_id` | uuid | Yes | The cart must belong to the caller |
| `payment_method` | enum | Yes | `card`, `cod` |
| `note` | string | No | at most 200 characters |

### 8. "etc."

**Bad:** Order status can be PENDING, PAID, etc.
**Good:** Order status is one of `PENDING`, `PAID`, `SHIPPED`, `CANCELLED`. If the source is incomplete: `TBD: full list of statuses?`

### 9. Inconsistent terms

**Bad:** When a user creates an order, the system saves the purchase request into the orders table.
**Good:** When a user creates an order, the system saves the order into the `orders` table.
**Convention:** "order" in prose, `orders` as the table name. Never "purchase" or "request" for the same thing.

### 10. Writing a condition

**Bad:** In the event that the user has not logged in, access shall be denied.
**Good:** When the request has no valid token, the system must return 401.

### 11. Errors listed twice

**Bad:** Processing step 2 says "return 409 `ROOM_TAKEN` when the room is booked". The Errors table says the same again with different wording.
**Good:** Processing step 2 says "If the room is booked, stop with the error `ROOM_TAKEN`." The Errors table is the only place that gives the status 409 and the condition.
**Fault:** Two owners for one fact drift apart.
**Fix:** Processing names the code. The Errors table owns the status and the condition.

### 12. Authorization listed three times

**Bad:** Identity says "staff only". Processing step 1 says "check that the caller is staff". Errors says "403 when the caller is not staff, as above".
**Good:** Identity says "Authorization: the roles `admin` and `staff`." Errors lists `403 FORBIDDEN` with the condition "the caller has another role". Processing does not mention roles.
**Fault:** Three places state one rule.
**Fix:** Identity owns the rule. Errors owns the failure.

### 13. "Same as siblings"

**Bad:** Errors: same as the other room endpoints.
**Good:** List every error of this endpoint in its own table. If the source is missing, write `TBD: which errors does this endpoint return?`
**Fault:** The reader cannot check the endpoint alone.
**Fix:** Write the rule here, or write `TBD` with a question.

### 14. A business rule with no step order

**Bad:** The system checks the overlap, the opening hours and the quota when it creates a reservation.
**Good:**
1. The system checks that the slot lies inside opening hours.
2. The system checks that no reservation overlaps the slot.
3. The system checks that the caller is under the daily quota.
4. The system saves the reservation.
**Fault:** The reader cannot tell which error wins when two checks fail.
**Fix:** Number the steps in execution order.

### 15. An empty-list case with no rule

**Bad:** The API returns the reservations of a room.
**Good:** The API returns the reservations of a room. When the room has none, it returns 200 with `items` as an empty array.
**Fault:** QA cannot tell 200 from 404 for an empty result.
**Fix:** Give the empty case its own sentence with a status.

### 16. Processing with steps and a diagram

**Bad:** A diagram alone, with no numbered steps. Or steps alone, for a flow with three branches.
**Good:** Numbered steps first, then one Mermaid block that shows the same order:

````markdown
1. The system checks that the slot lies inside opening hours.
2. The system checks that no reservation overlaps the slot.
3. The system saves the reservation.

```mermaid
sequenceDiagram
    Client->>API: POST /v1/reservations
    API->>DB: find overlapping reservations
    DB-->>API: none
    API->>DB: insert reservation
    API-->>Client: 201
```
````

**Fault:** The diagram holds rules that the steps do not state.
**Fix:** The steps own the rules. The diagram shows the order only.

## Complete filled API (reference shape)

````markdown
## Identity

- Method and path: `POST /v1/reservations`
- Purpose: create a reservation for one meeting room.
- Caller: the booking web app.
- Authorization: the roles `admin` and `staff`.
- Idempotency: not idempotent. A repeated call creates a second reservation.

## DTO and field mapping

| Field | Type | Required | Constraint |
|---|---|---|---|
| `room_id` | uuid | Yes | The room must exist |
| `starts_at` | datetime | Yes | The start must be in the future |
| `minutes` | integer | Yes | 30 to 240, in steps of 30 |
| `note` | string | No | at most 200 characters |

Response fields: `reservation_id` (uuid), `status` (string), `ends_at` (datetime).

## Endpoint

Request:

    {"room_id": "r-12", "starts_at": "2026-12-01T09:00:00Z", "minutes": 60}

Response, status 201:

    {"reservation_id": "rv-88", "status": "CONFIRMED", "ends_at": "2026-12-01T10:00:00Z"}

## Processing

1. The system checks that the slot lies inside opening hours.
2. The system checks that no reservation overlaps the slot. If one does, it stops with `ROOM_TAKEN`.
3. The system saves the reservation with status `CONFIRMED`.

```mermaid
sequenceDiagram
    Client->>API: POST /v1/reservations
    API->>DB: find overlapping reservations
    DB-->>API: none
    API->>DB: insert reservation
    API-->>Client: 201
```

## Errors

| HTTP | Code | Condition |
|---|---|---|
| 400 | `OUTSIDE_HOURS` | The slot lies outside opening hours |
| 403 | `FORBIDDEN` | The caller has another role |
| 409 | `ROOM_TAKEN` | Another reservation overlaps the slot |

## Side effects

The system writes one audit record for each saved reservation.

## Open items

- `TBD`: how many days ahead may a caller reserve?
````

## Your own samples

<!-- Paste one API you filled in well. The AI learns from this more than from any description. -->
