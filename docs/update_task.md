## Update Task

Updates an existing task in the task management API.

### Endpoint

`PUT /tasks/{task_id}/`

### Authentication

This endpoint requires authentication. Include a valid token in the `Authorization` header with the format `Bearer <token>`.

### Request

```json
{
  "title": "Updated Task",
  "description": "Updated description of the task.",
  "due_date": "2024-02-20",
  "status": "In Progress"
}
```

- **title** (str): The updated title of the task.
- **description** (str, optional): The updated description of the task.
- **due_date** (str, optional): The updated due date of the task in the format YYYY-MM-DD.
- **status** (str): The updated status of the task (e.g., "In Progress").

### Response

```json
Success (HTTP 200 OK)
```
```json
{
  "id": 5,
  "title": "Updated Task",
  "description": "Updated description of the task.",
  "due_date": "2024-02-20",
  "status": "In Progress",
  "author": 3
}
```

- **id** (int): The unique identifier for the updated task.
- **title** (str): The updated title of the task.
- **description** (str, optional): The updated description of the task.
- **due_date** (str, optional): The updated due date of the task in the format YYYY-MM-DD.
- **status** (str): The updated status of the task (e.g., "In Progress").
- **author** (int): The user ID of the author who updated the task.

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

### HTTP 500 Internal Server Error

Returned when:

- An unexpected server error occurs.

```json
{
    "error": "An unexpected error occurred. Please try again later."
}

```
