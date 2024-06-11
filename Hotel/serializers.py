from rest_framework import serializers
from .models import HotelCategory , Hotel , Hotelimage 
from datetime import date

class HotelCategorySerializer(serializers. ModelSerializer):
    class Meta:
        model=HotelCategory
        fields=['type']
        
class HotelimageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotelimage
        fields=['imageID','image','hotel', 'hotelImagedesc']        
               
class HotelSerializer(serializers.ModelSerializer):
    # hotel_types=HotelCategorySerializer()
    # rooms=RoomSerializer(many=True, read_only=True)
    Hotelimages=HotelimageSerializer(many=True,read_only=True)
    class Meta:
        model=Hotel
        fields=['type', 'name', 'hotelID', 'location', 'phoneNumber', 'hotelDescription','Hotelimages']