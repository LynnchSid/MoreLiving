from django.urls import path
from .views import CategoryListCreate, RestaurantListCreate,RestaurantImageListCreate, RestaurantImageDetail




urlpatterns = [
    path('categories/',CategoryListCreate.as_view(),name='category-list-create'),
    path('restaurants/',RestaurantListCreate.as_view(),name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantListCreate.as_view(), name='restaurant-detail'),
    path('restaurants/<int:restaurant_id>/images/', RestaurantImageListCreate.as_view(), name='restaurant-image-create'),
]