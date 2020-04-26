from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


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


def books(request):
    return render(request, 'library/books.html')


def about(request):
    return render(request, 'library/about.html')


def contact(request):
    return render(request, 'library/contact.html')


