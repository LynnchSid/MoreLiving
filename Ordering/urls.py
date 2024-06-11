from django.urls import path
from .views import  OrderListCreateView, OrderDetailView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order_list_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]