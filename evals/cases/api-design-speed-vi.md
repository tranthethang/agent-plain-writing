---
lang: vi
type: api-design
non_tech: false
---

# SIMULATED DATA

Endpoint, tên trường, quy tắc nghiệp vụ và mã lỗi đều được bịa cho bài eval này. Brief cố ý thiếu một điểm: không nêu thời hạn trả lời.

## Audience

Lập trình viên backend và QA triển khai, kiểm thử một API đơn hàng.

## Brief

### Idea
Thiết kế `GET /v1/orders/{order_id}` để đọc một đơn hàng. Mọi quy tắc dưới đây là giả lập.

### Business rules
- Chỉ vai trò `owner` và `support` được đọc đơn hàng. Vai trò khác nhận HTTP 403 (`order_forbidden`).
- Khi `order_id` không phải uuid, API trả HTTP 400 (`order_invalid_id`).
- Khi không có đơn hàng nào mang id đó, API trả HTTP 404 (`order_not_found`).
- API trả lời nhanh.
- Phản hồi có `order_id` và `status`. `status` là một trong `pending`, `paid`, `shipped`, `cancelled`.
- Khi thành công, API trả HTTP 200 và đơn hàng.

### Glossary
- `order_id`: id của đơn hàng (uuid).
- `status`: trạng thái của đơn hàng.

## Facts
- Endpoint: `GET /v1/orders/{order_id}`
- Vai trò được phép: `owner`, `support` (vai trò khác nhận HTTP 403 `order_forbidden`)
- `order_id` không phải uuid: HTTP 400 `order_invalid_id`
- Không có đơn hàng mang id đó: HTTP 404 `order_not_found`
- Giá trị status: `pending`, `paid`, `shipped`, `cancelled`
- Mã thành công: HTTP 200
