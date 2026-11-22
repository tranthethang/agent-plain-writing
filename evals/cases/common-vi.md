---
lang: vi
type: common
non_tech: false
---

# SIMULATED DATA

## Audience

Kỹ sư backend đọc thông báo bảo trì nội bộ trong bảng tin hệ thống.

## Brief

### Summary
Cụm PostgreSQL môi trường staging (`db-stage-02`) nâng RAM từ 16 GB lên 32 GB vào 04:00 UTC ngày 2026-12-03. Quá trình nâng cấp mất 8 phút; trong lúc này các kết nối tới staging bị ngắt và job CI đang chờ sẽ thử lại sau 30 giây. Chuỗi kết nối và thông tin đăng nhập giữ nguyên.

### Reader
Kỹ sư backend chạy test tích hợp trên staging, cần biết đúng khung giờ và ảnh hưởng.

### Words to use or avoid
- Use: `staging`, `cụm`, `thời gian gián đoạn`.
- Avoid: `liền mạch`, `tối ưu hóa`, `tôi`, `chúng tôi`.

## Facts
- Tên cụm: `db-stage-02`
- Hệ quản trị cơ sở dữ liệu: PostgreSQL
- Thay đổi RAM: 16 GB lên 32 GB
- Thời gian bảo trì: 04:00 UTC ngày 2026-12-03
- Thời lượng: 8 phút
- Thời gian chờ thử lại của CI: 30 giây
