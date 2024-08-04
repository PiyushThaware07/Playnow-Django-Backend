from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail', 
        read_only=True,
    )
    class Meta:
        model = Movie
        fields = "__all__"