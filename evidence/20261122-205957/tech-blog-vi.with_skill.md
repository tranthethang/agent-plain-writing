# Tôi chuyển việc xóa cache sang sau khi commit

Suốt hai tháng, cache 15 phút giúp trang danh sách sản phẩm giảm tải database. Sáng thứ Sáu, lúc 9 giờ, giá đổi trong đợt giảm giá nhưng khách vẫn thấy giá cũ suốt 12 phút. Có 40 đơn bị đặt nhầm.

## TTL ngắn hơn chưa giải quyết được việc

Lưu lượng tăng gấp 3 lần trong đợt giảm giá. Tôi thử hạ TTL xuống 15 giây để giá mới xuất hiện sớm hơn. Nhưng tải database tăng gấp đôi, nên nhóm bỏ cách đó.

Tôi đã dùng thời gian hết hạn để xử lý một thay đổi giá xảy ra đột ngột. Cách này vừa không cập nhật giá ngay, vừa khiến database chịu tải cao hơn khi TTL ngắn.

## Xóa cache khi giá đổi

Nhóm chuyển sang xóa cache khi có sự kiện cập nhật giá. Cache của trang danh sách và trang chi tiết sản phẩm đều được xóa theo sự kiện qua Redis pub/sub. TTL 60 giây vẫn được giữ làm dự phòng nếu sự kiện bị mất.

Sau khi sửa, độ trễ cập nhật giá xuống dưới 1 giây. Tỉ lệ cache hit giảm từ 97% xuống 92%. Nhóm triển khai bản sửa trong 3 ngày. Chúng tôi cũng gọi lại cho từng khách có đơn đặt nhầm trong một buổi chiều.

## Bản sửa đầu tiên vẫn nạp giá cũ

Trên staging, tôi thấy request kế tiếp vẫn nạp giá cũ vào cache. Sự kiện xóa cache chạy trước khi transaction ghi giá commit. Vì vậy, cache được nạp lại trước khi giá mới được lưu xong.

Nhóm chuyển thời điểm phát sự kiện sang sau khi transaction commit. Lúc đó, request nạp lại cache mới đọc được giá đã cập nhật. Bản sửa đầu tiên của tôi sai vì tôi chưa đặt việc phát sự kiện đúng sau commit.

## Chọn đúng lúc để xóa cache

Nếu giá có thể đổi đột ngột, đừng chỉ trông vào TTL để đưa giá mới lên cache. Hãy xóa cache sau khi transaction commit và giữ TTL ngắn làm phương án dự phòng.

<!-- report -->
Tôi giả định người kể là thành viên trong nhóm, theo giọng “tôi” trong yêu cầu.