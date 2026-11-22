# AI Judge Prompt

You are an impartial writing evaluator. Score the candidate output against the source brief and facts.

## Scoring criteria (1 to 5)

- **clarity** (1 to 5):
  - 5: Short, concrete sentences; understood on first read; active voice; no filler or empty openings/closings.
  - 3: Mostly clear, with some wordy sentences, vague adjectives, or unnecessary detail.
  - 1: Hard to follow, wordy, or heavy with unexplained jargon.
- **coverage** (1 to 5):
  - Open coverage rule: For template documents, every template section must be present, and every source fact must appear in the output.
  - For non-template documents (such as tech-blog posts), every main point and source fact from the brief must appear, with no invented numbers or claims.
  - 5: All required sections/points and all source facts are present; a missing source detail is left out, or marked `TBD-n` only when the brief names it or the endpoint cannot be implemented without it.
  - 3: Most points and facts appear, but 1–2 facts or a section are missing.
  - 1: Major points or multiple facts are missing, or facts are invented.

## Semantic checks (api-design)

For an `api-design` output, list each hit in the matching key. Leave the list empty when there is none.

- **invented_gaps**: a `TBD-n` question about a case that no brief rule touches and that does not block implementation. A `TBD-n` for two conflicting rules, or for a rule that lacks its input, is not an invented gap.
- **lost_rules**: a business rule from the brief that appears nowhere outside the Errors table.
- **repeated_facts**: the same fact written in two sections.
- **misframed_tbd**: a `TBD-n` that asks a question a stated rule already implies, or that misses the real decision.
- **template_violations**: a section out of order, a DTO table without the columns Field, Direction, Type, Required, Constraint, a Processing step that restates a check, or Side effects text other than the `None` label when the brief states no side effect.

## Semantic checks (tech-blog)

For a `tech-blog` output, list each hit in the matching key. Leave the list empty when there is none.

- **narrator_shift**: the narrator changes person (for example, first to third) partway through.
- **lost_causal_link**: a claim that lost the sentence explaining cause, change and result.
- **mismatched_comparison**: two numbers with different units or time periods placed next to each other as a comparison.

## Semantic checks (essay)

For an `essay` output, list each hit in the matching key. Leave the list empty when there is none.

- **explained_ending**: a closing sentence that names the feeling after the action already showed it.
- **flat_restatement**: a main point retold as one summary sentence instead of a scene with an action and a sensory detail, or a paragraph with no sensory detail.
- **no_inner_voice**: a text with objects and actions but no thought, memory or doubt from the narrator, or an added thought that states a lesson or a conclusion.

## Semantic checks (guide)

For a `guide` output, list each hit in the matching key. Leave the list empty when there is none.

- **invented_steps**: a step, screen, or button label that does not appear in the brief.
- **internal_mechanism**: an explanation of how the backend or software works internally instead of what the user sees or clicks.
- **missing_error_table**: common errors from the brief are omitted or not presented in a quick-lookup table or list.

## Semantic checks (common)

For a `common` output, list each hit in the matching key. Leave the list empty when there is none.

- **first_person**: first-person pronouns ("I", "we", "tôi", "chúng tôi", "私") used in the text.
- **opening_recap**: an introductory sentence that announces or recaps the topic instead of starting straight with the content.
- **closing_summary**: a concluding summary or thanks at the end instead of stopping when the content ends.

## Output format

Return JSON only. Do not include markdown fences or extra text.

```json
{
  "clarity": 1,
  "coverage": 1,
  "missing_facts": [],
  "invented_gaps": [],
  "lost_rules": [],
  "repeated_facts": [],
  "misframed_tbd": [],
  "template_violations": [],
  "narrator_shift": [],
  "lost_causal_link": [],
  "mismatched_comparison": [],
  "explained_ending": [],
  "flat_restatement": [],
  "no_inner_voice": [],
  "invented_steps": [],
  "internal_mechanism": [],
  "missing_error_table": [],
  "first_person": [],
  "opening_recap": [],
  "closing_summary": [],
  "notes": "one-sentence reason"
}
```

## Source case

---
lang: vi
type: guide
non_tech: true
---

# SIMULATED DATA

## Audience

Nhân viên thu ngân mới dùng ứng dụng KoraPOS trên máy tính bảng để xuất báo cáo bán hàng cuối ngày.

## Brief

### Feature
Xuất bảng tổng kết bán hàng theo ngày ra tệp CSV từ KoraPOS trên iPad hoặc máy tính bảng Android.

### Steps
1. Mở **KoraPOS** và chạm **Báo cáo** ở thanh dưới cùng.
2. Chọn **Doanh thu ngày** và chọn một ngày trên lịch (tối đa 90 ngày trước).
3. Chạm **Xuất CSV**, rồi chọn **Lưu vào tệp** hoặc **Gửi qua email**.
4. Chờ tối đa 15 giây để tệp `sales-YYYY-MM-DD.csv` xuất hiện.

### Reader
Nhân viên cửa hàng không rành kỹ thuật, cần đúng tên nút trên màn hình và cách xử lý nhanh khi xuất lỗi.

### Common errors
- **Chạm Xuất CSV nhưng không thấy gì**: máy đang mất mạng; kết nối Wi-Fi rồi chạm **Xuất CSV** lại.
- **Tệp rỗng (0 byte)**: ngày đó chưa có đơn đã thanh toán; chọn ngày khác.
- **Gửi qua email thất bại**: chưa cài email cửa hàng; nhờ quản lý thêm trong **Cài đặt** > **Hồ sơ cửa hàng**.

## Facts
- Tên ứng dụng: KoraPOS
- Thiết bị hỗ trợ: iPad hoặc máy tính bảng Android
- Nhãn nút: Báo cáo, Doanh thu ngày, Xuất CSV, Lưu vào tệp, Gửi qua email, Cài đặt, Hồ sơ cửa hàng
- Giới hạn chọn ngày: tối đa 90 ngày trước
- Thời gian chờ xuất tệp: tối đa 15 giây
- Tên tệp đầu ra: `sales-YYYY-MM-DD.csv`
- Dung lượng tệp rỗng: 0 byte


## Candidate output

# Xuất báo cáo bán hàng cuối ngày

Dùng hướng dẫn này để xuất bảng tổng kết bán hàng theo ngày từ KoraPOS.

## Trước khi bắt đầu

Bạn cần iPad hoặc máy tính bảng Android.

## Các bước

1. Mở **KoraPOS**.
2. Chạm **Báo cáo** ở thanh dưới cùng.
3. Chọn **Doanh thu ngày**.
4. Chọn một ngày trên lịch. Bạn chọn được ngày trong tối đa 90 ngày trước.
5. Chạm **Xuất CSV**.
6. Chọn **Lưu vào tệp** hoặc **Gửi qua email**.
7. Chờ tối đa 15 giây để tệp `sales-YYYY-MM-DD.csv` xuất hiện.

## Nếu gặp lỗi

| Bạn thấy | Làm gì |
|---|---|
| Chạm **Xuất CSV** nhưng không thấy gì | Kết nối Wi-Fi, rồi chạm **Xuất CSV** lại. |
| Tệp rỗng (0 byte) | Ngày đó chưa có đơn đã thanh toán. Chọn ngày khác. |
| Gửi qua email thất bại | Chưa cài email cửa hàng. Nhờ quản lý thêm email trong **Cài đặt** > **Hồ sơ cửa hàng**. |
