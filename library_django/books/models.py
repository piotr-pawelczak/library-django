from django.db import models
from django.urls import reverse
from datetime import datetime


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=300)
    year = models.IntegerField(default=datetime.now().year)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='')
    image = models.ImageField(default='books/default_book_img.png', upload_to='books')
    time = models.IntegerField(default=30)
    is_available = models.BooleanField(default=True)
    edition = models.IntegerField(default=1)

    def __str__(self):
        return f'"{self.title}", {self.author}'

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
