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
from tv_and_film_buffAPI.models import Comments
from tv_and_film_buffAPI.urls import EPISODES_LIST, EPISODE_RETRIEVE, COMMENTS_LIST_CREATE, COMMENTS_RETRIEVE_UPDATE


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
def test_episodes_list_endpoint_returns_episodes(episode):
    client = APIClient()
    url = reverse(
        viewname=EPISODES_LIST.name,
    )
    
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert response.json() == [
        {
            "comments": [],
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
def test_episodes_get_endpoint_returns_episode(episode):
    client = APIClient()
    url = reverse(viewname=EPISODE_RETRIEVE.name, kwargs={"imdb_id": "tt1480055"})
    
    response = client.get(url, format="json")

    assert response.status_code == 200
    assert response.json() == {
        "comments": [],
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
def test_episodes_get_endpoint_returns_404_for_non_existent_id(episode):
    client = APIClient()
    url = reverse(viewname=EPISODE_RETRIEVE.name, kwargs={"imdb_id": "tt1480052"})
    
    response = client.get(url, format="json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_comments_list_endpoint_returns_comments(comment):
    client = APIClient()
    url = reverse(viewname=COMMENTS_LIST_CREATE.name, kwargs={"imdb_id": "tt1480055"})
    
    response = client.get(url, format="json")
    
    assert response.status_code == 200
    assert response.json() == [
        {"body": "This is a comment for an episode", "episode": comment.episode.pk}
    ]


@pytest.mark.django_db
def test_comments_create_endpoint_adds_and_returns_comment(episode, comment):
    comments = Comments.objects.filter(episode=episode)
    assert comments.count() == 1
    client = APIClient()
    url = reverse(viewname=COMMENTS_LIST_CREATE.name, kwargs={"imdb_id": "tt1480055"})
    
    response = client.post(
        url,
        {"body": "this is a test comment", "episode": episode.pk},
        format="json"
    )
    
    assert response.status_code == 201
    assert response.json() == {"body": "this is a test comment", "episode": episode.pk}
    assert comments.count() == 2


@pytest.mark.django_db
def test_comments_delet_endpoint_deletes_comment(episode, comment):
    comments = Comments.objects.filter(episode=episode)
    assert comments.count() == 1
    client = APIClient()
    url = reverse(viewname=COMMENTS_RETRIEVE_UPDATE.name, kwargs={"imdb_id": "tt1480055", "id": comment.pk})
    
    response = client.delete(url,format="json")
    
    assert response.status_code == 204
    # TODO: should the delete endpoint return an empty list instead
    # assert response.json() == []
    assert comments.count() == 0