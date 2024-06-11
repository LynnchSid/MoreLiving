from django.contrib import admin
from .models import Category, Restaurant, RestaurantImage

class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 1

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [RestaurantImageInline]

admin.site.register(Category)
admin.site.register(Restaurant, RestaurantAdmin)
