from django.urls import path, include
from . import views
from .views import ArticleDetailView

urlpatterns = [
    path('', views.home, name="library-home"),
    path('books/', views.books, name="library-books"),
    path('about/', views.about, name="library-about"),
    path('contact/', views.contact, name="library-contact"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail')
]
