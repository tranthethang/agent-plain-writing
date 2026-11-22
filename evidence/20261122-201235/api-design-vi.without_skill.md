# Thiết kế API tạo bài viết

## Tổng quan

| Thuộc tính | Giá trị |
|---|---|
| Phương thức | `POST` |
| Endpoint | `/wp/v2/posts` |
| Chức năng | Tạo bài viết |

## Quyền truy cập

Chỉ người dùng có role `editor` hoặc `author` được tạo bài viết. Role khác nhận:

- HTTP `403`
- Mã lỗi: `rest_cannot_create`

## Dữ liệu đầu vào

| Trường | Ý nghĩa | Quy tắc |
|---|---|---|
| `title` | Tiêu đề bài viết | Có thể thiếu nếu có `content`. Độ dài tối đa: **TBD**. |
| `content` | Nội dung bài viết | Có thể thiếu nếu có `title`. |
| `status` | Trạng thái xuất bản | Giá trị cho phép: `publish`, `future`, `draft`, `pending`, `private`. Mặc định: `draft`. |
| `date` | Thời điểm của bài viết | Phải ở tương lai khi `status` là `future`. |
| `slug` | Phần URL của bài viết | Nếu thiếu, hệ thống tạo từ `title`. Nếu slug đã tồn tại, hệ thống thêm hậu tố số. |
| `categories` | Danh sách ID danh mục | Mỗi ID là số nguyên và phải tồn tại. |

## Quy tắc xử lý

1. Nếu thiếu cả `title` và `content`, trả HTTP `400` với mã `rest_empty_post`.
2. Nếu `status` là `publish`, chỉ role `editor` được phép đặt trạng thái này. Role `author` nhận HTTP `403` với mã `rest_cannot_publish`.
3. Nếu `status` là `future`, `date` phải sau thời điểm hiện tại. Nếu không, trả HTTP `400` với mã `rest_invalid_date`.
4. Nếu một ID trong `categories` không tồn tại, trả HTTP `400` với mã `rest_invalid_term`.
5. Khi tạo thành công, trả HTTP `201` cùng bài viết đã lưu.

## Mã phản hồi

| HTTP | Mã lỗi | Điều kiện |
|---|---|---|
| `201` | — | Tạo bài viết thành công; trả về bài viết đã lưu. |
| `400` | `rest_empty_post` | Thiếu cả `title` và `content`. |
| `400` | `rest_invalid_date` | `status` là `future` nhưng `date` không ở tương lai. |
| `400` | `rest_invalid_term` | Có ID danh mục không tồn tại. |
| `403` | `rest_cannot_create` | Role không phải `editor` hoặc `author`. |
| `403` | `rest_cannot_publish` | Role `author` gửi `status: publish`. |

## Điểm chưa được quy định

- Độ dài tối đa của `title`: **TBD**.
- Cấu trúc chi tiết của đối tượng bài viết trong phản hồi và định dạng body lỗi chưa được quy định.
- Định dạng của `date` và mã lỗi cho `status` không thuộc danh sách cho phép chưa được quy định.