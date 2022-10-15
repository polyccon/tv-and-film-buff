### tv-and-film-buff

**TO SETUP**

If you have pyenv installed (instructions for how to install pyenv here: https://github.com/pyenv/pyenv#installation)
then you can use it to create a virtualenv:

- First install 3.9.1 python version with pyenv:

`pyenv install 3.9.1`

- Then create a virtualenv using that python version:

`pyenv virtualenv 3.9.1 tv-and-film-buff-env`

where tv-and-film-buff-env is the virtualenv name we gave

You should see a virtualenv named `tv-and-film-buff-env` listed if you run the command:

`pyenv virtualenvs`

- and then to activate it:

`pyenv activate tv-and-film-buff-env`

- and to install dependencies

`pip3 install -r requirements.txt`

When you are done you can deactivate your virtualenv:

`pyenv deactivate`

ALTERNATIVELY If you don't have pyenv installed you can setup a virtualenv using virtualenv like so:

If you don't have virtualenv you can install it with:

`pip3 install virtualenv`

`python3 -m venv tv-and-film-buff-env`

where `tv-and-film-buff-env` the environment name

`source tv-and-film-buff-env/bin/activate`

`pip3 install -r requirements.txt`

When you are done you can deactivate your virtualenv:

`deactivate`

**TO RUN THE APP**

After you have successfully finished setting up you will need to create a .env file and add the token like so:

`API_KEY=*****`

First run the migration:

`python3 manage.py migrate`

and then to add data in the database login to the shell:

`python3 manage.py shell_plus` - This creates a shell with models already imported as opposed to `python3 manage.py shell`

and then

```
s = Series.objects.create(title="Game of Thrones", total_seasons=8, series_id="tt0944947")
Episodes.objects.create(
    title="Winter Is Coming",
    plot="Eddard Stark is torn between his family and an old friend when asked to serve at the side of King Robert Baratheon; Viserys plans to wed his sister to a nomadic warlord in exchange for an army.",
    episode_number=1,
    season_number=1,
    genre="Action, Adventure, Drama",
    language="English",
    imdbRating=9.0,
    imdbID="tt1480055",
    poster="https://m.media-amazon.com/images/M/MV5BOTYwZDNlMDMtZWRkNC00NzNkLTk2ZDMtNGQ1MmEwNzAwZGZhXkEyXkFqcGdeQXVyMjg2MTMyNTM@._V1_SX300.jpg",
    series=s
)
Episodes.objects.create(
    title="The Kingsroad",
    plot="While Bran recovers from his fall, Ned takes only his daughters to King's Landing. Jon Snow goes with his uncle Benjen to the Wall. Tyrion joins them.",
    episode_number=2,
    season_number=1,
    genre="Action, Adventure, Drama",
    language="English",
    imdbRating=8.0,
    imdbID="tt1668746",
    poster="https://m.media-amazon.com/images/M/MV5BMTQyMjMzMDIxOV5BMl5BanBnXkFtZTcwODU2ODg5NA@@._V1_SX300.jpg",
    series=s
)
```

or ` python3 manage.py dbshell` if you prefer running raw SQL commands

Then to run the app:

`python3 manage.py runserver`

and open

`localhost:8000/episodes` in your browser

then to view only one episode:

`localhost:8000/episodes/tt1668746` where `tt1668746` is imdbID

**TO RUN THE TESTS**

And then to run the tests with a coverage report running the following command:
`pytest tests`

or for including coverage report

`pytest --cov=tv_and_film_buffAPI tests/`

or

`pytest --cov-report term-missing --cov=tv_and_film_buffAPI tests`

You will need to set `export DJANGO_SETTINGS_MODULE=tv_and_film_buffAPI.config.settings`
directly pasting in your terminal, or adding it to .env and loading from there

If you get an error:
`E django.core.exceptions.ImproperlyConfigured. Requested setting ... but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.`

it's because that variable isn't set properly in your terminal where you are running the tests

### Some notes about plans for the future:

As a user I would like to:

- browse series options and add my favourite series to my account
- browse film options and add my favourite films to my account
- get a notification for when an episode has been added to one of my series
- get recommendations from similar users for what to watch
- filter for various things such as imdbRatings
- add comments on each episode
- e.t.c

There are various TODOS left in the code for things I would like to change and I have left notes, such as

- refactor the ingest_data.py script into a service, and
- create appropriate asynchronous tasks (such as ones that would check whether
  there is a new episode for the series the user has selected)
- Move to postgres
- Deploy to ECS and re-architecting some bits into AWS technologies
- A user interface could be fun to build for this app

Ideas are very welcome!
