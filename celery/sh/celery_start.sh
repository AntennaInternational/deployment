#!/bin/bash

DJANGODIR=/webapps/rack-webapp/src/             # Django project directory
USER=antenna                                        # the user to run as
GROUP=webapps                                     # the group to run as
DJANGO_SETTINGS_MODULE=settings.defaults             # which settings file should Django use
DJANGO_WSGI_MODULE=wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /webapps/venvs/rack_webapp/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

exec /webapps/venvs/rack_webapp/bin/celery worker --app=celery_app -l info --concurrency=10 -B