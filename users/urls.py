from django.urls import path
from .views import register
urlpatterns = [
    path('register/', view=register, name='user-register'),
]
