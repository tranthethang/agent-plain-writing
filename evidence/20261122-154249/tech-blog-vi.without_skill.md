# Cache giá cũ suốt 12 phút: bài học từ 40 đơn đặt nhầm

Tôi từng nghĩ đặt TTL 15 phút cho trang danh sách sản phẩm là cách nhanh để giảm tải database. Cách đó chạy ổn suốt 2 tháng, cho tới 9 giờ sáng thứ Sáu, khi giá sản phẩm thay đổi trong đợt giảm giá.

Lưu lượng lúc đó tăng gấp 3 lần. Nhưng cache vẫn giữ giá cũ, và khách tiếp tục nhìn thấy giá đó trong 12 phút. Kết quả là có 40 đơn được đặt nhầm. Chiều hôm ấy, nhóm tôi gọi lại cho từng khách để xử lý.

## Giảm TTL xuống 15 giây không phải lời giải

Phản ứng đầu tiên của tôi là rút TTL xuống còn 15 giây. Tôi muốn giá cũ tồn tại trong cache ít thời gian hơn. Nhưng tải database tăng gấp 2 lần, nên chúng tôi bỏ cách này.

Nhìn lại, vấn đề không chỉ là TTL dài hay ngắn. Giá có thể đổi đột ngột, còn cache theo thời gian cố định thì không biết điều đó vừa xảy ra. TTL 15 phút khiến giá cũ tồn tại quá lâu; TTL 15 giây lại đẩy thêm tải sang database.

## Xóa cache theo sự kiện cập nhật giá

Bản sửa của chúng tôi là xóa cache khi giá được cập nhật, thay vì chờ TTL hết hạn. Hai trang đọc cache giá là trang danh sách và trang chi tiết sản phẩm. Sự kiện được phát qua Redis pub/sub để cache được xóa sau lần cập nhật giá.

Trên staging, bản sửa đầu tiên vẫn sai: sự kiện xóa cache chạy trước khi transaction ghi giá commit. Request kế tiếp nạp lại giá cũ vào cache. Tôi đã bỏ sót thứ tự giữa việc phát sự kiện và commit transaction.

Chúng tôi chuyển việc phát sự kiện sang sau khi transaction commit. Sau đó, độ trễ cập nhật giá xuống dưới 1 giây.

## TTL vẫn cần làm lưới an toàn

Chúng tôi giữ TTL dự phòng 60 giây. Nếu sự kiện bị mất, cache vẫn hết hạn thay vì giữ giá cũ vô thời hạn.

Đổi lại, tỉ lệ cache hit giảm từ 97% xuống 92%. Với nhóm tôi, mức giảm đó chấp nhận được so với việc khách thấy giá cũ trong nhiều phút. Bản sửa mất 3 ngày để triển khai.

Bài học của tôi khá cụ thể: TTL hữu ích, nhưng không nên là cách duy nhất để phản ánh thay đổi giá. Nếu dữ liệu cần cập nhật ngay, hãy xóa cache theo sự kiện—và nhớ chỉ phát sự kiện sau khi transaction đã commit.