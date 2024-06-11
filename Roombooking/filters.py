# filters.py
import django_filters
from .models import RoomBooking

class RoomBookingFilter(django_filters.FilterSet):
    class Meta:
        model = RoomBooking
        fields = ['user', 'hotel', 'room', 'checkinDate', 'checkoutDate', 'createdAt'] 
                  # Add fields you want to filter on