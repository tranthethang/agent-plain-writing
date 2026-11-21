# Hồ sơ ngôn ngữ: tiếng Việt (vi)

Các con số nằm trong `profile.json`. File này giải thích cách dùng.

## Đơn vị đếm

- Script đếm theo **tiếng** (âm tiết, tách bằng khoảng trắng).
- 1 từ ≈ 1,4 tiếng. Câu 20 từ ≈ 28 tiếng.
- Độ dài (`length`) được quy đổi từ tiếng sang từ.

## Ngưỡng và giọng

Mọi con số (câu, đoạn, độ dài, thuật ngữ) nằm trong `profile.json`. File này không nhắc lại số.
Giọng, người xưng và cấu trúc do `doc-types/<loại>.md` quyết định. Ngôn ngữ chỉ cho dạng từ:

- Ngôi thứ nhất: "tôi". Gọi người đọc: "bạn".
- Tên nút in đậm, đúng nhãn trên màn hình.

## Từ chỉ mức bắt buộc (API design)

| Mức | Dùng từ |
|---|---|
| Bắt buộc | phải |
| Cấm | không được |
| Khuyến nghị | nên |
| Tùy chọn | có thể |

Mỗi mức một từ. Dùng nhất quán cả tài liệu.

## Thuật ngữ

- Người đọc là dev: giữ nguyên tên kỹ thuật tiếng Anh (API, token, cache). Một khái niệm một tên.
- Người đọc ngoài ngành: thay bằng bảng trong `examples/user-guide.md`.

## Bẫy hay gặp trong tiếng Việt

- Danh từ hóa động từ: "việc", "sự", "thực hiện việc", "tiến hành".
- Câu bị động kéo dài với "được".
- Cụm nối thừa: "bên cạnh đó", "ngoài ra" mở đầu câu liên tục.
- Tính từ rỗng: "toàn diện", "mạnh mẽ", "tối ưu".
- Số: dùng dấu chấm ngăn nghìn (200.000), dấu phẩy thập phân (1,5). Chọn một kiểu và giữ nguyên.
