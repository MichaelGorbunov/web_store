from django.apps import AppConfig
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ADDED, EVENT_JOB_REMOVED, EVENT_JOB_EXECUTED

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

scheduler = BackgroundScheduler()

scheduler.start()

def job_listener(event):
    if event.exception:
        print(f'Job {event.job_id} failed.')
    else:
        print(f'Job {event.job_id} **.')
        print(f'Job {event} **.')

scheduler.add_listener(job_listener, EVENT_JOB_ADDED | EVENT_JOB_REMOVED | EVENT_JOB_EXECUTED)

