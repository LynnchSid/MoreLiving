from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'rating', 'comment','created_at']

    def validate_rating(self, value,):
        if value< 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value