from settings import SPEECH_CLIENT,NLP_CLIENT,CHAT_PATH,VOICE,MONGO_DB
from uuid import uuid4
from bson import ObjectId
import os

def audio2text():
    pass

def text2audio(text):
    res = SPEECH_CLIENT.synthesis(text,"zh",1,VOICE)
    file_name = f"{uuid4()}.mp3"
    file_path = os.path.join(CHAT_PATH,file_name)
    with open(file_path,"wb") as f:
        f.write(res)
        
    return file_name

def get_remark(to_user,from_user):
    toy_info = MONGO_DB.toys.find_one({"_id":ObjectId(to_user)})
    friend_list = toy_info.get("friend_list")
    for friend in friend_list:
        if friend.get("friend_id") == from_user:
            return text2audio(f'你有来自{friend.get("friend_remark")}的消息')
    