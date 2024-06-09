from django.urls import path
from .views import CartView, AddToCartView, PlaceOrderFromCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart_view'),
    path('add/', AddToCartView.as_view(), name='add_to_cart'),
    path('order/', PlaceOrderFromCartView.as_view(), name='place_order_from_cart'),
]