# filters.py

import django_filters
from .models import HotelCategory, Hotel, Hotelimage

class HotelCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = HotelCategory
        fields = ['type']  # Add fields you want to filter on

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = ['name', 'type', 'location','hotelDescription']  # Add fields you want to filter on

class HotelimageFilter(django_filters.FilterSet):
    class Meta:
        model = Hotelimage
        fields = ['hotel']  # Add fields you want to filter on
