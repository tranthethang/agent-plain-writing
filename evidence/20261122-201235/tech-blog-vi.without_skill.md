# Cache giá cũ khiến chúng tôi phải gọi lại cho 40 khách

Tôi từng nghĩ đặt TTL 15 phút cho trang danh sách sản phẩm là cách nhanh nhất để giảm tải database. Mọi thứ chạy êm trong 2 tháng, cho tới 9 giờ sáng thứ Sáu, khi giá sản phẩm đổi.

Lưu lượng lúc đó tăng gấp 3 lần. Khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn. Chiều hôm đó, nhóm tôi gọi lại cho từng khách. Đây là sự cố do cách tôi xử lý cache, không phải do khách đọc nhầm.

## Vì sao TTL 15 phút thành vấn đề

Trang danh sách sản phẩm đọc giá từ cache. Khi giá đổi, cache vẫn giữ giá cũ cho đến khi TTL hết hạn. Với TTL 15 phút, khách có thể thấy dữ liệu cũ trong một khoảng thời gian đủ dài để đặt hàng theo giá không còn đúng.

Bài học nghe có vẻ hiển nhiên: dữ liệu giá thay đổi đột ngột thì chỉ dựa vào TTL cố định là không đủ.

## Vì sao tôi không giữ TTL 15 giây

Phản ứng đầu tiên của tôi là giảm TTL xuống 15 giây. Cách này làm dữ liệu cũ tồn tại trong thời gian ngắn hơn, nhưng tải database tăng gấp đôi. Tôi bỏ cách đó.

Sau đó, nhóm chuyển sang xóa cache khi có cập nhật giá. Cách này giảm độ trễ cập nhật xuống dưới 1 giây. Chúng tôi giữ TTL dự phòng ở 60 giây, để cache không tồn tại quá lâu nếu sự kiện xóa cache bị mất.

Có hai trang đọc cache giá: trang danh sách và trang chi tiết sản phẩm. Nhóm dùng Redis pub/sub để phát sự kiện xóa cache cho cả hai trang.

## Bản sửa đầu tiên vẫn sai

Trên staging, tôi gặp một lỗi dễ bỏ sót: sự kiện xóa cache chạy trước khi transaction ghi giá commit. Request tiếp theo đọc dữ liệu cũ từ database rồi nạp giá cũ trở lại cache.

Bản sửa lúc đầu vẫn cho kết quả sai, dù sự kiện xóa cache đã được phát. Vấn đề nằm ở thứ tự: cache bị xóa trước khi dữ liệu mới được commit.

Nhóm chuyển việc phát sự kiện sang sau khi transaction commit. Nhờ vậy, khi cache được xóa và request tiếp theo cần nạp lại giá, giá mới đã được ghi xong.

## Những gì chúng tôi giữ lại

Bản sửa mất 3 ngày để triển khai. Sau khi thay đổi, tỉ lệ cache hit giảm từ 97% xuống 92%. Độ trễ cập nhật giá xuống dưới 1 giây, còn TTL 60 giây làm lưới an toàn nếu sự kiện bị mất.

Tôi không còn xem TTL là cách duy nhất để giữ cache đúng với database. TTL vẫn có ích, nhưng khi giá thay đổi, việc xóa cache theo sự kiện mới là phần giúp cập nhật nhanh. Và thứ tự phát sự kiện cũng quan trọng: hãy phát sau khi transaction commit.