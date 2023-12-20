#!/bin/sh

# start the app

python manage.py migrate &&
python manage.py collectstatic --no-input &&
python manage.py runserver 0.0.0.0:8000
# gunicorn config.wsgi -b 0.0.0.0:8000 --keep-alive 2 --timeout 120 --workers 5 --worker-class gevent
