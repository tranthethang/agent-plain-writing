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
type: essay
non_tech: true
---

# SIMULATED DATA

## Audience

Độc giả phổ thông của một chuyên mục tản văn.

## Brief

### Summary
Một người viết nhớ tuần đầu tiên chuyển lên thành phố học đại học. Căn phòng thuê trống trơn. Bố đã sửa một chiếc quạt bàn cũ và gói vào thùng các tông. Chiều ngày thứ ba, người viết cắm quạt vào ổ điện, và căn phòng lần đầu có cảm giác có người ở.

### Main points
1. Căn phòng thuê trống trong 3 ngày đầu.
2. Bố không nhắc chuyện tiền, chỉ dặn cách thay cầu chì.
3. Lúc quạt quay là lúc căn phòng giống một mái nhà.

### Reader
Người lớn từng xa nhà, muốn đọc một câu chuyện lặng lẽ, thật, không phải lời khuyên.

### Voice
Ngôi thứ nhất, bình tĩnh, cụ thể. Cho thấy khoảnh khắc qua đồ vật và việc nhỏ.

### Sample paragraph
Chiếc vali để góc phòng, khóa kéo hỏng, buộc tạm bằng một đoạn dây ni lông.

### Words to use or avoid
- Dùng: `quạt`, `cầu chì`, `dây`, `căn phòng`.
- Tránh: `khó quên`, `tuyệt vời`, `bài học`, `tóm lại`.

## Facts
- Số ngày căn phòng trống: 3
- Món bố sửa: 1 chiếc quạt bàn
- Lời dặn của bố: thay cầu chì nếu động cơ nóng


## Candidate output

# Chiếc quạt trong căn phòng thuê

Tuần đầu lên thành phố học đại học, căn phòng thuê của tôi trống trơn suốt ba ngày. Chiếc vali nằm ở góc phòng, khóa kéo hỏng, buộc tạm bằng một đoạn dây ni lông.

Bố sửa chiếc quạt bàn cũ rồi gói vào thùng các-tông. Bố không nhắc chuyện tiền. Ông chỉ dặn tôi thay cầu chì nếu động cơ nóng. Tôi vẫn tự hỏi, có phải đó là điều duy nhất bố muốn nói với tôi không?

Chiều ngày thứ ba, tôi cắm quạt vào ổ điện. Cánh quạt quay. Tiếng máy vang trong căn phòng trống.

---

Tôi thêm một suy nghĩ mở: người kể tự hỏi liệu lời dặn về cầu chì có phải điều duy nhất bố muốn nói hay không.
