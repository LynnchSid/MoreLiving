from rest_framework import serializers
from .models import OpeningHour

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

    def validate(self, data):
        if data['open_time'] >= data['close_time']:
            raise serializers.ValidationError("Open time must be before close time.")
        return data