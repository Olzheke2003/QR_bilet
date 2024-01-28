from django.contrib import admin
from django.urls import path
from bilets.views import IndexView, UserLoginView, BuyBilets, ProverkaBilets

app_name = 'bilets'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('Login', UserLoginView.as_view(), name='UserLogin'),
    path('BuyBilets', BuyBilets.as_view(), name='BuyBilets'),
    path('ProverkaBilets', ProverkaBilets.as_view(), name='ProverkaBilets'),
]
