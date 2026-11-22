# Cặp xấu → tốt dùng chung

Dùng cho mọi loại văn bản, hoặc khi chưa có reference riêng.
Số liệu trong ví dụ chỉ để minh họa. Khi viết thật, dùng số của tác giả hoặc ghi `TBD`.

## 1. Mở bài rỗng

**Bad:** Trong thế giới công nghệ phát triển không ngừng như hiện nay, việc quản lý dữ liệu đóng vai trò vô cùng quan trọng. Hãy cùng tìm hiểu nhé!
**Good:** Tuần trước, file báo cáo của tôi mở mất 40 giây. Nguyên nhân là một bảng 200.000 dòng.
**Fault:** Mở bằng lời chung chung. **Fix:** Mở bằng một sự việc cụ thể.

## 2. Câu nhồi nhiều ý

**Bad:** Công cụ này, vốn được phát triển nhằm hỗ trợ lập trình viên quản lý các phiên làm việc với AI, cho phép lưu lại lịch sử và đồng thời giúp chuyển giao giữa các agent một cách liền mạch.
**Good:** Công cụ này giúp lập trình viên quản lý phiên làm việc với AI. Nó lưu lại lịch sử. Nhờ đó, agent này làm tiếp được việc của agent khác.
**Fault:** Ba ý trong một câu. **Fix:** Một câu một ý.

## 3. Danh từ hóa động từ

**Bad:** Việc thực hiện kiểm tra tính hợp lệ của dữ liệu được tiến hành trước khi lưu.
**Good:** Hệ thống kiểm tra dữ liệu trước khi lưu.
**Fault:** "việc", "thực hiện", "tiến hành", câu bị động. **Fix:** Chủ ngữ rõ, động từ trực tiếp.

## 4. Tính từ rỗng

**Bad:** Giao diện mới rất đẹp, hiện đại và thân thiện với người dùng.
**Good:** Mỗi màn hình chỉ có một nút chính. Người dùng không phải đoán bấm gì.
**Fault:** Tính từ đánh giá. **Fix:** Chi tiết nhìn thấy được.

## 5. Thuật ngữ nặng

**Bad:** Hệ thống sử dụng cơ chế bộ nhớ đệm nhằm mục đích tối ưu hóa hiệu năng truy xuất dữ liệu.
**Good:** Hệ thống lưu sẵn kết quả đã tính. Lần sau, nó trả lời nhanh hơn.
**Fault:** Ba thuật ngữ trong một câu. **Fix:** Nói kết quả, bỏ cơ chế.

## 6. Giải thích lặp

**Bad:** Ứng dụng cho phép đồng bộ dữ liệu. Nói cách khác, dữ liệu sẽ được cập nhật giữa các thiết bị. Điều này có nghĩa là bạn sẽ thấy dữ liệu giống nhau trên mọi thiết bị.
**Good:** Bạn sửa trên điện thoại, máy tính tự cập nhật theo.
**Fault:** Ba câu nói một ý. **Fix:** Giữ câu cụ thể nhất.

## 7. Liệt kê dạng văn xuôi

**Bad:** Công cụ không tự chạy giai đoạn, không lên lịch cho agent, không gọi trực tiếp mô hình, không xác minh tên mô hình và không đọc thư mục phiên bản cũ.
**Good:**
- Không tự chạy các giai đoạn.
- Không lên lịch cho agent.
- Không gọi trực tiếp LLM.
- Không xác minh tên model.
- Không đọc thư mục của phiên bản cũ.

**Fault:** Người đọc cần quét nhanh nhưng bị ép đọc liền mạch. **Fix:** Gạch đầu dòng, mỗi dòng một ý.

## 8. Chuyển đoạn thừa

**Bad:** Bên cạnh đó, một vấn đề khác cũng cần được lưu ý là việc xử lý lỗi.
**Good:** Vấn đề thứ hai: xử lý lỗi.
**Fault:** Chuyển đoạn dài hơn nội dung. **Fix:** Dùng tiêu đề hoặc một cụm ngắn.

## 9. Kết bài rỗng

**Bad:** Tóm lại, hy vọng bài viết đã mang đến cho bạn những thông tin hữu ích. Cảm ơn các bạn đã đọc!
**Good:** Hôm nay hãy thử một việc: mở dự án và đếm số biến toàn cục.
**Fault:** Tóm tắt lặp và cảm ơn rỗng. **Fix:** Kết bằng một việc người đọc làm được.

## 10. Hành văn hành chính

**Bad:** Hạng mục công việc được bàn giao qua lại giữa các agent trong quá trình triển khai.
**Good:** Công việc được chuyển qua lại giữa các agent.
**Fault:** "hạng mục", "trong quá trình triển khai". **Fix:** Từ thường, bỏ cụm thừa.

## 11. Bị động kéo dài

**Bad:** Các tệp cấu hình sẽ được tạo ra bởi hệ thống và sau đó sẽ được đọc bởi từng dịch vụ.
**Good:** Hệ thống tạo tệp cấu hình. Mỗi dịch vụ đọc tệp đó.

## 12. Số liệu thay cho cảm giác

**Bad:** Việc cải tiến này giúp hệ thống chạy nhanh hơn đáng kể.
**Good:** Sau khi sửa, thời gian xử lý giảm từ 3 giây xuống 200 ms.
**Nếu không có số:** "Chưa đo. Cần đo thời gian xử lý trước và sau khi sửa." Đừng bịa số.

## Mẫu hoàn chỉnh

```markdown
## Lịch sao lưu hằng đêm

Cơ sở dữ liệu thanh toán sao lưu toàn bộ lúc 02:00 UTC mỗi ngày. Bản sao lưu được giữ 30 ngày trên kho mã hóa rồi tự xóa.

Khôi phục một ổ 40 GB từ bản sao lưu mất khoảng 12 phút. Trong lúc khôi phục, dữ liệu mới tạm dừng ghi cho tới khi ổ gắn xong.

Nhóm cần bản sao ngoài giờ này có thể tạo bản sao thủ công trong bảng điều khiển quản trị. Bản sao thủ công dùng chung hạn mức 500 GB.
```

## Mẫu của bạn (thêm vào đây)

<!-- Dán các câu AI viết dở và bản bạn đã sửa. Dùng định dạng Bad / Good / Fault / Fix. -->
