# Đặc tả API tạo bài viết

## 1. Tổng quan

| Thuộc tính | Giá trị |
|---|---|
| Phương thức | `POST` |
| Endpoint | `/wp/v2/posts` |
| Mục đích | Tạo một bài viết |
| Thành công | HTTP `201`; trả về bài viết đã lưu |

## 2. Quyền truy cập

Chỉ các role `editor` và `author` được tạo bài viết.

| Điều kiện | Kết quả |
|---|---|
| Role không phải `editor` hoặc `author` | HTTP `403`, mã lỗi `rest_cannot_create` |
| Role `author` gửi `status: publish` | HTTP `403`, mã lỗi `rest_cannot_publish` |
| Role `editor` gửi `status: publish` | Được phép |

## 3. Trường dữ liệu

| Trường | Mô tả | Quy tắc |
|---|---|---|
| `title` | Tiêu đề bài viết | Độ dài tối đa: **TBD** |
| `content` | Nội dung bài viết | Phải có ít nhất một trong hai trường `title` hoặc `content` |
| `status` | Trạng thái xuất bản | Giá trị: `publish`, `future`, `draft`, `pending`, `private`. Mặc định: `draft` |
| `date` | Thời điểm của bài viết | Khi `status` là `future`, ngày phải ở tương lai |
| `slug` | Phần URL duy nhất của bài viết | Nếu không gửi, hệ thống tạo từ `title`. Nếu slug đã tồn tại, hệ thống thêm hậu tố số |
| `categories` | Danh sách ID danh mục | Các ID là số nguyên; mọi ID phải tồn tại |

### Quy tắc về `title` và `content`

Nếu thiếu cả `title` và `content`, API trả về HTTP `400` với mã lỗi `rest_empty_post`.

### Quy tắc về `status` và `date`

- Nếu không gửi `status`, giá trị mặc định là `draft`.
- Chỉ `editor` được tạo bài viết với `status: publish`.
- Nếu `status` là `future`, `date` phải sau thời điểm hiện tại. Nếu không, API trả về HTTP `400` với mã lỗi `rest_invalid_date`.

### Quy tắc về danh mục

Nếu một ID trong `categories` không tồn tại, API trả về HTTP `400` với mã lỗi `rest_invalid_term`.

## 4. Mã phản hồi

| HTTP | Mã lỗi | Điều kiện |
|---|---|---|
| `201` | — | Tạo thành công; trả về bài viết đã lưu |
| `400` | `rest_empty_post` | Thiếu cả `title` và `content` |
| `400` | `rest_invalid_date` | `status` là `future` nhưng `date` không ở tương lai |
| `400` | `rest_invalid_term` | Có ID danh mục không tồn tại |
| `403` | `rest_cannot_create` | Role không phải `editor` hoặc `author` |
| `403` | `rest_cannot_publish` | Role `author` gửi `status: publish` |

## 5. Ví dụ request

```http
POST /wp/v2/posts
```

```json
{
  "title": "Tiêu đề bài viết",
  "status": "draft"
}
```

## 6. Trường hợp kiểm thử QA

| Tình huống | Kết quả mong đợi |
|---|---|
| Tạo bài với role `editor` hoặc `author`, có `title` hoặc `content` | HTTP `201`; bài viết được lưu |
| Tạo bài với role không được phép | HTTP `403`, `rest_cannot_create` |
| Gửi cả `title` và `content` đều thiếu | HTTP `400`, `rest_empty_post` |
| Không gửi `status` | Bài viết dùng trạng thái `draft` |
| Role `author` gửi `status: publish` | HTTP `403`, `rest_cannot_publish` |
| Gửi `status: future` với `date` không ở tương lai | HTTP `400`, `rest_invalid_date` |
| Gửi ID danh mục không tồn tại | HTTP `400`, `rest_invalid_term` |
| Không gửi `slug` | Hệ thống tạo slug từ `title` |
| Slug đã tồn tại | Hệ thống thêm hậu tố số |

## 7. Điểm chưa được quy định

- Độ dài tối đa của `title`: **TBD**.
- Định dạng của `date`, cấu trúc body lỗi và schema chi tiết của bài viết trả về chưa được quy định.
- Thứ tự ưu tiên xử lý khi request đồng thời vi phạm nhiều quy tắc chưa được quy định.