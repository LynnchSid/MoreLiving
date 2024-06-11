from django.urls import path
from .views import CreatePaymentIntentView, ConfirmPaymentForBookingView, ConfirmPaymentForOrderView

urlpatterns = [
    path('create-payment-intent/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
    path('confirm-payment-booking/', ConfirmPaymentForBookingView.as_view(), name='confirm-payment-booking'),
    path('confirm-payment-order/', ConfirmPaymentForOrderView.as_view(), name='confirm-payment-order'),
]