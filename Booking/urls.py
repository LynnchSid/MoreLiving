from django.urls import path
from .views import BookingListCreate, BookingDetail

urlpatterns = [
    path('bookings/',BookingListCreate.as_view(),name='booking-list-create'),
    path('booking/<int:pk>/',BookingDetail.as_view(),name='booking-detail'),
]