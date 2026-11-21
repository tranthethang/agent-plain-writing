## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: create one post.
- Authorization: the roles `editor` and `author` may create a post. Only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Direction | Field | Type | Required | Constraint |
|---|---|---|---|---|
| Request | `title` | TBD-1 | Conditional (at least one of `title` or `content`) | Maximum length: TBD-2 |
| Request | `content` | TBD-3 | Conditional (at least one of `title` or `content`) | — |
| Request | `status` | TBD-4 | No | One of `publish`, `future`, `draft`, `pending`, `private`; defaults to `draft` |
| Request | `slug` | TBD-5 | No | If missing, the system builds it from `title`. If it already exists, the system adds a numeric suffix. |
| Request | `date` | TBD-6 | Conditional (`status` is `future`) | Must be later than the current time when `status` is `future` |
| Request | `categories` | List of integers | TBD-7 | Each id must exist |
| Response | Saved post | TBD-8 | — | The API returns the saved post; its response fields are not specified. |

## Endpoint

Success status: `201`.

## Processing

- The system checks the caller role. On failure, it stops with `rest_cannot_create`.
- The system checks whether the caller may set `status` to `publish`. On failure, it stops with `rest_cannot_publish`.
- When both `title` and `content` are missing, the system stops with `rest_empty_post`.
- The system applies the `status` default and allowed values. For an invalid value, it stops with TBD-9.
- When `status` is `future`, the system checks that `date` is later than the current time. On failure, it stops with `rest_invalid_date`.
- When `slug` is missing, the system builds it from `title`. When the slug already exists, the system adds a numeric suffix.
- The system checks that each id in `categories` exists. On failure, it stops with `rest_invalid_term`.
- The system saves the post and returns it.

Execution and error precedence: TBD-10.

## Errors

| HTTP | Code | Condition |
|---|---|---|
| 403 | `rest_cannot_create` | The caller's role is not `editor` or `author` |
| 403 | `rest_cannot_publish` | An `author` sets `status` to `publish` |
| 400 | `rest_empty_post` | Both `title` and `content` are missing |
| 400 | `rest_invalid_date` | `status` is `future` and `date` is not later than the current time |
| 400 | `rest_invalid_term` | A category id does not exist |
| TBD-11 | TBD-11 | `status` is not one of the allowed values |

## Side effects

No additional side effects are specified.

## Open items

- TBD-1: What is the type of `title`?
- TBD-2: What is the maximum length of `title`?
- TBD-3: What is the type of `content`?
- TBD-4: What is the type of `status`?
- TBD-5: What is the type of `slug`?
- TBD-6: What is the type of `date`?
- TBD-7: Is `categories` required?
- TBD-8: What fields and types does the saved-post response include?
- TBD-9: What HTTP status and error code apply when `status` is not one of the allowed values?
- TBD-10: What is the execution and error precedence for the checks?
- TBD-11: What HTTP status and error code apply when `status` is not one of the allowed values?