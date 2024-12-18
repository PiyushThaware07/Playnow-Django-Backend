from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    updated_by = serializers.ReadOnlyField(source='updated_by.username')
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_at = serializers.ReadOnlyField()
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')
    updated_at = serializers.ReadOnlyField()
    genre_name = serializers.SerializerMethodField()
    def get_genre_name(self, obj):
        return obj.genre.name if obj.genre else None
    
    class Meta:
        model = Movie
        fields = "__all__"