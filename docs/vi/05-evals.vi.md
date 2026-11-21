# Evals

`evals/` so sánh đầu ra của AI khi có và không có skill. Đây là bộ nhỏ, không phải benchmark.

| File | Vai trò |
|---|---|
| `cases/` | 6 ca: `blog` và `api-design`, mỗi loại có `vi`, `en`, `ja`. Mọi dữ liệu đều là giả lập |
| `score.py` | Bộ chấm cơ học. Đếm số không có trong ca, và với `api-design` còn báo `tbd_ids`, `tbd_without_question`, `tbd_in_code` và `tbd_duplicate_questions` |
| `judge-prompt.md` | Prompt cho AI giám khảo (độ rõ, độ đủ ý, và ba kiểm tra ngữ nghĩa cho `api-design`) |
| `run_eval.py` | Chạy mỗi ca hai lần (có skill và không có skill) |

## Chi phí

`run_eval.py` gọi AI 2 lần cho mỗi ca. Chạy cả 6 ca là 12 lần gọi và tốn hạn mức hoặc tiền. Luôn xem trước:

```bash
python3 evals/run_eval.py --dry-run
python3 evals/run_eval.py --type blog --lang vi --dry-run
```

Sau đó chạy thật. Script yêu cầu bạn gõ `yes`.

```bash
python3 evals/run_eval.py --tool openai   # mặc định; đọc OPENAI_API_URL, OPENAI_API_KEY, OPENAI_API_MODEL
python3 evals/run_eval.py --tool claude   # CLI `claude` trên máy
python3 evals/run_eval.py --tool antigravity
```

Đặt cấu hình API trong `evals/.env` hoặc `.env` ở thư mục gốc. Cả hai đều bị git bỏ qua. Đầu ra nằm ở `evals/runs/<timestamp>/`, cũng bị git bỏ qua.

Chấm một đầu ra:

```bash
python3 evals/score.py evals/cases/blog-en.md output.md
python3 evals/score.py evals/cases/blog-en.md output.md --judge-prompt
```

## Giới hạn trung thực

- Đầu ra các lần chạy bị git bỏ qua. Một lần chạy được giữ làm bằng chứng trong [evidence/](../../evidence/README.md). Đó chỉ là một lần chạy, chỉ có điểm cơ học, nên chưa chứng minh skill làm văn bản tốt hơn.
- Sáu ca chỉ phủ hai loại. Các loại còn lại chưa có ca.
- Giám khảo là AI. Điểm của nó chưa được đối chiếu với người đọc thật.
- Các ca dùng dữ liệu giả lập. Muốn thêm ca từ đề bài thật, xem `evals/README.md`.

Tiếp theo: [06-limitations](06-limitations.vi.md).
