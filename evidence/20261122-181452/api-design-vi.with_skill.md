## Thông tin chung

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo một bài viết.
- Phân quyền: role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Yêu cầu | string | Có điều kiện (`content` không có) | Độ dài tối đa: `TBD-1` |
| `content` | Yêu cầu | string | Có điều kiện (`title` không có) | — |
| `status` | Yêu cầu | string | Không | `publish`, `future`, `draft`, `pending`, `private` |
| `slug` | Yêu cầu | string | Không | — |
| `date` | Yêu cầu | `TBD-2` | Có điều kiện (`status` là `future`) | Phải ở tương lai |
| `categories` | Yêu cầu | mảng số nguyên | `TBD-3` | Mỗi id phải tồn tại |
| Bài viết đã lưu | Phản hồi | `TBD-4` | — | — |

## Endpoint

Yêu cầu:

```json
{"title":"Bài viết mẫu"}
```

Phản hồi thành công: HTTP 201.

## Xử lý

- Mặc định `status` là `draft`.
- Khi thiếu `slug`, hệ thống tạo slug từ `title`. Quy tắc chuyển `title` thành slug: `TBD-5`.
- Khi slug đã tồn tại, hệ thống thêm hậu tố số. Cách tạo hậu tố: `TBD-6`.
- Thứ tự xử lý: `TBD-7`.
- Ưu tiên lỗi khi nhiều điều kiện cùng thất bại: `TBD-8`.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `rest_cannot_create` | Người gọi không có role `editor` hoặc `author` |
| 403 | `rest_cannot_publish` | Người gọi có role `author` và gửi `status` là `publish` |
| 400 | `rest_empty_post` | Yêu cầu thiếu cả `title` và `content` |
| 400 | `rest_invalid_date` | `status` là `future` và `date` không ở tương lai |
| 400 | `rest_invalid_term` | Id trong `categories` không tồn tại |
| `TBD-9` | `TBD-9` | `status` không thuộc danh sách giá trị cho phép |

## Tác động kèm theo

Không có

## Mục còn mở

- `TBD-1`: Độ dài tối đa của `title` là bao nhiêu?
- `TBD-2`: Kiểu dữ liệu của `date` là gì?
- `TBD-3`: `categories` có bắt buộc không?
- `TBD-4`: Phản hồi gồm những trường nào và kiểu dữ liệu của từng trường là gì?
- `TBD-5`: Hệ thống chuyển `title` thành `slug` theo quy tắc nào?
- `TBD-6`: Hậu tố số được tạo theo quy tắc nào khi slug đã tồn tại?
- `TBD-7`: Thứ tự xử lý các quy tắc là gì?
- `TBD-8`: Khi nhiều điều kiện lỗi cùng lúc, lỗi nào được ưu tiên?
- `TBD-9`: HTTP status và mã lỗi nào được trả về khi `status` không hợp lệ?

---

Đã soạn tài liệu theo mẫu API. Các điểm chưa được quyết định trong brief được đánh dấu `TBD`; tôi không tự đặt giá trị cho chúng.