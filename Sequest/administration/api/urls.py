from django.urls import path
from administration.api import views

urlpatterns = [
                path('', views.index),
                path('api/administration/reportedrequest/', views.ReportedRequestListCreate.as_view(), name="reportedrequest"),
]
