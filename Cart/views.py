from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemCreateSerializer
from Ordering.serializers import OrderSerializer
from Ordering.models import Order, OrderItem

class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddToCartView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

class PlaceOrderFromCartView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        if not cart.items.exists():
            return Response({"detail": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        orders_data = {}
        for item in cart.items.all():
            restaurant_id = item.menu_item.restaurant.id
            if restaurant_id not in orders_data:
                orders_data[restaurant_id] = []
            orders_data[restaurant_id].append({
                "menu_item": item.menu_item.id,
                "quantity": item.quantity
            })

        created_orders = []
        with transaction.atomic():
            for restaurant_id, items in orders_data.items():
                order_data = {
                    "user": request.user.id,
                    "restaurant": restaurant_id,
                    "order_items_data": items
                }
                order_serializer = OrderSerializer(data=order_data)
                order_serializer.is_valid(raise_exception=True)
                order = order_serializer.save()
                created_orders.append(order_serializer.data)

            # Delete cart items only after all orders are successfully created
            cart.items.all().delete()

        return Response(created_orders, status=status.HTTP_201_CREATED)
