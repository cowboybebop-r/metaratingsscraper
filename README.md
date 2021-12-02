1. Migrate database and create super user:

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

2. Run the server:

```
python3 manage.py runserver
```

3. Run Celery:

```
celery -A main.tasks worker --loglevel=INFO
```
