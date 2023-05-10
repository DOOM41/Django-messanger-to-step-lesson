import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('messenger_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически найдите и импортируйте все файлы tasks.py в вашем проекте
app.autodiscover_tasks()