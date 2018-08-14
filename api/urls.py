from django.urls import path
from .views import todo

urlpatterns = [
    path("todo/add/", todo.add_todo, name="addTodo"),
    path("todo/getAll/", todo.get_all, name="getAllTodos"),
    path("todo/delete/", todo.delete_todo, name="deleteTodo")
]
