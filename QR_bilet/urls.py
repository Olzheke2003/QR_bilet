from django.contrib import admin
from django.urls import path, include
from bilets.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('bilets/', include('bilets.urls', namespace='bilets')),

]
