from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from TodoApp.models import TodoItem
from TodoApp.forms import TodoItemForm

import json

success_response = {"success": True}

@login_required
def get_all(request):
    if request.is_ajax():
        tasks = TodoItem.objects.all().reverse()
        data = serializers.serialize('json', tasks)
        return HttpResponse(data, content_type="application/json")
        
@login_required
def add_todo(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        form.save()
        return HttpResponse(json.dumps(success_response), content_type="application/json")

@login_required
def delete_todo(request):
    if request.method == "POST":
        task = get_object_or_404(TodoItem, pk=request.POST['id'])
        task.delete()
        return HttpResponse(json.dumps(success_response), content_type="application/json")

