from flask import Blueprint,request,jsonify,send_file
from serv import get_set_anthing
from settings import MONGO_DB
from settings import RET
from settings import VOICE_PATH
from bson import ObjectId
import os

chats = Blueprint("chats",__name__)

@chats.route("/recv_chat",methods=["POST"])
def recv_chat():
    toy_id = request.form.get("toy_id")
    user_id = request.form.get("user_id")
    user_list = [toy_id, user_id]
    
    # count = 3 [app,self,app]
    recv_count = get_set_anthing.redis_get_one(toy_id,user_id)
    recv_list = []

    chat_window = MONGO_DB.chats.find_one({"user_list": {"$all": user_list}})
    for chat in reversed(chat_window.get("chat_list")):
        if chat.get("sender") != toy_id:
            recv_list.append(chat)
        if len(recv_list) >= recv_count:
            break
    
    # [1,2,3,4,5,6,7]
    # [7,6,5,4,3,2,1]
    # [7,5,3]
    
    # chat_content = chat_window.get("chat_list")[-recv_count:]
    # {sender:"form_user",recv:"to_user",content:"yinpinming.mp3"}
    
    return jsonify(recv_list)# [7,5,3]

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