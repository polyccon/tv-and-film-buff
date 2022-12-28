"""tv_and_film_buff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from tv_and_film_buffAPI.views import EpisodesViewSet, CommentsViewSet, SeriesViewSet


EPISODES_LIST = path(
    "episodes/",
    EpisodesViewSet.as_view({"get": "list"}),
    name="episode-list",
)

EPISODE_RETRIEVE = path(
    "episodes/<imdb_id>/",
    EpisodesViewSet.as_view({"get": "retrieve"}),
    name="episode-retrieve",
)

COMMENTS_LIST_CREATE = path(
    "episodes/<imdb_id>/comments",
    CommentsViewSet.as_view({"get": "list", "post": "create"}),
    name="comments-list-create",
)

COMMENTS_RETRIEVE_UPDATE = path(
    "episodes/<imdb_id>/comments/<id>",
    CommentsViewSet.as_view({"get": "retrieve", "put":"update", "delete": "delete"}),
    name="comments-update",
)

SERIES_LIST = path(
    "series/",
    SeriesViewSet.as_view({"get": "list"}),
    name="series-list",
)

urlpatterns = [EPISODES_LIST, EPISODE_RETRIEVE, COMMENTS_LIST_CREATE, COMMENTS_RETRIEVE_UPDATE, SERIES_LIST]
