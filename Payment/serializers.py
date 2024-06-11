from rest_framework import serializers
from Booking.models import Booking
from Ordering.models import Order

class CreatePaymentIntentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class ConfirmPaymentSerializer(serializers.Serializer):
    payment_intent_id = serializers.CharField(max_length=255)
    booking_id = serializers.IntegerField(required=False)
    order_id = serializers.IntegerField(required=False)
