import django_filters
from django.db.models import (
    Max,
    Q,
    Subquery,
)

from tv_and_film_buffAPI.models import Episodes


class EpisodesListFilter(django_filters.FilterSet):
    class Meta:
        model = Episodes
        fields = ["imdb_rating", "series", "genre", "language"]

    imdb_rating = django_filters.CharFilter(
        method="imdb_rating_filter",
        label="imdb_rating",
        help_text="Filter for imdb_rating greater than or equal"
    )

    def imdb_rating_filter(self, qs, name, value):
        return qs.filter(imdb_rating__gte=value)

