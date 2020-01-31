# 数据库配置
import pymongo
client = pymongo.MongoClient(host="127.0.0.1",port=27017)
MONGO_DB = client["TuXingSunDB"]

from redis import Redis
REDIS_DB = Redis(host="127.0.0.1",port=6379,db=15)


# 目录配置
MUSIC_PATH = "Music"
IMAGE_PATH = "Image"
VOICE_PATH = "Voices"
CHAT_PATH = "Chats"

# RET配置
RET = {
    "code":0,
    "msg":"调用接口成功",
    "data":[]
}

# URL配置
LT_URL = "http://qr.liantu.com/api.php?text=%s"


# BaiduAI配置:
from aip import AipSpeech,AipNlp

APP_ID = '15217111'
API_KEY = 'jE38mGiHGGe8LnmK2YdbGGoX'
SECRET_KEY = 'KaoFdHZoaUWQsmpRgIEgxIGhdkDbW2V4'

SPEECH_CLIENT = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
NLP_CLIENT = AipNlp(APP_ID, API_KEY, SECRET_KEY)

VOICE = {
        "per": 4,
        "pit": 8,
        "spd": 4,
        'vol': 5,
    }