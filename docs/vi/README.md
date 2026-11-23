# agent-plain-writing

Bộ skill này giúp AI viết **văn bản ngắn, cụ thể**. Hỗ trợ tiếng Việt (`vi`), Anh (`en`) và Nhật (`ja`).

Bộ này gồm một skill router và năm sub-skill, mỗi loại văn bản một sub-skill. Mỗi sub-skill xử lý `vi`, `en` và `ja`. Các skill đưa cho AI các giới hạn đếm được. Đó là độ dài câu, độ dài đoạn, cụm từ bị cấm và thuật ngữ. Mỗi ngôn ngữ và loại văn bản có ví dụ xấu → tốt.

Một script kiểm tra bản nháp theo các giới hạn đó.

| | |
|---|---|
| Xấu | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Tốt | The system saves results it has already computed. Next time, it answers faster. |

![Ảnh banner của agent-plain-writing](../../assets/screenshot.png)

## Trạng thái

- Có năm loại văn bản, chia thành hai nhóm giọng. Nhóm `plain` gồm `tech-blog`, `api-design`, `user-guide`, `common`. Nhóm `creative` gồm `essay`. Mỗi loại có sub-skill riêng: `agent-plain-writing-<type>`. Router `agent-plain-writing` chọn loại khi yêu cầu không nêu rõ. Hiện chưa hỗ trợ `prose`, `poetry` và `screen-design`.
- **Thay đổi không tương thích:** `--type blog` nay là `--type tech-blog`. Giá trị mặc định là `common`.
- Script chỉ đếm, không đánh giá giọng văn. Script chỉ cảnh báo khi văn bản dài hơn giới hạn trên. Văn bản ngắn hơn là bình thường, không cần kéo dài cho đủ. Cảnh báo này không làm script báo lỗi.
- Các giới hạn số là ước lượng ban đầu. Chúng chưa được kiểm chứng.
- Bằng chứng còn ít. Mới có vài lần chạy eval trên ca mô phỏng, chỉ có điểm tự động. Xem [Bằng chứng](#bằng-chứng).
- Test tự động kiểm tra các điểm sau. Thống kê `TBD-n` và khoảng độ dài cho brief ngắn trong `evals/score.py`. Tập loại văn bản. Loại mặc định của script. Phép kiểm tra ô bảng, nhãn báo cáo và `--short-brief` của script. Các bảng Đơn vị. Cách đếm mốc giờ và ngày. Việc tìm `PLAIN-WRITING.md` từ thư mục con. Cảnh báo độ dài chỉ ở giới hạn trên. File `doc-types/` của mọi loại. Các mẫu hoàn chỉnh trong `examples/`. Việc các sub-skill được sinh ra khớp với `shared/`. Chạy test bằng `python3 -m unittest discover -s tests` và `python3 scripts/sync_shared.py --check`. `AGENTS.md` liệt kê các bước kiểm tra tay còn lại.
- GitHub Actions chạy hai lệnh trên khi push và mở pull request vào `main` (Python 3.7 và 3.x).

## Bắt đầu nhanh

1. Cài đặt. Bạn cần Node.js. Cách cài thủ công nằm trong [tài liệu](01-install.vi.md). Cả sáu skill được cài cùng lúc.

```bash
npx skills add tranthethang/agent-plain-writing -g
```

2. Gọi router, hoặc gọi thẳng một sub-skill:
   - `Use agent-plain-writing to shorten this text: ...` (router chọn loại)
   - `Use agent-plain-writing-user-guide to write a user guide in Japanese from these notes: ...`
3. Kiểm tra bản nháp. Bạn cần Python 3.7+ và không cần cài thêm gói nào.

```bash
python3 skills/agent-plain-writing-tech-blog/scripts/check_style.py draft.md --lang en --type tech-blog
python3 skills/agent-plain-writing-user-guide/scripts/check_style.py guide.md --lang vi --type user-guide
```

Mã thoát: `0` là sạch, `1` là có lỗi, `2` là gõ sai cách dùng.

## Đơn vị

Bảng này khớp với giới hạn `sentence` / `paragraph` trong `shared/languages/<lang>/profile.json`:

| Ngôn ngữ | Đơn vị | `tech-blog` | `essay` | `api-design` | `user-guide` | `common` |
|---|---|---|---|---|---|---|
| `vi` | âm tiết (*tiếng*) | 28 / 3 | 40 / 6 | 25 / 3 | 16 / 3 | 28 / 3 |
| `en` | từ | 20 / 3 | 30 / 6 | 18 / 3 | 12 / 3 | 20 / 3 |
| `ja` | ký tự (字) | 60 / 3 | 80 / 6 | 55 / 3 | 40 / 3 | 60 / 3 |

Độ dài của `tech-blog` có `length` và `length_short` (cho brief ngắn). Chỉ số lớn (giới hạn trên) mới gây cảnh báo.

- `vi`: 600–800 / 300–500 từ.
- `en`: 600–800 / 300–500 từ.
- `ja`: 1500–2000 / 750–1250 字.

Các loại khác không có khoảng độ dài.

## Bằng chứng

Các lần chạy eval nằm ở [evidence/](../../evidence/README.md). Mỗi lần chạy có thư mục riêng chứa đầu ra thô, `results.json` và một `README.md` ghi bảng số liệu, điều các số cho thấy và giới hạn. Mỗi lần chạy dùng một agent thật đã cài các skill (xem [evals/README.md](../../evals/README.md)). Kết quả chỉ lấy từ script. Không có AI chấm và không có người duyệt. Mỗi lần chạy là một mẫu nhỏ, chưa đủ để chứng minh.

## Tài liệu

Mỗi chủ đề có một file cho mỗi ngôn ngữ, nằm trong `docs/<lang>/`.

| # | Chủ đề | English | Tiếng Việt | 日本語 |
|---|---|---|---|---|
| 00 | Tổng quan | [en](../en/00-overview.en.md) | [vi](00-overview.vi.md) | [ja](../ja/00-overview.ja.md) |
| 01 | Cài đặt | [en](../en/01-install.en.md) | [vi](01-install.vi.md) | [ja](../ja/01-install.ja.md) |
| 02 | Cách dùng | [en](../en/02-usage.en.md) | [vi](02-usage.vi.md) | [ja](../ja/02-usage.ja.md) |
| 03 | Script kiểm tra | [en](../en/03-checker.en.md) | [vi](03-checker.vi.md) | [ja](../ja/03-checker.ja.md) |
| 04 | Tùy chỉnh | [en](../en/04-customize.en.md) | [vi](04-customize.vi.md) | [ja](../ja/04-customize.ja.md) |
| 05 | Eval | [en](../en/05-evals.en.md) | [vi](05-evals.vi.md) | [ja](../ja/05-evals.ja.md) |
| 06 | Giới hạn | [en](../en/06-limitations.en.md) | [vi](06-limitations.vi.md) | [ja](../ja/06-limitations.ja.md) |

## Đóng góp

Hãy đọc [AGENTS.md](../../AGENTS.md) trước khi sửa bất cứ thứ gì. File này giữ ba thư mục ngôn ngữ song song với nhau.

Bật hook `pre-commit` một lần sau khi clone để tránh commit khi `skills/` chưa đồng bộ với `shared/`:

```bash
git config core.hooksPath .githooks
```

## Giấy phép

GNU GPL v3. Xem [LICENSE](../../LICENSE).
