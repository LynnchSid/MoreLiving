from django.contrib import admin
from .models import Room,Roomimage,Facility,Feature
from Hotel.models import Hotel

class RoomimageAdmin(admin.TabularInline):
    model = Roomimage
    extra = 1
class FacilityAdmin(admin.TabularInline):
    model = Facility
    extra = 1
    
class FeatureAdmin(admin.TabularInline):
    model = Feature
    extra = 1
    
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomimageAdmin,FacilityAdmin,FeatureAdmin]
    list_display = ('roomNumber', 'roomType', 'children', 'adult','price','roomDescription','hotel')
    
    

admin.site.register(Room, RoomAdmin)

# Register your models here.
