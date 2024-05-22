import secrets
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse

from users.forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from users.models import User

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            'Подтверждение почты',
            f'Перейдите по ссылке для подтверждения почты {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
