from django.contrib import admin
from .models import Movie, ExtraInfo, Review, Actor


admin.site.register(Movie)
admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Actor)
