---
lang: vi
type: tech-blog
non_tech: false
---

# SIMULATED DATA

## Audience

Lập trình viên backend có 2–5 năm kinh nghiệm, đang vận hành dịch vụ web nhỏ.

## Brief

### Summary
Nhóm của bạn từng đặt cache 15 phút cho trang danh sách sản phẩm để giảm tải database. Sau một đợt giảm giá, khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn. Nhóm đã sửa bằng cách xóa cache theo sự kiện cập nhật giá và đặt TTL dự phòng 60 giây.

### Main points
1. Cache theo thời gian cố định dễ gây lệch dữ liệu khi giá đổi đột ngột.
2. Xóa cache ngay khi ghi dữ liệu mới giúp giảm độ trễ cập nhật xuống dưới 1 giây.
3. Giữ TTL ngắn (60 giây) làm lưới an toàn nếu sự kiện bị mất.

### Reader
Lập trình viên backend quen SQL và Redis, chưa từng gặp sự cố lệch cache khi lưu lượng tăng gấp 3 lần.

### Voice
Ngôi thứ nhất ("tôi", "bạn"), thẳng thắn như kể lại cho đồng nghiệp ngồi cạnh, thừa nhận sai lầm.

### Sample paragraph
Tôi từng nghĩ tăng TTL lên 15 phút là cách nhanh nhất để cứu database. Mọi thứ êm đẹp suốt 2 tháng, cho tới sáng thứ Sáu khi bảng giá đổi lúc 9 giờ.

### Words to use or avoid
- Dùng: `cache`, `TTL`, `database`.
- Tránh: `tối ưu hóa`, `mạnh mẽ`, `đóng vai trò quan trọng`.

## Facts
- TTL ban đầu: 15 phút
- Thời gian khách thấy giá cũ: 12 phút
- Số đơn đặt nhầm: 40 đơn
- Lưu lượng tăng: 3 lần
- Độ trễ cập nhật sau khi sửa: dưới 1 giây
- TTL dự phòng: 60 giây
- Thời điểm đổi giá: 9 giờ sáng thứ Sáu
- Thời gian chạy ổn trước sự cố: 2 tháng
