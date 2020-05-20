from django.shortcuts import render
from .models import Borrowing, Book
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class BorrowingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Borrowing
    fields = []
    template_name = 'borrowing/borrowing_form.html'
    success_message = "Book borrowed! You can now collect it in our library on Wall Street 14 between 8 a.m and 4 p.m."

    def form_valid(self, form):
        form.instance.user = self.request.user
        index = self.request.path.find('new/')
        cut_url = self.request.path[index+4:]
        id_end = cut_url.find('/')
        book_id = int(cut_url[0:id_end])
        form.instance.book = Book.objects.get(pk=book_id)
        form.instance.book.is_available = False
        form.instance.book.save()
        # why it does not save ??
        return super().form_valid(form)


class BorrowingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Borrowing
    template_name = 'borrowing/borrowing_detail.html'
    context_object_name = 'borrowing'

    def test_func(self):
        borrowing = self.get_object()
        return borrowing.user == self.request.user

