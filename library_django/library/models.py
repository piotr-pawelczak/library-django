from django.db import models
from django.contrib.auth.models import User, timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=300, default='')
    year = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    time = models.IntegerField(default=14)
    is_available = models.BooleanField(default=True)
    edition = models.IntegerField(default=1)

    def __str__(self):
        return f'"{self.title}", {self.author}'


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=2000)
    image = models.ImageField(default='static/library/images/news.jpg', upload_to='static/library/images')

    def __str__(self):
        return self.title
