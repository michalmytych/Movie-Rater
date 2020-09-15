from django.contrib.auth.models import User
from .models import Movie
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'year',
                  'description',
                  'imdb_link',
                  'imdb_rating',
                  'premiere',
                  'poster'
                  ]
