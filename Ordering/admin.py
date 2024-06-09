from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'restaurant', 'total_price', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemAdmin]
    actions = ['cancel_order', 'complete_order', 'delete_selected']

    def cancel_order(self, request, queryset):
        queryset.update(status='canceled')
    cancel_order.short_description = "Cancel selected orders"

    def complete_order(self, request, queryset):
        queryset.update(status='completed')
    complete_order.short_description = "Complete selected orders"

    def delete_selected(self, request, queryset):
        queryset.delete()
    delete_selected.short_description = "Delete selected orders"

admin.site.register(Order, OrderAdmin)
