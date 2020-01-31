from celery import Celery
my_task = Celery("task",
                 broker="redis://127.0.0.1:6379",
                 backend="redis://127.0.0.1:6379",
                 include=["Celery_task.task_one"])
