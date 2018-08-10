from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    published_date = models.DateTimeField('date_published', default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
