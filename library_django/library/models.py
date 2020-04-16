from django.db import models


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

