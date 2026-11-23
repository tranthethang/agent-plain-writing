# Ví dụ tiếng Việt: tech-blog

Mẫu riêng cho tiếng Việt. Cấu trúc nằm trong phần loại văn bản của `SKILL.md`, ngưỡng nằm trong `profile.json`.

## Cặp xấu → tốt

Ví dụ minh họa. Chi tiết trong câu chuyện là bịa để làm mẫu. Khi viết thật, dùng chuyện của tác giả.

### 1. Mở bài

**Bad:** Trong thế giới công nghệ phát triển không ngừng như hiện nay, việc quản lý trạng thái trong ứng dụng React đóng vai trò vô cùng quan trọng. Hãy cùng tìm hiểu nhé!
**Good:** Tuần trước, một nút bấm trong app React của tôi cập nhật chậm hai giây. Nguyên nhân: tôi nhét mọi thứ vào một state toàn cục.

### 2. Giải thích khái niệm

**Bad:** Cache là một cơ chế lưu trữ tạm thời nhằm mục đích tăng tốc độ truy xuất dữ liệu bằng cách lưu giữ các bản sao của dữ liệu thường xuyên được truy cập.
**Good:** Cache là bản sao lưu sẵn của dữ liệu hay dùng. Lần sau cần, hệ thống lấy bản sao, không phải tính lại.

### 3. Ý kiến cá nhân

**Bad:** Có thể nói rằng việc sử dụng TypeScript mang lại nhiều lợi ích đáng kể trong quá trình phát triển phần mềm.
**Good:** Từ khi chuyển sang TypeScript, trình soạn thảo báo lỗi kiểu dữ liệu ngay lúc tôi gõ. Tôi không còn đợi đến lúc chạy mới biết.

### 4. Điều rút ra

**Bad:** Qua trải nghiệm này, chúng ta có thể rút ra nhiều bài học quý giá về tầm quan trọng của việc lập kế hoạch.
**Good:** Tôi mất cả buổi chiều chỉ vì lao vào code mà không viết plan 10 phút trước. Từ hôm đó, tôi không bỏ qua bước này nữa.

### 5. Chuyển mục

**Bad:** Bên cạnh đó, một vấn đề khác cũng cần được lưu ý là việc xử lý lỗi.
**Good:** (dùng tiêu đề mục) `## Lỗi thứ hai: không xử lý lỗi`

### 6. Tính từ thành chi tiết

**Bad:** Giao diện mới rất đẹp, hiện đại và thân thiện với người dùng.
**Good:** Giao diện mới mỗi màn hình chỉ có một nút chính. Người dùng không phải đoán bấm gì.

### 7. Câu nhồi ý

**Bad:** Công cụ này, vốn được phát triển nhằm hỗ trợ lập trình viên trong việc quản lý các phiên làm việc với AI, cho phép lưu lại lịch sử và đồng thời giúp chuyển giao giữa các agent một cách liền mạch.
**Good:** Công cụ này giúp tôi quản lý phiên làm việc với AI. Nó lưu lại lịch sử. Agent này làm tiếp được việc của agent khác.

### 8. Lời khuyên chung chung

**Bad:** Chúng ta nên luôn luôn chú ý đến chất lượng mã nguồn để đảm bảo tính bền vững lâu dài của dự án.
**Good:** Đặt một quy tắc: không merge nếu test đỏ. Quy tắc này cứu tôi ba lần trong tháng qua.

### 9. Thừa nhận giới hạn

**Bad:** Giải pháp này tuy có thể còn một số hạn chế nhất định nhưng nhìn chung vẫn mang lại hiệu quả tương đối tốt.
**Good:** Giải pháp này chưa xử lý được trường hợp mất mạng giữa chừng. Tôi chưa tìm ra cách gọn hơn.

### 10. Cắt mất câu nêu nguyên nhân

(Brief: timeout tăng từ 30 lên 120 giây, hàng đợi vẫn nghẽn, mỗi batch vẫn đọc 50.000 bản ghi.)

**Bad:** Tăng timeout không làm hết nghẽn.
**Good:** Tăng timeout không làm hết nghẽn. Mỗi batch vẫn đọc 50.000 bản ghi, nên chờ lâu hơn chỉ cho lần đọc chậm đó thêm thời gian.
**Fault:** Câu kết luận đứng một mình. Người đọc không thấy vì sao thay đổi không có tác dụng.
**Fix:** Giữ câu nối nguyên nhân, thay đổi và kết quả.

### 11. Tiêu đề khẩu hiệu

**Bad:** `## Cái giá ẩn của sự tiện lợi`
**Good:** `## Vì sao state dùng chung làm chậm biểu mẫu`

## Bài mẫu hoàn chỉnh (khoảng 610 từ)

```markdown
# Tôi bỏ state toàn cục sau một buổi chiều mất trắng

Nút "Lưu" trong app của tôi phản hồi chậm hai giây sau mỗi lần người dùng gõ phím. Tôi mất cả buổi chiều đổ lỗi cho server trước khi nhận ra lỗi nằm ngay ở cái store toàn cục mình từng tự hào.

## Lúc đầu mọi thứ trông rất gọn

Ba tháng trước, trang cài đặt chỉ có bốn ô nhập: tên, email, múi giờ và ngôn ngữ. Tôi gom cả bốn vào một state toàn cục để khỏi phải truyền prop qua ba tầng component lồng nhau.

Cách làm này chạy mượt đến mức tôi thấy mình thông minh hẳn ra. Mỗi lần thêm tính năng mới, tôi lại ném thêm vài trường vào đúng chỗ cũ. Tôi cứ nghĩ đằng nào dữ liệu cũng thuộc về màn hình cài đặt.

Trong các buổi review code, không ai phản đối vì mọi thứ vẫn chạy bình thường. Số lượng dữ liệu còn ít nên máy tính xử lý xong trong nháy mắt. Sự trơn tru đó khiến tôi chủ quan suốt hai tháng liền.

Hai tháng sau, trang đó phình lên 40 ô nhập, kèm ba bảng chọn ngày và một khung xem trước. Không ai trong nhóm để ý, cho đến khi QA gửi video quay cảnh con trỏ chuột đứng khựng lại. Mỗi lần gõ một chữ, màn hình đứng im gần hai giây rồi mới hiện ra.

## Hai tiếng tìm lỗi nhầm chỗ

Phản xạ đầu tiên của tôi là mở tab Network để xem API nào đang treo. Toàn bộ request trả về dưới 80 ms, không một lỗi 500 nào xuất hiện. Tôi thậm chí còn gọi sang bạn backend để hỏi xem server có vừa đổi giới hạn gì không.

Bạn ấy kiểm tra log xong liền gửi lại ảnh chụp màn hình xanh lè, không một cảnh báo chậm. Thậm chí truy vấn nặng nhất trong cơ sở dữ liệu cũng chỉ mất 15 ms để phản hồi.

Tôi đành quay sang nghi ngờ trình duyệt thiếu bộ nhớ rồi thử tắt hết extension. Nút "Lưu" vẫn ì ạch như cũ.

Phải đến 4 giờ chiều, tôi mới mở React DevTools Profiler lên ghi lại một lần gõ phím. Màn hình hiện ra một màu đỏ rực: toàn bộ 40 ô nhập đều vẽ lại cùng lúc.

Chỉ cần sửa một chữ trong ô tên, cây component lại chạy lại từ gốc đến ngọn. Khung xem trước nặng nhất cũng tính toán lại theo, dù chẳng liên quan gì đến tên người dùng. Ba bảng chọn ngày cũng dựng lại toàn bộ lịch tháng chỉ vì một ký tự thay đổi ở tận góc trên.

## Cách tôi tách lại từng phần

Tôi tắt trình soạn thảo đi và ngồi vẽ ra giấy xem ô nhập nào thật sự cần nói chuyện với ô nào. Hóa ra phần lớn các nhóm cài đặt đều đứng độc lập với nhau. Chỉ có hai ô liên quan đến quyền hạn là cần đọc dữ liệu từ phần tài khoản.

Thay vì giữ một khối lớn, tôi tách state về đúng từng form con để mỗi phần tự giữ dữ liệu của mình. Những thứ dùng chung cho cả app như thông tin đăng nhập và ngôn ngữ hiển thị vẫn ở lại chỗ cũ. Phần xem trước chỉ đọc dữ liệu từ form đang mở thay vì lắng nghe cả cây state khổng lồ như trước.

Công việc mất đúng một buổi sáng, chủ yếu là xóa bớt các hook nối dây chằng chịt. Tôi giữ nguyên tên các trường dữ liệu để không làm hỏng phần lưu tạm trên trình duyệt. Nhờ vậy, người dùng đang nhập dở cũng không bị mất chữ khi bản cập nhật mới chạy lên.

Sau khi tách xong, tôi mở Profiler đo lại trên đúng thao tác gõ phím ban đầu. Thời gian vẽ lại giảm từ 1.800 ms xuống còn 12 ms, và con trỏ không còn khựng lại giữa chừng.

## Thứ vẫn còn vướng

Cách tách này giải quyết xong chuyện chậm, nhưng chưa phải phép màu cho mọi trường hợp. Khi hai tab khác nhau cần kiểm tra chéo dữ liệu trước lúc gửi lên server, tôi vẫn phải viết thêm một lớp nối nhỏ ở component cha.

Lớp nối đó trông hơi thủ công và tôi chưa tìm ra cách nào gọn hơn. Nếu gom lên lại store chung thì lại quay về vết xe đổ cũ. Với 20 form độc lập, tách nhỏ là đường thẳng nhất, còn với một bảng tính liên kết chằng chịt thì câu chuyện lại khác.

## Đừng hỏi chỗ nào tiện tay

Sai lầm của tôi không nằm ở thư viện quản lý state, mà nằm ở câu hỏi tôi đặt ra lúc mới code. Tôi đã hỏi "nhét dữ liệu vào đâu cho đỡ phải truyền nhiều tầng", thay vì hỏi "ai thật sự cần đọc dữ liệu này".

Hôm nay bạn thử mở dự án đang làm và đếm số trường nằm trong state toàn cục. Nếu con số vượt quá 5 mà không phải dữ liệu dùng chung cho cả app, hãy tách bớt trước khi nó làm chậm nút "Lưu" của bạn.
```

## Mẫu của bạn (thêm vào đây)

<!-- Dán đoạn bạn viết hoặc đã sửa ưng ý. Thêm cặp Bad / Good từ các bài AI viết dở. -->
