from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.todo_homepage, name="TodoHome"),
    path('delete/<int:todo_id>', views.delete_task, name="TodoDelete"),
]