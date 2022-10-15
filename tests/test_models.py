import os
import pytest
from tv_and_film_buffAPI.models import Series, Episodes
from tests.factories import SeriesFactory, EpisodesFactory


@pytest.mark.django_db
def test_series_record_created_correctly():
    s = SeriesFactory(title="Seinfeld")
    assert s.total_seasons == 8
    assert s.series_id == "tt0944947"


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
    assert e.imdb_rating == 9.0
    assert e.series.title == "Seinfeld"
