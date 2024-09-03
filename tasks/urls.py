# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('file/', views.file_view, name='file_view'),
]
