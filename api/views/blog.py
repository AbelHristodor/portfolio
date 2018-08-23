from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from BlogApp.models import Article
from BlogApp.forms import ArticleForm

import json

success_response = {"success": True}


@login_required
def get_all(request):
    if request.is_ajax():
        articles = Article.objects.all().order_by('published_date').reverse()
        data = serializers.serialize("json", articles)
        return HttpResponse(data, content_type="application/json")


@login_required
def get_article(request):
    if request.is_ajax():
        article = Article.objects.filter(pk=request.GET['id'])
        data = serializers.serialize("json", article)
        return HttpResponse(data, content_type="application/json")


@login_required
def add_blog(request):
    if request.method == "POST":
        article = ArticleForm(request.POST)
        article.save()
        return HttpResponse(json.dumps(success_response), content_type="application/json")


@login_required
def delete_blog(request):
    if request.method == "POST":
        article = Article.objects.filter(pk=request.POST['id'])
        article.delete()
        return HttpResponse(json.dumps(success_response), content_type="application/json")


@login_required
def update_blog(request):
    if request.method == "POST":
        article = get_object_or_404(Article, id=request.POST['id'])
        form = ArticleForm(request.POST or None, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(success_response), content_type="application/json")
