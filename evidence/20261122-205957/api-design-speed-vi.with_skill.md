## Thông tin chung

- Method và path: `GET /v1/orders/{order_id}`
- Mục đích: đọc một đơn hàng. Thời hạn trả lời: `TBD-1`.
- Phân quyền: chỉ role `owner` và `support` được đọc đơn hàng.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `order_id` | Yêu cầu | uuid | Có | — |
| `order_id` | Phản hồi | uuid | — | — |
| `status` | Phản hồi | string | — | `pending`, `paid`, `shipped`, `cancelled` |

## Endpoint

Yêu cầu:

```http
GET /v1/orders/00000000-0000-0000-0000-000000000000
```

Phản hồi, status 200:

```json
{"order_id":"00000000-0000-0000-0000-000000000000","status":"pending"}
```

## Xử lý

Thứ tự kiểm tra và ưu tiên lỗi khi nhiều điều kiện cùng đúng: `TBD-2`.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `order_forbidden` | Người gọi có role khác `owner` và `support` |
| 400 | `order_invalid_id` | `order_id` không phải uuid |
| 404 | `order_not_found` | Không có đơn hàng mang `order_id` đó |

## Tác động kèm theo

Không có

## Mục còn mở

- `TBD-1`: Thời hạn trả lời của API là bao lâu?
- `TBD-2`: Thứ tự kiểm tra là gì, và lỗi nào được ưu tiên khi nhiều điều kiện cùng đúng?

<!-- report -->
Giá trị UUID trong ví dụ là giá trị minh họa. `order_id` được xem là bắt buộc vì nó nằm trong path.