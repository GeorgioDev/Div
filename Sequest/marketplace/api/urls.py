from django.urls import path
from marketplace.api import views
from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
                path('', views.RequestListSerializer.as_view(), name="user-list"),
                path('api/marketplace/create/', views.RequestCreateSerializer.as_view(), name="request-create"),
                path('api/marketplace/<int:pk>/', views.RequestDetailSerializer.as_view(), name="request-detail"),
                path('api/marketplace/<int:pk>/edit/', views.RequestUpdateSerializer.as_view(), name="request-update"),
                path('api/marketplace/<int:pk>/delete/', views.RequestDeleteSerializer.as_view(), name="request-delete"),


                path('api/marketplace/offer/', views.OfferSerializer.as_view(), name="offer"),
                path('api/marketplace/offermedia/', views.OfferMediaSerializer.as_view(), name="offermedia"),
                path('api/marketplace/message/', views.MessageSerializer.as_view(), name="message"),
                path('api/marketplace/hiddenrequests/', views.HiddenRequestSerializer.as_view(), name="hiddenrequest"),
]
