# Generated by Django 5.0.6 on 2024-06-03 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_date', models.DateField()),
                ('payment_time', models.TimeField()),
                ('status', models.BooleanField(default=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='Booking.booking')),
            ],
        ),
    ]
