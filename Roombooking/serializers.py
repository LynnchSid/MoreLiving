from rest_framework import serializers
from .models import RoomBooking
from datetime import date
from django.db.models import Q

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = ['hotel', 'room', 'bookingPrice', 'bookingId', 'user', 'checkinDate', 'checkoutDate', 'createdAt']
        
    def validate(self, data):
        if data['checkoutDate'] < data['checkinDate']:
            raise serializers.ValidationError({"error": "Checkout date must be greater than check-in date"})
        created_at = self.instance.createdAt if self.instance else date.today()
        
        if data['checkinDate'] < created_at:
            raise serializers.ValidationError({"error": "Check-in date must be later than the creation date"})
        # Checking  for overlapping bookings eutai room ko lagi eutai time period ma
        overlapping_bookings = RoomBooking.objects.filter(
            room=data['room'],
            hotel=data['hotel'],
            status__in=['PENDING', 'ACCEPTED','accepted','pending']
        ).exclude(
            Q(checkoutDate__lte=data['checkinDate']) | Q(checkinDate__gte=data['checkoutDate'])
        )
        if overlapping_bookings.exists():
            raise serializers.ValidationError({"error": "This room is already booked for the given dates"})
        return data
    
    def calculate_booking_price(self, room, checkin_date, checkout_date):
        nights = (checkout_date - checkin_date).days
        return room.price * nights

    def create(self, validated_data):
        room = validated_data['room']
        checkin_date = validated_data['checkinDate']
        checkout_date = validated_data['checkoutDate']
        validated_data['bookingPrice'] = self.calculate_booking_price(room, checkin_date, checkout_date)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        room = validated_data.get('room', instance.room)
        checkin_date = validated_data.get('checkinDate', instance.checkinDate)
        checkout_date = validated_data.get('checkoutDate', instance.checkoutDate)
        validated_data['bookingPrice'] = self.calculate_booking_price(room, checkin_date, checkout_date)
        return super().update(instance, validated_data)
