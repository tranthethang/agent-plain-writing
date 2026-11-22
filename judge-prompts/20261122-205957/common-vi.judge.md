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
type: common
non_tech: false
---

# SIMULATED DATA

## Audience

Kỹ sư backend đọc thông báo bảo trì nội bộ trong bảng tin hệ thống.

## Brief

### Summary
Cụm PostgreSQL môi trường staging (`db-stage-02`) nâng RAM từ 16 GB lên 32 GB vào 04:00 UTC ngày 2026-12-03. Quá trình nâng cấp mất 8 phút; trong lúc này các kết nối tới staging bị ngắt và job CI đang chờ sẽ thử lại sau 30 giây. Chuỗi kết nối và thông tin đăng nhập giữ nguyên.

### Reader
Kỹ sư backend chạy test tích hợp trên staging, cần biết đúng khung giờ và ảnh hưởng.

### Words to use or avoid
- Use: `staging`, `cụm`, `thời gian gián đoạn`.
- Avoid: `liền mạch`, `tối ưu hóa`, `tôi`, `chúng tôi`.

## Facts
- Tên cụm: `db-stage-02`
- Hệ quản trị cơ sở dữ liệu: PostgreSQL
- Thay đổi RAM: 16 GB lên 32 GB
- Thời gian bảo trì: 04:00 UTC ngày 2026-12-03
- Thời lượng: 8 phút
- Thời gian chờ thử lại của CI: 30 giây


## Candidate output

## Bảo trì cụm staging `db-stage-02`

Cụm PostgreSQL staging `db-stage-02` sẽ được nâng RAM từ 16 GB lên 32 GB lúc 04:00 UTC ngày 2026-12-03.

Thời gian gián đoạn kéo dài 8 phút. Trong thời gian này, các kết nối tới staging sẽ bị ngắt. Job CI đang chờ sẽ thử lại sau 30 giây.

Chuỗi kết nối và thông tin đăng nhập giữ nguyên.
