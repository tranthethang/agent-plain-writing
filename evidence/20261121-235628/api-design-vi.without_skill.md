# Thiết kế API tạo bài viết

## Tổng quan

- **Endpoint:** `POST /wp/v2/posts`
- **Mục đích:** Tạo một bài viết.
- **Role được phép:** `editor`, `author`
- **Thành công:** HTTP `201`, trả về bài viết đã lưu.

Các quy tắc nghiệp vụ và mã lỗi dưới đây là quy tắc giả lập cho thiết kế này. Tên trường và các giá trị `status` được lấy từ tài liệu WordPress REST API về posts.

## Trường đầu vào

| Trường | Ý nghĩa | Quy tắc |
|---|---|---|
| `title` | Tiêu đề bài viết | Phải có `title` hoặc `content`. Độ dài tối đa: **TBD**. |
| `content` | Nội dung bài viết | Phải có `title` hoặc `content`. |
| `status` | Trạng thái xuất bản | Nhận một trong các giá trị `publish`, `future`, `draft`, `pending`, `private`. Mặc định là `draft`. Chỉ `editor` được đặt thành `publish`. |
| `slug` | Phần URL duy nhất của bài viết | Nếu không gửi, hệ thống tạo slug từ `title`. Nếu slug đã tồn tại, hệ thống thêm hậu tố số. |
| `date` | Thời điểm của bài viết | Khi `status` là `future`, giá trị phải ở tương lai. Định dạng cụ thể không được nêu trong tài liệu này. |
| `categories` | Danh sách ID danh mục, dạng số nguyên | Mỗi ID phải tồn tại. ID không tồn tại làm yêu cầu thất bại. |

Không có quy tắc nào được nêu về việc các trường ngoài những điều kiện trên là bắt buộc hay không.

## Quy tắc xử lý

1. Chỉ role `editor` và `author` được tạo bài viết.
2. Yêu cầu phải có ít nhất một trong hai trường `title` hoặc `content`.
3. Nếu `status` không được gửi, dùng `draft`.
4. Nếu `status` là `publish`, chỉ role `editor` được phép tạo bài viết.
5. Nếu `status` là `future`, `date` phải ở tương lai.
6. Nếu thiếu `slug`, tạo slug từ `title`; nếu slug đã tồn tại, thêm hậu tố số.
7. Mọi ID trong `categories` phải tương ứng với danh mục tồn tại.
8. Khi tạo thành công, trả HTTP `201` cùng bài viết đã lưu.

## Lỗi

| Điều kiện | HTTP | Mã lỗi |
|---|---:|---|
| Role không phải `editor` hoặc `author` | `403` | `rest_cannot_create` |
| Thiếu cả `title` và `content` | `400` | `rest_empty_post` |
| Role `author` gửi `status: publish` | `403` | `rest_cannot_publish` |
| `status` là `future` nhưng `date` không ở tương lai | `400` | `rest_invalid_date` |
| Có ID danh mục không tồn tại trong `categories` | `400` | `rest_invalid_term` |

## Checklist kiểm thử QA

- Role ngoài `editor` và `author` nhận `403 rest_cannot_create`.
- Yêu cầu thiếu cả `title` lẫn `content` nhận `400 rest_empty_post`.
- Không gửi `status` thì trạng thái mặc định là `draft`.
- Giá trị `status` nằm ngoài danh sách cho phép không được chấp nhận; mã lỗi cụ thể chưa được quy định trong brief.
- `author` gửi `status: publish` nhận `403 rest_cannot_publish`.
- `editor` gửi `status: publish` không bị từ chối theo quy tắc phân quyền publish.
- Với `status: future`, ngày không ở tương lai nhận `400 rest_invalid_date`.
- ID danh mục không tồn tại nhận `400 rest_invalid_term`.
- Khi bỏ trống `slug`, hệ thống tạo slug từ `title`; khi slug đã tồn tại, hệ thống thêm hậu tố số.
- Khi tạo thành công, phản hồi có HTTP `201` và bài viết đã lưu.

Định dạng chính xác của phản hồi, định dạng `date`, quy tắc cụ thể khi tạo hậu tố số và mã lỗi cho `status` không hợp lệ chưa được quy định trong brief.