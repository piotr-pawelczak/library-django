from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from users.models import Profile


# FIXME overriding home method with class ArticleListView may not be beneficial (consider it)
class ArticleListView(ListView):
    template_name = 'library/home.html'
    context_object_name = 'articles'
    # model = Article
    # ordering = ['-date_posted'] don't know why it doesn't work
    queryset = Article.objects.order_by('-date_posted')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        articles = []

        for article in Article.objects.all():
            content = article.content
            if len(content) > 500:
                content = article.content[0:500] + "..."
            articles.append((article, content))
            context = {'articles': articles}
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'library/article.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'image']
    permission_required = 'user.is_staff'
    # permission_denied_message = 'Permission denied'
    template_name = 'library/article_form.html'

    def form_valid(self, form):
        form.instance.author = Profile.objects.filter(user=self.request.user).first()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'image']
    permission_required = 'user.is_staff'
    # permission_denied_message = 'Permission denied'
    template_name = 'library/article_form.html'

    def form_valid(self, form):
        form.instance.author = Profile.objects.filter(user=self.request.user).first()
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'library/article-delete.html'
    permission_required = 'user.is_staff'
    # permission_denied_message = 'Permission denied'
    success_url = '/'


class AuthorDetailView(DetailView):
    template_name = 'library/author.html'
    context_object_name = 'author'
    model = Profile


def books(request):
    return render(request, 'library/books.html')


def about(request):
    return render(request, 'library/about.html')


def contact(request):
    return render(request, 'library/contact.html')


def terms_and_conditions(request):
    return render(request, 'library/terms_and_conditions.html')


def privacy_policy(request):
    return render(request, 'library/privacy_policy.html')