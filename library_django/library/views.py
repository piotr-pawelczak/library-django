from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    articles = []
    article_form = ArticleForm()

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('../')

    for article in Article.objects.all():
        content = article.content
        if len(content) > 500:
            content = article.content[0:500] + "..."
        articles.append((article, content))

    context = {'articles': articles,
               'article_form': article_form}

    return render(request, 'library/home.html', context)

# FIXME overriding home with class may not be beneficial (consider it)
# class ArticleListView(ListView):
#     model = Article
#     template_name = 'library/home.html'
#     context_object_name = 'articles'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ArticleListView, self).get_context_data(**kwargs)
#         context['article_form'] = article_form
#         return context


# to redirect to user articles after clicking on username on home page
class UserArticleListView(ListView):
    pass


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'library/article.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    pass


class ArticleUpdateView(UpdateView):
    pass


class ArticleDeleteView(DeleteView):
    pass


def books(request):
    return render(request, 'library/books.html')


def about(request):
    return render(request, 'library/about.html')


def contact(request):
    return render(request, 'library/contact.html')


