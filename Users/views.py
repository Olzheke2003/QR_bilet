from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import UserLoginForm
from django.contrib.auth.models import AbstractUser


class UserLoginView(LoginView):
    template_name = 'Users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


# class UserRegistration(CreateView):
#     model = AbstractUser