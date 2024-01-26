## Delete Task

Deletes an existing task from the task management API.

### Endpoint

`DELETE /tasks/{task_id}/`

### Authentication

This endpoint requires authentication. Include a valid token in the `Authorization` header with the format `Bearer <token>`.

### Request

No request parameters are required for this endpoint.

### Response

```json
Success (HTTP 204 No Content)
```

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

- The requested resource (e.g., task or endpoint) is not found.

```json
{
    "detail": "Not found."
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
