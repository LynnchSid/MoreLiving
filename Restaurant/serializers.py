from rest_framework import serializers 
from .models import Category , Restaurant
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ['name']

class RestaurantSerializer(serializers.ModelSerializer):
    tables = serializers.StringRelatedField(many=True, read_only=True)
    opening_hours = serializers.StringRelatedField(many=True, read_only=True)
    menus = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields =['id', 'name', 'category', 'description', 'image', 'location', 'phoneNumber','delivery', 'delivery_start_time', 'delivery_end_time','tables','menus', 'opening_hours']

        def validate(self, data):
            if data.get('delivery'):
                delivery_start_time = data.get('delivery_start_time')
                delivery_end_time = data.get('delivery_end_time')
                if not delivery_start_time or not delivery_end_time:
                    raise serializers.ValidationError("Delivery times must be provided if delivery is enabled.")
            return data