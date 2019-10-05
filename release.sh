#!/bin/bash -f

# run release scripts when releasing the app

python manage.py makemigrations
python manage.py migrate
