from django.contrib import admin
from .models import Movie, ExtraInfo, Review, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'year', 'imdb_rating']
    list_filter = ['year', 'imdb_rating']


admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Actor)

