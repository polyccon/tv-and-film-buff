from django.db import models

# from django.contrib.postgres.fields import ArrayField


class Series(models.Model):
    class Meta:
        ordering = ("title",)

    title = models.CharField(max_length=255)
    total_seasons = models.IntegerField(default=1)
    series_id = models.CharField(max_length=10, unique=True, primary_key=True)

    def __str__(self):
        return self.title


class Episodes(models.Model):
    class Meta:
        ordering = ("series",)

    IMDB_RATING_NOT_SET = -1
    language_choices = tuple((v, v) for v in ["English", "Greek", "Italian"])

    title = models.CharField(max_length=255)
    plot = models.CharField(max_length=255)
    episode_number = models.IntegerField(default=1)
    season_number = models.IntegerField(default=1)
    # TODO: change below to ArrayField with move to postgres?
    genre = models.CharField(default="Action", max_length=75)
    language = models.CharField(max_length=30, choices=language_choices)
    imdb_rating = models.FloatField(default=IMDB_RATING_NOT_SET)
    poster = models.URLField(max_length=200)
    imdb_id = models.CharField(max_length=10, unique=True)
    series = models.ForeignKey(
        "Series",
        on_delete=models.CASCADE,
        related_name="episodes",
    )

    def __str__(self):
        return self.imdb_id


class Comments(models.Model):
    body = models.TextField()
    episode = models.ForeignKey(
        "Episodes", on_delete=models.CASCADE, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)
