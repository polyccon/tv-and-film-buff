import os
import pytest
from tests.factories import SeriesFactory, EpisodesFactory, CommentsFactory


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


@pytest.mark.django_db
def test_comments_record_created_correctly():
    comment = CommentsFactory()
    assert comment.body == "This is a comment for an episode"
    assert comment.episode.title == "Winter Is Coming"
