# Create a Post API

## Endpoint

`POST /wp/v2/posts`

Creates one post.

## Authorization

Only users with the `editor` or `author` role may create a post. Other roles receive **HTTP 403** with error code `rest_cannot_create`.

Only an `editor` may set `status` to `publish`. An `author` who requests `publish` receives **HTTP 403** with error code `rest_cannot_publish`.

## Request fields

| Field | Description | Rules |
|---|---|---|
| `title` | Post title | Maximum length: **TBD** |
| `content` | Post body | Either `title` or `content` must be present. |
| `status` | Publication state | Allowed values: `publish`, `future`, `draft`, `pending`, `private`. Defaults to `draft`. |
| `date` | Post date | When `status` is `future`, this must be later than the current time. |
| `slug` | Unique URL part of the post | If missing, the system builds it from `title`. If it already exists, the system adds a numeric suffix. |
| `categories` | List of category IDs | Each ID must exist. IDs are integers. |

If both `title` and `content` are missing, the API returns **HTTP 400** with error code `rest_empty_post`.

When `status` is `future` and `date` is not later than the current time, the API returns **HTTP 400** with error code `rest_invalid_date`.

If any ID in `categories` does not exist, the API returns **HTTP 400** with error code `rest_invalid_term`.

## Responses

| Outcome | HTTP status | Error code or body |
|---|---:|---|
| Post created | 201 | The saved post |
| User role cannot create posts | 403 | `rest_cannot_create` |
| Author attempts to publish | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| Invalid date for a future post | 400 | `rest_invalid_date` |
| Unknown category ID | 400 | `rest_invalid_term` |

The response representation for the saved post is not specified here.

## QA checklist

- Verify that `editor` and `author` can create posts, and other roles receive `403 rest_cannot_create`.
- Verify that an author requesting `status: publish` receives `403 rest_cannot_publish`.
- Verify that an editor can request `status: publish`.
- Verify that omitting both `title` and `content` returns `400 rest_empty_post`.
- Verify that omitting `status` uses `draft`, and that the listed status values are accepted.
- Verify that a `future` post requires a `date` later than the current time; otherwise expect `400 rest_invalid_date`.
- Verify that a missing `slug` is built from `title`, and a duplicate slug receives a numeric suffix.
- Verify that unknown category IDs return `400 rest_invalid_term`.
- Verify that a successful request returns `201` and the saved post.

## Unspecified details

The maximum `title` length is **TBD**. The date format, the exact slug-generation and suffix rules, and the saved-post response representation are not specified.