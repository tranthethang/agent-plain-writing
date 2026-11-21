## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: Create one post.
- Authorization: Only the roles `editor` and `author` may create a post. Only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `title` | Request | string | No | Maximum length: `TBD-1` |
| `content` | Request | string | No | — |
| `status` | Request | enum | No | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | `TBD-3` | Conditional (`status` is `future`) | Must be later than the current time when `status` is `future` |
| `slug` | Request | string | No | — |
| `categories` | Request | array of integer ids | `TBD-2` | Each id must exist |
| Response body | Response | `TBD-4` | — | — |

## Endpoint

Request:

```json
{"title":"<title>"}
```

Success status: `201`

## Processing

- When `status` is absent, the system must set it to `draft`.
- When `slug` is absent and `title` is present, the system must build the slug from `title`.
- When a slug already exists, the system must add a numeric suffix. The suffix selection rule is `TBD-6`.
- When `slug` and `title` are both absent, slug generation is `TBD-5`.
- Execution order and error precedence: `TBD-8`.

## Errors

| Condition | HTTP status | Code |
|---|---:|---|
| The caller has a role other than `editor` or `author` | 403 | `rest_cannot_create` |
| An `author` sets `status` to `publish` | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| `status` is `future` and `date` is missing or not later than the current time | 400 | `rest_invalid_date` |
| A category id does not exist | 400 | `rest_invalid_term` |
| `title` exceeds the maximum length in `TBD-1` | `TBD-7` | `TBD-7` |

## Side effects

None

## Open items

- `TBD-1`: What is the maximum length of `title`?
- `TBD-2`: Is `categories` required?
- `TBD-3`: What is the type of `date`?
- `TBD-4`: What fields and types does the success response contain?
- `TBD-5`: What should the system do when both `slug` and `title` are absent?
- `TBD-6`: How does the system choose the numeric suffix for an existing slug?
- `TBD-7`: What HTTP status and error code apply when `title` exceeds its maximum length?
- `TBD-8`: What is the execution order, and which error takes precedence when multiple conditions fail?