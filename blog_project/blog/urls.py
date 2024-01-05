from django.urls import path
from django.contrib.auth.views import LoginView
from .views import PostListView, SignUpView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
