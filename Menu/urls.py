from django.urls import path
from .views import (DishListCreateAPIView,DishRetrieveUpdateDestroyAPIView,IngredientListCreateAPIView, IngredientRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('dishes/', DishListCreateAPIView.as_view(), name='dish-list-create'),
    path('dishes/<int:pk>/', DishRetrieveUpdateDestroyAPIView.as_view(), name='dish-detail'),
    path('ingredients/', IngredientListCreateAPIView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyAPIView.as_view(), name='ingredient-detail'),
]