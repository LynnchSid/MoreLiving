
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version='v1',
        description="API documentation for the Restaurant project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@restaurant.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hotel Booking API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="wKvHl@example.com"), 
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Authentication.urls')),
    path('restaurant/', include('Restaurant.urls')),
    path('table/', include('Table.urls')),
    path ('booking/', include('Booking.urls')),
    path ('opening-hours/', include('OpeningHours.urls')),
    path ('user/', include('Userprofile.urls')),
    path ('review/', include('Review.urls')),
    path ('payment/', include('Payment.urls')),
    path ('notification/', include('Notification.urls')),
    path ('menu/', include('Menu.urls')),
    path ('analytics/', include('Analytics.urls')),
    path ('order/',include ('Ordering.urls')),
    path('cart/',include('Cart.urls')),
    
    path('hotel/', include('Hotel.urls')),
    path('room/', include('Room.urls')),
    path('roombooking/', include('Roombooking.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
