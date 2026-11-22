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

Endpoint và tên trường lấy từ tài liệu công khai WordPress REST API về posts ("Create a Post"). Quy tắc nghiệp vụ và mã lỗi được bịa cho bài eval này.

## Audience

Lập trình viên backend và QA triển khai, kiểm thử một API blog.

## Brief

### Idea
Thiết kế `POST /wp/v2/posts` để tạo một bài viết. Nguồn: tài liệu WordPress REST API về posts, endpoint "Create a Post". Các quy tắc dưới đây là giả lập, trừ tên trường và giá trị cho phép.

### Business rules
- Chỉ role `editor` và `author` được tạo bài viết. Role khác nhận HTTP 403 (`rest_cannot_create`).
- Phải có `title` hoặc `content`. Nếu thiếu cả hai, API trả HTTP 400 (`rest_empty_post`).
- `status` là một trong `publish`, `future`, `draft`, `pending`, `private`. Mặc định là `draft`.
- Chỉ `editor` được đặt `status` là `publish`. `author` gửi `publish` nhận HTTP 403 (`rest_cannot_publish`).
- Khi `status` là `future`, `date` phải sau thời điểm hiện tại. Nếu không, API trả HTTP 400 (`rest_invalid_date`).
- Khi thiếu `slug`, hệ thống tạo từ `title`. Khi slug đã tồn tại, hệ thống thêm hậu tố số.
- Mỗi id trong `categories` phải tồn tại. Id không có trả HTTP 400 (`rest_invalid_term`).
- Khi thành công, API trả HTTP 201 và bài viết đã lưu.
- Nguồn không nêu độ dài tối đa của `title`. Ghi `TBD`.

### Glossary
- `title`: tiêu đề bài viết.
- `content`: nội dung bài viết.
- `status`: trạng thái xuất bản của bài viết.
- `slug`: phần URL duy nhất của bài viết.
- `categories`: danh sách id danh mục (số nguyên).

## Facts
- Endpoint: `POST /wp/v2/posts`
- Role được phép: `editor`, `author` (role khác nhận HTTP 403 `rest_cannot_create`)
- Giá trị status: `publish`, `future`, `draft`, `pending`, `private`; mặc định `draft`
- Chỉ `editor` được publish (nếu không, HTTP 403 `rest_cannot_publish`)
- Thiếu cả `title` và `content`: HTTP 400 `rest_empty_post`
- `future` cần `date` ở tương lai (nếu không, HTTP 400 `rest_invalid_date`)
- Id danh mục không có: HTTP 400 `rest_invalid_term`
- Mã thành công: HTTP 201


## Candidate output

## Thông tin chung

- Method và path: `POST /wp/v2/posts`
- Mục đích: tạo bài viết.
- Phân quyền: role `editor` và `author` được tạo bài viết. Chỉ role `editor` được đặt `status` là `publish`.

## DTO và ánh xạ trường

| Trường | Hướng | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|---|
| `title` | Yêu cầu | string | Có điều kiện (khi `content` vắng mặt) | Tối đa `TBD-1` |
| `content` | Yêu cầu | string | Có điều kiện (khi `title` vắng mặt) | — |
| `status` | Yêu cầu | string | Không | `publish`, `future`, `draft`, `pending`, `private` |
| `slug` | Yêu cầu | string | Không | — |
| `categories` | Yêu cầu | array<integer> | `TBD-3` | Mỗi id phải tồn tại |
| `date` | Yêu cầu | `TBD-4` | Có điều kiện (khi `status` là `future`) | Phải sau thời điểm hiện tại |
| Bài viết đã lưu | Phản hồi | `TBD-2` | — | — |

## Endpoint

Yêu cầu:

```json
{"title": "Tiêu đề bài viết"}
```

Phản hồi thành công có status `201`. Không có ví dụ phản hồi vì chưa có trường phản hồi với kiểu đã biết.

## Xử lý

- Khi thiếu `slug`, hệ thống tạo `slug` từ `title`. Khi `slug` đã tồn tại, hệ thống thêm hậu tố số.
- Khi thiếu `status`, hệ thống dùng `draft`.
- Thứ tự xử lý: `TBD-7`.
- Khi nhiều lỗi cùng xảy ra, lỗi ưu tiên: `TBD-8`.

## Lỗi

| Điều kiện | HTTP | Mã |
|---|---:|---|
| Người gọi có role khác `editor` hoặc `author` | 403 | `rest_cannot_create` |
| Thiếu cả `title` và `content` | 400 | `rest_empty_post` |
| Role `author` gửi `status` là `publish` | 403 | `rest_cannot_publish` |
| `status` không thuộc danh sách giá trị cho phép | `TBD-5` | `TBD-5` |
| `status` là `future` và `date` không ở tương lai | 400 | `rest_invalid_date` |
| Một id trong `categories` không tồn tại | 400 | `rest_invalid_term` |
| Độ dài `title` vượt giới hạn | `TBD-6` | `TBD-6` |

## Tác động kèm theo

Không có

## Mục còn mở

- `TBD-1`: Độ dài tối đa của `title` là bao nhiêu?
- `TBD-2`: Phản hồi gồm những trường nào và kiểu của từng trường là gì?
- `TBD-3`: `categories` có bắt buộc không?
- `TBD-4`: Kiểu dữ liệu của `date` là gì?
- `TBD-5`: API trả HTTP và mã lỗi nào khi `status` không thuộc danh sách cho phép?
- `TBD-6`: API trả HTTP và mã lỗi nào khi `title` vượt độ dài tối đa?
- `TBD-7`: Thứ tự xử lý các quy tắc là gì?
- `TBD-8`: Khi nhiều lỗi cùng xảy ra, lỗi nào được ưu tiên?
