from django.db import models
from django.contrib.auth.models import User
import uuid


class HotelCategory(models.Model):
    type=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}-{self.type}"
    
class Hotel(models.Model):
    hotelID= models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name=models.CharField(max_length=100)
    type=models.ForeignKey(HotelCategory,related_name='hotel_types',on_delete=models.CASCADE)
    location=models.CharField(max_length=150)
    phoneNumber=models.CharField(max_length=100)
    hotelDescription=models.CharField(max_length=350)
    hotelEmail=models.EmailField(max_length=100,null=True)
    
    class Meta:
        unique_together = ('name', 'type','location')
    
    def __str__(self):
        return f"{self.hotelID}  - {self.name}"
    
class Hotelimage(models.Model):
    imageID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    hotel=models.ForeignKey(Hotel,related_name='Hotelimages',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/hotels_images')
    hotelImagedesc= models.TextField(max_length=200)
    
    class Meta:
        unique_together = ('image', 'hotel')
        
    def __str__(self):
        return f"{self.image} - Room {self.hotelImagedesc}"

