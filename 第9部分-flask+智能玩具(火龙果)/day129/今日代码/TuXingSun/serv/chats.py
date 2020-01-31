from flask import Blueprint,request,jsonify,send_file
from serv import get_set_anthing
from settings import MONGO_DB
from settings import RET
from settings import VOICE_PATH
from baidu_aip import speech
from bson import ObjectId
import os

chats = Blueprint("chats",__name__)

@chats.route("/recv_chat",methods=["POST"])
def recv_chat():
    toy_id = request.form.get("toy_id")
    user_id = request.form.get("user_id")
    user_list = [toy_id, user_id]
    
    # count = 3 [app,self,app]
    recv_count,user_id2 = get_set_anthing.redis_get_one(toy_id,user_id)
    if user_id2:
        user_list = [toy_id, user_id2]
    recv_list = []

    chat_window = MONGO_DB.chats.find_one({"user_list": {"$all": user_list}})
    for chat in reversed(chat_window.get("chat_list")):
        if chat.get("sender") != toy_id:
            recv_list.append(chat)
        if len(recv_list) >= recv_count:
            break
    xxtx = speech.get_remark(toy_id, user_id2)
    recv_list.append({"sender":user_id2,"recv":toy_id,"content":xxtx})
    return jsonify(recv_list)#: [7,5,3,{content:"你有来自xxx的消息"}]

@chats.route("/chat_list",methods=["POST"])
def chat_list():
    chat_id = request.form.get("chat_id")
    to_user = request.form.get("user_id")
    from_user = request.form.get("toy_id")
    
    get_set_anthing.redis_get_one(to_user,from_user)

    chat_window = MONGO_DB.chats.find_one({"_id":ObjectId(chat_id)})
    
    RET["code"] = 0
    RET["msg"] = "查询消息"
    RET["data"] = chat_window.get("chat_list")
    
    return jsonify(RET)

@chats.route("/get_msg_count",methods=["POST"])
def get_msg_count():
    user_id = request.form.get("user_id")
    user_msg = get_set_anthing.redis_get_count(user_id)
    
    RET["code"] = 0
    RET["msg"] = "未读消息查询"
    RET["data"] = user_msg
    
    return jsonify(RET)