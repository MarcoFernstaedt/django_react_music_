# from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .forms import SignUpForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name= 'posts'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'blog/templates/blog/registration/signup.html'

class LoginView():
    pass
    # create logint