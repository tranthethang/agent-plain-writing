# agent-plain-writing

Skill này giúp AI viết **văn bản ngắn, cụ thể**. Hỗ trợ tiếng Việt (`vi`), Anh (`en`) và Nhật (`ja`).

Skill đưa cho AI các giới hạn đếm được. Đó là độ dài câu, độ dài đoạn, cụm từ bị cấm và thuật ngữ. Mỗi ngôn ngữ và loại văn bản có ví dụ xấu → tốt.

Một script kiểm tra bản nháp theo các giới hạn đó.

| | |
|---|---|
| Xấu | The system utilizes a caching mechanism in order to optimize data retrieval performance. |
| Tốt | The system saves results it has already computed. Next time, it answers faster. |

![Ảnh banner của agent-plain-writing](../../assets/screenshot.png)

## Trạng thái

- Có năm loại văn bản, chia thành hai nhóm giọng. Nhóm `plain` gồm `tech-blog`, `api-design`, `guide`, `common`. Nhóm `creative` gồm `essay`. Hiện chưa hỗ trợ `prose`, `poetry` và `screen-design`.
- **Thay đổi không tương thích:** `--type blog` nay là `--type tech-blog`. Đây cũng là giá trị mặc định mới.
- Script chỉ đếm, không đánh giá giọng văn. Độ dài ngoài khoảng cho phép chỉ in cảnh báo. Script không báo lỗi.
- Các giới hạn số là ước lượng ban đầu. Chúng chưa được kiểm chứng.
- Bằng chứng còn ít. Mới có một lần chạy eval, 9 ca mô phỏng, chỉ có điểm tự động. Xem [Bằng chứng](#bằng-chứng).
- Test tự động kiểm tra các điểm sau. Thống kê `TBD-n` và khoảng độ dài cho brief ngắn trong `evals/score.py`. Tập loại văn bản. Loại mặc định của script. Phép kiểm tra ô bảng, nhãn báo cáo và `--short-brief` của script. Các bảng Đơn vị. Chạy test bằng `python3 -m unittest discover -s tests`. `AGENTS.md` liệt kê các bước kiểm tra tay còn lại.

## Bắt đầu nhanh

1. Cài đặt. Bạn cần Node.js. Cách cài thủ công nằm trong [tài liệu](01-install.vi.md).

```bash
npx skills add tranthethang/agent-plain-writing -g
```

2. Ra lệnh cho AI: `Use agent-plain-writing to write a user guide in Japanese from these notes: ...`
3. Kiểm tra bản nháp. Bạn cần Python 3.7+ và không cần cài thêm gói nào.

```bash
python3 skills/agent-plain-writing/scripts/check_style.py draft.md --lang en --type tech-blog
```

Mã thoát: `0` là sạch, `1` là có lỗi, `2` là gõ sai cách dùng.

## Đơn vị

Bảng này khớp với giới hạn `sentence` / `paragraph` trong `skills/agent-plain-writing/languages/<lang>/profile.json`:

| Ngôn ngữ | Đơn vị | `tech-blog` | `essay` | `api-design` | `guide` | `common` |
|---|---|---|---|---|---|---|
| `vi` | âm tiết (*tiếng*) | 28 / 3 | 40 / 6 | 25 / 3 | 16 / 3 | 28 / 3 |
| `en` | từ | 20 / 3 | 30 / 6 | 18 / 3 | 12 / 3 | 20 / 3 |
| `ja` | ký tự (字) | 60 / 3 | 80 / 6 | 55 / 3 | 40 / 3 | 60 / 3 |

Độ dài của `tech-blog` có `length` và `length_short` (cho brief ngắn).

- `vi`: 600–800 / 300–500 từ.
- `en`: 600–800 / 300–500 từ.
- `ja`: 1500–2000 / 750–1250 字.

Các loại khác không có khoảng độ dài.

## Bằng chứng

Một lần chạy eval (`evidence/20261121-235628/`) so sánh cùng một AI khi có và không có skill.

Eval gồm 9 ca mô phỏng: `api-design`, `essay` và `tech-blog`, mỗi loại bằng `vi`, `en`, `ja`. Kết quả chỉ lấy từ script. Không có AI chấm và không có người duyệt.

- Có skill, 7 trên 9 bản pass script. Không có skill, chỉ 6 trên 9 bản pass.
- Có skill, câu trung bình ngắn hơn ở 8 trên 9 ca. Ngoại lệ là `tech-blog en`, với 14,7 so với 12,4 từ.
- Với `api-design`, cả 3 bản có skill đều pass. Bản `api-design vi` không có skill thì không pass. Số thuật ngữ giảm từ 2 xuống 1. Mỗi bản có 8 đến 9 dấu `TBD-n` gắn với câu hỏi. Script không cho biết như vậy có tốt hơn không.
- Với `essay`, cả 6 bản pass và không có lỗi. Các bản có skill ngắn hơn.
- Với `tech-blog`, bản `vi` pass ở cả hai chế độ. Bản `ja` có 2 lỗi đoạn ở cả hai chế độ. Bản `en` có nhiều lỗi hơn khi dùng skill (7 so với 3). Cả 6 bản ngắn hơn mức mục tiêu. Script chỉ in cảnh báo.
- Không bản nào bịa số.

Mẫu này nhỏ, chưa đủ để chứng minh. Chi tiết, bảng số liệu và giới hạn: [evidence/README.md](../../evidence/README.md).

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

## Giấy phép

GNU GPL v3. Xem [LICENSE](../../LICENSE).
