from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'restaurant', 'number', 'seats']

    def validate(self, data):
        if Table.objects.filter(restaurant=data['restaurant'], number=data['number']).exists():
            raise serializers.ValidationError("This table number already exists for this restaurant.")
        return data