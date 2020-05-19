from django.shortcuts import render
from .models import Borrowing, Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BorrowingCreateView(LoginRequiredMixin, CreateView):
    model = Borrowing
    fields = []
    template_name = 'borrowing/borrowing_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        index = self.request.path.find('new/')
        cut_url = self.request.path[index+4:]
        id_end = cut_url.find('/')
        book_id = int(cut_url[0:id_end])
        form.instance.book = Book.objects.get(pk=book_id)
        return super().form_valid(form)
