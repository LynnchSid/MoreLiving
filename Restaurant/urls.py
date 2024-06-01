from django.urls import path
from .views import CategoryListCreate, RestaurantListCreate




urlpatterns = [
    path('categories/',CategoryListCreate.as_view(),name='category-list-create'),
    path('restaurants/',RestaurantListCreate.as_view(),name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantListCreate.as_view(), name='restaurant-detail'),
]