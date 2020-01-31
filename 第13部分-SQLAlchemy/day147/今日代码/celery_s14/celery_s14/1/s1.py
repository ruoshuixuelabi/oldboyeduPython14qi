# Celery - 异步任务 定时任务 周期任务
# Celery - 基于Python实现的一个三方组件
# Celery 组成结构
#   1.app 应用 任务
#   2.缓存 存放任务的 Broker - Backend 缓存任务和缓存任务结果 redis or RabbitMQ
#   3.工人 Worker 执行任务
import time
from celery import Celery
my_task = Celery("task",broker="redis://127.0.0.1:6379",backend="redis://127.0.0.1:6379")

@my_task.task
def my_func1(a,b,ti):
    time.sleep(ti)
    return a+b

@my_task.task
def my_func2(a,b,c):
    return a+b+c