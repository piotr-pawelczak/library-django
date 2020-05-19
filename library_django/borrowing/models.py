from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrowed = models.DateField(default=timezone.now)

    def __str__(self):
        return f'"{self.book.title}" borrowed by {self.user.username} on {self.date_borrowed}'

    def get_absolute_url(self):
        return reverse('library-books')
