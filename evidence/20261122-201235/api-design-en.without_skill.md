# Create a Post API

## Endpoint

`POST /wp/v2/posts`

Creates one post.

## Authorization

| Caller role | Result |
|---|---|
| `editor` | May create a post |
| `author` | May create a post |
| Any other role | HTTP `403`, code `rest_cannot_create` |

Only an `editor` may create a post with `status: publish`. An `author` who requests that status receives HTTP `403`, code `rest_cannot_publish`.

## Request fields

| Field | Description | Rules |
|---|---|---|
| `title` | Post title | Must be present if `content` is absent. Maximum length: **TBD**. |
| `content` | Post body | Must be present if `title` is absent. |
| `status` | Publication state | Allowed values: `publish`, `future`, `draft`, `pending`, `private`. Defaults to `draft`. Only an `editor` may use `publish`. |
| `date` | Post date | Required when `status` is `future`; must be later than the current time. |
| `slug` | Unique URL part of the post | If omitted, the system builds it from `title`. If the slug already exists, the system adds a numeric suffix. |
| `categories` | List of category IDs | Each ID must exist. IDs are integers. |

At least one of `title` or `content` must be present. If both are missing, the API returns HTTP `400`, code `rest_empty_post`.

## Responses

### Success

Returns HTTP `201` and the saved post. The response schema is not specified here.

### Errors

| Condition | HTTP status | Error code |
|---|---:|---|
| Caller role is not `editor` or `author` | `403` | `rest_cannot_create` |
| An `author` requests `status: publish` | `403` | `rest_cannot_publish` |
| Both `title` and `content` are missing | `400` | `rest_empty_post` |
| `status` is `future` and `date` is not later than the current time | `400` | `rest_invalid_date` |
| A category ID does not exist | `400` | `rest_invalid_term` |

## Items not specified

- Maximum `title` length is **TBD**.
- The date format is not specified.
- Behavior when `title` is absent but `slug` is also omitted is not specified.
- The numeric suffix format and selection rules for an existing slug are not specified.
- Error precedence when multiple request rules fail is not specified.