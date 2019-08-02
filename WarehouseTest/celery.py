import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WarehouseTest.settings')

app = Celery('WarehouseTest')
app.conf.task_routes = {'warehouse.tasks.*': {'queue': 'warehouse'}}
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
