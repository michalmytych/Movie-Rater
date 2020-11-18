from rest_framework import viewsets

from .serializers import (
    UserSerializer, 
    User, 
    Movie, 
    MovieSerializer
)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer