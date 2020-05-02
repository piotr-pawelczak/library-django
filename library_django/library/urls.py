from django.urls import path, include
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, AuthorDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ArticleListView.as_view(), name="library-home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='new-article'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('books/', views.books, name="library-books"),
    path('about/', views.about, name="library-about"),
    path('contact/', views.contact, name="library-contact"),
    path('agreement/', views.terms_and_conditions, name='terms-and-conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
