from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="library-home"),
    path('books/', views.books, name="library-books"),
    path('about/', views.about, name="library-about"),
    path('contact/', views.contact, name="library-contact"),
]
