## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: create one post.
- Authorization: only the roles `editor` and `author` may create a post. Only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `title` | Request | string | Conditional (at least one of `title` or `content` is present) | Maximum length: TBD-1 |
| `content` | Request | string | Conditional (at least one of `title` or `content` is present) | — |
| `status` | Request | enum | No | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | TBD-2 | Conditional (`status` is `future`) | Later than the current time when `status` is `future` |
| `slug` | Request | string | No | — |
| `categories` | Request | array of integers | TBD-3 | — |
| Saved post | Response | TBD-4 | — | — |

## Endpoint

Request:

```json
{
  "title": "Example post",
  "content": "Example content",
  "status": "draft"
}
```

Success status: `201`

## Processing

- When `status` is missing, the system uses `draft`.
- When `slug` is missing, the system builds it from `title`. When that slug already exists, the system adds a numeric suffix.
- Execution order and error precedence: TBD-5.

## Errors

| HTTP | Code | Condition |
|---|---|---|
| 403 | `rest_cannot_create` | The caller has a role other than `editor` or `author` |
| 403 | `rest_cannot_publish` | The caller has the `author` role and sends `status` as `publish` |
| 400 | `rest_empty_post` | Both `title` and `content` are missing |
| 400 | `rest_invalid_date` | `status` is `future` and `date` is missing or is not later than the current time |
| 400 | `rest_invalid_term` | A category id does not exist |
| TBD-6 | TBD-6 | The title exceeds its maximum length |

## Side effects

None

## Open items

- `TBD-1`: What is the maximum length of `title`, and what unit measures it?
- `TBD-2`: What is the type of `date`?
- `TBD-3`: Is `categories` required?
- `TBD-4`: What fields and structure does the saved post response contain?
- `TBD-5`: What is the execution order of checks, and which error takes precedence when multiple checks fail?
- `TBD-6`: What HTTP status and error code does the system return when `title` exceeds its maximum length?
- `TBD-7`: What should the system do when both `slug` and `title` are missing?