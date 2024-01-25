from django.urls import path
from .views import TaskListView, TaskDetailView, create_task, update_task, delete_task

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', create_task, name='create-task'),
    path('tasks/update/<int:pk>/', update_task, name='update-task'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete-task'),
]
