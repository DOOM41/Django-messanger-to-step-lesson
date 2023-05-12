# Python
from os import environ

# Third party
from celery import Celery
from celery.schedules import crontab

# Django
from django.conf import settings


environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'settings.base'
)
app: Celery = Celery(
    'settings',
    broker=settings.CELERY_BROKER_URL,
    # include=(
    #     'auths.tasks',                  # For the future.
    # )
)
app.config_from_object(
    'django.conf:settings', namespace='CELERY'
)
app.autodiscover_tasks(
    lambda: settings.PROJECTS_APPS
)


# @app.task                  # test tasks
# def add(x, y):
#     return x / y  

app.conf.timezone = settings.TIME_ZONE
