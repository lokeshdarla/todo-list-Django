# users/urls.py
from django.urls import path
from .views import create_user, retrieve_user, update_user, delete_user, list_users

urlpatterns = [
   path('users/', list_users, name='task-list'),
    path('users/create/', create_user, name='create-user'),
    path('users/<int:pk>/', retrieve_user, name='retrieve-user'),
    path('users/<int:pk>/update/', update_user, name='update-user'),
    path('users/<int:pk>/delete/', delete_user, name='delete-user')
]
