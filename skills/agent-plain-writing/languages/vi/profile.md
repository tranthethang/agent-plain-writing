# Hồ sơ ngôn ngữ: tiếng Việt (vi)

Các con số nằm trong `profile.json`. File này giải thích cách dùng.

## Đơn vị đếm

- Script đếm theo **tiếng** (âm tiết, tách bằng khoảng trắng).
- 1 từ ≈ 1,4 tiếng. Câu 20 từ ≈ 28 tiếng.
- Độ dài bài blog (600–800 từ) được quy đổi từ tiếng sang từ.

## Ngưỡng theo loại văn bản

| Loại | Câu tối đa (tiếng) | Đoạn tối đa (câu) | Độ dài | Thuật ngữ |
|---|---|---|---|---|
| blog | 28 | 3 | 600–800 từ | không giới hạn (dùng `--non-tech` thì ≤ 3) |
| prose | 40 | 6 | tùy | không giới hạn |
| poetry | không áp dụng | không áp dụng | tùy | không giới hạn |
| design | 25 | 3 | theo template | không giới hạn |
| guide | 16 | 3 | tùy | ≤ 3 |

Đây là điểm khởi đầu. Chạy thử trên bài thật rồi chỉnh `profile.json`.

## Giọng và xưng hô

- Blog: xưng "tôi", gọi người đọc là "bạn".
- Guide: gọi người đọc là "bạn". Tên nút in đậm, đúng nhãn trên màn hình.
- Design: chủ ngữ rõ ("Hệ thống...", "Client..."). Không xưng "tôi" hay "bạn".
- Prose: theo điểm nhìn đã chọn. Không đổi giữa chừng.

## Từ chỉ mức bắt buộc (detail design)

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
