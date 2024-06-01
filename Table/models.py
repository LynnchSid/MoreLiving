from django.db import models
from Restaurant.models import Restaurant


# Create your models here.
class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    number = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant.name} - Table  {self.number}"
