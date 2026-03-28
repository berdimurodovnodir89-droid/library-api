# API Documentation

Base URL: `http://localhost:8000`

All request and response bodies use `application/json`.
All list endpoints support `skip` (default: `0`) and `limit` (default: `20`, max: `100`) query parameters for pagination.

---

## Table of Contents

- [Authors](#authors)
  - [List Authors](#get-authors)
  - [Create Author](#post-authors)
  - [Get Author](#get-authorsid)
  - [Update Author](#patch-authorsid)
  - [Delete Author](#delete-authorsid)
  - [Get Author's Books](#get-authorsidboks)
- [Genres](#genres)
  - [List Genres](#get-genres)
  - [Create Genre](#post-genres)
  - [Get Genre](#get-genresid)
  - [Update Genre](#patch-genresid)
  - [Delete Genre](#delete-genresid)
  - [Get Genre's Books](#get-genresidboks)
- [Books](#books)
  - [List Books](#get-books)
  - [Create Book](#post-books)
  - [Get Book](#get-booksid)
  - [Update Book](#patch-booksid)
  - [Delete Book](#delete-booksid)
- [Error Responses](#error-responses)

---

---

# Authors

---

## `GET /authors/`

Returns a paginated, searchable list of authors.

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `search` | string | No | Case-insensitive search on `first_name` or `last_name` |
| `skip` | integer | No | Number of records to skip (default: `0`) |
| `limit` | integer | No | Max records to return (default: `20`, max: `100`) |

### Example Request

```http
GET /authors/?search=tolkien&skip=0&limit=10
```

### Example Response `200 OK`

```json
[
  {
    "id": 1,
    "first_name": "J.R.R.",
    "last_name": "Tolkien",
    "bio": "English author and philologist, creator of Middle-earth.",
    "born_date": "1892-01-03"
  }
]
```

---

## `POST /authors/`

Creates a new author.

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `first_name` | string | ✅ | Author's first name |
| `last_name` | string | ✅ | Author's last name |
| `bio` | string | No | Short biography |
| `born_date` | string (ISO date) | No | Date of birth — format: `YYYY-MM-DD` |

### Example Request

```json
{
  "first_name": "J.R.R.",
  "last_name": "Tolkien",
  "bio": "English author and philologist, creator of Middle-earth.",
  "born_date": "1892-01-03"
}
```

### Example Response `201 Created`

```json
{
  "id": 1,
  "first_name": "J.R.R.",
  "last_name": "Tolkien",
  "bio": "English author and philologist, creator of Middle-earth.",
  "born_date": "1892-01-03"
}
```

---

## `GET /authors/{id}`

Returns a single author by ID.

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | Author ID |

### Example Request

```http
GET /authors/1
```

### Example Response `200 OK`

```json
{
  "id": 1,
  "first_name": "J.R.R.",
  "last_name": "Tolkien",
  "bio": "English author and philologist, creator of Middle-earth.",
  "born_date": "1892-01-03"
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Author with given ID does not exist |

---

## `PATCH /authors/{id}`

Partially updates an author. Only provided fields are changed.

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | Author ID |

### Request Body (all fields optional)

| Field | Type | Description |
|-------|------|-------------|
| `first_name` | string | New first name |
| `last_name` | string | New last name |
| `bio` | string | Updated biography |
| `born_date` | string (ISO date) | Updated birth date |

### Example Request

```json
{
  "bio": "Updated biography text."
}
```

### Example Response `200 OK`

```json
{
  "id": 1,
  "first_name": "J.R.R.",
  "last_name": "Tolkien",
  "bio": "Updated biography text.",
  "born_date": "1892-01-03"
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Author with given ID does not exist |

---

## `DELETE /authors/{id}`

Deletes an author and all their books (cascade).

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | Author ID |

### Example Request

```http
DELETE /authors/1
```

### Response `204 No Content`

No response body.

> ⚠️ **Warning:** Deleting an author permanently deletes all books associated with that author.

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Author with given ID does not exist |

---

## `GET /authors/{id}/books`

Returns all books written by a specific author.

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | Author ID |

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `skip` | integer | Pagination offset (default: `0`) |
| `limit` | integer | Max records (default: `20`, max: `100`) |

### Example Request

```http
GET /authors/1/books
```

### Example Response `200 OK`

```json
[
  {
    "id": 10,
    "title": "The Lord of the Rings",
    "published_year": 1954,
    "author": {
      "id": 1,
      "first_name": "J.R.R.",
      "last_name": "Tolkien"
    },
    "genres": [
      { "id": 2, "name": "Fantasy", "description": null }
    ]
  }
]
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Author with given ID does not exist |

---

---

# Genres

---

## `GET /genres/`

Returns a paginated, searchable list of genres.

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `search` | string | No | Case-insensitive search on `name` |
| `skip` | integer | No | Pagination offset (default: `0`) |
| `limit` | integer | No | Max records (default: `20`, max: `100`) |

### Example Request

```http
GET /genres/?search=sci
```

### Example Response `200 OK`

```json
[
  {
    "id": 3,
    "name": "Science Fiction",
    "description": "Stories based on futuristic science and technology."
  }
]
```

---

## `POST /genres/`

Creates a new genre. Genre names are unique (case-insensitive).

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Genre name (must be unique) |
| `description` | string | No | Short description of the genre |

### Example Request

```json
{
  "name": "Science Fiction",
  "description": "Stories based on futuristic science and technology."
}
```

### Example Response `201 Created`

```json
{
  "id": 3,
  "name": "Science Fiction",
  "description": "Stories based on futuristic science and technology."
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `400 Bad Request` | A genre with this name already exists |

---

## `GET /genres/{id}`

Returns a single genre by ID.

### Example Response `200 OK`

```json
{
  "id": 3,
  "name": "Science Fiction",
  "description": "Stories based on futuristic science and technology."
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Genre with given ID does not exist |

---

## `PATCH /genres/{id}`

Partially updates a genre. Only provided fields are changed.

### Request Body (all fields optional)

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | New name (must be unique) |
| `description` | string | Updated description |

### Example Request

```json
{
  "description": "Updated genre description."
}
```

### Example Response `200 OK`

```json
{
  "id": 3,
  "name": "Science Fiction",
  "description": "Updated genre description."
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Genre with given ID does not exist |
| `400 Bad Request` | New name already used by another genre |

---

## `DELETE /genres/{id}`

Deletes a genre. Books that had this genre will simply lose the genre association.

### Response `204 No Content`

No response body.

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Genre with given ID does not exist |

---

## `GET /genres/{id}/books`

Returns all books that belong to a specific genre.

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `skip` | integer | Pagination offset (default: `0`) |
| `limit` | integer | Max records (default: `20`, max: `100`) |

### Example Response `200 OK`

```json
[
  {
    "id": 10,
    "title": "The Lord of the Rings",
    "published_year": 1954,
    "author": {
      "id": 1,
      "first_name": "J.R.R.",
      "last_name": "Tolkien"
    },
    "genres": [
      { "id": 2, "name": "Fantasy", "description": null }
    ]
  }
]
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Genre with given ID does not exist |

---

---

# Books

---

## `GET /books/`

Returns a filtered, searchable, paginated list of books.

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `search` | string | No | Case-insensitive search on `title` |
| `author_id` | integer | No | Filter by author ID |
| `genre_id` | integer | No | Filter by genre ID |
| `year_from` | integer | No | Filter books published from this year (inclusive) |
| `year_to` | integer | No | Filter books published up to this year (inclusive) |
| `skip` | integer | No | Pagination offset (default: `0`) |
| `limit` | integer | No | Max records (default: `20`, max: `100`) |

### Example Requests

```http
# Search by title
GET /books/?search=ring

# Filter by author and genre
GET /books/?author_id=1&genre_id=2

# Filter by year range
GET /books/?year_from=1950&year_to=1960

# Combined filters
GET /books/?search=lord&author_id=1&genre_id=2&year_from=1950&limit=5
```

### Example Response `200 OK`

```json
[
  {
    "id": 10,
    "title": "The Lord of the Rings",
    "published_year": 1954,
    "author": {
      "id": 1,
      "first_name": "J.R.R.",
      "last_name": "Tolkien"
    },
    "genres": [
      { "id": 2, "name": "Fantasy", "description": null }
    ]
  }
]
```

---

## `POST /books/`

Creates a new book. `author_id` must reference an existing author. All IDs in `genre_ids` must reference existing genres.

### Request Body

| Field | Type | Required | Validation | Description |
|-------|------|----------|------------|-------------|
| `title` | string | ✅ | — | Book title |
| `author_id` | integer | ✅ | Must exist in DB | ID of the author |
| `genre_ids` | integer[] | No | Each ID must exist | List of genre IDs |
| `description` | string | No | — | Book description |
| `isbn` | string | No | Must be unique | ISBN number |
| `published_year` | integer | No | 1000–2100 | Year of publication |
| `pages` | integer | No | > 0 | Number of pages |

### Example Request

```json
{
  "title": "The Lord of the Rings",
  "author_id": 1,
  "genre_ids": [2, 5],
  "description": "An epic high-fantasy novel.",
  "isbn": "978-0618640157",
  "published_year": 1954,
  "pages": 1178
}
```

### Example Response `201 Created`

```json
{
  "id": 10,
  "title": "The Lord of the Rings",
  "description": "An epic high-fantasy novel.",
  "isbn": "978-0618640157",
  "published_year": 1954,
  "pages": 1178,
  "author_id": 1,
  "author": {
    "id": 1,
    "first_name": "J.R.R.",
    "last_name": "Tolkien"
  },
  "genres": [
    { "id": 2, "name": "Fantasy", "description": null },
    { "id": 5, "name": "Adventure", "description": null }
  ]
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | `author_id` does not exist |
| `404 Not Found` | One or more `genre_ids` do not exist |
| `400 Bad Request` | `isbn` already exists |
| `422 Unprocessable Entity` | `published_year` out of range or `pages` < 1 |

---

## `GET /books/{id}`

Returns a single book with full details including author and genres.

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | Book ID |

### Example Response `200 OK`

```json
{
  "id": 10,
  "title": "The Lord of the Rings",
  "description": "An epic high-fantasy novel.",
  "isbn": "978-0618640157",
  "published_year": 1954,
  "pages": 1178,
  "author_id": 1,
  "author": {
    "id": 1,
    "first_name": "J.R.R.",
    "last_name": "Tolkien"
  },
  "genres": [
    { "id": 2, "name": "Fantasy", "description": null }
  ]
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Book with given ID does not exist |

---

## `PATCH /books/{id}`

Partially updates a book. Only provided fields are changed.

To replace genres entirely, provide a new `genre_ids` list. To remove all genres, pass an empty list `[]`.

### Request Body (all fields optional)

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | New title |
| `description` | string | Updated description |
| `isbn` | string | New ISBN (must be unique) |
| `published_year` | integer | Updated year (1000–2100) |
| `pages` | integer | Updated page count (> 0) |
| `author_id` | integer | Reassign to another author |
| `genre_ids` | integer[] | Replace genre list entirely |

### Example Request — update title only

```json
{
  "title": "The Lord of the Rings: Special Edition"
}
```

### Example Request — reassign genres

```json
{
  "genre_ids": [2, 7]
}
```

### Example Request — remove all genres

```json
{
  "genre_ids": []
}
```

### Example Response `200 OK`

```json
{
  "id": 10,
  "title": "The Lord of the Rings: Special Edition",
  "description": "An epic high-fantasy novel.",
  "isbn": "978-0618640157",
  "published_year": 1954,
  "pages": 1178,
  "author_id": 1,
  "author": {
    "id": 1,
    "first_name": "J.R.R.",
    "last_name": "Tolkien"
  },
  "genres": [
    { "id": 2, "name": "Fantasy", "description": null },
    { "id": 7, "name": "Classic", "description": null }
  ]
}
```

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Book with given ID does not exist |
| `404 Not Found` | New `author_id` does not exist |
| `404 Not Found` | One or more `genre_ids` do not exist |
| `400 Bad Request` | New `isbn` already used by another book |

---

## `DELETE /books/{id}`

Permanently deletes a book.

### Response `204 No Content`

No response body.

### Error Cases

| Status | Reason |
|--------|--------|
| `404 Not Found` | Book with given ID does not exist |

---

---

# Error Responses

All errors follow a consistent structure:

```json
{
  "detail": "Human-readable error message"
}
```

### Standard HTTP Status Codes

| Code | Meaning |
|------|---------|
| `200 OK` | Successful GET or PATCH |
| `201 Created` | Successful POST |
| `204 No Content` | Successful DELETE |
| `400 Bad Request` | Business logic violation (duplicate name, ISBN conflict, etc.) |
| `404 Not Found` | Requested resource does not exist |
| `422 Unprocessable Entity` | Request body failed schema validation (wrong types, out-of-range values) |

### Example `404` Response

```json
{
  "detail": "Book not found"
}
```

### Example `400` Response

```json
{
  "detail": "ISBN already exists"
}
```

### Example `422` Response

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "published_year"],
      "msg": "Value error, published_year must be between 1000 and 2100",
      "input": 999
    }
  ]
}
```
