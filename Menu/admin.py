from django.contrib import admin
from .models import Dish
from .models import DishIngredient
from .models import Ingredient


# Register your models here.
admin.site.register(Dish)
admin.site.register(DishIngredient)
admin.site.register(Ingredient)



