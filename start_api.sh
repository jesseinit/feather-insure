#!/bin/bash

# source venv/bin/activate
source .env

while ! nc -z feather-db 5432; do echo 'Waiting for Postgres Database Startup' & sleep 1; done;

echo "<<<<<<<<<< Running Migrations >>>>>>>>>>"
python manage.py db migrate
python manage.py db upgrade
echo "<<<<<<<<<< Migrations Completed >>>>>>>>>>"

echo "<<<<<<<<<< Starting Server>>>>>>>>>>"
gunicorn wsgi:application -b 0.0.0.0:5000 --workers=2 --access-logfile -
