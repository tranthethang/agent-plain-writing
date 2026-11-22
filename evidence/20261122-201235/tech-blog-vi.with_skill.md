# Tôi chuyển sự kiện xóa cache sang sau commit

Thứ Sáu, lúc 9 giờ sáng, nhóm tôi đổi giá sản phẩm. Khách vẫn thấy giá cũ suốt 12 phút và đặt nhầm 40 đơn.

## TTL 15 phút che mất giá mới

Tôi từng nghĩ TTL 15 phút sẽ giảm tải database. Cách này chạy ổn suốt 2 tháng, cho đến khi lưu lượng tăng gấp 3 lần trong đợt giảm giá.

Cache giá phục vụ cả trang danh sách lẫn trang chi tiết sản phẩm. Trước sự cố, tỉ lệ cache hit đạt 97%. Nhưng khi giá đổi đột ngột, thời hạn cache cố định khiến khách tiếp tục thấy dữ liệu cũ.

Nhóm tôi gọi lại cho từng khách trong một buổi chiều để xử lý 40 đơn đặt nhầm. Sau đó, tôi thử hạ TTL xuống 15 giây. Tải database tăng gấp đôi, nên nhóm bỏ cách này.

## Xóa cache theo sự kiện

Nhóm chuyển sang xóa cache khi có cập nhật giá. Khi thử trên staging, bản sửa đầu tiên vẫn nạp giá cũ: sự kiện xóa cache chạy trước khi transaction ghi giá commit.

Request kế tiếp đọc database trước khi giá mới được ghi xong, rồi đưa giá cũ trở lại cache. Tôi đã đặt sai thứ tự giữa việc ghi giá và phát sự kiện.

Tôi chuyển sự kiện sang thời điểm sau commit. Nhóm dùng Redis pub/sub để phát sự kiện, rồi xóa cache giá khi nhận được tin cập nhật. Sau sửa đổi này, độ trễ cập nhật giảm xuống dưới 1 giây.

## TTL ngắn làm lưới an toàn

Nhóm vẫn giữ TTL 60 giây. Nếu sự kiện bị mất, cache cũ sẽ hết hạn trong tối đa 60 giây thay vì giữ giá sai suốt 15 phút.

Sau bản sửa, tỉ lệ cache hit giảm từ 97% xuống 92%. Nhóm mất 3 ngày để triển khai thay đổi. Tôi chấp nhận mức giảm đó để giá mới đến cache nhanh hơn.

Trước khi đổi TTL để xử lý dữ liệu cũ, hãy kiểm tra tải database. Nếu xóa cache theo sự kiện, hãy phát sự kiện sau khi transaction commit.