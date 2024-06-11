from django.urls import path
from .views import NotificationListCreate

urlpatterns = [
    path('notifications/', NotificationListCreate.as_view(), name='notification-list-create'),
]
