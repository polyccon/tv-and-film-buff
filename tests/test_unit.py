import pytest
from rest_framework.reverse import reverse

from rest_framework.test import (
    APIClient,
)
from tests.factories import SeriesFactory, EpisodesFactory
from tv_and_film_buffAPI.urls import EPISODE_LIST, EPISODE_RETRIEVE


@pytest.fixture
def episode():
    return EpisodesFactory(
        title="The Stake Out",
        episode_number=2,
        genre="Comedy",
        plot="Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
        series=SeriesFactory(title="Seinfeld"),
    )


@pytest.mark.django_db
def test_list_endpoint_returns_episodes(episode):
    client = APIClient()
    url = reverse(
        viewname=EPISODE_LIST.name,
    )
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert response.json() == [
        {
            "imdbID": "tt1480055",
            "title": "The Stake Out",
            "plot": "Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
            "season_number": 1,
            "episode_number": 2,
            "genre": "Comedy",
            "language": "English",
            "imdbRating": 9.0,
            "poster": "https://m.media-amazon.com/images/M/MV5BOTYwZDNlMDMtZWRkNC00NzNkLTk2ZDMtNGQ1MmEwNzAwZGZhXkEyXkFqcGdeQXVyMjg2MTMyNTM@._V1_SX300.jpg",
            "series": "tt0944947",
        }
    ]


@pytest.mark.django_db
def test_get_endpoint_returns_episode(episode):
    client = APIClient()
    url = reverse(viewname=EPISODE_RETRIEVE.name, kwargs={"imdbID": "tt1480055"})
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert response.json() == {
        "imdbID": "tt1480055",
        "title": "The Stake Out",
        "plot": "Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
        "season_number": 1,
        "episode_number": 2,
        "genre": "Comedy",
        "language": "English",
        "imdbRating": 9.0,
        "poster": "https://m.media-amazon.com/images/M/MV5BOTYwZDNlMDMtZWRkNC00NzNkLTk2ZDMtNGQ1MmEwNzAwZGZhXkEyXkFqcGdeQXVyMjg2MTMyNTM@._V1_SX300.jpg",
        "series": "tt0944947",
    }
