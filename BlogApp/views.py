from django.shortcuts import render, redirect
from .models import Article
from django.utils import timezone

# Create your views here.

# Usefull Funcs


def get_all_articles(request):
    context = dict()
    context['articles'] = Article.objects.all()
    return context


def get_article(request, article_id):
    context = dict()
    context['article'] = Article.objects.get(pk=article_id)
    return context

# Real requests handlers


def blog_home(request):
    if request.method == 'GET':
        context = get_all_articles(request)
        return render(request, "Blog/blogHome.html", context)


def blog_create(request):
    if request.method == 'GET':
        context = get_all_articles(request)
        return render(request, "Blog/blogCreate.html", context)

    elif request.method == 'POST':
        article_title = request.POST['title']
        article_text = request.POST['text']
        article_author = request.POST['author']
        article = Article.objects.create(title=article_title, text=article_text, author=article_author)
        article.save()
        return redirect("/blog/home")


def blog_content(request, article_id):
    if request.method == 'GET':
        context = get_article(request, article_id=article_id)
        return render(request, "Blog/blogContent.html", context)


def blog_delete(request, article_id):
    if request.method == 'GET':
        Article.objects.get(pk=article_id).delete()
        return redirect("BlogHome")

