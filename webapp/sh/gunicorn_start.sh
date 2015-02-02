#!/bin/bash

NAME="rack_webapp"                                  # Name of the application
DJANGODIR=/webapps/rack_webapp/src/             # Django project directory
SOCKFILE=/webapps/venvs/rack_webapp/run/gunicorn.sock  # we will communicte using this unix socket
USER=antenna                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=settings.defaults             # which settings file should Django use
DJANGO_WSGI_MODULE=wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /webapps/venvs/rack_webapp/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

cd /webapps/rack_webapp/src
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /webapps/venvs/rack_webapp/bin/gunicorn\
    ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-