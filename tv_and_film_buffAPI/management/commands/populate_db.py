import logging
import os
import json
import sys
from pathlib import Path

from django.core.management.base import BaseCommand

from tv_and_film_buffAPI.models import Series, Episodes

logger = logging.getLogger(__name__)

# sys.path.insert(0, os.path.dirname(Path(__file__).parent))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tv_and_film_buffAPI.config.settings")
# django.setup()

EPISODES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../../../data/episodes"
)


def create_series_records():
    print(os.listdir(EPISODES_DIR))
    for _file in os.listdir(EPISODES_DIR):
        with open(os.path.join(EPISODES_DIR, _file), "r") as f:
            print("f", f)
            text = json.loads(f.read())
            title = text["Title"]
            total_seasons = 8
            # total_seasons = int(text["totalSeasons"])
            seriesID = text["seriesID"]
            s = Series.objects.create(
                title=title, total_seasons=total_seasons, seriesID=seriesID
            )
            return s


def create_episode_records():
    series = Series.objects.get(seriesID="tt0944947")
    print(os.listdir(EPISODES_DIR))
    for _file in os.listdir(EPISODES_DIR):
        with open(os.path.join(EPISODES_DIR, _file), "r") as f:
            print("f", f)
            text = json.loads(f.read())
            title = text["Title"]
            # total_seasons = 8
            # seriesID = text["seriesID"]

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
                if created:
                    episode.title = title
                    # total_seasons=total_seasons,
                    # seriesID=seriesID,
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
            except Exception as e:
                print(f"Error: {e}")


class Command(BaseCommand):
    help = "Populate db"

    def handle(self, *args, **options):
        # create_series_records()
        create_episode_records()
