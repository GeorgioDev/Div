from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace.api.urls')),
    path('', include('administration.api.urls')),
    path('', include('accounts.api.urls')),

]
