# tasks.py
from celery import shared_task

@shared_task
def print_task_name(name):
    print(f"New task created: {name}")
    return name
