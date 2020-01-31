from Celery_task.task_one import run_time,xiaopapaerge

# for i in range(6):
#     run_time.delay()

# import requests

content_id_erge_list = ["/ertong/424529/7713675",
                   "/ertong/424529/7713660",
                   "/ertong/424529/7713647",
                   "/ertong/424529/7713577",
                   "/ertong/424529/7713571",
                   "/ertong/424529/7713544"]
#
for item in content_id_erge_list:
    res = xiaopapaerge.delay(item)