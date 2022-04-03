from django.urls import path
from .views import (
    TransferListView,
    TransferUpdateView,
    TransferDeleteView,
    TransferDetailView,
    TransferCreateView,
    transfer_detail_comment,
    ReputationView,
    TransferViewView,
    like,
    status_change
)

urlpatterns = [
    path('<int:pk>/edit/', TransferUpdateView.as_view(), name='transfer_edit'),
    path('<int:pk>/', TransferDetailView.as_view(), name='transfer_detail'),
    path('<int:pk>/delete/', TransferDeleteView.as_view(), name='transfer_delete'),
    path('new/', TransferCreateView.as_view(), name='transfer_new'),
    path('', TransferListView.as_view(), name='transfer_list'),
    path('like/<int:pk>', like, name='like_transfer'),
    path('reputation/<int:pk>', ReputationView, name='reputation_transfer'),
    path('status/<int:pk>', status_change, name='status_change'),
    path('view/<int:pk>', TransferViewView, name='view_transfer'),
    path('comment/<int:pk>', transfer_detail_comment, name='transfer_detail_comment'),
]