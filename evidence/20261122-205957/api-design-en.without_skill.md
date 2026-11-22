# Create a Post API

## Endpoint

`POST /wp/v2/posts`

Creates one post.

## Access

Only users with the `editor` or `author` role may create a post. Other roles receive **HTTP 403** with code `rest_cannot_create`.

Only an `editor` may create a post with `status: publish`. An `author` who requests that status receives **HTTP 403** with code `rest_cannot_publish`.

## Request fields

| Field | Description | Rules |
|---|---|---|
| `title` | Post title | Maximum length: **TBD**. |
| `content` | Post body | Either `title` or `content` must be present. |
| `status` | Publication state | Allowed values: `publish`, `future`, `draft`, `pending`, `private`. Defaults to `draft`. |
| `date` | Post date | When `status` is `future`, this must be later than the current time. |
| `slug` | Unique URL part of the post | If omitted, the system builds it from `title`. If it already exists, the system adds a numeric suffix. |
| `categories` | List of category IDs | Each ID must exist. |

## Validation and errors

| Condition | Response |
|---|---|
| Role is neither `editor` nor `author` | **HTTP 403**, `rest_cannot_create` |
| Both `title` and `content` are missing | **HTTP 400**, `rest_empty_post` |
| An `author` sets `status` to `publish` | **HTTP 403**, `rest_cannot_publish` |
| `status` is `future` and `date` is not later than the current time | **HTTP 400**, `rest_invalid_date` |
| A category ID does not exist | **HTTP 400**, `rest_invalid_term` |

## Success

On success, the API returns **HTTP 201** and the saved post.