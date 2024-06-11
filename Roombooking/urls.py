from django.urls import path
from .views import RoomBookingListCreate

urlpatterns = [
   
    path('roombookings/',RoomBookingListCreate.as_view(),name='roombooking-list-create'),
    path('roombooking/<pk>/', RoomBookingListCreate.as_view(), name='roombooking-details'),
  
]