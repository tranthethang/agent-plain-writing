# Cache giá cũ trong 12 phút và 40 đơn đặt nhầm

Tôi từng nghĩ đặt TTL 15 phút cho cache là cách nhanh nhất để giảm tải database. Mọi thứ chạy ổn suốt 2 tháng, cho tới 9 giờ sáng thứ Sáu, khi giá sản phẩm đổi trong đợt giảm giá.

Khách vẫn thấy giá cũ trong 12 phút. Kết quả là 40 đơn được đặt nhầm. Nhóm tôi gọi lại cho từng khách trong một buổi chiều.

Điều làm tôi ngại nhất là lỗi này không đến từ một hệ thống phức tạp. Chúng tôi chỉ có hai trang đọc cache giá: trang danh sách và trang chi tiết sản phẩm. Nhưng khi lưu lượng tăng gấp 3 lần, TTL cố định 15 phút đã để dữ liệu cũ tồn tại lâu hơn mức chúng tôi có thể chấp nhận.

## Vì sao giảm TTL chưa giải quyết được vấn đề

Phản ứng đầu tiên của tôi là giảm TTL xuống 15 giây. Cách này có vẻ đơn giản: cache hết hạn nhanh hơn thì giá mới sẽ xuất hiện sớm hơn.

Nhưng tải database tăng gấp 2 lần. Chúng tôi bỏ cách đó.

Bài học của tôi là TTL ngắn hơn không tự động giải quyết được mọi vấn đề. Nó rút ngắn thời gian cache có thể giữ dữ liệu cũ, nhưng cũng làm database phải nhận thêm tải. Với trường hợp của chúng tôi, đó không phải đánh đổi có thể chấp nhận.

## Xóa cache khi giá được cập nhật

Bản sửa tiếp theo là xóa cache theo sự kiện cập nhật giá, thay vì chờ TTL 15 phút hết hạn. Chúng tôi dùng Redis pub/sub để phát sự kiện xóa cache. Khi giá được cập nhật, cache liên quan được xóa; lần đọc sau đó sẽ lấy giá mới.

Sau khi sửa, độ trễ cập nhật giảm xuống dưới 1 giây. TTL không còn là cơ chế chính để chờ giá mới xuất hiện. Chúng tôi đặt TTL dự phòng ở 60 giây, để giới hạn thời gian dữ liệu cũ có thể tồn tại nếu sự kiện bị mất.

Có một lỗi mà bản thử đầu tiên của chúng tôi chưa bắt được.

## Sự kiện phát trước khi transaction commit

Trên staging, sự kiện xóa cache chạy trước khi transaction ghi giá commit. Request kế tiếp đọc dữ liệu và nạp lại giá cũ vào cache. Cache đã bị xóa, nhưng thời điểm xóa lại không đúng.

Tôi đã sửa thứ tự: chỉ phát sự kiện sau khi transaction commit. Như vậy, khi request tiếp theo nạp lại cache, dữ liệu mới đã được ghi xong.

Đây là phần tôi đã đánh giá thấp lúc đầu. Xóa cache theo sự kiện nghe có vẻ đúng, nhưng nếu phát sự kiện trước khi dữ liệu commit thì lần nạp cache kế tiếp vẫn có thể lấy giá cũ.

## Cái giá của bản sửa

Bản sửa mất 3 ngày để triển khai. Tỉ lệ cache hit giảm từ 97% xuống 92%. Đó là mức giảm chúng tôi chấp nhận để giá được cập nhật dưới 1 giây, thay vì để khách thấy giá cũ trong nhiều phút.

Nếu tôi làm lại, tôi sẽ không bắt đầu bằng cách chỉ giảm TTL. Tôi sẽ kiểm tra cả thời điểm phát sự kiện so với transaction commit, rồi giữ TTL ngắn làm lưới an toàn. Với hệ thống của chúng tôi, sự kết hợp giữa xóa cache sau commit và TTL dự phòng 60 giây phù hợp hơn TTL cố định 15 phút.