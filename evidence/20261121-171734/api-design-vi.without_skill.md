# Thiết kế API: Tạo bài viết

Các quy tắc nghiệp vụ và mã lỗi trong tài liệu này là quy tắc giả lập. Tên endpoint, tên trường và các giá trị `status` được lấy từ tài liệu WordPress REST API về posts.

## Endpoint

```http
POST /wp/v2/posts
```

## Quyền truy cập

Chỉ role `editor` và `author` được tạo bài viết. Role khác nhận:

- HTTP `403`
- Mã lỗi: `rest_cannot_create`

Chỉ role `editor` được tạo bài viết với `status: publish`. Nếu `author` gửi trạng thái này, API trả HTTP `403` với mã lỗi `rest_cannot_publish`.

## Request

Request có thể chứa các trường sau:

| Trường | Ý nghĩa | Quy tắc |
|---|---|---|
| `title` | Tiêu đề bài viết | Phải có `title` hoặc `content`. Độ dài tối đa: **TBD**. |
| `content` | Nội dung bài viết | Phải có `title` hoặc `content`. |
| `status` | Trạng thái bài viết | Một trong `publish`, `future`, `draft`, `pending`, `private`. Mặc định là `draft`. |
| `date` | Ngày của bài viết | Khi `status` là `future`, ngày phải sau thời điểm hiện tại. |
| `slug` | Phần URL duy nhất của bài viết | Nếu thiếu, hệ thống tạo từ `title`. Nếu slug đã tồn tại, hệ thống thêm hậu tố số. |
| `categories` | Danh sách ID danh mục | Mỗi ID là số nguyên và phải tồn tại. |

### Kiểm tra dữ liệu

- Nếu thiếu cả `title` và `content`, trả HTTP `400` với mã `rest_empty_post`.
- Nếu `status` là `future` nhưng `date` không ở tương lai, trả HTTP `400` với mã `rest_invalid_date`.
- Nếu một ID trong `categories` không tồn tại, trả HTTP `400` với mã `rest_invalid_term`.

## Phản hồi

### Thành công

Khi tạo bài viết thành công:

- HTTP `201`
- Trả về bài viết đã lưu.

Cấu trúc chi tiết của đối tượng phản hồi chưa được quy định trong brief.

## Mã lỗi

| HTTP | Mã lỗi | Điều kiện |
|---|---|---|
| `400` | `rest_empty_post` | Thiếu cả `title` và `content`. |
| `400` | `rest_invalid_date` | `status` là `future` nhưng `date` không ở tương lai. |
| `400` | `rest_invalid_term` | Có ID danh mục không tồn tại. |
| `403` | `rest_cannot_create` | Role không phải `editor` hoặc `author`. |
| `403` | `rest_cannot_publish` | `author` gửi `status: publish`. |

## Nội dung chưa được quy định

- Độ dài tối đa của `title`: **TBD**.
- Định dạng của `date`, cấu trúc chi tiết của phản hồi thành công và cơ chế xác thực không được quy định trong brief.