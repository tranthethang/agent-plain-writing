## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: create one post.
- Authorization: only the roles `editor` and `author` may create a post. Only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `title` | Request | string | Conditional (at least one of `title` or `content`) | At most `TBD-1` characters |
| `content` | Request | string | Conditional (at least one of `title` or `content`) | — |
| `status` | Request | enum | No | `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | `TBD-4` | Conditional (`status` is `future`) | — |
| `slug` | Request | string | No | — |
| `categories` | Request | array of integers | `TBD-3` | — |
| Saved post | Response | `TBD-5` | — | — |

## Endpoint

Request:

```json
{"title": "Post title", "content": "Post content"}
```

Success status: `201`.

## Processing

- The system uses `draft` as the default `status`.
- When `slug` is missing, the system builds it from `title` and adds a numeric suffix if the slug already exists. When `slug` and `title` are both missing, the system’s behavior is `TBD-6`.
- Execution order: `TBD-8`.
- Error precedence: `TBD-8`.

## Errors

| Condition | HTTP status | Code |
|---|---:|---|
| The caller has a role other than `editor` or `author` | 403 | `rest_cannot_create` |
| An `author` sends `status` as `publish` | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| `status` is not one of the allowed values | `TBD-7` | `TBD-7` |
| `status` is `future` and `date` is not later than the current time | 400 | `rest_invalid_date` |
| A `categories` id does not exist | 400 | `rest_invalid_term` |
| `title` exceeds `TBD-1` characters | `TBD-2` | `TBD-2` |

## Side effects

None

## Open items

- `TBD-1`: What is the maximum length of `title`?
- `TBD-2`: Which HTTP status and error code apply when `title` exceeds the maximum length?
- `TBD-3`: Is `categories` required?
- `TBD-4`: What is the type and format of `date`?
- `TBD-5`: What fields and types does the saved post response contain?
- `TBD-6`: What should the system do when `slug` is missing and `title` is also missing?
- `TBD-7`: Which HTTP status and error code apply when `status` is not an allowed value?
- `TBD-8`: What is the execution order, and which error takes precedence when multiple conditions fail?

---

The API design is complete. I made no assumptions; unspecified details are marked as open items.