
from dj_rest_auth.registration.views import *
from django.urls import path, include
# from .views import  GoogleLogin ,GoogleConnect

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('login/', include('dj_rest_auth.urls')),
    path('logout/', include('dj_rest_auth.urls')),
    path('auth/social/', include('allauth.socialaccount.urls')),
    path('registration/account-confirm-email/<str:key>/', include('dj_rest_auth.registration.urls')),
    path('password/reset/', include('dj_rest_auth.urls')),
    path('password/reset/confirm/', include('dj_rest_auth.urls')),
    path('password/change/', include('dj_rest_auth.urls')),
    path('password/change/done/', include('dj_rest_auth.urls')),
    path('verify-email/', include('dj_rest_auth.urls')),
    path('verify-email/complete/', include('dj_rest_auth.urls')),
    path('verify-email/resend/', include('dj_rest_auth.urls')),
    path('user/', include('dj_rest_auth.urls')),
    path('auth/social/', include('allauth.socialaccount.urls')),
    # path('login/google/', GoogleLogin.as_view(), name='google_login'),
    # path('connect/google/', GoogleConnect.as_view(), name='google_connect'),
]