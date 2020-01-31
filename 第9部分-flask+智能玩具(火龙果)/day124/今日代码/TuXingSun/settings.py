# 数据库配置
import pymongo
client = pymongo.MongoClient(host="127.0.0.1",port=27017)
MONGO_DB = client["TuXingSunDB"]


# 目录配置
MUSIC_PATH = "Music"
IMAGE_PATH = "Image"

# RET配置
RET = {
    "code":0,
    "msg":"调用接口成功",
    "data":[]
}

# URL配置
LT_URL = "http://qr.liantu.com/api.php?text=%s"