from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required


@login_required
def blog_home(request):
    if request.method == 'GET':
        return render(request, "Blog/blogHome.html")


@login_required
def blog_content(request, article_id):
    if request.method == 'GET':
        article = Article.objects.get(pk=article_id)
        return render(request, "Blog/blogContent.html", {"article": article})
