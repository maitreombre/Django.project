from django.urls import path
from .views import create_task, profile

urlpatterns = [
    path('create/', create_task, name='create_task'),
]
