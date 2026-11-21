# Create a post

## Endpoint

`POST /wp/v2/posts`

Creates one post.

## Request fields

| Field | Meaning and rules |
|---|---|
| `title` | Post title. Maximum length: **TBD**. |
| `content` | Post body. |
| `status` | Publication state: `publish`, `future`, `draft`, `pending`, or `private`. Defaults to `draft`. Only an `editor` may set it to `publish`. |
| `date` | When `status` is `future`, this must be later than the current time. The required date format is not specified. |
| `slug` | Unique URL part of the post. If omitted, the system builds it from `title`. If the slug already exists, the system adds a numeric suffix. |
| `categories` | List of category IDs (integers). Each ID must exist. |

A request must include `title` or `content`, or both. If both are missing, the API returns `400 rest_empty_post`.

## Authorization and validation

- Only users with the `editor` or `author` role may create a post. Other roles receive `403 rest_cannot_create`.
- An `author` who sets `status` to `publish` receives `403 rest_cannot_publish`.
- If `status` is `future` and `date` is not later than the current time, the API returns `400 rest_invalid_date`.
- If any ID in `categories` is unknown, the API returns `400 rest_invalid_term`.

## Responses

| Outcome | HTTP status | Error code or response |
|---|---:|---|
| Post created | `201` | The saved post |
| User role cannot create posts | `403` | `rest_cannot_create` |
| Author attempts to publish | `403` | `rest_cannot_publish` |
| Both `title` and `content` are missing | `400` | `rest_empty_post` |
| `future` post has an invalid date | `400` | `rest_invalid_date` |
| Category ID is unknown | `400` | `rest_invalid_term` |

## QA checks

- Verify that `editor` and `author` can create a post, and that other roles receive `403 rest_cannot_create`.
- Verify that a request missing both `title` and `content` receives `400 rest_empty_post`.
- Verify the default `status` is `draft` when `status` is omitted.
- Verify that an `editor` can set `status` to `publish` and an `author` receives `403 rest_cannot_publish` for that value.
- Verify that a `future` post requires a `date` later than the current time; otherwise expect `400 rest_invalid_date`.
- Verify that an unknown category ID produces `400 rest_invalid_term`.
- Verify that an omitted `slug` is built from `title` and that an existing slug receives a numeric suffix.
- Verify successful creation returns `201` and the saved post.

The request date format, saved-post response schema, and title maximum length are not specified here.