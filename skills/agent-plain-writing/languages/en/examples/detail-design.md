# English examples: detail design

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

## Complete filled API (reference shape; your real template comes first)

```markdown
## POST /v1/orders

### 1. Purpose
Create a new order from the cart of a signed-in user.

### 2. Input
| Field | Type | Required | Constraint |
|---|---|---|---|
| `cart_id` | uuid | Yes | The cart must belong to the caller |
| `payment_method` | enum | Yes | `card`, `cod` |
| `note` | string | No | at most 200 characters |

### 3. Processing
1. The system checks that the cart is not empty.
2. The system checks stock for each line. If stock is short, it returns `OUT_OF_STOCK`.
3. The system creates the order with status `PENDING` in one transaction.
4. The system clears the cart.

### 4. Output
201. Body: `order_id`, `status`, `total`.

### 5. Errors
| HTTP | Code | Condition |
|---|---|---|
| 400 | `EMPTY_CART` | The cart is empty |
| 401 | `UNAUTHORIZED` | No valid token |
| 409 | `OUT_OF_STOCK` | A line exceeds stock |

### 6. Notes
- `TBD`: how long is stock held for a `PENDING` order?
```

## Your own samples

<!-- Paste one API you filled in well. The AI learns from this more than from any description. -->
