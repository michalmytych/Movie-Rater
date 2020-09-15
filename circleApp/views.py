from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, ExtraInfo, Review
from .forms import MovieForm, ExtraInfoForm, ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import UserSerializer, User, MovieSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


def all_movies(request):
    
    movies = Movie.objects.all()

    movies_amount = len(movies)

    return render(request, 'all_movies.html', 
        {
        'movies' : movies,
        'movies_amount' : movies_amount})


@login_required
def add_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    extra_form = ExtraInfoForm(request.POST or None)

    if all((form.is_valid(), extra_form.is_valid())):
        new_movie = form.save(commit=False)
        new_movie.extra_info = extra_form.save()
        new_movie.save()
        return redirect(all_movies)

    return render(request, 'new_movie.html', {'form': form, 'extra_form' : extra_form})


@login_required
def edit_movie(request, id):
    edited_movie = get_object_or_404(Movie, pk=id)
    reviews = Review.objects.filter(movie=edited_movie)

    try:
        extra = ExtraInfo.objects.get(movie=edited_movie.id)
    except ExtraInfo.DoesNotExist:
        extra = None

    form = MovieForm(request.POST or None, request.FILES or None, instance=edited_movie)
    extra_form = ExtraInfoForm(request.POST or None, instance=extra)
    review_form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if 'stars' in request.POST:
            review = review_form.save(commit=False)
            review.movie = edited_movie
            review.save()

    if all((form.is_valid(), extra_form.is_valid())):
        edited_movie = form.save(commit=False)
        edited_movie.extra_info = extra_form.save()
        edited_movie.save()
        return redirect(all_movies)
    
    return render(request, 'new_movie.html', {'form': form, 'reviews': reviews, 'extra_form' : extra_form, 'review_form' : review_form})


@login_required
def delete_movie(request, id):
    selected_movie = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        selected_movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'selected_movie': selected_movie})
