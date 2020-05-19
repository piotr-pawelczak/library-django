from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BorrowingCreateView

urlpatterns = [
    # path('', BorrowingListView.as_view(), name="library-books"),
    path('new/<int:pk>/', BorrowingCreateView.as_view(), name='book-borrow'),
    # path('<int:pk>/', BorrowingDetailView.as_view(), name='borrowing-detail'),
    # path('<int:pk>/delete/', BorrowingDeleteView.as_view(), name='book-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)