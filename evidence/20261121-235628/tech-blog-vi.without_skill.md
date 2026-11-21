# TTL 15 phút khiến 40 đơn hàng dùng giá cũ

Tôi từng nghĩ tăng TTL lên 15 phút là cách nhanh nhất để giảm tải database. Cách đó chạy ổn suốt 2 tháng, cho tới 9 giờ sáng thứ Sáu, khi giá sản phẩm đổi trong một đợt giảm giá.

Lưu lượng lúc đó tăng gấp 3 lần. Khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn. Nhóm tôi phải gọi lại cho từng khách trong một buổi chiều.

## Vì sao giảm TTL không giải quyết được

Phản ứng đầu tiên của tôi là giảm TTL từ 15 phút xuống 15 giây. Giá mới sẽ lên cache nhanh hơn, tôi nghĩ vậy. Nhưng tải database tăng gấp đôi, nên chúng tôi bỏ cách này.

Vấn đề không chỉ là TTL quá dài. Khi giá thay đổi đột ngột, cache vẫn giữ dữ liệu cũ cho đến khi hết hạn. Chúng tôi cần cập nhật cache ngay khi giá được ghi mới, nhưng vẫn phải có TTL làm lưới an toàn.

## Xóa cache khi giá đổi

Chúng tôi sửa để xóa cache theo sự kiện cập nhật giá, rồi đặt TTL dự phòng là 60 giây. Khi cache được nạp lại sau sự kiện, khách thấy giá mới trong chưa đầy 1 giây.

Cache giá được dùng ở hai trang: danh sách sản phẩm và chi tiết sản phẩm. Trước khi sửa, tỉ lệ cache hit là 97%; sau khi chuyển sang TTL ngắn hơn, con số này còn 92%. Đổi lại, cache không còn phải chờ hết TTL mới phản ánh giá mới.

Bản sửa đầu tiên của tôi còn sai. Trên staging, sự kiện xóa cache qua Redis pub/sub chạy trước khi transaction ghi giá commit. Request kế tiếp nạp lại giá cũ vào cache.

Tôi đã chuyển việc phát sự kiện sang sau khi transaction commit. Như vậy, khi cache bị xóa và được nạp lại, giá mới đã được ghi xong.

## TTL vẫn là lưới an toàn

Xóa cache theo sự kiện giúp giảm độ trễ cập nhật, nhưng chúng tôi vẫn giữ TTL 60 giây phòng khi sự kiện bị mất. Bản sửa mất 3 ngày để triển khai.

Bài học của tôi: TTL cố định tiện để giảm tải database, nhưng không đảm bảo dữ liệu sẽ cập nhật kịp khi giá đổi đột ngột. Nếu dùng sự kiện để xóa cache, hãy kiểm tra thời điểm phát sự kiện so với lúc transaction commit. Ngược lại, nếu chỉ giảm TTL thật thấp, database có thể phải gánh thêm tải—như lần chúng tôi thử 15 giây và thấy tải tăng gấp đôi.