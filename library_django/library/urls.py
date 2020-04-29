from django.urls import path, include
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name="library-home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='new-article'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),
    path('books/', views.books, name="library-books"),
    path('about/', views.about, name="library-about"),
    path('contact/', views.contact, name="library-contact"),
]
