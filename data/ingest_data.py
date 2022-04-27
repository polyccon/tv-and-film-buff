import json
import logging
import os
import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
LOGGER = logging.getLogger(__name__)

SEASONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seasons/")
EPISDOES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "episodes/")


def get_request(url):
    r = requests.get(url)
    return r.text


def write_in_file(file_directory, file_name, text):
    with open(os.path.join(file_directory, file_name), "w") as f:
        f.write(text)


def get_season_content(url, season):
    content = get_request(url)
    return write_in_file(SEASONS_DIR, f"GameOfThrones_season_{season}.json", content)


def get_episode_imdbs(season):
    imdbIDs = []
    with open(
        os.path.join(SEASONS_DIR, f"GameOfThrones_season_{season}.json"), "r"
    ) as f:
        text = json.loads(f.read())
        for episode in text["Episodes"]:
            imdbIDs.append(episode["imdbID"])
        return imdbIDs


def get_episode_content(urls, season):
    for index, url in enumerate(urls):
        content = get_request(url)
        write_in_file(
            EPISDOES_DIR,
            f"GameOfThrones_season_{season}_episode_{index+1}.json",
            content,
        )


def get_all_seasons(total_seasons):
    LOGGER.info("Started fetching data for seasons")
    for i in range(1, total_seasons + 1):
        season = i
        season_url = f"http://www.omdbapi.com/?t=Game of Thrones&Season={season}&apikey={api_key}"
        get_season_content(season_url, season)
        LOGGER.info(f"Successfully retrieved data for season {season}")


def get_all_episodes(season):
    LOGGER.info(f"Started fetching data for episodes season {season}")
    imdbIDs = get_episode_imdbs(season)

    episode_urls = [
        f"http://www.omdbapi.com/?i={imdbID}&apikey={api_key}" for imdbID in imdbIDs
    ]
    get_episode_content(episode_urls, season)
    LOGGER.info(f"Successfully retrieved data season {season} episodes")


def main():
    # TODO: remove hardcoded number for total_seasons
    get_all_seasons(9)
    for i in range(1, 9):
        get_all_episodes(i)


if __name__ == "__main__":
    main()
