# revolt-backend
Backend for radiorevolt.no

## Setup - Development

### Virtualenv

```bash
pip install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
sudo apt-get install libpq-dev python3-dev
pip install psycopg2
```

### Change settings

```bash
cp app/settings_example.py app/settings.py
```
Change the `app/settings.py` file: (This will probably be changed later)

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
```

### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata chimera_import_script/data.json
```

### Start the development server
```bash
python manage.py runserver
```

## Setup - Deployment

### Nginx

```bash
apt-get install nginx
```

Copy the nginx config (Updated as of 12/02/2017) to /etc/nginx/sites-available/radiorevolt.conf:
```
server {

  listen 80;
  # Type your domain name below
  server_name radiorevolt.no www.radiorevolt.no beta.radiorevolt.no;

  root /var/www;
  index index.html;
    
# Always serve index.html for any request
  location / {
    try_files $uri $uri/ /index.html;
    allow all;
  }
  location /static/ {
      alias   /var/www/static/;
  }
  
  location /media/ {
      alias   /var/www/media/;
  }
  location ~ /.well-known {
        allow all;
  }	
##
# If you want to use Node/Rails/etc. API server
# on the same port (443) config Nginx as a reverse proxy.
# For security reasons use a firewall like ufw in Ubuntu
# and deny port 3000/tcp.
##

   location /staging/api {
    proxy_pass http://localhost:9000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }

  location /graphql {
    proxy_pass http://localhost:8000/graphql;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /admin/ {
    proxy_pass http://localhost:8000/admin/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /graphiql {
    proxy_pass http://localhost:8000/graphiql;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /grappelli {
    proxy_pass http://localhost:8000/grappelli;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /summernote/ {
    proxy_pass http://localhost:8000/summernote/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }
}
```
Enable the config by creating a symlink in /etc/nginx/sites-enabled:
```bash
sudo ln -s /etc/nginx/sites-available/radiorevolt.conf /etc/nginx/sites-enabled/radiorevolt.conf
```

If the server is only listening to IPv6 addresses replace this line:
```
listen 80;
```
With this line:
```
listen [::]:80 default ipv6only=on;
```


### Clone repo

```bash
mkdir /webapps
cd /webapps
git clone https://github.com/Studentmediene/revolt-backend.git
```

### Install PostgreSQL

```
sudo apt-get install postgresql postgresql-contrib
su - postgres
createuser --interactive -P
```

```
Enter name of role to add: revolt-backend
Enter password for new role: **********
Enter it again: (Ask your closest project leader for this)
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n
```

```bash
createdb --owner revolt-backend radiorevolt
\q
exit
```

### Create an application user

```bash
groupadd --system webapps
useradd --system --gid webapps --shell /bin/bash --home /webapps/revolt-backend revoltbackend
chown -R revoltbackend: /webapps/revolt-backend
```

### Virtualenvironment

```bash
cd /webapps/revolt-backend/
sudo apt-get install python3-pip
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
sudo apt-get install libpq-dev python3-dev
pip install psycopg2
pip install gunicorn
pip install setproctitle
sudo apt-get install supervisor
```

Copy data dump:
```bash
sudo cp chimera_import_script/data.json /webapps/revolt-backend/
```


### Change settings
```bash
cp app/settings_example.py app/settings.py
```

Change the URLs in `app/settings.py` file:

```python
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/media/'
```

Change the timezone:

```python
TIME_ZONE = 'CET'
```
And the database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'radiorevolt',
        'USER': 'revolt-backend',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
If the server is running IPv6, change the following as well:
```python
'HOST': '127.0.0.1',
```
### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata data.json
```

### Setup Gunicorn
Copy the Gunicorn config to /webapps/revolt-backend/gunicorn_start:
```
#!/bin/bash

NAME="revolt-backend"                               # Name of the application
DJANGODIR=/webapps/revolt-backend                   # Django project directory
SOCKFILE=/webapps/revolt-backend/run/gunicorn.sock  # we will communicate using this unix socket
USER=revoltbackend                                  # the user to run as
GROUP=webapps                                       # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=app.settings               # which settings file should Django use
DJANGO_WSGI_MODULE=app.wsgi                       # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
#  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```
Make the file exectuable:
```bash
chmod +x /webapps/revolt-backend/gunicorn_start
```


### Setup Supervisor
Copy the Supervisor config to /etc/supervisor/conf.d/revolt-backend.conf:
```
[program:revolt-backend]
command =sh /webapps/revolt-backend/gunicorn_start
user = revoltbackend
stdout_logfile = /webapps/revolt-backend/logs/gunicorn_supervisor.log
redirect_stderr = true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
```
Enable Supervisor:
```
sudo systemctl enable supervisor.service
```
Create log file and restart Supervisor:
```bash
mkdir -p /webapps/revolt-backend/logs/
touch /webapps/revolt-backend/logs/gunicorn_supervisor.log
supervisorctl reread
```

IF YOU GET AN ERROR (https://github.com/Supervisor/supervisor/issues/121):

```
service supervisor start
supervisorctl reload
supervisorctl update
```
