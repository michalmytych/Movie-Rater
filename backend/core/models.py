from django.db import models


class Movie(models.Model):
    class Meta:
        db_table = 'core_movies'

    year = models.PositiveSmallIntegerField(default=2000, blank=True)
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=200, default="")
    imdb_link = models.URLField(null=True)
    imdb_rating = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    premiere = models.DateField(null=True, blank=True)
    poster = models.ImageField(
        upload_to="posters", 
        null=True, 
        blank=True
    )
    extra_info = models.OneToOneField(
        "ExtraInfo", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.title + ' (' + str(self.year) + ') '


class ExtraInfo(models.Model):
    class Meta:
        db_table = 'core_extra_infos'

    GENRES = [
        (0, 'Wojenny'),
        (1, 'Dramat obyczajowy'),
        (2, 'Przygodowy'),
        (3, 'Thriller'),
        (4, 'Horror'),
        (5, 'Historyczny'),
        (6, 'Komedia miłosna'),
        (7, 'Melodramat'),
        (8, 'Komedia')
    ]
    duration = models.PositiveSmallIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRES)

    def __str__(self):
        return 'Movie object of genre: ' + str(self.genre) + ' and duration of ' + str(self.duration) + ' minutes.'


class Review(models.Model):
    class Meta:
        db_table = 'core_reviews'

    text_review = models.TextField(default='Brak recenzji.')
    stars = models.PositiveSmallIntegerField(default=3)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return 'Review object of movie: ' + self.movie.title


class Actor(models.Model):
    class Meta:
        db_table = 'core_actors'

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    movies = models.ManyToManyField("Movie")

    def __str__(self):
        return 'Actor object: ' + self.first_name + ' ' + self.last_name
