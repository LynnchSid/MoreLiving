# Generated by Django 5.0.6 on 2024-06-01 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/restaurants_images')),
                ('location', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('delivery', models.BooleanField(default=False)),
                ('delivery_start_time', models.TimeField(blank=True, null=True)),
                ('delivery_end_time', models.TimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='Restaurant.category')),
            ],
        ),
    ]
