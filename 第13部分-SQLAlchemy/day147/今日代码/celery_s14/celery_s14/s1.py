from celery import Celery
from celery.schedules import crontab
my_task = Celery("task",
                 broker="redis://127.0.0.1:6379",
                 backend="redis://127.0.0.1:6379")

@my_task.task
def my_func1():
    return "my_func1 - 完成周期任务"

@my_task.task
def my_func2(a,b):
    return f"my_func2 {a}{b} - 完成周期任务"

my_task.conf.beat_schedule={
    "each10s_task":{
        "task":"s1.my_func1",
        "schedule":10, # 每10秒钟执行一次
        # "args":(10,10)
    },
    "each5s_task": {
        "task": "s1.my_func2",
        "schedule": 5, # 每一分钟执行一次
        "args": (20, 30)
    },
}

