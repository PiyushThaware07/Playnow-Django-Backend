from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='created_by.username')
    updated_at = serializers.ReadOnlyField()
    class Meta:
        model = Movie
        fields = "__all__"