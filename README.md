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

Copy the nginx config:
```
TODO
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
```

### Virtualenvironment

```bash
pip install virtualenv
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

### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata data.json
```

### Setup Supervisor
```bash
mkdir -p /webapps/revolt_backend/logs/
touch /webapps/revolt-backend/logs/gunicorn_supervisor.log
supervisorctl reread
```

IF YOU GET AN ERROR (https://github.com/Supervisor/supervisor/issues/121):

```
service supervisor start
supervisorctl reload
supervisorctl update
```
