from django.shortcuts import render


def home_view(request):
    return render(request, "Portfolio/home_page.html", {})


def work_view(request):
    return render(request, "Portfolio/work.html", {})


def about_view(request):
    return render(request, "Portfolio/about.html", {})