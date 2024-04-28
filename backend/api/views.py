from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    #get list of User objects (making sure user does not already exists)
    queryset = User.objects.all()
    #serializer telling what sort of data to accept to create a user
    serializer_class = UserSerializer
    #who can access this (anyone who wants to register)
    permission_classes = [AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # view only the notes written by user
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # only validated users can create note
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

        # view only the notes written by user
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
