from django.urls import path
from .views import UserLoginView

app_name = 'Users'

urlpatterns = [
    path('UserLogin/', UserLoginView.as_view(), name='UserLogin'),
]
