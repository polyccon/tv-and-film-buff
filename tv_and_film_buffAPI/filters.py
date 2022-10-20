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

