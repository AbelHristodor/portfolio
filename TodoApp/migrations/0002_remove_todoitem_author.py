# Generated by Django 2.0.7 on 2018-08-10 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='author',
        ),
    ]