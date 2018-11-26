from django.urls import path
from accounts.api import views

urlpatterns = [
                path('', views.index),
                path('api/accounts/profile/', views.ProfileListCreate.as_view(), name="profile"),
                path('api/accounts/user/', views.UserListCreate.as_view(), name="user"),
]
