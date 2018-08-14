from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def todo_homepage(request):
    if request.method == 'GET':
        return render(request, "Todo/todo.html")

