# admin.py

from django.contrib import admin
from .models import RoomBooking

@admin.action(description='Mark selected bookings as accepted')
def accept_bookings(modeladmin, request, queryset):
    queryset.update(status='ACCEPTED')

@admin.action(description='Mark selected bookings as canceled')
def cancel_bookings(modeladmin, request, queryset):
    queryset.update(status='CANCELED')

class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'hotel', 'room', 'checkinDate', 'checkoutDate', 'status']
    actions = [accept_bookings, cancel_bookings]

admin.site.register(RoomBooking, RoomBookingAdmin)
