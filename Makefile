PREFIX_COMPOSE           := \
	COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME} \
	${CI_COMPOSE_PREFIX} \
	docker-compose ${CI_COMPOSE_ARGS}
RUN_COMPOSE				 := ${PREFIX_COMPOSE} run --rm backend

## some tests in CI can run as docker run
DOCKER_RUN_TEST			 := docker run --rm ${DOCKER_IMAGE_LAYER_TEST}
SIMPLE_RUN_TEST          := $(if ${CI}, ${DOCKER_RUN_TEST}, ${RUN_COMPOSE})

help: ## Prints this help/overview message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-17s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

run: stop build up ## Builds all containers and (re)runs them in foreground.

restart: stop start ## Restarts all containers

build: ## Builds all containers
	${PREFIX_COMPOSE} build

build_no_cache: ## Builds all containers without cache
	${PREFIX_COMPOSE} build --no-cache

rebuild: down build start ## Fully rebuild containers

up: ## Starts all containers in foreground
	${PREFIX_COMPOSE} up

stop: ## Stops all containers
	${PREFIX_COMPOSE} stop

down: ## Fully stops containers, removing persistence
	${PREFIX_COMPOSE} down

clean: ## Cleans all build containers and images. Stops everything as well.
	${PREFIX_COMPOSE} down --volumes --rmi all || true
	rm -rf cover .mypy_cache .venv* .coverage

status: ## Shows status of all containers
	${PREFIX_COMPOSE} ps

test: ## Updates requirements, rules and runs all available tests locally.
	${RUN_COMPOSE} pytest ${USE_MULTIPLE_CORES} . ${TEST_PARAMS} -vv

test_coverage: ## Updates requirements, rules and runs all available tests locally with coverage information.
	${RUN_COMPOSE} pytest ${USE_MULTIPLE_CORES} --cov-report term-missing --cov=tv_and_film_buffAPI . ${TEST_PARAMS} -vv

format:
	${SIMPLE_RUN_TEST} black . --check

safety:
	${SIMPLE_RUN_TEST} safety check -r requirements.txt

logs: ## Follow the logs for the microservice
	${PREFIX_COMPOSE} logs -f ${CI_PROJECT_NAME}

sh: ## Follow the logs for the microservice
	${RUN_COMPOSE} /bin/bash

list_fixtures:
	${RUN_COMPOSE} pytest --fixtures

coverage: ## Runs unit test coverage test. Does not update requirements or rules.
	${RUN_COMPOSE} coverage report --skip-covered

manage:
	${RUN_COMPOSE} python manage.py ${MANAGE_CMD}

migrations: ## Make migrations in the local source against the built docker db from previous state
	${RUN_COMPOSE} python manage.py makemigrations

migrate:
	${RUN_COMPOSE} python manage.py migrate

psql: ## Enter the database backing service cli
	docker exec db psql -U postgres

populate_db:
	${RUN_COMPOSE} python manage.py populate_db

ingest_data:
	${RUN_COMPOSE} python manage.py ingest_data