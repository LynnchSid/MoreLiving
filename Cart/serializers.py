from rest_framework import serializers
from .models import Cart, CartItem
from Menu.models import MenuItem
from Menu.serializers import MenuItemSerializer

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    restaurant = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'menu_item', 'quantity', 'restaurant']

    def get_restaurant(self, obj):
        return obj.menu_item.restaurant.name

class CartItemCreateSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = CartItem
        fields = ['menu_item', 'quantity']

    def validate(self, attrs):
        menu_item = attrs['menu_item']
        restaurant = menu_item.restaurant
        if not restaurant:
            raise serializers.ValidationError("This menu item does not belong to a valid restaurant.")
        return attrs

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']
