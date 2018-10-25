# revolt-backend
[![Build Status](https://travis-ci.org/Studentmediene/kapina-backend.svg?branch=dev)](https://travis-ci.org/Studentmediene/kapina-backend)
[![Test Coverage](https://api.codeclimate.com/v1/badges/00e9c6201d2821d81f79/test_coverage)](https://codeclimate.com/github/Studentmediene/kapina-backend/test_coverage)

Backend for radiorevolt.no

## Environment settings

Settings are read from environment variables.
By default settings are configured for development and should just work, but some changes are required in production. 

|Name|Default|Description|
|:---|:------|:----------|
|REVOLT_DEBUG|True|Enable Django debug. Set to false in production|
|REVOLT_ALLOWED_HOSTS|(Empty)|Hosts allowed to access webserver. e.g. 'radiorevolt.no'|
|DATABASE_URL|(BASE_DIR)/db.sqlite3|[See dj-database-url](https://github.com/kennethreitz/dj-database-url#url-schema)
|REVOLT_STATIC_ROOT|(BASE_DIR)/staticfiles|Folder where static files are located|
|REVOLT_MEDIA_ROOT|(BASE_DIR)/mediafiles|Files where uploaded media is located|
|REVOLT_SECRET_KEY|replace_this_secret_key|[See Django SECRET_KEY](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-SECRET_KEY). **It is important that this is changed in production.**
|REVOLT_RAVEN_DSN|(Empty)|Sentry DSN using this format: https://user:pass@sentry.io/project|


## Setup - Development

Run the following command:
```bash
. scripts/setup-dev.sh
```
### Change settings

The default settings provided should work fine for development, but if any changes are needed a tool like [direnv](https://direnv.net/) is recommended for handling environment variables. 

### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata data_models/fixtures/beta_fixtures.json
```

### Start the development server
```bash
python manage.py runserver
```

### Testing and linting
We use `pytest`, `isort` and `flake8`  to test and lint the project.
Run the commands before commiting:
```bash
flake8 api_graphql app data_models
yapf -pir api_graphql app data_models -e '**/migrations' -e '**/snapshots'
isort -rc api_graphql app data_models
pytest
```

## Deployment

Check out the deployment guide at [our wiki](https://confluence.smint.no/display/IT/Deployment).
