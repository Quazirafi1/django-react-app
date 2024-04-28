from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    #get list of User objects (making sure user does not already exists)
    queryset = User.objects.all()
    #serializer telling what sort of data to accept to create a user
    serializer_class = UserSerializer
    #who can access this (anyone who wants to register)
    permission_classes = [AllowAny]