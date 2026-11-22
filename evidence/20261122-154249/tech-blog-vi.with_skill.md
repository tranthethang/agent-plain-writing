# Tôi chuyển xóa cache giá sang sau khi transaction commit

Suốt 2 tháng, cache giá chạy ổn. Đến đợt giảm giá lúc 9 giờ sáng thứ Sáu, khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn.

## TTL ngắn hơn không giải quyết được

Trang danh sách sản phẩm dùng cache với TTL 15 phút để giảm tải database. Khi lưu lượng tăng gấp 3 lần, cách đặt TTL cố định không theo kịp thay đổi giá.

Tôi thử hạ TTL xuống 15 giây. Tải database tăng gấp đôi, nên chúng tôi bỏ cách đó. Giảm thời gian cache tồn tại cũng đồng nghĩa database phải xử lý nhiều lượt đọc hơn.

## Xóa cache khi giá đổi

Chúng tôi chuyển sang xóa cache khi có sự kiện cập nhật giá, rồi đặt TTL dự phòng 60 giây nếu sự kiện bị mất. Redis pub/sub phát sự kiện này. Cache giá được dùng trên cả trang danh sách và trang chi tiết sản phẩm.

Trên staging, bản sửa đầu tiên vẫn nạp giá cũ. Sự kiện xóa cache chạy trước khi transaction ghi giá commit. Request kế tiếp nạp lại giá cũ vào cache.

Tôi chuyển thời điểm phát sự kiện sang sau khi transaction commit. Sau thay đổi đó, độ trễ cập nhật giảm xuống dưới 1 giây.

## Đổi mới phải trả bằng gì

Bản sửa mất 3 ngày để triển khai. Tỉ lệ cache hit giảm từ 97% xuống 92%, nhưng cache vẫn giữ TTL dự phòng nếu sự kiện bị mất.

Chúng tôi gọi lại cho từng khách có đơn đặt nhầm trong một buổi chiều. Đó là phần xử lý không thể thay bằng một thay đổi trong cache.

Nếu bạn dùng cache cho giá sản phẩm, hãy phát sự kiện xóa cache sau khi transaction commit và giữ TTL dự phòng 60 giây.