# book_club/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_club.settings")
app = Celery("book_club")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
