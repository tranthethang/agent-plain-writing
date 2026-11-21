# Tôi bỏ TTL cố định sau khi khách đặt nhầm 40 đơn

Khách vẫn thấy giá cũ sau đợt giảm giá, và 40 đơn được đặt nhầm theo mức giá đó. Tôi đã đặt TTL 15 phút để giảm tải database; cách này khiến cache giữ giá cũ lâu hơn mức nhóm chấp nhận được.

## Mười hai phút với giá cũ

Trong hai tháng, cache 15 phút chạy ổn cho trang danh sách sản phẩm. Đến 9 giờ sáng thứ Sáu, nhóm đổi giá trong đợt giảm giá. Khách vẫn thấy giá cũ trong 12 phút, rồi đặt nhầm 40 đơn.

TTL giới hạn thời gian một mục dữ liệu nằm trong cache trước khi hết hạn. Nó không tự biết giá trong database vừa đổi. Vì vậy, một giá trị cũ có thể tiếp tục được trả về cho đến khi cache hết hạn hoặc bị xóa.

Tôi đã chọn một khoảng thời gian cố định để giảm số lần đọc database. Lựa chọn đó có tác dụng với tải database, nhưng không xử lý được lúc giá đổi đột ngột. Khi khách cần giá mới, họ vẫn có thể đọc giá cũ từ cache.

Nhóm gọi lại từng khách có đơn đặt nhầm trong một buổi chiều. Việc đó xử lý các đơn bị ảnh hưởng, nhưng không thay đổi cách cache nhận biết giá đã cập nhật. Tôi cần sửa luồng cập nhật, thay vì chỉ chờ TTL hết hạn.

## TTL ngắn không sửa được nguyên nhân

Thử đầu tiên của tôi là giảm TTL xuống 15 giây. Cache hết hạn nhanh hơn, nên dữ liệu cũ ít nằm lại sau khi giá đổi. Nhưng database nhận tải gấp đôi, và nhóm bỏ cách đó.

Lưu lượng tăng gấp 3 lần, nên tăng số lần đọc database không phải lựa chọn tôi muốn giữ. TTL ngắn hơn đổi một vấn đề lấy một vấn đề khác: cache giữ dữ liệu cũ ít lâu hơn, nhưng database phải chịu thêm tải.

Vấn đề nằm ở chỗ TTL cố định không gắn với thời điểm cập nhật giá. Dù đặt TTL dài hay ngắn, cache vẫn chỉ tự hết hạn theo đồng hồ. Tôi muốn xóa mục giá ngay khi nhóm ghi giá mới.

## Xóa cache khi giá đổi

Nhóm chuyển sang xóa cache theo sự kiện cập nhật giá. Khi giá thay đổi, hệ thống phát sự kiện qua Redis pub/sub để xóa mục cache tương ứng. Cache không cần chờ TTL hết hạn mới bỏ giá cũ.

Cả trang danh sách sản phẩm lẫn trang chi tiết đều đọc cache giá. Vì vậy, thay đổi này cần làm mới dữ liệu cho cả hai nơi. Sau khi sửa, độ trễ cập nhật giá giảm xuống dưới một giây.

Tỉ lệ cache hit giảm từ 97% xuống 92%. Tôi chấp nhận mức giảm đó để giá mới xuất hiện sớm hơn, thay vì giữ mục cache cũ cho đến khi hết hạn. Nhóm vẫn giữ TTL 60 giây làm lưới an toàn nếu sự kiện bị mất.

## Sự kiện phải chạy sau commit

Bản sửa đầu tiên chưa chạy đúng trên staging. Sự kiện xóa cache chạy trước khi transaction ghi giá commit. Request kế tiếp đọc database khi giá mới chưa được ghi xong, rồi nạp giá cũ trở lại cache.

Tôi đã để việc xóa cache chạy quá sớm. Nhóm chuyển thời điểm phát sự kiện sang sau khi transaction commit. Như vậy, request nạp cache sau khi nhận sự kiện sẽ đọc giá đã ghi xong, thay vì nạp lại giá cũ.

Nhóm mất 3 ngày để triển khai bản sửa. Lần sau bạn đổi dữ liệu đang được cache, hãy gắn việc xóa cache với thời điểm ghi dữ liệu hoàn tất. TTL ngắn có thể giới hạn thời gian giữ dữ liệu cũ, nhưng không thay thế được bước đó.