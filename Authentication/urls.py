from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import *
from django.urls import path, include

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('registration/account-confirm-email/<str:key>/', include('dj_rest_auth.registration.urls')),
    path('password/reset/', include('dj_rest_auth.urls')),
    path('password/reset/confirm/', include('dj_rest_auth.urls')),
    path('password/change/', include('dj_rest_auth.urls')),
    path('password/change/done/', include('dj_rest_auth.urls')),
    path('verify-email/', include('dj_rest_auth.urls')),
    path('verify-email/complete/', include('dj_rest_auth.urls')),
    path('verify-email/resend/', include('dj_rest_auth.urls')),
    path('user/', include('dj_rest_auth.urls')),
]