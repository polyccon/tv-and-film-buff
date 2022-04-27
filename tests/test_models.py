import json
import os
from unittest.mock import (
    MagicMock,
    patch,
)

import pytest
from django.contrib.auth.models import User
from tv_and_film_buffAPI.models import Series, Episodes
from tests.factories import SeriesFactory, EpisodesFactory


@pytest.mark.django_db
def test_series_record_created_correctly():
    s = SeriesFactory(title="Seinfeld")
    assert s.total_seasons == 8
    assert s.seriesID == "tt0944947"


@pytest.mark.django_db
def test_episodes_record_created_correctly():
    s = SeriesFactory(title="Seinfeld")
    e = EpisodesFactory(
        title="The Stake Out",
        episode_number=2,
        genre="Comedy",
        plot="Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
        series=s,
    )
    assert e.season_number == 1
    assert e.language == "English"
    assert e.imdbRating == 9.0
    assert e.series.title == "Seinfeld"
