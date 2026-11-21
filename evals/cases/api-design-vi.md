---
lang: vi
type: api-design
non_tech: false
---

# SIMULATED DATA

Endpoint và tên trường lấy từ tài liệu công khai WordPress REST API về posts ("Create a Post"). Quy tắc nghiệp vụ và mã lỗi được bịa cho bài eval này.

## Audience

Lập trình viên backend và QA triển khai, kiểm thử một API blog.

## Brief

### Idea
Thiết kế `POST /wp/v2/posts` để tạo một bài viết. Nguồn: tài liệu WordPress REST API về posts, endpoint "Create a Post". Các quy tắc dưới đây là giả lập, trừ tên trường và giá trị cho phép.

### Business rules
- Chỉ role `editor` và `author` được tạo bài viết. Role khác nhận HTTP 403 (`rest_cannot_create`).
- Phải có `title` hoặc `content`. Nếu thiếu cả hai, API trả HTTP 400 (`rest_empty_post`).
- `status` là một trong `publish`, `future`, `draft`, `pending`, `private`. Mặc định là `draft`.
- Chỉ `editor` được đặt `status` là `publish`. `author` gửi `publish` nhận HTTP 403 (`rest_cannot_publish`).
- Khi `status` là `future`, `date` phải sau thời điểm hiện tại. Nếu không, API trả HTTP 400 (`rest_invalid_date`).
- Khi thiếu `slug`, hệ thống tạo từ `title`. Khi slug đã tồn tại, hệ thống thêm hậu tố số.
- Mỗi id trong `categories` phải tồn tại. Id không có trả HTTP 400 (`rest_invalid_term`).
- Khi thành công, API trả HTTP 201 và bài viết đã lưu.
- Nguồn không nêu độ dài tối đa của `title`. Ghi `TBD`.

### Glossary
- `title`: tiêu đề bài viết.
- `content`: nội dung bài viết.
- `status`: trạng thái xuất bản của bài viết.
- `slug`: phần URL duy nhất của bài viết.
- `categories`: danh sách id danh mục (số nguyên).

## Facts
- Endpoint: `POST /wp/v2/posts`
- Role được phép: `editor`, `author` (role khác nhận HTTP 403 `rest_cannot_create`)
- Giá trị status: `publish`, `future`, `draft`, `pending`, `private`; mặc định `draft`
- Chỉ `editor` được publish (nếu không, HTTP 403 `rest_cannot_publish`)
- Thiếu cả `title` và `content`: HTTP 400 `rest_empty_post`
- `future` cần `date` ở tương lai (nếu không, HTTP 400 `rest_invalid_date`)
- Id danh mục không có: HTTP 400 `rest_invalid_term`
- Mã thành công: HTTP 201
