# Ví dụ tiếng Việt: detail design

Mẫu riêng cho tiếng Việt. Cấu trúc nằm trong `doc-types/`, ngưỡng nằm trong `profile.json`.

## Cặp xấu → tốt

### 1. Hiệu năng mơ hồ

**Xấu:** API trả kết quả một cách nhanh chóng.
**Tốt:** API phải trả lời trong ≤ 500 ms ở P95. (Nếu chưa có số: `TBD: ngưỡng P95 cho API này?`)

### 2. Xử lý lỗi mơ hồ

**Xấu:** Hệ thống xử lý lỗi một cách phù hợp khi sản phẩm hết hàng.
**Tốt:** Khi một sản phẩm hết hàng, hệ thống trả 409 với mã `OUT_OF_STOCK` và không tạo đơn hàng.

### 3. Phân quyền mơ hồ

**Xấu:** Chỉ người dùng có quyền thích hợp mới được thực hiện thao tác này.
**Tốt:** Chỉ role `admin` và `staff` được gọi API này. Role khác nhận 403.

### 4. Bảo mật mơ hồ

**Xấu:** Dữ liệu được lưu trữ một cách an toàn.
**Tốt:** Mật khẩu lưu dạng hash bcrypt. Hệ thống không được lưu mật khẩu gốc.

### 5. Quy trình bằng văn xuôi

**Xấu:** Đầu tiên hệ thống sẽ tiến hành kiểm tra xem giỏ hàng có rỗng hay không, sau đó nếu không rỗng thì sẽ kiểm tra tồn kho của từng sản phẩm và nếu đủ thì tạo đơn hàng rồi xóa giỏ hàng.
**Tốt:**
1. Hệ thống kiểm tra giỏ hàng không rỗng.
2. Hệ thống kiểm tra tồn kho từng dòng.
3. Hệ thống tạo đơn hàng, trạng thái `PENDING`.
4. Hệ thống xóa giỏ hàng.

### 6. Thử lại mơ hồ

**Xấu:** Nếu cần thì hệ thống sẽ thử lại.
**Tốt:** Khi gọi dịch vụ thanh toán thất bại, hệ thống thử lại tối đa 3 lần, cách nhau 2 giây. Quá 3 lần, hệ thống trả 503.
(Nếu nguồn không nêu số lần: `TBD: số lần và khoảng cách thử lại?`)

### 7. Đầu vào bằng văn xuôi

**Xấu:** API nhận vào các thông tin cần thiết như mã giỏ hàng, phương thức thanh toán và ghi chú nếu có.
**Tốt:**

| Trường | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `cart_id` | uuid | Có | Giỏ phải thuộc người gọi |
| `payment_method` | enum | Có | `card`, `cod` |
| `note` | string | Không | ≤ 200 ký tự |

### 8. "v.v."

**Xấu:** Trạng thái đơn hàng gồm PENDING, PAID, v.v.
**Tốt:** Trạng thái đơn hàng gồm `PENDING`, `PAID`, `SHIPPED`, `CANCELLED`. Nếu nguồn chưa đủ: `TBD: danh sách đầy đủ trạng thái?`

### 9. Thuật ngữ không nhất quán

**Xấu:** Khi người dùng tạo order, hệ thống lưu đơn đặt hàng vào bảng orders.
**Tốt:** Khi người dùng tạo đơn hàng, hệ thống lưu đơn hàng vào bảng `orders`.
**Quy ước:** "đơn hàng" trong văn bản, `orders` trong tên bảng. Không dùng "order" hay "đơn đặt hàng" cho cùng một khái niệm.

### 10. Mô tả điều kiện

**Xấu:** Trong trường hợp mà người dùng chưa đăng nhập thì sẽ không được phép truy cập.
**Tốt:** Khi request không có token hợp lệ, hệ thống phải trả 401.

## Mẫu API điền hoàn chỉnh

Khuôn tham khảo. Template thật của bạn mới là khuôn chính.

```markdown
## POST /v1/orders

### 1. Mục đích
Tạo đơn hàng mới từ giỏ hàng của người dùng đã đăng nhập.

### 2. Đầu vào
| Trường | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `cart_id` | uuid | Có | Giỏ phải thuộc người gọi |
| `payment_method` | enum | Có | `card`, `cod` |
| `note` | string | Không | ≤ 200 ký tự |

### 3. Xử lý
1. Hệ thống kiểm tra giỏ hàng không rỗng.
2. Hệ thống kiểm tra tồn kho từng dòng. Nếu thiếu, trả lỗi `OUT_OF_STOCK`.
3. Hệ thống tạo đơn hàng trạng thái `PENDING` trong một transaction.
4. Hệ thống xóa giỏ hàng.

### 4. Đầu ra
201. Body: `order_id`, `status`, `total`.

### 5. Lỗi
| HTTP | Mã | Điều kiện |
|---|---|---|
| 400 | `EMPTY_CART` | Giỏ hàng rỗng |
| 401 | `UNAUTHORIZED` | Không có token hợp lệ |
| 409 | `OUT_OF_STOCK` | Một dòng vượt tồn kho |

### 6. Ghi chú
- `TBD`: thời gian giữ tồn kho cho đơn `PENDING`?
```

## Mẫu của bạn (thêm vào đây)

<!-- Dán một API bạn đã điền chuẩn. AI học từ đây tốt hơn học từ mọi lời mô tả. -->
