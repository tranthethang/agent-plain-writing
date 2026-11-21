## Danh tính

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo bài viết.
- Phân quyền: role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `title` | `TBD-2` | Có điều kiện (khi thiếu `content`) | Tối đa `TBD-1` |
| `content` | `TBD-3` | Có điều kiện (khi thiếu `title`) | — |
| `status` | `TBD-4` | Không | Một trong `publish`, `future`, `draft`, `pending`, `private`; mặc định là `draft` |
| `date` | `TBD-5` | Có điều kiện (khi `status` là `future`) | Phải sau thời điểm hiện tại |
| `slug` | `TBD-6` | Không | Khi thiếu, hệ thống tạo từ `title`. Nếu slug đã tồn tại, hệ thống thêm hậu tố số. |
| `categories` | `array<integer>` | `TBD-7` | Mỗi id phải tồn tại |
| Trường trả về | `TBD-9` | `TBD-9` | `TBD-9` |

## Endpoint

Request:

```json
{"categories": []}
```

Mã thành công: `201`. API trả bài viết đã lưu.

## Xử lý

Thứ tự thực hiện và ưu tiên lỗi: `TBD-10`.

- Hệ thống kiểm tra quyền tạo bài viết. Nếu không đạt, dừng với `rest_cannot_create`.
- Hệ thống kiểm tra quyền đặt `status` là `publish`. Nếu không đạt, dừng với `rest_cannot_publish`.
- Khi thiếu cả `title` và `content`, hệ thống dừng với `rest_empty_post`.
- Khi `status` không nằm trong danh sách cho phép, hệ thống dừng với mã `TBD-8`.
- Khi `status` là `future` và `date` thiếu hoặc không sau thời điểm hiện tại, hệ thống dừng với `rest_invalid_date`.
- Với mỗi id trong `categories`, hệ thống kiểm tra id đó tồn tại. Nếu không, hệ thống dừng với `rest_invalid_term`.
- Khi thiếu `slug`, hệ thống tạo slug từ `title`. Khi slug đã tồn tại, hệ thống thêm hậu tố số.
- Khi không có `status`, hệ thống dùng `draft`.
- Khi các kiểm tra thành công, hệ thống lưu bài viết và trả bài viết đó.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `rest_cannot_create` | Người gọi không có role được phép tạo bài viết |
| 403 | `rest_cannot_publish` | Người gọi không được phép đặt `status` là `publish` |
| 400 | `rest_empty_post` | Thiếu cả `title` và `content` |
| `TBD-8` | `TBD-8` | `status` không nằm trong danh sách cho phép |
| 400 | `rest_invalid_date` | `status` là `future`, nhưng `date` thiếu hoặc không sau thời điểm hiện tại |
| 400 | `rest_invalid_term` | Có id trong `categories` không tồn tại |

## Tác dụng phụ

Không có tác dụng phụ nào khác được nêu.

## Mục còn mở

- `TBD-1`: Độ dài tối đa của `title` là bao nhiêu?
- `TBD-2`: Kiểu của `title` là gì?
- `TBD-3`: Kiểu của `content` là gì?
- `TBD-4`: Kiểu của `status` là gì?
- `TBD-5`: Kiểu của `date` là gì?
- `TBD-6`: Kiểu của `slug` là gì?
- `TBD-7`: `categories` có bắt buộc không?
- `TBD-8`: HTTP status và mã lỗi nào áp dụng khi `status` không nằm trong danh sách cho phép?
- `TBD-9`: API trả về những trường nào, với kiểu và trạng thái bắt buộc nào?
- `TBD-10`: Thứ tự thực hiện các bước và ưu tiên lỗi là gì?