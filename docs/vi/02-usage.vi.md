# Cách dùng

Yêu cầu bằng lời thường và đưa một bản tóm tắt đầu vào tốt:

```
Dùng agent-plain-writing để viết hướng dẫn người dùng bằng tiếng Nhật từ ghi chú sau: ...
Viết lại thiết kế API này bằng tiếng Anh. Dùng mẫu api-design. Ghi TBD cho phần còn thiếu.
Rút gọn bài blog này. Đoạn văn của tôi đính kèm làm mẫu nhịp câu.
```

Mỗi file trong `skills/agent-plain-writing/doc-types/` liệt kê thông tin AI cần cho loại đó: tóm tắt, ý chính, người đọc, một đoạn văn mẫu của bạn, từ nên dùng hoặc tránh. Bạn đưa càng ít, AI càng phải đoán nhiều.

## Quy trình skill làm theo

1. Chọn ngôn ngữ đầu ra (`vi`, `en`, `ja`). Đó là ngôn ngữ của văn bản được viết ra, không phải của prompt.
2. Chọn loại văn bản. Chỉ đọc file của loại đó và ví dụ của ngôn ngữ đó.
3. Xác định người đọc. Hỏi một câu nếu chưa rõ.
4. Lập dàn ý, với văn bản dài hơn khoảng 400 từ.
5. Viết nháp.
6. Sửa ở một lượt riêng: cắt, đối chiếu checklist, chạy script kiểm tra.
7. Báo kết quả và những điều phải đoán. Phần báo cáo nằm ngoài văn bản.

## Loại văn bản

| Loại | `--type` | File quy tắc |
|---|---|---|
| Bài blog | `blog` | `doc-types/blog.md` |
| Truyện, tiểu luận | `prose` | `doc-types/prose.md` |
| Thơ | `poetry` | `doc-types/poetry.md` |
| Thiết kế API (một endpoint) | `api-design` | `doc-types/api-design.md` |
| Hướng dẫn người dùng | `guide` | `doc-types/user-guide.md` |
| Thiết kế màn hình | không có | giữ chỗ, chưa làm |

Với `api-design`, AI dùng một mẫu cố định gồm bảy mục. Khi đề bài thiếu thông tin, AI chỉ ghi `TBD-n` cho chỗ trống mà đề bài nêu tên, hoặc chỗ trống chặn việc triển khai. Mỗi `TBD-n` có một câu hỏi ở mục Open items.

Tiếp theo: [03-checker](03-checker.vi.md).
