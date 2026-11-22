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

The endpoint and the field names come from the public WordPress REST API reference for posts ("Create a Post"). The business rules and error codes are invented for this eval.

## Audience

Backend developers and QA engineers who implement and test a blog API.

## Brief

### Idea
Design `POST /wp/v2/posts` to create one post. Source: the WordPress REST API reference for posts, endpoint "Create a Post". The rules below are simulated, apart from the field names and allowed values.

### Business rules
- Only the roles `editor` and `author` may create a post. Other roles receive HTTP 403 (`rest_cannot_create`).
- `title` or `content` must be present. If both are missing, the API returns HTTP 400 (`rest_empty_post`).
- `status` is one of `publish`, `future`, `draft`, `pending`, `private`. The default is `draft`.
- Only an `editor` may set `status` to `publish`. An `author` who sends `publish` receives HTTP 403 (`rest_cannot_publish`).
- When `status` is `future`, `date` must be later than the current time. Otherwise the API returns HTTP 400 (`rest_invalid_date`).
- When `slug` is missing, the system builds it from `title`. When the slug already exists, the system adds a numeric suffix.
- Each id in `categories` must exist. An unknown id returns HTTP 400 (`rest_invalid_term`).
- On success, the API returns HTTP 201 and the saved post.
- The maximum length of `title` is not given by the source. Mark it `TBD`.

### Glossary
- `title`: the title of the post.
- `content`: the body of the post.
- `status`: the publication state of the post.
- `slug`: the unique URL part of the post.
- `categories`: list of category ids (integers).

## Facts
- Endpoint: `POST /wp/v2/posts`
- Allowed roles: `editor`, `author` (others get HTTP 403 `rest_cannot_create`)
- Status values: `publish`, `future`, `draft`, `pending`, `private`; default `draft`
- Only `editor` may publish (otherwise HTTP 403 `rest_cannot_publish`)
- Missing `title` and `content`: HTTP 400 `rest_empty_post`
- `future` needs a later `date` (otherwise HTTP 400 `rest_invalid_date`)
- Unknown category id: HTTP 400 `rest_invalid_term`
- Success status: HTTP 201


## Candidate output

## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: create one post.
- Authorization: the roles `editor` and `author` may create a post. Only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `title` | Request | string | Conditional (at least one of `title` or `content`) | Maximum length: TBD-1 |
| `content` | Request | string | Conditional (at least one of `title` or `content`) | — |
| `status` | Request | string | No | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | TBD-2 | Conditional (`status` is `future`) | Later than the current time when `status` is `future` |
| `slug` | Request | string | No | — |
| `categories` | Request | array of integers | No | Each category id must exist |
| Saved post | Response | TBD-3 | — | — |

## Endpoint

Success status: `201`

Request:

```json
{"title": "Example", "status": "draft"}
```

## Processing

When `status` is omitted, the system sets it to `draft`.

When `slug` is missing, the system builds it from `title`. When the slug already exists, the system adds a numeric suffix.

When `slug` is missing and `title` is absent, the system behavior is TBD-5.

Execution order and error precedence: TBD-4.

## Errors

| Condition | HTTP status | Code |
|---|---:|---|
| The caller has a role other than `editor` or `author` | 403 | `rest_cannot_create` |
| The caller is an `author` and sets `status` to `publish` | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| `status` is `future` and `date` is missing or not later than the current time | 400 | `rest_invalid_date` |
| A category id does not exist | 400 | `rest_invalid_term` |
| `title` exceeds its maximum length | TBD-6 | TBD-6 |
| `status` is not one of the allowed values | TBD-7 | TBD-7 |

## Side effects

Not specified.

## Open items

- `TBD-1`: What is the maximum length of `title`?
- `TBD-2`: What is the type of `date`?
- `TBD-3`: Which fields does the saved-post response contain?
- `TBD-4`: What is the execution order, and which error takes precedence when multiple conditions fail?
- `TBD-5`: What should the system do when `slug` is missing and `title` is absent?
- `TBD-6`: What HTTP status and error code should the system return when `title` exceeds its maximum length?
- `TBD-7`: What HTTP status and error code should the system return when `status` is not one of the allowed values?
