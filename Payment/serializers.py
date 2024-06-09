from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['booking','order_item', 'amount', 'payment_date', 'payment_time', 'status']