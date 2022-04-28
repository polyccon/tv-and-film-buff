# tv-and-film-buff

__TO SETUP__

If you have pyenv installed (instructions for how to install pyenv here: https://github.com/pyenv/pyenv#installation) 
then you can use it to create a virtualenv:

First install 3.9.1 python version with pyenv:

`pyenv install 3.9.1`

Then create a virtualenv using that python version:

`pyenv virtualenv 3.9.1 tv-and-film-buff-env`

where applications-env is the virtualenv name we gave

You should see a virtualenv named `tv-and-film-buff-env` listed if you run the command:

`pyenv virtualenvs`

and then to activate it:

`pyenv activate tv-and-film-buff-env-3.9.1`

and to install dependencies

`pip3 install -r requirements.txt`

When you are done you can deactivate your virtualenv:

`pyenv deactivate`


ALTERNATIVELY, If you don't have pyenv installed you can setup a virtualenv using virtualenv like so:

If you don't have virtualenv you can install it with:

`pip3 install virtualenv`

`python3 -m venv tv-and-film-buff-env-env`

where `tv-and-film-buff-env-env` the environment name

`source tv-and-film-buff-env-env/bin/activate`

`pip3 install -r requirements.txt`

When you are done you can deactivate your virtualenv:

`deactivate`



__TO RUN THE APP__


After you have successfully finished setting up you will need to create a .env file and add the token like so:

`API_KEY=*****`

Then to run the app:

`python3 manage.py runserver`

and open 

`localhost:5000/episodes` in your browser



__TO RUN THE TESTS__

And then to run the tests with a coverage report running the following command:
`pytest tests`
 
 or for including coverage report

`pytest --cov=tv_and_film_buffAPI tests/` 

or

`pytest --cov-report term-missing --cov=tv_and_film_buffAPI tests`