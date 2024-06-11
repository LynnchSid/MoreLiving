import django_filters
from .models import Room, Feature, Facility, Roomimage

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = [ 'hotel', 'roomType', 'children', 'adult', 'price']  # Add fields you want to filter on

class FeatureFilter(django_filters.FilterSet):
    class Meta:
        model = Feature
        fields = ['room','featureName']  # Add fields you want to filter on

class FacilityFilter(django_filters.FilterSet):
    class Meta:
        model = Facility
        fields = ['room','facilityName'] 
class RoomimageFilter(django_filters.FilterSet):
    class Meta:
        model = Roomimage
        fields = ['room']  # Add fields you want to filter on