---
lang: vi
type: user-guide
non_tech: true
---

# SIMULATED DATA

## Audience

Nhân viên thu ngân mới dùng ứng dụng KoraPOS trên máy tính bảng để xuất báo cáo bán hàng cuối ngày.

## Brief

### Feature
Xuất bảng tổng kết bán hàng theo ngày ra tệp CSV từ KoraPOS trên iPad hoặc máy tính bảng Android.

### Steps
1. Mở **KoraPOS** và chạm **Báo cáo** ở thanh dưới cùng.
2. Chọn **Doanh thu ngày** và chọn một ngày trên lịch (tối đa 90 ngày trước).
3. Chạm **Xuất CSV**, rồi chọn **Lưu vào tệp** hoặc **Gửi qua email**.
4. Chờ tối đa 15 giây để tệp `sales-YYYY-MM-DD.csv` xuất hiện.

### Reader
Nhân viên cửa hàng không rành kỹ thuật, cần đúng tên nút trên màn hình và cách xử lý nhanh khi xuất lỗi.

### Common errors
- **Chạm Xuất CSV nhưng không thấy gì**: máy đang mất mạng; kết nối Wi-Fi rồi chạm **Xuất CSV** lại.
- **Tệp rỗng (0 byte)**: ngày đó chưa có đơn đã thanh toán; chọn ngày khác.
- **Gửi qua email thất bại**: chưa cài email cửa hàng; nhờ quản lý thêm trong **Cài đặt** > **Hồ sơ cửa hàng**.

## Facts
- Tên ứng dụng: KoraPOS
- Thiết bị hỗ trợ: iPad hoặc máy tính bảng Android
- Nhãn nút: Báo cáo, Doanh thu ngày, Xuất CSV, Lưu vào tệp, Gửi qua email, Cài đặt, Hồ sơ cửa hàng
- Giới hạn chọn ngày: tối đa 90 ngày trước
- Thời gian chờ xuất tệp: tối đa 15 giây
- Tên tệp đầu ra: `sales-YYYY-MM-DD.csv`
- Dung lượng tệp rỗng: 0 byte
