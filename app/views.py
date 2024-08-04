from django.shortcuts import render
from . models import *
from rest_framework import viewsets
from . serializers import *
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=None,updated_at=None)

    def perform_update(self,serializer):
        serializer.save(updated_by=self.request.user,updated_at=timezone.now())    

    @action(detail=True,methods=['get'])
    def movies(self,request,pk=None):
        genre = Genre.objects.all()
        print(genre)
        return Response({
                "status" : "success",
                "message" : pk
        })
      


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=None,updated_at=None)

    def perform_update(self,serializer):
        serializer.save(updated_by=self.request.user,updated_at=timezone.now())