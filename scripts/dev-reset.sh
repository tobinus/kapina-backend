# This resets the current environment to a fresh database state,
# with all new dependency and static files collected. 
# The script has been tested on Ubuntu 18.04


# Activate virtual environemnt
source venv/bin/activate


# Install python requirements
pip install -r requirements.txt


# Setup Django 
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata data_models/fixtures/beta_fixtures.json