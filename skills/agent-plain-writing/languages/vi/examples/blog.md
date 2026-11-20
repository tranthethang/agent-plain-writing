# Ví dụ tiếng Việt: blog chia sẻ

Mẫu riêng cho tiếng Việt. Cấu trúc nằm trong `doc-types/`, ngưỡng nằm trong `profile.json`.

## Cặp xấu → tốt

Ví dụ minh họa. Chi tiết trong câu chuyện là bịa để làm mẫu. Khi viết thật, dùng chuyện của tác giả.

### 1. Mở bài

**Xấu:** Trong thế giới công nghệ phát triển không ngừng như hiện nay, việc quản lý trạng thái trong ứng dụng React đóng vai trò vô cùng quan trọng. Hãy cùng tìm hiểu nhé!
**Tốt:** Tuần trước, một nút bấm trong app React của tôi cập nhật chậm hai giây. Nguyên nhân: tôi nhét mọi thứ vào một state toàn cục.

### 2. Giải thích khái niệm

**Xấu:** Cache là một cơ chế lưu trữ tạm thời nhằm mục đích tăng tốc độ truy xuất dữ liệu bằng cách lưu giữ các bản sao của dữ liệu thường xuyên được truy cập.
**Tốt:** Cache là bản sao lưu sẵn của dữ liệu hay dùng. Lần sau cần, hệ thống lấy bản sao, không phải tính lại.

### 3. Ý kiến cá nhân

**Xấu:** Có thể nói rằng việc sử dụng TypeScript mang lại nhiều lợi ích đáng kể trong quá trình phát triển phần mềm.
**Tốt:** Từ khi chuyển sang TypeScript, trình soạn thảo báo lỗi kiểu dữ liệu ngay lúc tôi gõ. Tôi không còn đợi đến lúc chạy mới biết.

### 4. Bài học

**Xấu:** Qua trải nghiệm này, chúng ta có thể rút ra nhiều bài học quý giá về tầm quan trọng của việc lập kế hoạch.
**Tốt:** Bài học: viết plan 10 phút trước khi code. Tôi mất cả buổi chiều vì bỏ qua bước này.

### 5. Chuyển mục

**Xấu:** Bên cạnh đó, một vấn đề khác cũng cần được lưu ý là việc xử lý lỗi.
**Tốt:** (dùng tiêu đề mục) `## Lỗi thứ hai: không xử lý lỗi`

### 6. Tính từ thành chi tiết

**Xấu:** Giao diện mới rất đẹp, hiện đại và thân thiện với người dùng.
**Tốt:** Giao diện mới mỗi màn hình chỉ có một nút chính. Người dùng không phải đoán bấm gì.

### 7. Câu nhồi ý

**Xấu:** Công cụ này, vốn được phát triển nhằm hỗ trợ lập trình viên trong việc quản lý các phiên làm việc với AI, cho phép lưu lại lịch sử và đồng thời giúp chuyển giao giữa các agent một cách liền mạch.
**Tốt:** Công cụ này giúp tôi quản lý phiên làm việc với AI. Nó lưu lại lịch sử. Agent này làm tiếp được việc của agent khác.

### 8. Lời khuyên chung chung

**Xấu:** Chúng ta nên luôn luôn chú ý đến chất lượng mã nguồn để đảm bảo tính bền vững lâu dài của dự án.
**Tốt:** Đặt một quy tắc: không merge nếu test đỏ. Quy tắc này cứu tôi ba lần trong tháng qua.

### 9. Kết bài

**Xấu:** Tóm lại, hy vọng bài viết đã mang đến cho bạn những thông tin hữu ích. Cảm ơn các bạn đã đọc và hẹn gặp lại!
**Tốt:** Hôm nay thử một việc: mở dự án, đếm số state toàn cục. Nếu quá 5, bắt đầu tách.

### 10. Thừa nhận giới hạn

**Xấu:** Giải pháp này tuy có thể còn một số hạn chế nhất định nhưng nhìn chung vẫn mang lại hiệu quả tương đối tốt.
**Tốt:** Giải pháp này chưa xử lý được trường hợp mất mạng giữa chừng. Tôi chưa tìm ra cách gọn hơn.

## Bài mẫu hoàn chỉnh (khoảng 180 từ, rút gọn để làm khuôn nhịp)

```markdown
# Tôi bỏ state toàn cục sau một buổi chiều mất trắng

Nút "Lưu" trong app của tôi phản hồi chậm hai giây. Tôi mất cả buổi chiều mới tìm ra lý do.

## Mọi thứ nằm trong một chỗ

Tôi để toàn bộ dữ liệu trong một state duy nhất. Sửa một ô, cả trang vẽ lại.

Lúc đầu nó chạy ổn. Hai tháng sau, trang có 40 ô nhập.

## Cách tôi sửa

Tôi tách state theo từng form. Mỗi form tự giữ dữ liệu của nó.
Chỉ dữ liệu dùng chung (người dùng, ngôn ngữ) mới ở lại chỗ cũ.

Kết quả: sửa một ô, chỉ form đó vẽ lại.

## Bài học

Đừng hỏi "dữ liệu này để ở đâu cho tiện". Hãy hỏi "ai thật sự cần dữ liệu này".

Hôm nay thử một việc: mở dự án, đếm số state toàn cục. Nếu quá 5, bắt đầu tách.
```

## Mẫu của bạn (thêm vào đây)

<!-- Dán đoạn bạn viết hoặc đã sửa ưng ý. Thêm cặp Xấu / Tốt từ các bài AI viết dở. -->
