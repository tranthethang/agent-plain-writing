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
lang: en
type: tech-blog
non_tech: true
---

# SIMULATED DATA

## Audience

Independent bakery and cafe owners who manage daily stock on spreadsheets and are not software engineers.

## Brief

### Summary
Last month a small bakery switched from paper order slips to a shared online sheet with automatic low-stock alerts. Before the switch, the shop ran out of flour twice in 3 weeks and threw away 18 kg of unsold dough in those 3 weeks. The first alert, set at 10 kg, came too late because the supplier needs 2 days to deliver and the shop uses about 8 kg a day. After moving the alert to 20 kg, waste dropped to 4 kg per week and the shop had no stockout in the next 4 weeks. In the first week, staff forgot to update the sheet twice, so the owner taped a printed reminder next to the till.

### Main points
1. Paper slips hide what is running low until the shelf is empty.
2. One shared sheet with a fixed reorder number prevents panic buying.
3. Checking the sheet takes 5 minutes at closing time.

### Reader
Shop owners with no technical background who want practical steps, not software jargon.

### Voice
First person ("I", "you"), plain and practical, like one shop owner talking to another over coffee.

### Sample paragraph
I used to count flour bags by hand every Sunday night. Twice in three weeks, we still ran out before noon on Tuesday.

The first alert I set was 10 kg. It went off on a Thursday evening, and we still ran out on Saturday morning. The supplier needs two days, and we go through about 8 kg a day.

### Words to use or avoid
- Use: `sheet`, `alert`, `stock`.
- Avoid: `database`, `webhook`, `pipeline`, `leverage`, `seamless`.

## Facts
- Flour stockouts before switch: 2 times in 3 weeks
- Unsold dough wasted before switch: 18 kg in those 3 weeks
- Reorder alert threshold: 20 kg
- Waste after switch: 4 kg per week
- Daily check time: 5 minutes at closing time
- First alert threshold tried: 10 kg (flour ran out once more in the first week)
- Supplier delivery time: 2 days
- Daily flour use: about 8 kg
- Stockouts in the 4 weeks after moving the alert to 20 kg: 0
- Emergency flour runs before switch: 2 trips to a wholesale store, 40 minutes each
- Staff who update the sheet: 3
- Missed sheet updates in the first week: 2
- Fix for missed updates: a printed reminder taped next to the till
- Sheet tool: a free online spreadsheet


## Candidate output

# A 20 kg alert gave us time to order flour

Last month, I replaced our paper order slips with a shared online sheet and low-stock alerts. My first alert came too late, so I changed its threshold.

## Paper hid what was running low

Before the switch, we ran out of flour twice in three weeks. In those same three weeks, we threw away 18 kg of unsold dough. I also made two emergency trips to a wholesale store, 40 minutes each.

Paper slips did not give us one shared view of what was running low. We needed a way for the three staff members who update stock to see the same information.

## The first alert came too late

I first set the flour alert at 10 kg. It went off on Thursday evening, but we ran out again on Saturday morning.

Our supplier needs two days to deliver. We use about 8 kg of flour a day, so that alert left too little time to restock.

## A fixed threshold helped

I moved the alert to 20 kg. In the next four weeks, we had no flour stockouts. Waste dropped to 4 kg per week.

The shared sheet also gave us a set place to check stock. At closing, the daily check takes five minutes.

## A reminder made the routine stick

In the first week, staff forgot to update the sheet twice. I taped a printed reminder next to the till.

If you use a shared sheet, choose a fixed reorder point and check it at closing. Put a reminder where staff will see it if updates slip.

---

I wrote this as a short tech blog for independent bakery and café owners, using the owner’s first-person voice. I did not add facts beyond the brief.
