# Script kiểm tra

```bash
python3 skills/agent-plain-writing/scripts/check_style.py draft.md --lang en --type tech-blog
python3 skills/agent-plain-writing/scripts/check_style.py spec.md  --lang ja --type api-design
python3 skills/agent-plain-writing/scripts/check_style.py guide.md --lang vi --type guide
python3 skills/agent-plain-writing/scripts/check_style.py post.md  --lang en --type tech-blog --non-tech
```

| Tùy chọn | Giá trị |
|---|---|
| `--lang` | `vi`, `en`, `ja`. Có thể bỏ nếu `PLAIN-WRITING.md` có `default_lang` |
| `--type` | `tech-blog`, `essay`, `api-design`, `guide`, `common` (`user-guide` cũng được). Mặc định: `default_type` hoặc `tech-blog` |
| `--non-tech` | Giới hạn thuật ngữ còn 3. Loại `guide` luôn áp dụng giới hạn thuật ngữ |
| `--config` | Đường dẫn tới file `PLAIN-WRITING.md`. Mặc định: `./PLAIN-WRITING.md` nếu có |

Mã thoát: `0` sạch, `1` có vi phạm, `2` sai cách dùng. `--type blog` đã bị bỏ và trả về mã thoát `2`; hãy dùng `--type tech-blog`.

## Script kiểm tra gì

- Độ dài câu, độ dài đoạn, cụm từ cấm, số thuật ngữ, độ dài văn bản. Độ dài văn bản ngoài khoảng cho phép sẽ in cảnh báo và không làm đổi mã thoát.
- Nhãn báo cáo (như `Result:`) ở 3 dòng không rỗng đầu hoặc cuối.
- Xuống dòng bằng dấu cách cuối dòng.

Script bỏ qua khối code, bảng và tiêu đề. Với mục danh sách, script kiểm tra độ dài câu nhưng không kiểm tra độ dài đoạn.

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
