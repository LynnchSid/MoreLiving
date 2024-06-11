from rest_framework import serializers
from .models import Booking
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
         model = Booking
         fields = ['id', 'user', 'restaurant', 'table', 'bookingDate','bookingTime', 'number_of_adults','number_of_children','total_guests','payment_status', 'stripe_charge_id','created_at']
         read_only_fields = ['payment_status', 'stripe_charge_id']

    def get_total_guests(self, obj):
        return obj.number_of_adults+obj.number_of_children

    def validate_bookingDate(self, value):
        current_date = timezone.localdate()
        if value < current_date:
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return value
    def validate(self, data):
        table = data.get('table')
        number_of_adults = data.get('number_of_adults')
        number_of_children = data.get('number_of_children')
        total_guests = number_of_adults + number_of_children

        if total_guests > table.seats:
            raise serializers.ValidationError(f"Cannot book table {table.number} as it has only {table.seats} seats available.")

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)