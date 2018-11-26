from administration.models import ReportedRequest
from administration.api.administration_serializer import ReportedRequestSerializer
from rest_framework import generics
from django.shortcuts import render


class ReportedRequestListCreate(generics.ListCreateAPIView):
    queryset = ReportedRequest.objects.all()
    serializer_class = ReportedRequestSerializer


def index(request):
    return render(request, 'index.html')
