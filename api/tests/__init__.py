from TodoApp.models import TodoItem
from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = factory.Faker('name')

    class Meta:
        model = User


class TodoItemFactory(DjangoModelFactory):
    text = factory.Faker('text')

    class Meta:
        model = TodoItem
