from django.urls import path
from .views import RoomListCreate, FacilityListCreate , FeatureListCreate, RoomimageListCreate

urlpatterns = [
   
    path('rooms/',RoomListCreate.as_view(),name='room-list-create'),
    path('rooms/<pk>/', RoomListCreate.as_view(), name='room-details'),
    path('rooms/facilities/', FacilityListCreate.as_view(), name='facility-list-create'),
    path('rooms/facilities/<pk>/', FacilityListCreate.as_view(), name='facility-details'),
    path('rooms/features/', FeatureListCreate.as_view(), name='feature-list-create'),
    path('rooms/features/<pk>/', FeatureListCreate.as_view(), name='feature-details'),
    path('rooms/roomimages/', RoomimageListCreate.as_view(), name='roomimage-list-create'),
    path('rooms/roomimages/<pk>/', RoomimageListCreate.as_view(), name='roomimage-details'),
    
]