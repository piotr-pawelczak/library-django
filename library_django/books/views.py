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


class BookListView(ListView):
    template_name = 'books/book_search.html'
    context_object_name = 'books'
    model = Book
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("q")
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
                                                          Q(publisher__exact=book.publisher) & Q(edition__exact=book.edition))
                num_of_copies_available = 0
                for elem in same_books[counter]:
                    if elem.is_available:
                        num_of_copies_available += 1
                books.append((same_books[counter].first(), num_of_copies_available))

        return books

