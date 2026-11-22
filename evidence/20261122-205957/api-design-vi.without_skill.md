# Đặc tả API tạo bài viết

## Tổng quan

| Thuộc tính | Giá trị |
|---|---|
| Phương thức | `POST` |
| Endpoint | `/wp/v2/posts` |
| Chức năng | Tạo bài viết |
| Thành công | HTTP `201`; trả về bài viết đã lưu |

Tên endpoint và trường được nêu dưới đây dựa trên tài liệu WordPress REST API về “Create a Post”. Các quy tắc nghiệp vụ và mã lỗi trong đặc tả này là quy tắc giả lập.

## Quyền truy cập

Chỉ người dùng có role `editor` hoặc `author` được tạo bài viết.

| Trường hợp | HTTP | Mã lỗi |
|---|---:|---|
| Role không phải `editor` hoặc `author` | `403` | `rest_cannot_create` |
| Role `author` gửi bài viết có `status: publish` | `403` | `rest_cannot_publish` |

Chỉ role `editor` được đặt trạng thái `publish`.

## Trường yêu cầu

| Trường | Mô tả | Quy tắc |
|---|---|---|
| `title` | Tiêu đề bài viết | Độ dài tối đa: **TBD**. Phải có `title` hoặc `content`. |
| `content` | Nội dung bài viết | Phải có `title` hoặc `content`. |
| `status` | Trạng thái xuất bản | Giá trị cho phép: `publish`, `future`, `draft`, `pending`, `private`. Mặc định: `draft`. Chỉ `editor` được dùng `publish`. |
| `date` | Ngày của bài viết | Khi `status` là `future`, ngày phải sau thời điểm hiện tại. |
| `slug` | Phần URL duy nhất của bài viết | Nếu không gửi, hệ thống tạo từ `title`. Nếu slug đã tồn tại, hệ thống thêm hậu tố số. |
| `categories` | Danh sách ID danh mục | Mỗi ID phải tồn tại; ID không tồn tại làm yêu cầu thất bại. |

Đặc tả này không quy định trường nào là bắt buộc ngoài quy tắc cần có ít nhất một trong `title` hoặc `content`.

## Quy tắc xử lý

1. Kiểm tra role của người gửi.
2. Yêu cầu phải có `title` hoặc `content`.
3. Nếu có `status`, giá trị phải thuộc danh sách cho phép; nếu không có, dùng `draft`.
4. Nếu `status` là `publish`, chỉ role `editor` được phép tạo.
5. Nếu `status` là `future`, `date` phải ở tương lai.
6. Kiểm tra các ID trong `categories`. ID không tồn tại làm yêu cầu thất bại.
7. Nếu thiếu `slug`, tạo slug từ `title`. Nếu slug đã tồn tại, thêm hậu tố số.
8. Khi tạo thành công, trả HTTP `201` cùng bài viết đã lưu.

## Mã lỗi

| HTTP | Mã lỗi | Điều kiện |
|---:|---|---|
| `400` | `rest_empty_post` | Thiếu cả `title` và `content`. |
| `400` | `rest_invalid_date` | `status` là `future` nhưng `date` không ở tương lai. |
| `400` | `rest_invalid_term` | Có ID danh mục không tồn tại. |
| `403` | `rest_cannot_create` | Người gửi không có role `editor` hoặc `author`. |
| `403` | `rest_cannot_publish` | Role `author` gửi `status: publish`. |

## Điểm cần xác định thêm

- Độ dài tối đa của `title`: **TBD**.
- Định dạng cụ thể của `date` chưa được quy định trong đặc tả này.
- Cấu trúc chi tiết của request và response, cũng như cấu trúc body lỗi, chưa được nêu.