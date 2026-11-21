## Thông tin chung

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo bài viết.
- Phân quyền: chỉ role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Request | `string` | Có điều kiện (phải có `title` hoặc `content`) | Độ dài tối đa: `TBD-1` |
| `content` | Request | `string` | Có điều kiện (phải có `title` hoặc `content`) | — |
| `status` | Request | `string` | Không | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | `TBD-2` | Có điều kiện (khi `status` là `future`) | Phải sau thời điểm hiện tại |
| `slug` | Request | `string` | Không | — |
| `categories` | Request | Mảng số nguyên | `TBD-3` | Mỗi id phải tồn tại |
| Bài viết đã lưu | Response | `TBD-6` | — | — |

## Endpoint

Request:

```json
{"title":"Tiêu đề"}
```

Phản hồi thành công: HTTP 201.

## Xử lý

Khi thiếu `status`, hệ thống dùng `draft`.

Khi thiếu `slug`, hệ thống tạo slug từ `title`. Khi slug đã tồn tại, hệ thống thêm hậu tố số. Trường hợp thiếu cả `slug` và `title`: `TBD-4`.

Thứ tự xử lý: `TBD-7`.

Ưu tiên lỗi khi nhiều điều kiện cùng xảy ra: `TBD-8`.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `rest_cannot_create` | Người gọi không có role `editor` hoặc `author` |
| 403 | `rest_cannot_publish` | Người gọi có role `author` và gửi `status` là `publish` |
| 400 | `rest_empty_post` | Request thiếu cả `title` và `content` |
| 400 | `rest_invalid_date` | `status` là `future` và `date` không sau thời điểm hiện tại |
| 400 | `rest_invalid_term` | Id trong `categories` không tồn tại |
| `TBD-5` | `TBD-5` | `status` không thuộc danh sách giá trị cho phép |

## Tác động kèm theo

Không có

## Mục còn mở

- `TBD-1`: Độ dài tối đa của `title` là bao nhiêu?
- `TBD-2`: `date` dùng kiểu dữ liệu và định dạng nào?
- `TBD-3`: `categories` có bắt buộc không?
- `TBD-4`: Hệ thống tạo `slug` thế nào khi thiếu cả `slug` và `title`?
- `TBD-5`: Hệ thống trả HTTP status và mã lỗi nào khi `status` không thuộc danh sách cho phép?
- `TBD-6`: Phản hồi thành công gồm những trường nào và có kiểu dữ liệu gì?
- `TBD-7`: Thứ tự xử lý các quy tắc là gì?
- `TBD-8`: Khi nhiều điều kiện lỗi cùng xảy ra, lỗi nào được trả trước?