from django.urls import path 
from .views import OpeningHourListCreate

urlpatterns =[
    path ('opening-hours/', OpeningHourListCreate.as_view(), name='opening-hour-list-create'),
    
]