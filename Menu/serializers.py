from rest_framework import serializers
from .models import Ingredient, Dish, DishIngredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'amount']

class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = DishIngredient
        fields = ['ingredient', 'quantity']

class DishSerializer(serializers.ModelSerializer):
    ingredients = DishIngredientSerializer(source='dishingredient_set', many=True)

    class Meta:
        model = Dish
        fields = ['name','price', 'ingredients']