from django.contrib import admin
from .models import Cart, CartItem

class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ('id', 'user', 'total_cost', 'total_items')
    list_filter = ('user', 'created_at')

    def total_cost(self, obj):
        return obj.total_cost()
    total_cost.short_description = 'Total Cost'

    def total_items(self, obj):
        return obj.total_items()
    total_items.short_description = 'Total Items'

    def cancel_order(self, request, queryset):
        queryset.update(status='cancelled')

    def complete_order(self, request, queryset):
        queryset.update(status='completed')

    def delete_selected(self, request, queryset):
        queryset.delete()

    actions = [cancel_order, complete_order, delete_selected]

admin.site.register(Cart, CartAdmin)
