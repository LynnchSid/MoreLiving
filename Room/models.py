from django.db import models
from django.contrib.auth.models import User
from Hotel.models import Hotel
import uuid

class Room(models.Model):
    roomId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    hotel=models.ForeignKey(Hotel,related_name='rooms',on_delete=models.CASCADE)
    roomNumber = models.IntegerField()
    roomType = models.CharField(max_length=100)
    children = models.IntegerField()
    adult = models.IntegerField()
    price=models.FloatField()
    roomDescription=models.CharField(max_length=350)
    
    class Meta:
        unique_together = ('roomNumber', 'roomType','hotel')
    
    def __str__(self):
        return f"{self.hotel.name} - Room {self.roomNumber}"
    
class Roomimage(models.Model):
    imageID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    room=models.ForeignKey(Room,related_name='Roomimages',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/rooms_images')
    roomImagedesc= models.TextField(max_length=200)
    
    class Meta:
        unique_together = ('image', 'room')
    
    def __str__(self):
        return f"{self.image} - Room {self.roomImagedesc}"
                            
    
    
class Facility(models.Model):
    facilityId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    room = models.ForeignKey(Room,related_name='Facilities',on_delete=models.CASCADE)
    facilityName = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ('facilityName', 'room')
    
    def __str__(self):
        return self.facilityName
    
class Feature(models.Model):
    featureId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    room = models.ForeignKey(Room,related_name='Features',on_delete=models.CASCADE)
    featureName = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ('featureName', 'room')
    
    def __str__(self):
        return self.featureName
    

