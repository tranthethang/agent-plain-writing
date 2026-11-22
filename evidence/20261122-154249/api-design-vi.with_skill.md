## Thông tin chung

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo bài viết.
- Bên gọi: TBD-8.
- Phân quyền: role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Request | string | Có điều kiện (ít nhất một trong `title` hoặc `content`) | Độ dài tối đa: TBD-1 |
| `content` | Request | string | Có điều kiện (ít nhất một trong `title` hoặc `content`) | — |
| `status` | Request | enum string | Không | `publish`, `future`, `draft`, `pending`, `private` |
| `slug` | Request | string | Không | — |
| `date` | Request | TBD-7 | Có điều kiện (khi `status` là `future`) | Phải sau thời điểm hiện tại khi `status` là `future` |
| `categories` | Request | array<integer> | TBD-5 | Mỗi id phải tồn tại |
| Bài viết đã lưu | Response | TBD-2 | — | — |

## Endpoint

Request:

```json
{"title":"Bài viết"}
```

Mã thành công: `201`

## Xử lý

- Hệ thống đặt `status` mặc định là `draft`.
- Khi thiếu `slug`, hệ thống tạo slug từ `title`. Khi slug đã tồn tại, hệ thống thêm hậu tố số. Khi thiếu cả `slug` và `title`: TBD-6.
- Thứ tự xử lý và ưu tiên lỗi khi nhiều điều kiện cùng xảy ra: TBD-4.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `rest_cannot_create` | Người gọi có role khác `editor` và `author` |
| 403 | `rest_cannot_publish` | Người gọi có role `author` và gửi `status` là `publish` |
| 400 | `rest_empty_post` | Request thiếu cả `title` và `content` |
| 400 | `rest_invalid_date` | `status` là `future` và `date` không ở tương lai |
| 400 | `rest_invalid_term` | Một id trong `categories` không tồn tại |
| TBD-3 | TBD-3 | `status` không thuộc danh sách giá trị cho phép |

## Tác động kèm theo

Không có

## Mục còn mở

- TBD-1: Độ dài tối đa của `title` là bao nhiêu?
- TBD-2: Response bài viết đã lưu gồm những trường nào và có cấu trúc ra sao?
- TBD-3: HTTP status và mã lỗi nào áp dụng khi `status` không thuộc danh sách cho phép?
- TBD-4: Thứ tự xử lý là gì, và lỗi nào được ưu tiên khi nhiều điều kiện cùng xảy ra?
- TBD-5: `categories` có bắt buộc không?
- TBD-6: Hệ thống xử lý thế nào khi thiếu `slug` và `title`?
- TBD-7: Kiểu và định dạng của `date` là gì?
- TBD-8: Bên gọi API là ứng dụng hoặc thành phần nào?

---

Đã soạn đặc tả theo các quy tắc trong brief. Tôi ghi “Không có” ở mục tác động kèm theo vì brief không nêu tác động nào ngoài việc tạo và lưu bài viết.