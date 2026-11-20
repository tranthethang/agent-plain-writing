---
lang: vi
type: design
non_tech: false
---

# SIMULATED DATA

## Audience

Lập trình viên backend và QA đọc đặc tả API nội bộ.

## Brief

### Template
```markdown
## <METHOD> <PATH>
### 1. Mục đích
### 2. Đầu vào
### 3. Xử lý
### 4. Đầu ra
### 5. Lỗi
### 6. Ghi chú
```

### Idea
Thiết kế API `POST /v1/coupons/redeem` để áp dụng mã giảm giá cho một đơn hàng đang ở trạng thái `PENDING`.

### Business rules
- Mã giảm giá phải đang hoạt động (`ACTIVE`) và chưa hết hạn.
- Mỗi mã chỉ dùng tối đa 1 lần cho mỗi tài khoản người dùng.
- Đơn hàng phải có tổng tiền tối thiểu 100000 VND trước giảm giá.
- Nếu mã hợp lệ, hệ thống giảm tối đa 50000 VND và đánh dấu mã đã dùng trong cùng một transaction.
- Nếu hết lượt dùng toàn hệ thống, trả về HTTP 409 với mã lỗi `COUPON_EXHAUSTED`.
- Thời gian giữ mã khi thanh toán thất bại: chưa có quyết định (cần đánh dấu `TBD`).

### Glossary
- `coupon_code`: mã giảm giá (chuỗi 6–12 ký tự chữ hoa và số).
- `order_id`: mã đơn hàng (UUID).
- `PENDING`: trạng thái đơn hàng chưa thanh toán.

## Facts
- Endpoint: `POST /v1/coupons/redeem`
- Trạng thái đơn hợp lệ: `PENDING`
- Trạng thái mã hợp lệ: `ACTIVE`
- Số lần dùng mỗi tài khoản: tối đa 1 lần
- Tổng tiền tối thiểu: 100000 VND
- Mức giảm tối đa: 50000 VND
- Độ dài `coupon_code`: 6–12 ký tự
- Mã lỗi hết lượt: HTTP 409, `COUPON_EXHAUSTED`
- Mã lỗi đơn không hợp lệ hoặc không tìm thấy: HTTP 400 / 404 (nếu thiếu chi tiết, ghi `TBD`)
