from  rest_framework import serializers
from .models import MenuItem,MenuItemType,Ingredient
class MenuItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemType
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'type', 'name', 'description', 'price', 'ingredients']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        menu_item = MenuItem.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
            menu_item.ingredients.add(ingredient)
        return menu_item

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        instance.restaurant = validated_data.get('restaurant', instance.restaurant)
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        instance.ingredients.clear()
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
            instance.ingredients.add(ingredient)

        return instance