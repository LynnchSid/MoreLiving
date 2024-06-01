from rest_framework import serializers
from .models import Booking
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
         model = Booking
         fields = ['id', 'user', 'restaurant', 'table', 'bookingDate','bookingTime', 'number_of_adults','number_of_children','total_guests','created_at']

    def get_total_guests(self, obj):
        return obj.number_of_adults+obj.number_of_children

    def validate_bookingDate(self, value):
        current_date = timezone.localdate()
        if value < current_date:
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return value