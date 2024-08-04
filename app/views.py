from django.shortcuts import render
from . models import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from . serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
