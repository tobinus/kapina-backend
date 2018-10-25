# This script installs and sets up all needed dependencies for a newly cloned project.
# The script has been tested on Ubuntu 18.04


# Install virtualenv requirements
sudo apt-get install libpq-dev python3-dev
pip install virtualenv
virtualenv -p python3 env
source env/bin/activate


# Install python requirements
pip install -r requirements.txt


# Setup Django 
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata data_models/fixtures/beta_fixtures.json