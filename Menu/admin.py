from django.contrib import admin
from .models import MenuItem, MenuItemType, Ingredient



# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type')
    list_filter = ('type',)

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemType)
admin.site.register(Ingredient)




