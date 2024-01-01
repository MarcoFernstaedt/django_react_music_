from django.urls import path
from .views import PostListView, SignUpView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('signup/', SignUpView.as_view(), name='signup')
]