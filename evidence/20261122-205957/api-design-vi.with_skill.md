## Thông tin chung

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo một bài viết.
- Phân quyền: role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Yêu cầu | `string` | Có điều kiện (`title` hoặc `content`) | Độ dài tối đa: `TBD-3` |
| `content` | Yêu cầu | `string` | Có điều kiện (`title` hoặc `content`) | — |
| `status` | Yêu cầu | `enum` | Không | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Yêu cầu | `TBD-4` | Có điều kiện (`status` là `future`) | Phải sau thời điểm hiện tại khi `status` là `future` |
| `slug` | Yêu cầu | `string` | Không | — |
| `categories` | Yêu cầu | Mảng số nguyên | `TBD-5` | Mỗi id phải trỏ đến danh mục tồn tại |
| Bài viết đã lưu | Phản hồi | `TBD-8` | — | — |

## Endpoint

Yêu cầu:

```json
{"title": "Tiêu đề bài viết"}
```

Phản hồi thành công: HTTP 201.

## Xử lý

- Khi request không gửi `status`, hệ thống dùng `draft`.
- Khi request thiếu `slug`, hệ thống tạo `slug` từ `title`. Khi slug đã tồn tại, hệ thống thêm hậu tố số.
- Khi request thiếu cả `slug` và `title`: `TBD-7`.
- Thứ tự xử lý: `TBD-1`.
- Khi nhiều điều kiện lỗi cùng lúc, lỗi nào được trả trước: `TBD-2`.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `rest_cannot_create` | Người gọi có role khác `editor` hoặc `author` |
| 403 | `rest_cannot_publish` | Người gọi có role `author` và gửi `status` là `publish` |
| 400 | `rest_empty_post` | Request thiếu cả `title` và `content` |
| `TBD-6` | `TBD-6` | `status` không thuộc danh sách giá trị cho phép |
| 400 | `rest_invalid_date` | `status` là `future`, nhưng `date` thiếu hoặc không sau thời điểm hiện tại |
| 400 | `rest_invalid_term` | Id trong `categories` không tồn tại |

## Tác động kèm theo

—

## Mục còn mở

- `TBD-1`: Thứ tự xử lý các bước là gì?
- `TBD-2`: Khi nhiều điều kiện lỗi cùng lúc, lỗi nào được trả trước?
- `TBD-3`: Độ dài tối đa của `title` là bao nhiêu và tính theo đơn vị nào?
- `TBD-4`: Kiểu dữ liệu của `date` là gì?
- `TBD-5`: `categories` là trường bắt buộc không?
- `TBD-6`: Khi `status` không thuộc danh sách cho phép, API trả HTTP status và mã lỗi nào?
- `TBD-7`: Khi request thiếu cả `slug` và `title`, hệ thống tạo `slug` như thế nào?
- `TBD-8`: Phản hồi bài viết đã lưu gồm những trường nào và kiểu dữ liệu của từng trường là gì?