# Ví dụ tiếng Việt: user guide

Mẫu riêng cho tiếng Việt. Cấu trúc nằm trong `doc-types/`, ngưỡng nằm trong `profile.json`.

## Cách thay thuật ngữ

| Thuật ngữ | Nói cho người dùng |
|---|---|
| cache | dữ liệu lưu tạm |
| token | mã đăng nhập |
| API key | mã kết nối |
| đồng bộ | tự cập nhật giống nhau trên mọi thiết bị |
| xác thực | đăng nhập, xác nhận bạn là ai |
| xác thực hai lớp | bước xác nhận thêm bằng mã gửi về điện thoại |
| phiên đăng nhập hết hạn | app yêu cầu đăng nhập lại |
| backup | bản sao lưu |
| restore | khôi phục từ bản sao lưu |
| cấu hình | cài đặt |
| firmware | phần mềm bên trong thiết bị |
| server | máy chủ, hoặc bỏ qua nếu không cần |
| log | nhật ký hoạt động |

Nếu một thuật ngữ **xuất hiện trên màn hình** (ví dụ nút "Token"), dùng đúng chữ đó, kèm giải thích một lần.

## Cặp xấu → tốt

### 1. Bước dồn nhiều hành động

**Xấu:** Bạn hãy truy cập vào phần cài đặt, sau đó tìm đến mục tài khoản và tiến hành thay đổi mật khẩu bằng cách nhập mật khẩu cũ và mật khẩu mới.
**Tốt:**
1. Bấm **Cài đặt**.
2. Chọn **Tài khoản**.
3. Bấm **Đổi mật khẩu**.
4. Nhập mật khẩu cũ, rồi nhập mật khẩu mới.
5. Bấm **Lưu**. Bạn sẽ thấy dòng "Đã đổi mật khẩu".

### 2. Cơ chế → kết quả

**Xấu:** Ứng dụng sử dụng cơ chế đồng bộ nền để tự động cập nhật dữ liệu giữa các thiết bị thông qua máy chủ đám mây.
**Tốt:** Bạn sửa trên điện thoại, máy tính tự cập nhật theo. Bạn không cần làm gì thêm.

### 3. Thuật ngữ

**Xấu:** Nếu token hết hạn, bạn cần xác thực lại.
**Tốt:** Nếu app báo phiên đăng nhập hết hạn, hãy đăng nhập lại.

### 4. Cảnh báo

**Xấu:** Lưu ý rằng việc xóa dữ liệu có thể dẫn đến tình trạng không thể khôi phục được trong một số trường hợp.
**Tốt:** **Chú ý:** Dữ liệu đã xóa không lấy lại được.

### 5. Xử lý lỗi

**Xấu:** Trong trường hợp xảy ra lỗi, vui lòng kiểm tra kết nối mạng hoặc liên hệ bộ phận hỗ trợ kỹ thuật để được trợ giúp.
**Tốt:**

| Bạn thấy | Làm gì |
|---|---|
| "Không thể kết nối" | Kiểm tra Wi-Fi, rồi thử lại. |
| Vẫn lỗi sau khi thử lại | Chụp màn hình và gửi cho [địa chỉ hỗ trợ]. |

### 6. Mô tả tính năng bằng tính từ

**Xấu:** Tính năng báo cáo cung cấp nhiều tùy chọn đa dạng giúp người dùng phân tích dữ liệu một cách toàn diện.
**Tốt:** Dùng **Báo cáo** để xem tháng này bạn bán được bao nhiêu.

### 7. Dịch toàn bộ cơ chế (lỗi hay gặp)

**Xấu:** Khi bạn bấm Gửi, yêu cầu sẽ được đưa vào hàng đợi xử lý. Một tiến trình nền sẽ lấy yêu cầu ra, kiểm tra dữ liệu, rồi ghi vào cơ sở dữ liệu. Sau đó hệ thống thông báo kết quả cho bạn qua email.
**Tốt:** Bấm **Gửi**. Vài phút sau, bạn nhận được email báo kết quả.
**Quy tắc:** Hỏi "người dùng cần biết điều này để làm gì?". Nếu không để làm gì, bỏ.

### 8. Tên nút sai

**Xấu:** Bấm nút xác nhận để lưu thay đổi.
**Tốt:** Bấm **Lưu**.

### 9. Điều kiện trước

**Xấu:** Trước khi tiến hành thao tác, bạn cần đảm bảo rằng mình đã được cấp các quyền hạn cần thiết.
**Tốt:** Bạn cần là **Quản trị viên**. Nếu không thấy nút **Thêm**, hãy nhờ quản trị viên cấp quyền.

### 10. Mục tiêu

**Xấu:** Hướng dẫn này nhằm cung cấp cho người dùng những thông tin cần thiết để có thể sử dụng chức năng xuất báo cáo.
**Tốt:** Hướng dẫn này giúp bạn xuất báo cáo ra file Excel.

## Mẫu hướng dẫn hoàn chỉnh

```markdown
# Đổi mật khẩu

Dùng khi bạn quên mật khẩu hoặc muốn đổi mật khẩu mới.

## Chuẩn bị
- Bạn đã đăng nhập.
- Bạn nhớ mật khẩu cũ.

## Các bước
1. Bấm **Cài đặt**.
2. Chọn **Tài khoản**.
3. Bấm **Đổi mật khẩu**.
4. Nhập mật khẩu cũ, rồi nhập mật khẩu mới hai lần.
5. Bấm **Lưu**. Bạn sẽ thấy dòng "Đã đổi mật khẩu".

## Nếu gặp lỗi

| Bạn thấy | Làm gì |
|---|---|
| "Mật khẩu cũ không đúng" | Nhập lại mật khẩu cũ. Quên thì bấm **Quên mật khẩu** ở màn hình đăng nhập. |
| "Mật khẩu quá ngắn" | Dùng ít nhất 8 ký tự. |
```

## Mẫu của bạn (thêm vào đây)

<!-- Dán một hướng dẫn bạn đã viết tốt, và các câu AI dịch dài dòng kèm bản bạn rút gọn. -->
