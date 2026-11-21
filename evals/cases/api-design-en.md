---
lang: en
type: api-design
non_tech: false
---

# SIMULATED DATA

The endpoint and the field names come from the public WordPress REST API reference for posts ("Create a Post"). The business rules and error codes are invented for this eval.

## Audience

Backend developers and QA engineers who implement and test a blog API.

## Brief

### Idea
Design `POST /wp/v2/posts` to create one post. Source: the WordPress REST API reference for posts, endpoint "Create a Post". The rules below are simulated, apart from the field names and allowed values.

### Business rules
- Only the roles `editor` and `author` may create a post. Other roles receive HTTP 403 (`rest_cannot_create`).
- `title` or `content` must be present. If both are missing, the API returns HTTP 400 (`rest_empty_post`).
- `status` is one of `publish`, `future`, `draft`, `pending`, `private`. The default is `draft`.
- Only an `editor` may set `status` to `publish`. An `author` who sends `publish` receives HTTP 403 (`rest_cannot_publish`).
- When `status` is `future`, `date` must be later than the current time. Otherwise the API returns HTTP 400 (`rest_invalid_date`).
- When `slug` is missing, the system builds it from `title`. When the slug already exists, the system adds a numeric suffix.
- Each id in `categories` must exist. An unknown id returns HTTP 400 (`rest_invalid_term`).
- On success, the API returns HTTP 201 and the saved post.
- The maximum length of `title` is not given by the source. Mark it `TBD`.

### Glossary
- `title`: the title of the post.
- `content`: the body of the post.
- `status`: the publication state of the post.
- `slug`: the unique URL part of the post.
- `categories`: list of category ids (integers).

## Facts
- Endpoint: `POST /wp/v2/posts`
- Allowed roles: `editor`, `author` (others get HTTP 403 `rest_cannot_create`)
- Status values: `publish`, `future`, `draft`, `pending`, `private`; default `draft`
- Only `editor` may publish (otherwise HTTP 403 `rest_cannot_publish`)
- Missing `title` and `content`: HTTP 400 `rest_empty_post`
- `future` needs a later `date` (otherwise HTTP 400 `rest_invalid_date`)
- Unknown category id: HTTP 400 `rest_invalid_term`
- Success status: HTTP 201
