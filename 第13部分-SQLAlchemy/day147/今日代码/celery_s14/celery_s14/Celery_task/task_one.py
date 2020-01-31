from Celery_task.celery import my_task
import time,requests,os
from uuid import uuid4

@my_task.task
def xiaopapaerge(item):
    time.sleep(1)
    content_id = item.split("/")[-1]
    print(content_id)
    content_dict = requests.get("http://m.ximalaya.com/tracks/%s.json" % (content_id))
    print(content_dict)
    #
    # # 获取音频内容
    # play_path = content_dict.get("play_path")
    # music = requests.get(play_path).content
    # music_name = f"{uuid4()}.mp3"
    # music_path = os.path.join(music_name)
    # with open(music_path, "wb") as mf:
    #     mf.write(music)
    #
    # # 获取图片内容
    # cover_url = content_dict.get("cover_url")
    # cover = requests.get(cover_url).content
    # cover_name = f"{uuid4()}.jpg"
    # cover_path = os.path.join(cover_name)
    # with open(cover_path, "wb") as cf:
    #     cf.write(cover)

@my_task.task
def run_time():
    time.sleep(2)
    return "运行完成"


# start = time.time()
# xiaopapaerge(content_id_erge_list)
# end = time.time() - start
#
# print(end)