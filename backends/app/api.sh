#!/bin/sh

until python3 manage.py makemigrations
do
    echo "Waiting for db to be ready..."
    sleep 3
done


until python3 manage.py migrate
do
    sleep 3
done

until python3 manage.py collectstatic --noinput
do
    sleep 3
done





gunicorn app.wsgi --bind 0.0.0.0:8000 --workers 3 --threads 3