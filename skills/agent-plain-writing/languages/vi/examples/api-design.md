# Ví dụ tiếng Việt: API design

Câu chuyện và con số trong các ví dụ chỉ để minh họa, không phải sự thật.

Mẫu riêng cho tiếng Việt. Cấu trúc nằm trong `doc-types/`, ngưỡng nằm trong `profile.json`.

## Bad → good pairs

### 1. Hiệu năng mơ hồ

**Bad:** API trả kết quả một cách nhanh chóng.
**Good:** API phải trả lời trong ≤ 500 ms ở P95. (Nếu chưa có số: ghi `TBD-1` và thêm `- TBD-1: ngưỡng P95 cho API này?` vào mục còn mở)

### 2. Xử lý lỗi mơ hồ

**Bad:** Hệ thống xử lý lỗi một cách phù hợp khi sản phẩm hết hàng.
**Good:** Khi một sản phẩm hết hàng, hệ thống trả 409 với mã `OUT_OF_STOCK` và không tạo đơn hàng.

### 3. Phân quyền mơ hồ

**Bad:** Chỉ người dùng có quyền thích hợp mới được thực hiện thao tác này.
**Good:** Chỉ role `admin` và `staff` được gọi API này. Role khác nhận 403.

### 4. Bảo mật mơ hồ

**Bad:** Dữ liệu được lưu trữ một cách an toàn.
**Good:** Mật khẩu lưu dạng hash bcrypt. Hệ thống không được lưu mật khẩu gốc.

### 5. Quy trình bằng văn xuôi

**Bad:** Đầu tiên hệ thống sẽ tiến hành kiểm tra xem giỏ hàng có rỗng hay không, sau đó nếu không rỗng thì sẽ kiểm tra tồn kho của từng sản phẩm và nếu đủ thì tạo đơn hàng rồi xóa giỏ hàng.
**Good:**
1. Hệ thống kiểm tra giỏ hàng không rỗng.
2. Hệ thống kiểm tra tồn kho từng dòng.
3. Hệ thống tạo đơn hàng, trạng thái `PENDING`.
4. Hệ thống xóa giỏ hàng.

### 6. Thử lại mơ hồ

**Bad:** Nếu cần thì hệ thống sẽ thử lại.
**Good:** Khi gọi dịch vụ thanh toán thất bại, hệ thống thử lại tối đa 3 lần, cách nhau 2 giây. Quá 3 lần, hệ thống trả 503.
(Nếu nguồn không nêu số lần: ghi `TBD-1` và thêm `- TBD-1: số lần và khoảng cách thử lại?` vào mục còn mở)

### 7. Đầu vào bằng văn xuôi

**Bad:** API nhận vào các thông tin cần thiết như mã giỏ hàng, phương thức thanh toán và ghi chú nếu có.
**Good:**

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `cart_id` | Request | uuid | Có | Giỏ phải thuộc người gọi |
| `payment_method` | Request | enum | Có | `card`, `cod` |
| `note` | Request | string | Không | ≤ 200 ký tự |

### 8. "v.v."

**Bad:** Trạng thái đơn hàng gồm PENDING, PAID, v.v.
**Good:** Trạng thái đơn hàng gồm `PENDING`, `PAID`, `SHIPPED`, `CANCELLED`. Nếu nguồn chưa đủ: ghi `TBD-1` và thêm `- TBD-1: danh sách đầy đủ trạng thái?` vào mục còn mở.

### 9. Thuật ngữ không nhất quán

**Bad:** Khi người dùng tạo order, hệ thống lưu đơn đặt hàng vào bảng orders.
**Good:** Khi người dùng tạo đơn hàng, hệ thống lưu đơn hàng vào bảng `orders`.
**Convention:** "đơn hàng" trong văn bản, `orders` trong tên bảng. Không dùng "order" hay "đơn đặt hàng" cho cùng một khái niệm.

### 10. Mô tả điều kiện

**Bad:** Trong trường hợp mà người dùng chưa đăng nhập thì sẽ không được phép truy cập.
**Good:** Khi request không có token hợp lệ, hệ thống phải trả 401.

### 11. Lỗi liệt kê hai lần

**Bad:** Bước 2 của Xử lý ghi "trả 409 `ROOM_TAKEN` khi phòng đã có người đặt". Bảng Lỗi ghi lại điều đó bằng lời khác.
**Good:** Xử lý không nhắc đến phòng đã có người đặt. Bảng Lỗi có một dòng: 409, `ROOM_TAKEN`, "Một lượt đặt khác trùng khung giờ".
**Fault:** Hai nơi giữ một sự thật sẽ lệch nhau.
**Fix:** Bảng Lỗi giữ mọi phép kiểm tra: điều kiện, mã HTTP và mã lỗi. Xử lý không liệt kê phép kiểm tra nào.

### 12. Phân quyền ghi ba lần

**Bad:** Thông tin chung ghi "chỉ staff". Bước 1 của Xử lý ghi "kiểm tra người gọi là staff". Bảng Lỗi ghi "403 khi người gọi không phải staff, như trên".
**Good:** Thông tin chung ghi "Phân quyền: role `admin` và `staff`." Bảng Lỗi ghi `403 FORBIDDEN` với điều kiện "người gọi có role khác". Xử lý không nhắc đến role.
**Fault:** Ba nơi nêu một quy tắc.
**Fix:** Thông tin chung giữ quy tắc. Bảng Lỗi giữ trường hợp thất bại.

### 13. "Giống các API cùng nhóm"

**Bad:** Lỗi: giống các endpoint phòng họp khác.
**Good:** Liệt kê mọi lỗi của endpoint này trong bảng riêng. Nếu nguồn thiếu, ghi `TBD-1` trong bảng và đưa `- TBD-1: <câu hỏi>` vào mục còn mở.
**Fault:** Người đọc không thể kiểm tra endpoint một mình.
**Fix:** Ghi quy tắc ngay tại đây, hoặc ghi `TBD-1` rồi đưa `- TBD-1: <câu hỏi>` vào mục còn mở.

### 14. Quy tắc nghiệp vụ không có thứ tự bước

**Bad:** Hệ thống kiểm tra trùng lịch, giờ mở cửa và hạn mức khi tạo lượt đặt.
**Good:** Thứ tự kiểm tra: giờ mở cửa, trùng lịch, hạn mức trong ngày. Khi hai phép kiểm tra cùng thất bại, phép đầu tiên theo thứ tự này quyết định lỗi.
**Fault:** Người đọc không biết lỗi nào trả trước khi hai bước cùng thất bại.
**Fix:** Ghi một dòng thứ tự và một dòng ưu tiên lỗi trong Xử lý. Khi brief chưa nêu thứ tự, ghi `TBD-1` kèm `- TBD-1: thứ tự kiểm tra và lỗi ưu tiên khi hai bước cùng lỗi?` ở mục còn mở.

### 15. Danh sách rỗng không có quy tắc

**Bad:** API trả các lượt đặt của một phòng.
**Good:** API trả các lượt đặt của một phòng. Khi phòng chưa có lượt nào, API trả 200 với `items` là mảng rỗng.
**Fault:** QA không biết kết quả rỗng là 200 hay 404.
**Fix:** Viết trường hợp rỗng thành một câu riêng, kèm mã HTTP.

### 16. Xử lý có bước và sơ đồ

**Bad:** Chỉ có sơ đồ, không có bước đánh số. Hoặc chỉ có bước, trong luồng có ba nhánh.
**Good:** Bước đánh số trước, rồi một khối Mermaid cho cùng thứ tự:

````markdown
1. Hệ thống tạo `reservation_id`.
2. Hệ thống tính `ends_at` từ `starts_at` và `minutes`.
3. Hệ thống lưu lượt đặt với trạng thái `CONFIRMED`.

```mermaid
sequenceDiagram
    Client->>API: POST /v1/reservations
    API->>API: tạo id và tính giờ kết thúc
    API->>DB: lưu lượt đặt
    API-->>Client: phản hồi
```
````

**Fault:** Sơ đồ chứa hành vi mà các bước không nêu.
**Fix:** Các bước giữ quy tắc. Sơ đồ chỉ cho thấy thứ tự.

### 17. Dùng TBD-n cho kiểu đã biết từ bảng thuật ngữ

(Bảng thuật ngữ nêu `title` là "tiêu đề bài viết".)

**Bad:**

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Request | `TBD-1` | Có | — |

**Good:**

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Request | string | Có | — |

**Fault:** Mở `TBD-n` cho kiểu của trường mà bảng thuật ngữ đã mô tả là văn bản.
**Fix:** Khi bảng thuật ngữ mô tả trường là văn bản (như tiêu đề, nội dung, tên, phần URL), ghi `string` và không mở `TBD-n`.

### 18. TBD-n hỏi điều quy tắc đã nêu

(Brief nêu: `date` phải là ngày ở tương lai, và thiếu `date` chưa có mã lỗi.)

**Bad:** `- TBD-1: ngày có phải ở tương lai không?`
**Good:** `- TBD-1: hệ thống trả mã HTTP và mã lỗi nào khi thiếu `date`?`
**Fault:** Câu hỏi lặp lại quy tắc đã nêu và bỏ qua quyết định brief còn thiếu.
**Fix:** `TBD-n` hỏi quyết định còn thiếu, ở đây là lỗi khi thiếu `date`.

## Mẫu API điền hoàn chỉnh

Khuôn tham khảo. Cấu trúc nằm trong `doc-types/api-design.md`.

````markdown
## Thông tin chung

- Method và path: `POST /v1/reservations`
- Mục đích: tạo lượt đặt cho một phòng họp.
- Bên gọi: web app đặt phòng.
- Phân quyền: role `admin` và `staff`.
- Idempotency: không idempotent. Gọi lại tạo thêm một lượt đặt.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `room_id` | Request | uuid | Có | Phòng phải tồn tại |
| `starts_at` | Request | datetime | Có | Giờ bắt đầu phải ở tương lai; đặt trước tối đa `TBD-1` ngày |
| `minutes` | Request | integer | Có | 30 đến 240, bước 30 |
| `note` | Request | string | Không | ≤ 200 ký tự |
| `reservation_id` | Response | uuid | — | — |
| `status` | Response | string | — | — |
| `ends_at` | Response | datetime | — | — |

## Endpoint

Request:

    {"room_id": "r-12", "starts_at": "2026-12-01T09:00:00Z", "minutes": 60}

Response, status 201:

    {"reservation_id": "rv-88", "status": "CONFIRMED", "ends_at": "2026-12-01T10:00:00Z"}

## Xử lý

1. Hệ thống tạo `reservation_id`.
2. Hệ thống tính `ends_at` từ `starts_at` và `minutes`.
3. Hệ thống lưu lượt đặt với trạng thái `CONFIRMED`.

Thứ tự kiểm tra: giờ mở cửa, rồi trùng lịch. Khi hai phép kiểm tra cùng thất bại, phép đầu tiên theo thứ tự này quyết định lỗi.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 400 | `OUTSIDE_HOURS` | Khung giờ nằm ngoài giờ mở cửa |
| 403 | `FORBIDDEN` | Người gọi có role khác |
| 409 | `ROOM_TAKEN` | Một lượt đặt khác trùng khung giờ |

## Tác động kèm theo

Hệ thống ghi một bản ghi audit cho mỗi lượt đặt được lưu.

## Mục còn mở

- `TBD-1`: người gọi được đặt trước tối đa bao nhiêu ngày?
````

## Mẫu của bạn (thêm vào đây)

<!-- Dán một API bạn đã điền chuẩn. AI học từ đây tốt hơn học từ mọi lời mô tả. -->
