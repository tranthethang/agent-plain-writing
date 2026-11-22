# Evals

`evals/` so sánh đầu ra của AI khi có và không có skill. Đây là bộ nhỏ, không phải benchmark.

| File | Vai trò |
|---|---|
| `cases/` | 15 ca: `tech-blog`, `essay`, `api-design`, `guide` và `common`, mỗi loại có `vi`, `en`, `ja`. Mọi dữ liệu đều là giả lập |
| `score.py` | Bộ chấm cơ học. Đếm số không có trong ca, và với `api-design` còn báo `tbd_ids`, `tbd_without_question`, `tbd_in_code`, `tbd_duplicate_questions` và `tbd_without_inline` |
| `judge-prompt.md` | Prompt cho AI giám khảo (độ rõ, độ đủ ý, và các kiểm tra ngữ nghĩa theo loại cho `api-design`, `tech-blog`, `essay`, `guide` và `common`) |
| `run_eval.py` | Chạy mỗi ca hai lần (có skill và không có skill) |

## Chi phí

`run_eval.py` gọi AI 2 lần cho mỗi ca. Chạy cả 15 ca là 30 lần gọi và tốn hạn mức hoặc tiền. Luôn xem trước:

```bash
python3 evals/run_eval.py --dry-run
python3 evals/run_eval.py --type tech-blog --lang vi --dry-run
```

Sau đó chạy thật. Script yêu cầu bạn gõ `yes`.

```bash
python3 evals/run_eval.py --tool openai   # mặc định; đọc OPENAI_API_URL, OPENAI_API_KEY, OPENAI_API_MODEL
python3 evals/run_eval.py --tool claude   # CLI `claude` trên máy
python3 evals/run_eval.py --tool antigravity
```

Đặt cấu hình API trong `evals/.env` hoặc `.env` ở thư mục gốc. Cả hai đều bị git bỏ qua. Đầu ra nằm ở `evidence/<timestamp>/`, được git theo dõi.

Chấm một đầu ra:

```bash
python3 evals/score.py evals/cases/tech-blog-en.md output.md
python3 evals/score.py evals/cases/tech-blog-en.md output.md --judge-prompt
python3 evals/run_eval.py --judge-prompts 20261122-181452
```

`--judge-prompts <run>` tạo prompt giám khảo cho mọi đầu ra `with_skill` của một thư mục trong `evidence/`. Kết quả nằm ở `judge-prompts/<run>/<case>.judge.md` và không gọi AI. Nếu không đưa giá trị, lệnh làm việc đó sau một lượt chạy mới.

## Giới hạn trung thực

- Đầu ra các lần chạy được lưu trong `evidence/` và git theo dõi. Mỗi lần chạy có bản tóm tắt riêng trong [evidence/](../../evidence/README.md). Mỗi lần chỉ là một lần chạy, chỉ có điểm cơ học, nên chưa chứng minh skill làm văn bản tốt hơn.
- Các ca trong `evals/cases/` phủ mọi loại văn bản. Mỗi lần chạy phủ những ca nào thì ghi trong `README.md` của lần chạy đó.
- Giám khảo là AI. Điểm của nó chưa được đối chiếu với người đọc thật.
- Các ca dùng dữ liệu giả lập. Muốn thêm ca từ đề bài thật, xem `evals/README.md`.

Tiếp theo: [06-limitations](06-limitations.vi.md).
