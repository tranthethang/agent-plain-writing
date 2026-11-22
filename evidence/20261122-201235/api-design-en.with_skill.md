## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: create one post.
- Authorization: only the roles `editor` and `author` may create a post. Only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `title` | Request | string | Conditional (at least one of `title` or `content`) | At most `TBD-1` characters |
| `content` | Request | string | Conditional (at least one of `title` or `content`) | — |
| `status` | Request | enum of strings | No | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | `TBD-2` | Conditional (`status` is `future`) | — |
| `slug` | Request | string | No | — |
| `categories` | Request | array of integers | `TBD-3` | — |
| Response body | Response | `TBD-5` | — | — |

## Endpoint

Request:

```json
{
  "title": "Example post",
  "status": "draft"
}
```

Success status: `201`

## Processing

- When `status` is missing, the system uses `draft`.
- When `slug` is missing, the system builds it from `title`. If `title` is also missing, the slug behavior is `TBD-4`.
- When the generated slug already exists, the system adds a numeric suffix.
- Execution order and error precedence: `TBD-6`.

## Errors

| Condition | HTTP status | Code |
|---|---:|---|
| The caller has a role other than `editor` or `author` | 403 | `rest_cannot_create` |
| The caller is an `author` and sends `status` as `publish` | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| `status` is not one of the allowed values | `TBD-7` | `TBD-7` |
| `status` is `future` and `date` is absent or not later than the current time | 400 | `rest_invalid_date` |
| A category id does not exist | 400 | `rest_invalid_term` |
| `title` exceeds `TBD-1` characters | `TBD-8` | `TBD-8` |

## Side effects

None

## Open items

- `TBD-1`: What is the maximum length of `title`?
- `TBD-2`: What is the type and format of `date`?
- `TBD-3`: Is `categories` required?
- `TBD-4`: How should the system build `slug` when `title` is missing?
- `TBD-5`: What fields and types does the saved post response contain?
- `TBD-6`: What is the execution order of the checks, and which error takes precedence when multiple checks fail?
- `TBD-7`: What HTTP status and code does the system return when `status` is not an allowed value?
- `TBD-8`: What HTTP status and code does the system return when `title` exceeds its maximum length?

---

The API design is drafted. I treated a missing `date` as invalid when `status` is `future`. I omitted the response example because the response fields are unspecified.