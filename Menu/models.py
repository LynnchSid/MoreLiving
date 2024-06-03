from django.db import models
from Restaurant.models import Restaurant

class MenuItemType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.amount})"

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    type = models.ForeignKey(MenuItemType, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, related_name='menu_items')

    def __str__(self):
        return self.name