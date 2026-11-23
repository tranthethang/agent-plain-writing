# Evals

`evals/` kiểm thử các skill bằng một agent thật. Đây là bộ nhỏ, không phải benchmark.

| File | Vai trò |
|---|---|
| `cases/` | 18 ca: `tech-blog`, `essay`, `api-design`, `user-guide` và `common`, mỗi loại có `vi`, `en`, `ja`, cộng 3 ca `api-design-speed`. Mọi dữ liệu đều là giả lập |
| `smoke-prompts.md` | Bộ Smoke: 5 prompt để kiểm tra nhanh sau mỗi thay đổi |
| `score.py` | Bộ chấm cơ học. Đếm số không có trong ca, và với `api-design` còn báo `tbd_ids`, `tbd_without_question`, `tbd_in_code`, `tbd_duplicate_questions` và `tbd_without_inline` |
| `judge-prompt.md` | Prompt cho AI giám khảo (độ rõ, độ đủ ý, và các kiểm tra ngữ nghĩa theo loại cho `api-design`, `tech-blog`, `essay`, `user-guide` và `common`) |

## Quy trình

Không có script nào gọi API. Một agent thật viết từng đầu ra.

1. Cổng cục bộ: `python3 -m unittest discover -s tests` và `python3 scripts/sync_shared.py --check`.
2. Cài cả sáu skill: `npx skills add tranthethang/agent-plain-writing -g`.
3. Tạo `evidence/<run>/`.
4. Chạy các prompt trong agent của bạn. Bộ Smoke là `evals/smoke-prompts.md`. Bộ Full là mọi file trong `evals/cases/`. Mỗi prompt yêu cầu agent ghi đầu ra vào `evidence/<run>/<case>.with_skill.md`.
5. Chấm từng đầu ra và lưu kết quả vào `evidence/<run>/results.json`:

```bash
python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md
python3 evals/score.py evals/cases/tech-blog-en.md evidence/<run>/tech-blog-en.with_skill.md --judge-prompt
```

`evals/README.md` có một script ngắn để chấm mọi đầu ra của một lần chạy vào một file `results.json`.

## Giới hạn trung thực

- Đầu ra các lần chạy được lưu trong `evidence/` và git theo dõi. Mỗi lần chạy có bản tóm tắt riêng trong [evidence/](../../evidence/README.md). Mỗi lần chạy chỉ có điểm cơ học, nên chưa chứng minh skill làm văn bản tốt hơn.
- Các ca trong `evals/cases/` phủ mọi loại văn bản. Mỗi lần chạy phủ những ca nào thì ghi trong `README.md` của lần chạy đó.
- Giám khảo là AI. Điểm của nó chưa được đối chiếu với người đọc thật.
- Các ca dùng dữ liệu giả lập. Muốn thêm ca từ đề bài thật, xem `evals/README.md`.

Tiếp theo: [06-limitations](06-limitations.vi.md).
