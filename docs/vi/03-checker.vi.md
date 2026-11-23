# Script kiểm tra

```bash
python3 skills/agent-plain-writing-tech-blog/scripts/check_style.py draft.md --lang en --type tech-blog
python3 skills/agent-plain-writing-api-design/scripts/check_style.py spec.md  --lang ja --type api-design
python3 skills/agent-plain-writing-user-guide/scripts/check_style.py guide.md --lang vi --type user-guide
python3 skills/agent-plain-writing-tech-blog/scripts/check_style.py post.md  --lang en --type tech-blog --non-tech
```

| Tùy chọn | Giá trị |
|---|---|
| `--lang` | `vi`, `en`, `ja`. Có thể bỏ nếu `PLAIN-WRITING.md` có `default_lang` |
| `--type` | `tech-blog`, `essay`, `api-design`, `user-guide`, `common`. Mặc định: `default_type` hoặc `common` |
| `--non-tech` | Giới hạn thuật ngữ còn 3. Loại `user-guide` luôn áp dụng giới hạn thuật ngữ |
| `--config` | Đường dẫn tới file `PLAIN-WRITING.md`. Mặc định: tìm ở thư mục hiện tại rồi các thư mục cha (dừng ở `.git`) |
| `--short-brief` | Dùng `length_short` cho loại có khoảng này (ví dụ `tech-blog`) |

Mã thoát: `0` sạch, `1` có vi phạm, `2` sai cách dùng. `--type blog` đã bị bỏ và trả về mã thoát `2`; hãy dùng `--type tech-blog`.

## Script kiểm tra gì

- Độ dài câu, độ dài đoạn, cụm từ cấm, số thuật ngữ, độ dài văn bản. Văn bản dài hơn giới hạn trên sẽ in cảnh báo và không làm đổi mã thoát. Văn bản ngắn hơn là bình thường, không cần kéo dài.
- Nhãn báo cáo (như `Result:`) ở đầu bất kỳ dòng nào ngoài khối code.
- Xuống dòng bằng dấu cách cuối dòng.

Script bỏ qua khối code, bảng và tiêu đề. Với `api-design`, script kiểm tra độ dài câu trong từng ô bảng. Với mục danh sách, script kiểm tra độ dài câu nhưng không kiểm tra độ dài đoạn.

## Script không kiểm tra gì

Giọng văn, sự thật, và câu có tự nhiên không. Script chỉ đếm cơ học. Kết quả sạch nghĩa là các con số đạt, không có nghĩa là văn bản hay.

## Đơn vị đếm

| Ngôn ngữ | Đơn vị | Giới hạn câu của `tech-blog` |
|---|---|---|
| `vi` | tiếng (âm tiết) | 28 (khoảng 20 từ) |
| `en` | từ | 20 |
| `ja` | ký tự (字), không tính dấu câu và khoảng trắng | 60 |

Giới hạn của mọi loại chỉ nằm trong `profile.json` của từng ngôn ngữ. Bảng trên chép lại dòng `tech-blog`.

Tiếp theo: [04-customize](04-customize.vi.md).
