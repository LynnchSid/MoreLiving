# Generated by Django 5.0.6 on 2024-06-10 07:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Restaurant', '0001_initial'),
        ('Table', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingDate', models.DateField()),
                ('bookingTime', models.TimeField()),
                ('number_of_adults', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('number_of_children', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(default='pending', max_length=20)),
                ('stripe_charge_id', models.CharField(blank=True, max_length=50, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='Restaurant.restaurant')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='Table.table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('restaurant', 'table', 'bookingDate', 'bookingTime')},
            },
        ),
    ]
