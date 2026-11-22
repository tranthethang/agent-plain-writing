# API đọc đơn hàng

## Endpoint

`GET /v1/orders/{order_id}`

Đọc thông tin của một đơn hàng theo ID.

## Quyền truy cập

Chỉ vai trò `owner` và `support` được phép đọc đơn hàng. Vai trò khác nhận:

- HTTP `403`
- Mã lỗi: `order_forbidden`

## Tham số đường dẫn

| Tên | Ý nghĩa | Quy tắc |
|---|---|---|
| `order_id` | ID của đơn hàng | Phải là UUID |

## Phản hồi thành công

Khi tìm thấy đơn hàng, API trả HTTP `200` cùng đơn hàng. Phản hồi có các trường:

| Trường | Ý nghĩa | Giá trị |
|---|---|---|
| `order_id` | ID của đơn hàng | UUID |
| `status` | Trạng thái của đơn hàng | `pending`, `paid`, `shipped` hoặc `cancelled` |

Brief không quy định định dạng JSON cụ thể ngoài các trường trên.

## Phản hồi lỗi

| Trường hợp | HTTP | Mã lỗi |
|---|---:|---|
| Vai trò không được phép | `403` | `order_forbidden` |
| `order_id` không phải UUID | `400` | `order_invalid_id` |
| Không có đơn hàng mang ID đó | `404` | `order_not_found` |

Brief không quy định cấu trúc nội dung phản hồi lỗi hoặc thứ tự ưu tiên xử lý khi có nhiều điều kiện lỗi cùng lúc.

## Lưu ý về thời gian phản hồi

Yêu cầu nêu API cần “trả lời nhanh” nhưng không cung cấp thời hạn cụ thể. Cần xác định mục tiêu thời gian phản hồi nếu cần đưa vào tiêu chí triển khai hoặc kiểm thử.