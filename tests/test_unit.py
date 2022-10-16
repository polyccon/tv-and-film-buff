import django
from django.utils import timezone
import pytest
from rest_framework.reverse import reverse

from rest_framework.test import (
    APIClient,
)
from tests.factories import (
    CommentsFactory,
    SeriesFactory,
    EpisodesFactory,
    CommentsFactory,
)
from tv_and_film_buffAPI.urls import EPISODES_LIST, EPISODE_RETRIEVE, COMMENTS_LIST


@pytest.fixture
def episode():
    return EpisodesFactory(
        title="The Stake Out",
        episode_number=2,
        genre="Comedy",
        plot="Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
        series=SeriesFactory(title="Seinfeld"),
    )


@pytest.fixture
def comment(episode):
    return CommentsFactory(episode=episode)


@pytest.mark.django_db
def test_list_endpoint_returns_episodes(episode):
    client = APIClient()
    url = reverse(
        viewname=EPISODES_LIST.name,
    )
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert response.json() == [
        {
            "imdb_id": "tt1480055",
            "title": "The Stake Out",
            "plot": "Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
            "season_number": 1,
            "episode_number": 2,
            "genre": "Comedy",
            "language": "English",
            "imdb_rating": 9.0,
            "poster": "https://m.media-amazon.com/images/M/MV5BOTYwZDNlMDMtZWRkNC00NzNkLTk2ZDMtNGQ1MmEwNzAwZGZhXkEyXkFqcGdeQXVyMjg2MTMyNTM@._V1_SX300.jpg",
            "series": "tt0944947",
        }
    ]


@pytest.mark.django_db
def test_get_endpoint_returns_episode(episode):
    client = APIClient()
    url = reverse(viewname=EPISODE_RETRIEVE.name, kwargs={"imdb_id": "tt1480055"})
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert response.json() == {
        "imdb_id": "tt1480055",
        "title": "The Stake Out",
        "plot": "Jerry and Elaine have just ended their relationship, but have chosen to remain friends",
        "season_number": 1,
        "episode_number": 2,
        "genre": "Comedy",
        "language": "English",
        "imdb_rating": 9.0,
        "poster": "https://m.media-amazon.com/images/M/MV5BOTYwZDNlMDMtZWRkNC00NzNkLTk2ZDMtNGQ1MmEwNzAwZGZhXkEyXkFqcGdeQXVyMjg2MTMyNTM@._V1_SX300.jpg",
        "series": "tt0944947",
    }


@pytest.mark.django_db
def test_get_endpoint_returns_404_for_non_existent_id(episode):
    client = APIClient()
    url = reverse(viewname=EPISODE_RETRIEVE.name, kwargs={"imdb_id": "tt1480052"})
    response = client.get(url, format="json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_list_endpoint_returns_comments(comment):
    client = APIClient()
    url = reverse(viewname=COMMENTS_LIST.name, kwargs={"imdb_id": "tt1480055"})
    response = client.get(url, format="json")
    assert response.status_code == 200
    assert response.json() == [
        {
            "body": "This is a comment for an episode",
            "episode": 6,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        }
    ]
