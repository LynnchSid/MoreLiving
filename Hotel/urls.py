from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',HotelCategoryListCreate.as_view(),name='hotel-category-list-create'),
    path('categories/<pk>/',HotelCategoryListCreate.as_view(),name='hotel-category-individual'),
    path('hotels/',HotelListCreate.as_view(),name='hotel-list-create'),
    path('hotels/<pk>/',HotelListCreate.as_view(),name='hotel-individual'),
    path('hotels/<pk>/images/',HotelimageListCreate.as_view(),name='hotel-images'),
    path('hotels/<pk>/images/<image_id>/',HotelimageListCreate.as_view(),name='hotel-image-individual'),
    
    
         
]