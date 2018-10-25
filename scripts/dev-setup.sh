# This script installs and sets up all needed dependencies 
# for a newly cloned project.
# The script has been tested on Ubuntu 18.04


# Install required system packages.
sudo apt-get install libpq-dev python3-dev


# Install virtualenv
pip install virtualenv
virtualenv -p python3 venv

# Run reset script
./scripts/dev-reset.sh