from marketplace.models import Request, Offer, OfferMedia, Message, HiddenRequest
from marketplace.api.marketplace_serializer import RequestListSerializer, RequestCreateSerializer, RequestDetailSerializer, RequestDeleteSerializer, RequestUpdateSerializer, OfferSerializer, OfferMediaSerializer, MessageSerializer, HiddenRequestSerializer

from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response


class RequestListSerializer(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestListSerializer
    permission_classes = [AllowAny]


class RequestCreateSerializer(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer
    permission_classes = [IsAuthenticated]
    throttle_scope = 'create_thread'


class RequestDetailSerializer(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestDetailSerializer
    permission_classes = [AllowAny]


class RequestDeleteSerializer(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestDeleteSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]


class RequestUpdateSerializer(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestUpdateSerializer
    permission_classes = [IsAdminUser]





class OfferSerializer(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer





class MessageSerializer(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def index(request):
    return render(request, 'index.html')
