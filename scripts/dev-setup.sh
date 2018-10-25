#!/bin/bash

# This script installs and sets up all needed dependencies 
# for a newly cloned project.
# The script has been tested on Ubuntu 16.04 and 18.04


# Install required system packages.
sudo apt-get install python3 python3-pip libpq-dev python3-dev



# Install virtualenv
pip3 install virtualenv
virtualenv -p python3 venv

# Run reset script
./scripts/dev-reset.sh
