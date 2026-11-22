## Thông tin chung

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo bài viết.
- Phân quyền: role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Yêu cầu | string | Có điều kiện (khi `content` vắng mặt) | Tối đa `TBD-1` |
| `content` | Yêu cầu | string | Có điều kiện (khi `title` vắng mặt) | — |
| `status` | Yêu cầu | string | Không | `publish`, `future`, `draft`, `pending`, `private` |
| `slug` | Yêu cầu | string | Không | — |
| `categories` | Yêu cầu | array<integer> | `TBD-3` | Mỗi id phải tồn tại |
| `date` | Yêu cầu | `TBD-4` | Có điều kiện (khi `status` là `future`) | Phải sau thời điểm hiện tại |
| Bài viết đã lưu | Phản hồi | `TBD-2` | — | — |

## Endpoint

Yêu cầu:

```json
{"title": "Tiêu đề bài viết"}
```

Phản hồi thành công có status `201`. Không có ví dụ phản hồi vì chưa có trường phản hồi với kiểu đã biết.

## Xử lý

- Khi thiếu `slug`, hệ thống tạo `slug` từ `title`. Khi `slug` đã tồn tại, hệ thống thêm hậu tố số.
- Khi thiếu `status`, hệ thống dùng `draft`.
- Thứ tự xử lý: `TBD-7`.
- Khi nhiều lỗi cùng xảy ra, lỗi ưu tiên: `TBD-8`.

## Lỗi

| Điều kiện | HTTP | Mã |
|---|---:|---|
| Người gọi có role khác `editor` hoặc `author` | 403 | `rest_cannot_create` |
| Thiếu cả `title` và `content` | 400 | `rest_empty_post` |
| Role `author` gửi `status` là `publish` | 403 | `rest_cannot_publish` |
| `status` không thuộc danh sách giá trị cho phép | `TBD-5` | `TBD-5` |
| `status` là `future` và `date` không ở tương lai | 400 | `rest_invalid_date` |
| Một id trong `categories` không tồn tại | 400 | `rest_invalid_term` |
| Độ dài `title` vượt giới hạn | `TBD-6` | `TBD-6` |

## Tác động kèm theo

Không có

## Mục còn mở

- `TBD-1`: Độ dài tối đa của `title` là bao nhiêu?
- `TBD-2`: Phản hồi gồm những trường nào và kiểu của từng trường là gì?
- `TBD-3`: `categories` có bắt buộc không?
- `TBD-4`: Kiểu dữ liệu của `date` là gì?
- `TBD-5`: API trả HTTP và mã lỗi nào khi `status` không thuộc danh sách cho phép?
- `TBD-6`: API trả HTTP và mã lỗi nào khi `title` vượt độ dài tối đa?
- `TBD-7`: Thứ tự xử lý các quy tắc là gì?
- `TBD-8`: Khi nhiều lỗi cùng xảy ra, lỗi nào được ưu tiên?