from django.db import models
from django.db.models import Q, UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from Room.models import Room
from Hotel.models import Hotel
import uuid

class RoomBooking(models.Model):
    bookingId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, related_name="hotelbookings", on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name="hotelbookings", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="hotelbookings", on_delete=models.CASCADE)
    bookingPrice = models.FloatField(null=True)
    checkinDate = models.DateField()
    checkoutDate = models.DateField()
    createdAt = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('PENDING', 'pending'), ('ACCEPTED', 'accepted'), ('cancelled', 'CANCELLED')], default='PENDING')
    
    def __str__(self):
        return f"Booked by {self.user.username} for {self.checkinDate} to {self.checkoutDate}"
