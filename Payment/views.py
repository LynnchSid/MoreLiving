from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import stripe
from .models import Payment
from Booking.models import Booking
from Ordering.models import Order
from .serializers import CreatePaymentIntentSerializer, ConfirmPaymentSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntentView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreatePaymentIntentSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            try:
                intent = stripe.PaymentIntent.create(
                    amount=int(amount * 100),  # Stripe expects the amount in cents
                    currency='usd',
                    payment_method_types=['card'],
                )
                return Response({'client_secret': intent.client_secret}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmPaymentForBookingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ConfirmPaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment_intent_id = serializer.validated_data['payment_intent_id']
            booking_id = serializer.validated_data.get('booking_id')
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                intent.confirm()
                booking = Booking.objects.get(id=booking_id)
                booking.stripe_charge_id = intent.id
                booking.payment_status = intent.status
                booking.save()
                return Response({'message': 'Payment confirmed for booking'}, status=status.HTTP_200_OK)
            except stripe.error.CardError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except stripe.error.StripeError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmPaymentForOrderView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ConfirmPaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment_intent_id = serializer.validated_data['payment_intent_id']
            order_id = serializer.validated_data.get('order_id')
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                intent.confirm()
                order = Order.objects.get(id=order_id)
                order.stripe_charge_id = intent.id
                order.payment_status = intent.status
                order.save()
                return Response({'message': 'Payment confirmed for order'}, status=status.HTTP_200_OK)
            except stripe.error.CardError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except stripe.error.StripeError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
