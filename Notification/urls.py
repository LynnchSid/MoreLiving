from django.urls import path
from .views import NotificationListCreate

urlpatterns = [
    path('notifications/', NotificationListCreate.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationListCreate.as_view(), name='notification-detail'),
]