import time

from celery import Celery

celery_app = Celery(
    "worker",
    backend="redis://redis:6379/0",
    broker="redis://redis:6379/0"
)

celery_app.autodiscover_tasks(packages=['src.tasks.add'])


@celery_app.task
def add(a: int, b: int):
    # this time to simulate a long running task
    time.sleep(30)
    return a + b
