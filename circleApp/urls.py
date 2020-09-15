from django.urls import path
from filmyweb.views import all_movies, add_movie, edit_movie, delete_movie

urlpatterns = [
    path('all/', all_movies, name="all"),
    path('new/', add_movie, name="new"),
    path('edit/<int:id>/', edit_movie, name="edit"),
    path('delete/<int:id>/', delete_movie, name="delete"),
]