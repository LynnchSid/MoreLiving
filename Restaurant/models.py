from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='restaurants', on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    delivery=models.BooleanField(default=False)
    delivery_start_time=models.TimeField(null=True,blank=True)
    delivery_end_time=models.TimeField(null=True,blank=True)


    def __str__(self):
        return self.name
    
class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/restaurants_images')

    def __str__(self):
        return f"Image for {self.restaurant.name}"
