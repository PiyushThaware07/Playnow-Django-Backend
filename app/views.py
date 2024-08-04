from django.shortcuts import render
from . models import *
from rest_framework import viewsets
from . serializers import *
from django.utils import timezone

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=None,updated_at=None)

    def perform_update(self,serializer):
        serializer.save(updated_by=self.request.user,updated_at=timezone.now())