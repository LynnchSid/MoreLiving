from rest_framework import serializers
from .models import Order, OrderItem
from Restaurant.models import Restaurant
from Menu.models import MenuItem
from Menu.serializers import MenuItemSerializer
from Ordering.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity']

class OrderItemCreateSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    order_items_data = OrderItemCreateSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'restaurant', 'order_items', 'total_price', 'created_at', 'status', 'order_items_data']
        read_only_fields = ['total_price']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items_data')
        total_price = 0
        order = Order.objects.create(**validated_data)
        
        for order_item_data in order_items_data:
            menu_item = MenuItem.objects.get(id=order_item_data['menu_item'].id)
            quantity = order_item_data['quantity']
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
            total_price += menu_item.price * quantity
        
        order.total_price = total_price
        order.save()
        return order