# Generated by Django 5.0.6 on 2024-06-03 09:10

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotel', '0003_alter_hotelimage_unique_together'),
        ('Room', '0003_alter_facility_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('bookingId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bookingPrice', models.FloatField(null=True)),
                ('checkinDate', models.DateField()),
                ('checkoutDate', models.DateField()),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotelbookings', to='Hotel.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotelbookings', to='Room.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotelbookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('hotel', 'room', 'checkinDate', 'checkoutDate')},
            },
        ),
    ]
