from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Task

class TaskApiTests(TestCase):
    # Set up a user, a task, and an API client with authentication
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(title='Test Task', description='Testing', due_date='2024-01-31', status='Pending', author=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    # Test the successful retrieval of the task list
    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test the successful retrieval of a task detail
    def test_task_detail(self):
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test the successful creation of a new task
    def test_task_create(self):
        url = reverse('task-create')
        data = {'title': 'New Task', 'description': 'Creating a new task', 'due_date': '2024-02-01', 'status': 'In Progress'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test the successful update of an existing task
    def test_task_update(self):
        url = reverse('task-update', kwargs={'pk': self.task.id})
        data = {'title': 'Updated Task', 'description': 'Updating the task', 'due_date': '2024-02-02', 'status': 'Completed'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test the successful deletion of an existing task
    def test_task_delete(self):
      initial_count = Task.objects.count()
      url = reverse('task-delete', kwargs={'pk': self.task.id})
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertEqual(Task.objects.count(), initial_count - 1)

    # Test unauthorized access to the task list endpoint
    def test_task_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test unauthorized access to a task detail endpoint
    def test_task_detail_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test the creation of a task with missing required fields
    def test_task_create_invalid_data(self):
        url = reverse('task-create')
        data = {'description': 'Creating a new task', 'due_date': '2024-02-01', 'status': 'In Progress'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test unauthorized update of an existing task
    def test_task_update_unauthorized(self):
        unauthorized_user = User.objects.create_user(username='unauthorized', password='testpassword')
        self.client.force_authenticate(user=unauthorized_user)
        
        url = reverse('task-update', kwargs={'pk': self.task.id})
        data = {'title': 'Updated Task', 'description': 'Updating the task', 'due_date': '2024-02-02', 'status': 'Completed'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test deletion of a non-existing task returns 404
    def test_task_delete_not_found(self):
        url = reverse('task-delete', kwargs={'pk': 9999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    # Test unauthorized access to the task creation endpoint
    def test_task_create_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('task-create')
        data = {'title': 'New Task', 'description': 'Creating a new task', 'due_date': '2024-02-01', 'status': 'In Progress'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test task creation with missing required fields
    def test_task_create_missing_required_fields(self):
        url = reverse('task-create')
        data = {'description': 'Creating a new task', 'due_date': '2024-02-01', 'status': 'In Progress'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test task creation with an invalid due_date format
    def test_task_create_invalid_due_date_format(self):
        url = reverse('task-create')
        data = {'title': 'New Task', 'description': 'Creating a new task', 'due_date': '2024/02/01', 'status': 'In Progress'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test task creation with an invalid status choice
    def test_task_create_invalid_status_choice(self):
        url = reverse('task-create')
        data = {'title': 'New Task', 'description': 'Creating a new task', 'due_date': '2024-02-01', 'status': 'InvalidStatus'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test task update with an invalid due_date format
    def test_task_update_invalid_due_date_format(self):
        url = reverse('task-update', kwargs={'pk': self.task.id})
        data = {'title': 'Updated Task', 'description': 'Updating the task', 'due_date': '2024/02/02', 'status': 'Completed'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test task update with an invalid status choice
    def test_task_update_invalid_status_choice(self):
        url = reverse('task-update', kwargs={'pk': self.task.id})
        data = {'title': 'Updated Task', 'description': 'Updating the task', 'due_date': '2024-02-02', 'status': 'InvalidStatus'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
