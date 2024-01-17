from django.urls import path, include
from rest_framework import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns =[
    path('api/token/', TokenObtainPairView),
    path('api/token/refesh', TokenRefreshView),
    path('api/token/verify', TokenVerifyView),
]