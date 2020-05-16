from django.urls import path, include
from . import views
from .views import BookCreateView, BookDeleteView, BookDetailView, BookUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.books, name="library-books"),
    path('new/', BookCreateView.as_view(), name='new-book'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
