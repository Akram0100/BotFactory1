web: gunicorn main:app
worker: celery -A celery_app.celery worker --loglevel=info
beat: celery -A celery_app.celery beat --loglevel=info
scheduler: python scheduler.py