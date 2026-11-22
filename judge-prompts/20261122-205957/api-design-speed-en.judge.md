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
type: api-design
non_tech: false
---

# SIMULATED DATA

The endpoint, the field names, the business rules and the error codes are invented for this eval. The brief has one gap on purpose: it gives no time limit for the response.

## Audience

Backend developers and QA engineers who implement and test an order API.

## Brief

### Idea
Design `GET /v1/orders/{order_id}` to read one order. All rules below are simulated.

### Business rules
- Only the roles `owner` and `support` may read an order. Other roles receive HTTP 403 (`order_forbidden`).
- When `order_id` is not a uuid, the API returns HTTP 400 (`order_invalid_id`).
- When no order has that id, the API returns HTTP 404 (`order_not_found`).
- The API responds quickly.
- The response holds `order_id` and `status`. `status` is one of `pending`, `paid`, `shipped`, `cancelled`.
- On success, the API returns HTTP 200 and the order.

### Glossary
- `order_id`: the id of the order (uuid).
- `status`: the state of the order.

## Facts
- Endpoint: `GET /v1/orders/{order_id}`
- Allowed roles: `owner`, `support` (others get HTTP 403 `order_forbidden`)
- `order_id` is not a uuid: HTTP 400 `order_invalid_id`
- No order with that id: HTTP 404 `order_not_found`
- Status values: `pending`, `paid`, `shipped`, `cancelled`
- Success status: HTTP 200


## Candidate output

## Identity

- Method and path: `GET /v1/orders/{order_id}`
- Purpose: read one order. Response-time limit: `TBD-1`.
- Authorization: only the roles `owner` and `support` may read an order.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `order_id` | Request | uuid | Yes | — |
| `order_id` | Response | uuid | — | — |
| `status` | Response | string | — | — |

## Endpoint

Request:

    GET /v1/orders/00000000-0000-4000-8000-000000000000

Response, status 200:

    {"order_id": "00000000-0000-4000-8000-000000000000", "status": "pending"}

## Processing

Execution order and error precedence: `TBD-2`.

## Errors

| Condition | HTTP status | Code |
|---|---:|---|
| The caller has a role other than `owner` or `support` | 403 | `order_forbidden` |
| `order_id` is not a UUID | 400 | `order_invalid_id` |
| No order has the requested ID | 404 | `order_not_found` |

## Side effects

None

## Open items

- `TBD-1`: What response-time limit defines “quickly”?
- `TBD-2`: In what order does the API apply authorization, UUID validation, and order lookup, and which error takes precedence when multiple conditions apply?
