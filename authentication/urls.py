from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProfileView

urlpatterns=[
    path("register/",UserRegistrationAPIView.as_view(),name="register-user"),
    path("login/",UserLoginAPIView.as_view(),name="login-user"),
    path("logout/",UserLogoutAPIView.as_view(),name="logout-user"),
    path("token/refresh/",TokenRefreshView.as_view(), name="token-refresh"),
    path('profile/', ProfileView.as_view()),

]
