from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register_page(request):
    if request.method == "GET":
        return render(request, "authentication/register.html")
    elif request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        auth_user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, auth_user)
        else:
            redirect("register-page")
        return redirect("home-view")

def login_page(request):
    if request.method == "GET":
        return render(request, "authentication/login.html")
    elif request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('home-view')
        else: 
            return redirect('register-page')
    
@login_required
def logout_page(request):
    logout(request)
    return redirect("home-view")
