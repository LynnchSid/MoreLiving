from django.urls import path 
from  .views import PaymentListCreate, PaymentDetail

urlpatterns = [
    path('payments/',PaymentListCreate.as_view(),name='payment-list-create'),
    path('payments/<int:pk>/',PaymentDetail.as_view(),name='payment-detail'),
]