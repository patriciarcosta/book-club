# members/tasks.py
from celery import shared_task


@shared_task
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"
