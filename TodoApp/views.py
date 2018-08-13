from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def todo_homepage(request):
    tasks = TodoItem.objects.all()
    context = {'tasks': tasks}
    if request.method == "POST":
        task = TodoItem(text=request.POST['task'])
        task.save()
        tasks = TodoItem.objects.all()
        context['tasks'] = tasks
        return redirect("TodoHome")

    elif request.method == 'GET':
        return render(request, "Todo/todo.html", context)

@login_required
def delete_task(request, todo_id):
    if request.method == 'GET':
        TodoItem.objects.get(pk=todo_id).delete()
        return redirect("TodoHome")


