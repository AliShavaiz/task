# mainCelery.py
# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelteqTask.settings')
# ('DJANGO_SETTINGS_MODULE', 'SelteqTask.settings')

app = Celery('SelteqTask')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# @app.task
# def add(name):
#     sleep(5)
#     return name + 1

# @app.task(bind=True,ignore_result=True)
# def debug_task(self):
#     print(f'request : {self.request!r}')