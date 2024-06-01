from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$',
                       message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
