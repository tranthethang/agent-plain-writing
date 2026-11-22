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
lang: ja
type: essay
non_tech: true
---

# SIMULATED DATA

## Audience

エッセイ欄の一般読者。

## Brief

### Summary
書き手は、大学のために知らない街へ引っ越した最初の週を思い出す。借りた部屋は何もなかった。父は古い卓上扇風機を直し、段ボール箱に入れて持たせた。3日目の午後にコンセントを差すと、部屋に初めて人の気配が生まれた。

### Main points
1. 借りた部屋は最初の3日間、空っぽに感じた。
2. 父はお金の話をせず、ヒューズの替え方だけを教えた。
3. 扇風機が回った瞬間、部屋が家になった。

### Reader
家を離れた経験があり、助言ではなく静かで正直な話を読みたい大人。

### Voice
一人称、落ち着いた調子、具体的に。物と小さな動作で場面を見せる。

### Sample paragraph
隅に置いたスーツケースは、壊れたファスナーを紐で結んだままだった。

### Words to use or avoid
- 使う: `扇風機`、`ヒューズ`、`紐`、`部屋`。
- 避ける: `忘れられない`、`素晴らしい`、`教訓`、`結論として`。

## Facts
- 部屋が空っぽだった日数: 3
- 父が直したもの: 卓上扇風機 1台
- 父の指示: モーターが熱くなったらヒューズを替える


## Candidate output

# 三日目の扇風機

隅に置いたスーツケースは、壊れたファスナーを紐で結んだままだった。借りた部屋は空っぽだった。そのまま三日間が過ぎた。

父は古い卓上扇風機を直し、段ボール箱に入れて持たせた。お金の話はしなかった。モーターが熱くなったらヒューズを替える、と父は教えた。父には、ヒューズの替え方を教えるだけで足りていたのだろうか。

三日目の午後、私は扇風機のプラグをコンセントに差した。羽根が回り始めた。部屋の空気が動いた。空っぽだった部屋に、初めて人の気配が生まれた。

---

本文では、三つの要点を場面として描きました。加えた内面の一文は、父がヒューズの説明だけで足りると思っていたのかを問うものです。事実関係に推測は加えていません。
