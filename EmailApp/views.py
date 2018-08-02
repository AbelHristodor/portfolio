from django.shortcuts import render, redirect
from django.core.mail import send_mail


def contact_view(request):
    if request.method == "POST":
        emailfrom = request.POST['email']
        title = request.POST['title']
        message = request.POST['content']
        response = send_mail(
            subject=title,
            message=message,
            from_email=emailfrom,
            recipient_list=['lmaoayy059@gmail.com']
        )
        if response == 1:
            return render(request, "Portfolio/contact.html", {"msg": "Email successfully sent"})
        else:
            return render(request, "Portfolio/contact.html", {"msg": "An error has occurred. Try again later."})
    elif request.method == "GET":
        return render(request, "Portfolio/contact.html", {})