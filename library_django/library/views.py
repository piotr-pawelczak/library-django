from django.shortcuts import render
from .models import Article


def home(request):
    context = {'articles': []}
    for article in Article.objects.all():
        content = article.content
        if len(content) > 500:
            content = article.content[0:500] + "..."
        context['articles'].append((article, content))
    return render(request, 'library/home.html', context)


def books(request):
    return render(request, 'library/books.html')


def about(request):
    return render(request, 'library/about.html')


def login(request):
    return render(request, 'library/login.html')


def register(request):
    return render(request, 'library/register.html')


def contact(request):
    return render(request, 'library/contact.html')


