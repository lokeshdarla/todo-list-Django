## Get Task by ID

Retrieves a specific task from the task management API based on its unique identifier.

### Endpoint

`GET /tasks/{id}/`

### Authentication

This endpoint requires authentication. Include a valid token in the `Authorization` header with the format `Bearer <token>`.

### Request

No request parameters are required for this endpoint.

### Response

```json
Success (HTTP 200 OK)
```
```json
{
  "id": 1,
  "title": "Exploring the Wonders of Machine Learning",
  "description": "Discover the fascinating world of machine learning and its applications.",
  "due_date": "2024-02-10",
  "status": "In Progress",
  "author": 7
}
```

- **id** (int): The unique identifier for the task.
- **title** (str): The title of the task.
- **description** (str): A description of the task.
- **due_date** (str): The due date of the task in the format YYYY-MM-DD.
- **status** (str): The status of the task (e.g., "In Progress").
- **author** (int): The user ID of the author who created the task.

### Error Responses

#### HTTP 401 Unauthorized

Returned when:

- The request lacks valid authentication credentials.
- An invalid token is provided in the `Authorization` header.

```json
{
    "detail": "Authentication credentials were not provided or are invalid."
}
```

### HTTP 403 Forbidden

Returned when:

- The provided token does not have the necessary permissions.

```json
{
    "detail": "You do not have permission to perform this action."
}
```

### HTTP 404 Not Found

Returned when:

- The requested task with the specified ID is not found.

```json
{
    "detail": "Task not found."
}

```
### HTTP 500 Internal Server Error

Returned when:

- An unexpected server error occurs.

```json
{
    "error": "An unexpected error occurred. Please try again later."
}

```
