from flask import Blueprint,request,jsonify,send_file
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

    chat_window = MONGO_DB.chats.find_one({"user_list": {"$all": user_list}})
    chat_content = chat_window.get("chat_list")[-1]
    
    return jsonify(chat_content)

@chats.route("/chat_list",methods=["POST"])
def chat_list():
    chat_id = request.form.get("chat_id")
    chat_window = MONGO_DB.chats.find_one({"_id":ObjectId(chat_id)})
    
    RET["code"] = 0
    RET["msg"] = "查询消息"
    RET["data"] = chat_window.get("chat_list")
    
    return jsonify(RET)
    