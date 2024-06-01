from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)  # e.g., "200g", "2 tsp", etc.

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, through='DishIngredient')

    def __str__(self):
        return self.name

class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)  # Quantity used in the dish
