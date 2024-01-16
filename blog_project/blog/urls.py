from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostSerializer, CommentSerializer

router = DefaultRouter()
router.register('posts', PostSerializer)
router.register('comments', CommentSerializer)

urlpatterns = [
    path('', include(router.urls)),
]