from django.urls import path
from . import views

urlpatterns = [
    path('home', views.contact_view, name="contact-view")
]