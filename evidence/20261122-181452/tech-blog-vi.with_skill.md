# Tôi chuyển sự kiện xóa cache sang sau khi commit

Lúc 9 giờ sáng thứ Sáu, giá sản phẩm đổi trong đợt giảm giá nhưng khách vẫn thấy giá cũ suốt 12 phút. Họ đặt nhầm 40 đơn.

## TTL 15 phút không theo kịp giá

Tôi từng đặt TTL 15 phút cho trang danh sách sản phẩm để giảm tải database. Cách này chạy ổn suốt 2 tháng, đến khi lưu lượng tăng gấp 3 lần trong đợt giảm giá.

Cache vẫn giữ giá cũ sau khi giá mới được ghi. Nhóm tôi gọi lại cho từng khách trong một buổi chiều để xử lý 40 đơn đặt nhầm.

## TTL 15 giây làm tải database tăng

Thử đầu tiên của tôi là giảm TTL xuống 15 giây. Tải database tăng gấp 2 lần, nên nhóm bỏ cách đó.

Chúng tôi chuyển sang xóa cache khi có sự kiện cập nhật giá, đồng thời giữ TTL dự phòng 60 giây. Cache hit giảm từ 97% xuống 92% sau thay đổi này.

## Phát sự kiện sau khi commit

Bản sửa đầu tiên vẫn sai trên staging. Sự kiện xóa cache chạy trước khi transaction ghi giá commit, nên request kế tiếp nạp lại giá cũ vào cache.

Tôi chuyển thời điểm phát sự kiện sang sau khi transaction commit. Nhóm dùng Redis pub/sub để phát sự kiện; khi giá đổi, cache được xóa và cập nhật trong dưới 1 giây.

## Cùng xử lý hai trang đọc giá

Trang danh sách và trang chi tiết sản phẩm đều đọc cache giá. Nhóm áp dụng việc xóa cache theo sự kiện cho cả hai trang.

Bản sửa mất 3 ngày để triển khai. TTL 60 giây vẫn ở đó để làm lưới an toàn nếu sự kiện bị mất.

Khi giá có thể đổi đột ngột, hãy xóa cache sau khi transaction commit và giữ TTL dự phòng ngắn.