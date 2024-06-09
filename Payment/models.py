from django.db import models
from Booking.models import Booking
from Ordering.models import OrderItem


# Create your models here.
class Payment(models.Model):
    booking = models.ForeignKey(Booking,related_name='payments', on_delete=models.CASCADE)
    order_item = models.ForeignKey(OrderItem,related_name='payments', on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField()
    payment_time = models.TimeField()
    status = models.BooleanField(default =False)
