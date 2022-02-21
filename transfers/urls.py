from django.urls import path
from .views import (
    TransferListView,
    TransferUpdateView,
    TransferDeleteView,
    TransferDetailView,
    TransferCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', TransferUpdateView.as_view(), name='transfer_edit'),
    path('<int:pk>/', TransferDetailView.as_view(), name='transfer_detail'),
    path('<int:pk>/delete/', TransferDeleteView.as_view(), name='transfer_delete'),
    path('new/', TransferCreateView.as_view(), name='transfer_new'),
    path('', TransferListView.as_view(), name='transfer_list'),
]