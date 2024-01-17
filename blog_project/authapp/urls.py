from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UserRegistrationView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refesh', TokenRefreshView.as_view()),
    path('api/token/verify', TokenVerifyView.as_view()),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]