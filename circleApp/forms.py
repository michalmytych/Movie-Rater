from django.forms import ModelForm
from .models import Movie, ExtraInfo, Review

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = [
            'year',
            'title',
            'description',
            'imdb_link',
            'imdb_rating',
            'premiere',
            'poster'
        ]

class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = [
            'duration',
            'genre'
        ]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'stars',
            'text_review'
        ]


