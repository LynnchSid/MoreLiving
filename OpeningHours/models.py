from django.db import models
from Restaurant.models import Restaurant

# Create your models here.
class OpeningHour(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='opening_hours', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.day_of_week}"