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
type: api-design
non_tech: false
---

# SIMULATED DATA

Endpoint, tên trường, quy tắc nghiệp vụ và mã lỗi đều được bịa cho bài eval này. Brief cố ý thiếu một điểm: không nêu thời hạn trả lời.

## Audience

Lập trình viên backend và QA triển khai, kiểm thử một API đơn hàng.

## Brief

### Idea
Thiết kế `GET /v1/orders/{order_id}` để đọc một đơn hàng. Mọi quy tắc dưới đây là giả lập.

### Business rules
- Chỉ vai trò `owner` và `support` được đọc đơn hàng. Vai trò khác nhận HTTP 403 (`order_forbidden`).
- Khi `order_id` không phải uuid, API trả HTTP 400 (`order_invalid_id`).
- Khi không có đơn hàng nào mang id đó, API trả HTTP 404 (`order_not_found`).
- API trả lời nhanh.
- Phản hồi có `order_id` và `status`. `status` là một trong `pending`, `paid`, `shipped`, `cancelled`.
- Khi thành công, API trả HTTP 200 và đơn hàng.

### Glossary
- `order_id`: id của đơn hàng (uuid).
- `status`: trạng thái của đơn hàng.

## Facts
- Endpoint: `GET /v1/orders/{order_id}`
- Vai trò được phép: `owner`, `support` (vai trò khác nhận HTTP 403 `order_forbidden`)
- `order_id` không phải uuid: HTTP 400 `order_invalid_id`
- Không có đơn hàng mang id đó: HTTP 404 `order_not_found`
- Giá trị status: `pending`, `paid`, `shipped`, `cancelled`
- Mã thành công: HTTP 200


## Candidate output

## Thông tin chung

- Method và path: `GET /v1/orders/{order_id}`
- Mục đích: đọc một đơn hàng. Thời hạn trả lời: `TBD-1`.
- Phân quyền: chỉ role `owner` và `support` được đọc đơn hàng.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `order_id` | Yêu cầu | uuid | Có | — |
| `order_id` | Phản hồi | uuid | — | — |
| `status` | Phản hồi | string | — | `pending`, `paid`, `shipped`, `cancelled` |

## Endpoint

Yêu cầu:

```http
GET /v1/orders/00000000-0000-0000-0000-000000000000
```

Phản hồi, status 200:

```json
{"order_id":"00000000-0000-0000-0000-000000000000","status":"pending"}
```

## Xử lý

Thứ tự kiểm tra và ưu tiên lỗi khi nhiều điều kiện cùng đúng: `TBD-2`.

## Lỗi

| HTTP | Mã | Điều kiện |
|---|---|---|
| 403 | `order_forbidden` | Người gọi có role khác `owner` và `support` |
| 400 | `order_invalid_id` | `order_id` không phải uuid |
| 404 | `order_not_found` | Không có đơn hàng mang `order_id` đó |

## Tác động kèm theo

Không có

## Mục còn mở

- `TBD-1`: Thời hạn trả lời của API là bao lâu?
- `TBD-2`: Thứ tự kiểm tra là gì, và lỗi nào được ưu tiên khi nhiều điều kiện cùng đúng?

<!-- report -->
Giá trị UUID trong ví dụ là giá trị minh họa. `order_id` được xem là bắt buộc vì nó nằm trong path.
