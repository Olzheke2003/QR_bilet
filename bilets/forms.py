from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import AbstractUser
from bilets.models import Proverka

class UserLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите email'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = AbstractUser
        fields = ('email', 'password')

class ProverkaForm(forms.Form):
    invoiceId_Vvod = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    class Meta:
        model = Proverka
        fields = ('invoiceId_Vvod',)