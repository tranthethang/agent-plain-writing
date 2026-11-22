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