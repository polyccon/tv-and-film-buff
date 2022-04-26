from django.db import models
from django.contrib.postgres.fields import ArrayField


class Series(models.Model):
    class Meta:
        ordering = ("id",)

    title = models.CharField(max_length=255)
    total_seasons = models.IntegerField(default=1)


class Episodes(models.Model):
    class Meta:
        ordering = ("id",)

    genre_choices = tuple((v, v) for v in ["Action", "Adventure", "Drama"])
    language_choices = tuple((v, v) for v in ["English", "Greek", "Italian"])

    title = models.CharField(max_length=255)
    plot = models.CharField(max_length=255)
    episode_number = models.IntegerField(default=1)
    season_number = models.IntegerField(default=1)
    genre = ArrayField(
        models.CharField(choices=genre_choices, default="Action", max_length=22)
    )
    language = models.CharField(max_length=30, choices=language_choices)
    imdbRating = models.CharField(max_length=10)
    series = models.ForeignKey(
        "Series",
        on_delete=models.CASCADE,
        related_name="episodes",
    )
