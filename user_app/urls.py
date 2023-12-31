from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .apiviews import RegistrationAPIView, LogoutAPIView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),  # Token based authentication -Login
    path('register/', RegistrationAPIView.as_view(), name='register'),  # Token based authentication - Register
    path('logout/', LogoutAPIView.as_view(), name='logout'),  # Token based authentication - Logout
]
