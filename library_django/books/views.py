from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'image', 'year', 'publisher', 'genre', 'time', 'edition']
    permission_required = 'user.is_staff'
    # permission_denied_message = 'Permission denied'
    template_name = 'books/book_form.html'


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'image', 'year', 'publisher', 'genre', 'time', 'edition']
    permission_required = 'user.is_staff'
    # permission_denied_message = 'Permission denied'
    template_name = 'books/book_form.html'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book-delete.html'
    permission_required = 'user.is_staff'
    # permission_denied_message = 'Permission denied'
    success_url = '/books/'


# list view ?
def books(request):
    # copies = Book.objects.filter(is_available=True).count()
    query = request.GET.get("q")
    found_books = []
    same_books = {}
    books = []

    if query:
        found_books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        for counter, book in enumerate(found_books):
            stop = False
            for key in same_books:
                if book in same_books[key]:
                    stop = True
                    break
            if stop:
                continue

            same_books[counter] = Book.objects.filter(Q(title__exact=book.title) & Q(author__exact=book.author) &
                                                      Q(publisher__exact=book.publisher))
            books.append((same_books[counter].first(), len(same_books[counter])))

    return render(request, 'books/book_search.html', {'books': books})
