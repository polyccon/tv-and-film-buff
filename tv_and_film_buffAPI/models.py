from django.db import models

# from django.contrib.postgres.fields import ArrayField


class Series(models.Model):
    class Meta:
        ordering = ("title",)

    title = models.CharField(max_length=255)
    total_seasons = models.IntegerField(default=1)
    seriesID = models.CharField(max_length=10, unique=True, primary_key=True)

    def __str__(self):
        return self.title


class Episodes(models.Model):
    class Meta:
        ordering = ("series",)

    genre_choices = tuple((v, v) for v in ["Action", "Adventure", "Drama"])
    language_choices = tuple((v, v) for v in ["English", "Greek", "Italian"])

    title = models.CharField(max_length=255)
    plot = models.CharField(max_length=255)
    episode_number = models.IntegerField(default=1)
    season_number = models.IntegerField(default=1)
    # TODO: change below to ArrayField with move to postgres
    genre = models.CharField(choices=genre_choices, default="Action", max_length=22)
    language = models.CharField(max_length=30, choices=language_choices)
    # TODO: change the imdbRating to a more flexible field type or allow empty values because sometimes it's missing
    imdbRating = models.FloatField()
    poster = models.URLField(max_length=200)
    imdbID = models.CharField(max_length=10, unique=True)
    series = models.ForeignKey(
        "Series",
        on_delete=models.CASCADE,
        related_name="episodes",
    )

    def __str__(self):
        return self.title
