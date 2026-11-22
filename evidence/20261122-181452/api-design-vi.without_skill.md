# Đặc tả API tạo bài viết

## Tổng quan

| Thuộc tính | Giá trị |
|---|---|
| Phương thức | `POST` |
| Endpoint | `/wp/v2/posts` |
| Thành công | HTTP `201`; trả về bài viết đã lưu |

## Quyền truy cập

Chỉ người dùng có role `editor` hoặc `author` được tạo bài viết. Role khác nhận HTTP `403` với mã `rest_cannot_create`.

Chỉ role `editor` được tạo bài viết với `status: "publish"`. Nếu `author` gửi trạng thái này, API trả HTTP `403` với mã `rest_cannot_publish`.

## Request

Các trường được mô tả trong đặc tả:

| Trường | Ý nghĩa | Quy tắc |
|---|---|---|
| `title` | Tiêu đề bài viết | Độ dài tối đa: **TBD** |
| `content` | Nội dung bài viết | Có thể gửi cùng `title` hoặc gửi một mình |
| `status` | Trạng thái xuất bản | Nhận một trong `publish`, `future`, `draft`, `pending`, `private`; mặc định là `draft` |
| `date` | Thời điểm dùng cho bài viết `future` | Khi `status` là `future`, ngày phải sau thời điểm hiện tại |
| `slug` | Phần URL duy nhất của bài viết | Nếu thiếu, hệ thống tạo từ `title`; nếu slug đã tồn tại, hệ thống thêm hậu tố số |
| `categories` | Danh sách ID danh mục | Mỗi ID phải tồn tại; ID không tồn tại làm request thất bại |

Phải có ít nhất một trong hai trường `title` hoặc `content`. Nếu thiếu cả hai, API trả HTTP `400` với mã `rest_empty_post`.

## Lỗi

| Điều kiện | HTTP | Mã lỗi |
|---|---:|---|
| Role không được phép tạo bài viết | `403` | `rest_cannot_create` |
| `author` gửi `status: "publish"` | `403` | `rest_cannot_publish` |
| Thiếu cả `title` và `content` | `400` | `rest_empty_post` |
| `status` là `future` nhưng `date` không ở tương lai | `400` | `rest_invalid_date` |
| Có ID danh mục không tồn tại | `400` | `rest_invalid_term` |

Định dạng response lỗi không được quy định trong brief.

## Hành vi khi thành công

Khi request hợp lệ, API trả HTTP `201` và bài viết đã lưu. Cấu trúc chi tiết của response không được quy định trong brief.

## Gợi ý kiểm thử QA

- Tạo bài viết với role `editor` và `author`; xác nhận các role khác nhận `403 rest_cannot_create`.
- Gửi request chỉ có `title`, chỉ có `content`, và request thiếu cả hai; trường hợp cuối phải nhận `400 rest_empty_post`.
- Kiểm tra mặc định `status` là `draft` và các giá trị status được chấp nhận.
- Xác nhận `editor` có thể đặt `publish`, còn `author` nhận `403 rest_cannot_publish`.
- Với `status: "future"`, kiểm tra ngày tương lai được chấp nhận và ngày không ở tương lai nhận `400 rest_invalid_date`.
- Kiểm tra slug được tạo khi thiếu và được thêm hậu tố số khi trùng.
- Kiểm tra ID danh mục không tồn tại nhận `400 rest_invalid_term`.
- Xác nhận request hợp lệ trả `201` và bài viết đã lưu.

## Điểm chưa được quy định

Brief không nêu định dạng của `date`, cấu trúc request/response đầy đủ, định dạng response lỗi, quy tắc xử lý khi thiếu `title` nhưng cần tạo `slug`, hoặc cách đánh số hậu tố khi slug trùng. Độ dài tối đa của `title` là **TBD**.