# Cache giá cũ trong 12 phút: bài học từ 40 đơn đặt nhầm

Tôi từng nghĩ đặt TTL 15 phút cho cache trang danh sách sản phẩm là cách nhanh nhất để giảm tải database. Mọi thứ chạy ổn suốt 2 tháng, cho tới sáng thứ Sáu, lúc 9 giờ, khi giá sản phẩm thay đổi.

Lưu lượng khi đó tăng gấp 3 lần. Khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn. Chiều hôm đó, nhóm tôi gọi lại cho từng khách để xử lý. Đây là một sự cố do chính lựa chọn cache của chúng tôi gây ra.

## TTL ngắn hơn chưa phải lời giải

Phản ứng đầu tiên của tôi là giảm TTL từ 15 phút xuống 15 giây. Cách này giúp cache hết hạn nhanh hơn, nhưng tải database tăng gấp đôi. Với lưu lượng đang cao, đó không phải cái giá chúng tôi muốn trả, nên nhóm bỏ phương án này.

Vấn đề là giá có thể đổi đột ngột, còn TTL cố định thì không biết điều đó vừa xảy ra. Chờ cache tự hết hạn đồng nghĩa với việc khách có thể tiếp tục đọc dữ liệu cũ trong một khoảng thời gian đáng kể.

## Xóa cache khi giá được cập nhật

Chúng tôi chuyển sang xóa cache theo sự kiện cập nhật giá, qua Redis pub/sub. Khi giá thay đổi, cache liên quan được xóa để request tiếp theo nạp dữ liệu mới. Sau khi sửa, độ trễ cập nhật giảm xuống dưới 1 giây.

Có hai trang đọc cache giá: trang danh sách sản phẩm và trang chi tiết sản phẩm. Trước khi sửa, tỉ lệ cache hit là 97%; sau khi chuyển sang xóa cache theo sự kiện, con số này còn 92%. Nhóm chấp nhận mức giảm đó để khách không phải chờ TTL hết hạn mới thấy giá mới.

Tuy vậy, bản sửa đầu tiên của tôi vẫn sai.

Trên staging, sự kiện xóa cache chạy trước khi transaction ghi giá commit. Request kế tiếp thấy cache đã bị xóa, nhưng transaction chưa commit; nó nạp lại giá cũ vào cache. Tôi đã xóa cache đúng lúc… để rồi cache chứa lại dữ liệu cũ.

Chúng tôi chuyển việc phát sự kiện sang sau khi transaction commit. Như vậy, khi cache bị xóa và có request đọc lại, giá mới đã được ghi xong.

## TTL vẫn cần thiết làm phương án dự phòng

Xóa cache theo sự kiện giảm độ trễ cập nhật, nhưng chúng tôi vẫn giữ TTL 60 giây làm lưới an toàn nếu sự kiện bị mất. Đây không phải cách xử lý chính cho mỗi lần đổi giá; nó giới hạn thời gian dữ liệu cũ có thể còn trong cache khi cơ chế sự kiện không hoạt động như dự kiến.

Bản sửa mất 3 ngày để triển khai. Nhìn lại, tôi đã dựa quá nhiều vào TTL 15 phút vì hệ thống chạy êm trong 2 tháng. Nhưng khi giá đổi và lưu lượng tăng gấp 3 lần, sự êm đó không còn ý nghĩa.

Nếu bạn đang cache dữ liệu có thể đổi đột ngột, TTL cố định có thể chưa đủ. Tôi sẽ giữ TTL dự phòng, nhưng với giá sản phẩm, giờ đây tôi cũng xóa cache sau khi transaction cập nhật đã commit.