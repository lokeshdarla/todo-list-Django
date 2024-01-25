# users/urls.py
from django.urls import path
from .views import UserListView, UserDetailView, get_tokens_for_user

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', get_tokens_for_user, name='token_obtain_pair')
]
