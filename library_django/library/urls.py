from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="library-home"),
    path('books/', views.books, name="library-books"),
    path('about/', views.about, name="library-about"),
    path('login/', views.login, name="library-login"),
    path('register/', views.register, name="library-register"),
    path('contact/', views.contact, name="library-contact"),
]
