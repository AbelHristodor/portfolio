from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.todo_homepage, name="TodoHome")
]