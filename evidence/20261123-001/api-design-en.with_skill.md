## Identity

- Method and path: `POST /wp/v2/posts`
- Purpose: create one post.
- Authorization: only the roles `editor` and `author` may create a post.
- Publish rule: only an `editor` may set `status` to `publish`.

## DTO and field mapping

| Field | Direction | Type | Required | Constraint |
|---|---|---|---|---|
| `title` | Request | string | Conditional (`title` or `content` must be present) | At most `TBD-1` characters |
| `content` | Request | string | Conditional (`title` or `content` must be present) | — |
| `status` | Request | string | No | One of `publish`, `future`, `draft`, `pending`, `private` |
| `date` | Request | `TBD-2` | No | When `status` is `future`, it must be later than the current time |
| `slug` | Request | string | No | When `title` is also missing: `TBD-5` |
| `categories` | Request | array of integer | No | Each id must exist |
| the saved post | Response | `TBD-3` | — | — |

## Endpoint

Request:

    {"title": "Hello", "status": "draft", "categories": [3]}

Success status: 201. The body is the saved post.

## Processing

- When `status` is missing, the system must set it to `draft`.
- When `slug` is missing, the system must build it from `title`.
- When the slug already exists, the system must add a numeric suffix.

Execution order of the checks and error precedence: `TBD-4`.

## Errors

| Condition | HTTP | Code |
|---|---|---|
| The caller has a role other than `editor` or `author` | 403 | `rest_cannot_create` |
| An `author` sends `status` `publish` | 403 | `rest_cannot_publish` |
| `title` and `content` are both missing | 400 | `rest_empty_post` |
| `status` is `future` and `date` is not later than the current time | 400 | `rest_invalid_date` |
| An id in `categories` does not exist | 400 | `rest_invalid_term` |

## Side effects

None

## Open items

- `TBD-1`: what is the maximum length of `title`?
- `TBD-2`: what is the type of `date`?
- `TBD-3`: what are the fields of the saved post in the response?
- `TBD-4`: in what order does the system run the checks, and which error wins when two checks fail?
- `TBD-5`: how does the system build `slug` when `title` is missing?
