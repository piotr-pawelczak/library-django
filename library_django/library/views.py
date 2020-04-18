from django.shortcuts import render


def home(request):
    return render(request, 'library/home.html')


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


