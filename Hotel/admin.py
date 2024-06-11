from django.contrib import admin
from .models import HotelCategory,Hotel,Hotelimage

admin.site.register(HotelCategory)

class HotelimageAdmin(admin.TabularInline):
    model = Hotelimage
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelimageAdmin]
    list_display = ('name','hotelID' ,'location', 'phoneNumber', 'hotelDescription','hotelEmail')
    
    
admin.site.register(Hotel, HotelAdmin)
