from django.urls import path
from . import views

urlpatterns = [
    path('home', views.blog_home, name="BlogHome"),
    path('content/<int:article_id>', views.blog_content, name="BlogContent"),
]