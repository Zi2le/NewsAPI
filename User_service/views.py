from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import  UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]


   
