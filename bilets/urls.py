from django.urls import path
from bilets.views import IndexView, BuyBilets, ProverkaBilets

app_name = 'bilets'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('BuyBilets', BuyBilets.as_view(), name='BuyBilets'),
    path('ProverkaBilets', ProverkaBilets.as_view(), name='ProverkaBilets'),
]
