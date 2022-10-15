import datetime as dt
import json
import os

import factory
from django.utils import timezone
from factory.fuzzy import FuzzyInteger
from tv_and_film_buffAPI.models import Series, Episodes


class SeriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Series

    title = "Game of Thrones"
    total_seasons = 8
    seriesID = "tt0944947"


class EpisodesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Episodes

    title = "Winter Is Coming"
    plot = "Eddard Stark is torn between his family and an old friend when asked to serve at the side of King Robert Baratheon; Viserys plans to wed his sister to a nomadic warlord in exchange for an army."
    episode_number = 1
    season_number = 1
    genre = "Action, Adventure, Drama"
    language = "English"
    imdb_rating = 9.0
    imdb_id = "tt1480055"
    poster = "https://m.media-amazon.com/images/M/MV5BOTYwZDNlMDMtZWRkNC00NzNkLTk2ZDMtNGQ1MmEwNzAwZGZhXkEyXkFqcGdeQXVyMjg2MTMyNTM@._V1_SX300.jpg"
    series = factory.SubFactory(SeriesFactory)
