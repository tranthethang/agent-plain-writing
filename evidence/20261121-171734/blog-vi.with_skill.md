# Tôi để cache giữ giá cũ suốt 12 phút

Sáng thứ Sáu, lúc 9 giờ, nhóm tôi đổi giá cho đợt giảm giá. Khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn.

## TTL 15 phút trông có vẻ ổn

Tôi từng nghĩ đặt TTL 15 phút là cách nhanh nhất để giảm tải database. Cache chạy ổn suốt hai tháng, nên tôi không thấy lý do phải đổi cách làm.

Nhưng trong đợt giảm giá, lưu lượng tăng gấp ba lần. Cache theo thời gian cố định không biết giá đã đổi, nên khách vẫn nhận dữ liệu cũ cho đến khi cache hết hạn.

## Xóa cache khi giá đổi

Nhóm tôi sửa luồng cập nhật giá để xóa cache theo sự kiện. Khi ghi giá mới, hệ thống xóa cache liên quan. Độ trễ cập nhật giảm xuống dưới một giây.

Cách này xử lý được tình huống giá đổi đột ngột. Tôi đã dựa quá nhiều vào TTL và xem nhẹ việc dữ liệu có thể thay đổi trước khi cache hết hạn.

## Giữ TTL làm lưới an toàn

Nhóm tôi vẫn giữ TTL, nhưng giảm xuống còn 60 giây. Nếu sự kiện cập nhật bị mất, cache sẽ không giữ giá cũ quá lâu.

TTL ngắn không thay thế việc xóa cache theo sự kiện. Nó chỉ giới hạn thời gian dữ liệu cũ có thể tồn tại khi sự kiện không đến được nơi cần xử lý.

## Kiểm tra luồng đổi dữ liệu

Nếu dịch vụ của bạn cache dữ liệu có thể đổi đột ngột, hãy kiểm tra điều gì xảy ra ngay sau khi ghi dữ liệu mới. Đừng chỉ dựa vào TTL để giữ cache khớp với database.