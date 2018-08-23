from django.urls import path
from .views import todo, blog

urlpatterns = [
    path("todo/add/", todo.add_todo, name="addTodo"),
    path("todo/getAll/", todo.get_all, name="getAllTodos"),
    path("todo/delete/", todo.delete_todo, name="deleteTodo"),
    path("blog/getAll/", blog.get_all, name="getAllBlogs"),
    path("blog/get/", blog.get_article, name="getBlog"),
    path("blog/add/", blog.add_blog, name="addBlog"),
    path("blog/delete/", blog.delete_blog, name="deleteBlog"),
    path("blog/update/", blog.update_blog, name="updateBlog"),
]
