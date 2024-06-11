from rest_framework import serializers 
from .models import Category , Restaurant, RestaurantImage
from Table.serializers import TableSerializer
from Menu.serializers import MenuItemSerializer
from Review.serializers import ReviewSerializer
from OpeningHours.serializers import OpeningHourSerializer


class RestaurantImageSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = RestaurantImage
        fields = ['id','restaurant','image']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = ['name']

class RestaurantSerializer(serializers.ModelSerializer):
    images = RestaurantImageSerializer(many=True, read_only=True)
    tables = TableSerializer(many=True, read_only=True)
    opening_hours = OpeningHourSerializer(many=True, read_only=True)
    menu_items =MenuItemSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields =['id', 'name', 'category', 'description', 'images', 'location', 'phoneNumber','delivery', 'delivery_start_time', 'delivery_end_time','tables','menu_items', 'opening_hours','reviews']

        def validate(self, data):
            if data.get('delivery'):
                delivery_start_time = data.get('delivery_start_time')
                delivery_end_time = data.get('delivery_end_time')
                if not delivery_start_time or not delivery_end_time:
                    raise serializers.ValidationError("Delivery times must be provided if delivery is enabled.")
            return data
        def create(self, validated_data):
            images_data = self.context['request'].FILES
            restaurant = Restaurant.objects.create(**validated_data)
            for image_data in images_data.getlist('images'):
                RestaurantImage.objects.create(restaurant=restaurant, image=image_data)
            return restaurant