## Create Task

Creates a new task in the task management API.

### Endpoint

`POST /tasks/`

### Authentication

This endpoint requires authentication. Include a valid token in the `Authorization` header with the format `Bearer <token>`.

### Request

```json
{
  "title": "New Task",
  "description": "Description of the new task.",
  "due_date": "2024-02-15",
  "status": "Pending"
}
```

- **title** (str): The title of the new task.
- **description** (str, optional): A description of the new task.
- **due_date** (str, optional): The due date of the new task in the format YYYY-MM-DD.
- **status** (str): The status of the new task (e.g., "Pending").

### Response

```json
Success (HTTP 201 Created)
```
```json
{
  "id": 5,
  "title": "New Task",
  "description": "Description of the new task.",
  "due_date": "2024-02-15",
  "status": "Pending",
  "author": 3
}
```

- **id** (int): The unique identifier for the newly created task.
- **title** (str): The title of the new task.
- **description** (str, optional): A description of the new task.
- **due_date** (str, optional): The due date of the new task in the format YYYY-MM-DD.
- **status** (str): The status of the new task (e.g., "Pending").
- **author** (int): The user ID of the author who created the new task.

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
