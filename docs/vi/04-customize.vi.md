# Tùy chỉnh

- **Cấu hình dự án.** Chép `skills/agent-plain-writing/templates/PLAIN-WRITING.example.md` thành `PLAIN-WRITING.md` ở thư mục gốc dự án. Đặt `default_lang`, `default_type`, giọng văn, thuật ngữ thêm, cụm từ cấm thêm và giới hạn. Script đọc khối JSON. AI đọc các mục Markdown.
- **Mẫu của bạn.** Mỗi file `examples/*.md` kết thúc bằng mục "Your own samples". Dán câu AI viết dở và bản bạn sửa. Mẫu của bạn có giá trị hơn mẫu do AI viết.
- **Cụm từ cấm.** Thêm cụm từ vào `banned.txt` và `banned-guide.md` trong cùng thư mục ngôn ngữ. Tiêu đề như `[tech-blog,essay]` dùng chung một danh sách cụm từ cho nhiều loại.
- **Giới hạn.** Sửa `profile.json`. Nếu giới hạn câu của `tech-blog` đổi, cập nhật bảng đơn vị ở `README.md` và [03-checker](03-checker.vi.md).
- **Thêm ngôn ngữ.** Tạo `languages/<code>/` với `profile.json`, `profile.md`, `banned.txt`, `banned-guide.md`, `terms.txt` và `examples/`. Script hỗ trợ ba đơn vị: `syllable`, `word`, `char`. Cập nhật thêm `SKILL.md`, `README.md` và tài liệu này. Xem `AGENTS.md`.

Tiếp theo: [05-evals](05-evals.vi.md).
