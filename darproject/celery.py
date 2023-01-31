import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'darproject.settings')

app = Celery('darproject', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

