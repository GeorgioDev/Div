from accounts.models import Profile
from accounts.api.account_serializer import ProfileSerializer, UserSerializer
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth.models import User


class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    return render(request, 'index.html')
