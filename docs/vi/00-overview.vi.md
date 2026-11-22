# Tổng quan

`agent-plain-writing` là một skill cho AI agent. Skill yêu cầu AI viết văn bản ngắn, cụ thể bằng tiếng Việt (`vi`), tiếng Anh (`en`) hoặc tiếng Nhật (`ja`).

## Vấn đề

Bản nháp của AI thường có cùng một số lỗi:

- Câu dài, khó theo dõi.
- Thuật ngữ mà người đọc không biết.
- Khi viết cho người ngoài ngành, AI giải thích mọi chi tiết kỹ thuật. Văn bản dài hơn nhưng không rõ hơn.

Thêm chữ "rõ ràng" hay "thân thiện" vào prompt không sửa được. Skill dùng giới hạn đếm được, ví dụ có thể bắt chước, và một lượt sửa riêng.

| | |
|---|---|
| Xấu | Hệ thống sử dụng cơ chế bộ nhớ đệm nhằm tối ưu hóa hiệu năng truy xuất dữ liệu. |
| Tốt | Hệ thống lưu lại kết quả đã tính. Lần sau, hệ thống trả lời nhanh hơn. |

## Gồm những gì

- **Quy tắc lõi và quy trình** trong `SKILL.md` (6 quy tắc chung và quy tắc riêng cho từng nhóm giọng văn, viết nháp rồi sửa).
- **Năm loại văn bản trong hai nhóm giọng văn:** `plain` (`tech-blog`, `api-design`, `guide`, `common`) và `creative` (`essay`). Mỗi loại có một file trong `doc-types/` về giọng văn, cấu trúc và độ dài, trừ `common` không có file ở đó.
- **Ba thư mục ngôn ngữ** chứa đơn vị đếm, giới hạn số, cụm từ cấm, danh sách thuật ngữ và ví dụ.
- **Một script kiểm tra**, `check_style.py` (Python 3.7+, chỉ dùng thư viện chuẩn).
- **Bộ eval** trong `evals/` (xem [05-evals](05-evals.vi.md)).

`prose`, `poetry` và `screen-design` hiện nằm ngoài phạm vi.

## Ai sở hữu quy tắc nào

Mỗi thông tin có một file chủ. File khác chỉ trỏ tới file đó.

| Thông tin | File chủ |
|---|---|
| Quy trình và quy tắc lõi | `SKILL.md` |
| Giọng văn, cấu trúc, độ dài, nhịp câu | `doc-types/<type>.md` |
| Đơn vị đếm và giới hạn số | `languages/<lang>/profile.json` |
| Cụm từ cấm | `languages/<lang>/banned.txt` (danh sách cho checker), `banned-guide.md` (AI đọc file này) |
| Bẫy ngữ pháp, đại từ, từ chỉ mức độ | `languages/<lang>/profile.md` |
| Danh sách thuật ngữ | `languages/<lang>/terms.txt` |

Về giới hạn và cấu trúc, `doc-types` thắng `SKILL.md`. Về từ ngữ và ngữ pháp, `languages` thắng `doc-types`. Về mức được thêm ngoài nguồn, họ văn và `doc-types` thắng core rules; các dữ kiện trong core rule 5 thì không bao giờ đổi. Bảng đầy đủ nằm trong `AGENTS.md`.

## Cấu trúc repo

```
.
├── README.md
├── AGENTS.md                 # quy tắc khi sửa repo này
├── docs/{en,vi,ja}/          # tài liệu này
├── evals/                    # ca thử, bộ chấm, prompt giám khảo, bộ chạy
└── skills/agent-plain-writing/
    ├── SKILL.md
    ├── doc-types/            # tech-blog, essay, api-design, user-guide
    ├── languages/{vi,en,ja}/ # profile.json, profile.md, banned.txt, banned-guide.md,
    │                         # terms.txt, examples/
    ├── templates/PLAIN-WRITING.example.md
    └── scripts/check_style.py
```

Tiếp theo: [01-install](01-install.vi.md).
