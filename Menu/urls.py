from django.urls import path
from .views import MenuItemTypeListCreate, MenuItemListCreate

urlpatterns = [
    path ('menu-item-types/', MenuItemTypeListCreate.as_view(), name='menu-item-type-list-create'),
    path ('menu-items/', MenuItemListCreate.as_view(), name='menu-item-list-create'),
]