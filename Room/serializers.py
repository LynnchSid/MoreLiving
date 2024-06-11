from rest_framework import serializers
from .models import Room , Roomimage , Facility , Feature
from django.contrib.auth.models import User

                
class RoomimageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roomimage
        fields=['imageID', 'room', 'roomImagedesc']
        
        

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Facility
        fields=['facilityId' , 'room' , 'facilityName']
        
        
        
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feature
        fields=['featureId' , 'room' , 'featureName']
        
        
               

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['roomDescription', 'hotel', 'roomId', 'roomNumber', 'roomType', 'children', 'adult','Roomimages','Features','price','Facilities']
        
        
        
        