import logging
import os
import json
import sys
from pathlib import Path

from django.core.management.base import BaseCommand

from tv_and_film_buffAPI.models import Series, Episodes

LOGGER = logging.getLogger(__name__)

EPISODES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../../../data/episodes"
)


def create_series_records():
    LOGGER.info("Creating series records")
    for _file in os.listdir(EPISODES_DIR):
        with open(os.path.join(EPISODES_DIR, _file), "r") as f:
            text = json.loads(f.read())
            title = text["Title"]
            # TODO: total seasons to be a variable in order to make
            # script flexible to create records for any series
            total_seasons = 8
            series_id = text["seriesID"]
            s = Series.objects.get_or_create(
                title=title, total_seasons=total_seasons, series_id=series_id
            )
            return s


def create_episode_records():
    LOGGER.info("Creating episodes records")
    # TODO: make series_id a variable
    series = Series.objects.get(series_id="tt0944947")
    for _file in os.listdir(EPISODES_DIR):
        with open(os.path.join(EPISODES_DIR, _file), "r") as f:
            text = json.loads(f.read())
            title = text["Title"]
            plot = text["Plot"]
            episode_number = text["Episode"]
            season_number = text["Season"]
            genre = text["Genre"]
            language = text["Language"]
            imdb_rating = text["imdbRating"]
            imdb_id = text["imdbID"]
            poster = text["Poster"]

            try:
                episode, created = Episodes.objects.get_or_create(
                    imdb_id=imdb_id, series=series
                )
                episode.title = title
                episode.plot = plot
                episode.episode_number = episode_number
                episode.season_number = season_number
                episode.genre = genre
                episode.language = language
                episode.imdb_rating = (
                    -1 if type(imdb_rating) == str else float(imdb_rating)
                )
                episode.imdb_id = imdb_id
                episode.poster = poster
                episode.save()
                LOGGER.info("Episodes created successfully")
            except Exception as e:
                LOGGER.error(f"Error: {e}")


class Command(BaseCommand):
    help = "Populate db"

    def handle(self, *args, **options):
        create_series_records()
        create_episode_records()
