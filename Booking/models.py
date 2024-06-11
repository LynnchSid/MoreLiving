from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from Restaurant.models import Restaurant
from Table.models import Table

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='bookings', on_delete=models.CASCADE)
    table = models.ForeignKey(Table, related_name='bookings', on_delete=models.CASCADE)
    bookingDate = models.DateField()
    bookingTime = models.TimeField()
    number_of_adults = models.IntegerField(validators=[MinValueValidator(1)])
    number_of_children = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending')
    stripe_charge_id = models.CharField(max_length=50, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    @property
    def total_guests(self):
        return self.number_of_adults + self.number_of_children
    class Meta:
        unique_together = ('restaurant', 'table', 'bookingDate', 'bookingTime')

    def __str__(self):
        return f"Booking by {self.user.username} on {self.bookingDate} at {self.bookingTime}"

