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
type: tech-blog
non_tech: false
---

# SIMULATED DATA

## Audience

Lập trình viên backend có 2–5 năm kinh nghiệm, đang vận hành dịch vụ web nhỏ.

## Brief

### Summary
Nhóm của bạn từng đặt cache 15 phút cho trang danh sách sản phẩm để giảm tải database. Sau một đợt giảm giá, khách vẫn thấy giá cũ trong 12 phút và đặt nhầm 40 đơn. Nhóm thử giảm TTL xuống 15 giây trước, nhưng tải database tăng gấp đôi nên bỏ cách đó. Nhóm đã sửa bằng cách xóa cache theo sự kiện cập nhật giá và đặt TTL dự phòng 60 giây. Trên staging, sự kiện xóa cache chạy trước khi transaction ghi giá commit, nên cache nạp lại giá cũ; nhóm chuyển việc phát sự kiện sang sau commit.

### Main points
1. Cache theo thời gian cố định dễ gây lệch dữ liệu khi giá đổi đột ngột.
2. Xóa cache ngay khi ghi dữ liệu mới giúp giảm độ trễ cập nhật xuống dưới 1 giây.
3. Giữ TTL ngắn (60 giây) làm lưới an toàn nếu sự kiện bị mất.

### Reader
Lập trình viên backend quen SQL và Redis, chưa từng gặp sự cố lệch cache khi lưu lượng tăng gấp 3 lần.

### Voice
Ngôi thứ nhất ("tôi", "bạn"), thẳng thắn như kể lại cho đồng nghiệp ngồi cạnh, thừa nhận sai lầm.

### Sample paragraph
Tôi từng nghĩ tăng TTL lên 15 phút là cách nhanh nhất để cứu database. Mọi thứ êm đẹp suốt 2 tháng, cho tới sáng thứ Sáu khi bảng giá đổi lúc 9 giờ.

Bản sửa đầu tiên của tôi còn sai. Sự kiện xóa cache bắn ra trước khi transaction commit, và request kế tiếp nạp lại đúng cái giá cũ vào cache.

### Words to use or avoid
- Dùng: `cache`, `TTL`, `database`.
- Tránh: `tối ưu hóa`, `mạnh mẽ`, `đóng vai trò quan trọng`.

## Facts
- TTL ban đầu: 15 phút
- Thời gian khách thấy giá cũ: 12 phút
- Số đơn đặt nhầm: 40 đơn
- Lưu lượng tăng: 3 lần
- Độ trễ cập nhật sau khi sửa: dưới 1 giây
- TTL dự phòng: 60 giây
- Thời điểm đổi giá: 9 giờ sáng thứ Sáu
- Thời gian chạy ổn trước sự cố: 2 tháng
- TTL thử trước khi sửa: 15 giây (tải database tăng gấp 2 lần, nên bỏ)
- Lỗi trên staging: sự kiện xóa cache chạy trước khi transaction commit, cache nạp lại giá cũ
- Cách sửa lỗi staging: phát sự kiện sau khi transaction commit
- Kênh phát sự kiện: Redis pub/sub
- Số trang đọc cache giá: 2 (trang danh sách và trang chi tiết sản phẩm)
- Tỉ lệ cache hit: 97% trước khi sửa, 92% sau khi sửa
- Xử lý 40 đơn đặt nhầm: nhóm gọi lại cho từng khách trong 1 buổi chiều
- Thời gian triển khai bản sửa: 3 ngày


## Candidate output

# Tôi chuyển sự kiện xóa cache sang sau commit

Thứ Sáu, lúc 9 giờ sáng, nhóm tôi đổi giá sản phẩm. Khách vẫn thấy giá cũ suốt 12 phút và đặt nhầm 40 đơn.

## TTL 15 phút che mất giá mới

Tôi từng nghĩ TTL 15 phút sẽ giảm tải database. Cách này chạy ổn suốt 2 tháng, cho đến khi lưu lượng tăng gấp 3 lần trong đợt giảm giá.

Cache giá phục vụ cả trang danh sách lẫn trang chi tiết sản phẩm. Trước sự cố, tỉ lệ cache hit đạt 97%. Nhưng khi giá đổi đột ngột, thời hạn cache cố định khiến khách tiếp tục thấy dữ liệu cũ.

Nhóm tôi gọi lại cho từng khách trong một buổi chiều để xử lý 40 đơn đặt nhầm. Sau đó, tôi thử hạ TTL xuống 15 giây. Tải database tăng gấp đôi, nên nhóm bỏ cách này.

## Xóa cache theo sự kiện

Nhóm chuyển sang xóa cache khi có cập nhật giá. Khi thử trên staging, bản sửa đầu tiên vẫn nạp giá cũ: sự kiện xóa cache chạy trước khi transaction ghi giá commit.

Request kế tiếp đọc database trước khi giá mới được ghi xong, rồi đưa giá cũ trở lại cache. Tôi đã đặt sai thứ tự giữa việc ghi giá và phát sự kiện.

Tôi chuyển sự kiện sang thời điểm sau commit. Nhóm dùng Redis pub/sub để phát sự kiện, rồi xóa cache giá khi nhận được tin cập nhật. Sau sửa đổi này, độ trễ cập nhật giảm xuống dưới 1 giây.

## TTL ngắn làm lưới an toàn

Nhóm vẫn giữ TTL 60 giây. Nếu sự kiện bị mất, cache cũ sẽ hết hạn trong tối đa 60 giây thay vì giữ giá sai suốt 15 phút.

Sau bản sửa, tỉ lệ cache hit giảm từ 97% xuống 92%. Nhóm mất 3 ngày để triển khai thay đổi. Tôi chấp nhận mức giảm đó để giá mới đến cache nhanh hơn.

Trước khi đổi TTL để xử lý dữ liệu cũ, hãy kiểm tra tải database. Nếu xóa cache theo sự kiện, hãy phát sự kiện sau khi transaction commit.
