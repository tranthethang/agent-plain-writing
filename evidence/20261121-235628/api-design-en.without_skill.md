# Create a Post API Design

## Endpoint

`POST /wp/v2/posts`

Creates one post.

## Request fields

| Field | Description | Rules |
|---|---|---|
| `title` | The title of the post. | Its maximum length is **TBD**. |
| `content` | The body of the post. | At least one of `title` or `content` must be present. |
| `status` | The publication state of the post. | Allowed values: `publish`, `future`, `draft`, `pending`, `private`. Defaults to `draft`. |
| `date` | The post date. | When `status` is `future`, it must be later than the current time. |
| `slug` | The unique URL part of the post. | If omitted, it is built from `title`. If it already exists, a numeric suffix is added. |
| `categories` | A list of category IDs. | Each ID is an integer and must exist. |

## Business rules

- Only users with the `editor` or `author` role may create a post.
- Only an `editor` may set `status` to `publish`.
- If both `title` and `content` are missing, the request fails.
- If `status` is `future`, `date` must be later than the current time.
- Every ID in `categories` must identify an existing category.

## Responses

### Success

Returns **HTTP 201** with the saved post.

### Errors

| Condition | HTTP status | Error code |
|---|---:|---|
| Caller’s role is neither `editor` nor `author` | 403 | `rest_cannot_create` |
| An `author` attempts to set `status` to `publish` | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| `status` is `future` and `date` is not later than the current time | 400 | `rest_invalid_date` |
| A category ID does not exist | 400 | `rest_invalid_term` |

## QA checks

- Verify that `editor` and `author` can create posts, and that other roles receive `403 rest_cannot_create`.
- Verify that a request missing both `title` and `content` receives `400 rest_empty_post`.
- Verify the default status is `draft` and that the listed status values are accepted.
- Verify that an `author` setting `publish` receives `403 rest_cannot_publish`.
- Verify that `future` requires a later `date`; otherwise the response is `400 rest_invalid_date`.
- Verify that an omitted `slug` is built from `title`, and that an existing slug receives a numeric suffix.
- Verify that an unknown category ID receives `400 rest_invalid_term`.
- Verify that a successful creation returns `201` with the saved post.

**Open specification detail:** The maximum length of `title` is **TBD**.