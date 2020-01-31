from celery.result import AsyncResult
from s1 import my_task

# 异步获取任务返回值
async_task = AsyncResult(id="31ec65e8-3995-4ee1-b3a8-1528400afd5a",app=my_task)

# 判断异步任务是否执行成功
if async_task.successful():
    #获取异步任务的返回值
    result = async_task.get()
    print(result)
else:
    print("任务还未执行完成")