# Cài đặt

Chạy lệnh sau trong terminal. Cần có Node.js (để dùng `npx`).

```bash
npx skills add tranthethang/agent-plain-writing -g
```

- `tranthethang/agent-plain-writing` là repo GitHub chứa skill.
- `-g` cài skill ở mức toàn cục (cho tài khoản của bạn), không chỉ cho một dự án. Bỏ `-g` để cài vào dự án hiện tại.

Lệnh này cài cả sáu skill cùng lúc: router `agent-plain-writing` và năm sub-skill `agent-plain-writing-<type>`. Sau đó yêu cầu agent dùng `agent-plain-writing`, hoặc một sub-skill. Xem [02-usage](02-usage.vi.md).

## Cài thủ công

Nếu không dùng `npx`, chép mọi thư mục `skills/agent-plain-writing*/` vào thư mục skill của agent. Chép đủ cả sáu. Giữ tên mỗi thư mục trùng với trường `name` trong `SKILL.md` của nó.

| Công cụ | Vị trí |
|---|---|
| Claude Code | `.claude/skills/` (theo dự án) hoặc `~/.claude/skills/` (cá nhân) |
| Công cụ khác đọc `SKILL.md` | Xem tài liệu của công cụ đó |

## Lưu ý

- Chỉ cần Python 3.15 trở lên để chạy script kiểm tra ([03-checker](03-checker.vi.md)). Skill không phụ thuộc gì khác.

Tiếp theo: [02-usage](02-usage.vi.md).
