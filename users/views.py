from django.urls import reverse_lazy

from users.forms import UserRegisterForm
from django.shortcuts import render
from django.views.generic import CreateView
from users.models import User

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
