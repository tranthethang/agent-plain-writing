# Cache giá sản phẩm: bài học từ 40 đơn đặt nhầm

Tôi từng nghĩ đặt TTL 15 phút cho cache danh sách sản phẩm là cách nhanh nhất để giảm tải database. Mọi thứ chạy ổn trong 2 tháng, cho tới sáng thứ Sáu, khi giá đổi lúc 9 giờ.

Trong đợt giảm giá, khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn. Khi lưu lượng tăng gấp 3 lần, sự cố này khiến tôi phải nhìn lại cách cache đang hoạt động.

## TTL cố định không biết giá vừa đổi

TTL 15 phút có vẻ hợp lý khi dữ liệu ít thay đổi. Nhưng giá sản phẩm có thể đổi đột ngột. Cache không tự biết database vừa có giá mới; nó tiếp tục trả dữ liệu cũ cho tới khi TTL hết hạn.

Đó là điều tôi đã bỏ qua. TTL giới hạn thời gian tồn tại của dữ liệu trong cache, nhưng không đảm bảo dữ liệu được cập nhật ngay sau khi giá thay đổi.

## Xóa cache khi ghi giá mới

Chúng tôi sửa bằng cách xóa cache theo sự kiện cập nhật giá. Khi ghi dữ liệu mới, cache liên quan được xóa ngay thay vì chờ TTL hết hạn. Sau thay đổi này, độ trễ cập nhật giảm xuống dưới 1 giây.

Cách làm này xử lý được phần chính của vấn đề: khách không phải đợi cache cũ tự hết hạn mới thấy giá mới.

## TTL ngắn làm lưới an toàn

Tôi vẫn không muốn phụ thuộc hoàn toàn vào sự kiện. Nếu sự kiện bị mất, cache có thể tiếp tục giữ dữ liệu cũ. Vì vậy, chúng tôi đặt TTL dự phòng 60 giây.

TTL ngắn không thay thế việc xóa cache theo sự kiện. Nó là lưới an toàn cho trường hợp sự kiện không đến được nơi cần xử lý.

Bài học của tôi khá đơn giản: cache theo thời gian cố định có thể làm dữ liệu lệch khi giá thay đổi bất ngờ. Hãy xóa cache khi ghi dữ liệu mới, rồi giữ TTL ngắn để phòng khi luồng sự kiện gặp trục trặc.