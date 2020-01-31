from s1 import my_func1
import time,datetime

now_time = time.time()
utc_now = datetime.datetime.utcfromtimestamp(now_time)
add_time = datetime.timedelta(days=1)

action_time = utc_now + add_time

res = my_func1.apply_async(args=(),eta=action_time)
print(res)