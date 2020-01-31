from settings import SPEECH_CLIENT,NLP_CLIENT,CHAT_PATH,VOICE,MONGO_DB
from uuid import uuid4
from bson import ObjectId
import os
from baidu_aip.goto_tuling import tl

def get_file_content(filePath):
    print("我正在将wav转换成pcm")
    os.system(f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()


def audio2text(filename):
    res = SPEECH_CLIENT.asr(get_file_content(filename), 'pcm', 16000, {
        'dev_pid': 1536,
    })
    print("我正在将pcm发送给百度转换成文字")
    return res.get("result")[0]


def text2audio(text):
    print(text, "图灵处理的结果")
    res = SPEECH_CLIENT.synthesis(text,"zh",1,VOICE)
    file_name = f"{uuid4()}.mp3"
    file_path = os.path.join(CHAT_PATH,file_name)
    with open(file_path,"wb") as f:
        f.write(res)
    
    print("百度将文字合成语音")
    return file_name

def get_remark(to_user,from_user):
    toy_info = MONGO_DB.toys.find_one({"_id":ObjectId(to_user)})
    friend_list = toy_info.get("friend_list")
    for friend in friend_list:
        if friend.get("friend_id") == from_user:
            return text2audio(f'你有来自{friend.get("friend_remark")}的消息')


def my_nlp_lowb(Q,toy_id): # Q = 我想听小毛驴
    print(Q, "我正在进行思考My_nlp")
    if "我想听" in Q or "我要听" in Q or "播放" in Q or "来一首" in Q:
        content_list = list(MONGO_DB.content.find({}))
        for content in content_list:
            if content.get("title") in Q:
                return {"music":content.get("audio")} # 我还不知道

    # 我想给爸爸发消息 给爸爸发消息 我想和爸爸聊聊天
    if "发消息" in Q :
        toy_info = MONGO_DB.toys.find_one({"_id":ObjectId(toy_id)})
        for friend in toy_info.get("friend_list"):
            if friend.get("friend_remark") in Q or friend.get("friend_name") in Q:
                filename = text2audio(f'可以给{friend.get("friend_remark")}发消息了')
                return {"chat":filename,"from_user":friend.get("friend_id"),"user_type":friend.get("friend_type")}
    
    
    
    print(Q, "我自己看来是不行了,给图灵吧")
    filename = text2audio(tl(Q,toy_id))
    print(filename,"这个文件给玩具")
    return {"chat":filename,"from_user":"ai"}
    