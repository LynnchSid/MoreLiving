from django.urls import path 
from .views import UserProfileListCreate, UserProfileDetail

urlpatterns = [
    path('users/', UserProfileListCreate.as_view(), name='user-profile-list-create'),
    path('users/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),
]