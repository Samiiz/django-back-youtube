#!/bin/sh

set -e

python3 manage.py wait_for_db
python3 manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi