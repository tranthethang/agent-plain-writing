# Create a Post

Creates one post.

## Endpoint

`POST /wp/v2/posts`

## Authorization

Only users with the `editor` or `author` role may create a post. Other roles receive **HTTP 403** with code `rest_cannot_create`.

Only an `editor` may create a post with `status: "publish"`. An `author` who requests that status receives **HTTP 403** with code `rest_cannot_publish`.

## Request fields

| Field | Description | Rules |
|---|---|---|
| `title` | Title of the post. | Must be present, or `content` must be present. Maximum length: **TBD**. |
| `content` | Body of the post. | Must be present, or `title` must be present. |
| `status` | Publication state of the post. | Allowed values: `publish`, `future`, `draft`, `pending`, `private`. Defaults to `draft`. Only an `editor` may use `publish`. |
| `date` | Date for the post. | When `status` is `future`, the date must be later than the current time. |
| `slug` | Unique URL part of the post. | If omitted, the system builds it from `title`. If the slug already exists, the system adds a numeric suffix. |
| `categories` | List of category IDs (integers). | Each ID must exist. |

## Validation and errors

| Condition | HTTP status | Error code |
|---|---:|---|
| User role is neither `editor` nor `author` | 403 | `rest_cannot_create` |
| An `author` requests `status: "publish"` | 403 | `rest_cannot_publish` |
| Both `title` and `content` are missing | 400 | `rest_empty_post` |
| `status` is `future` and `date` is not later than the current time | 400 | `rest_invalid_date` |
| A category ID does not exist | 400 | `rest_invalid_term` |

## Success response

On success, the API returns **HTTP 201** and the saved post. The response fields are not specified here.