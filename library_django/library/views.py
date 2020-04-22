from django.shortcuts import render
from .models import Article


def home(request):

    articles = []

    for article in Article.objects.all():
        content = article.content
        if len(content) > 500:
            content = article.content[0:500] + "..."
        articles.append((article, content))

    context = {'articles': articles}

    return render(request, 'library/home.html', context)


def books(request):
    return render(request, 'library/books.html')


def about(request):
    return render(request, 'library/about.html')


def login(request):
    return render(request, 'library/login.html')


def contact(request):
    return render(request, 'library/contact.html')


