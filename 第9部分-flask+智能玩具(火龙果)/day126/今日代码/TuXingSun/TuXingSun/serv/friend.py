from flask import Blueprint,request,jsonify,send_file
from settings import MONGO_DB
from settings import RET
from settings import VOICE_PATH
from bson import ObjectId
import os

friend = Blueprint("friend",__name__)

@friend.route("/friend_list", methods=["POST"])
def friend_list():
    user_id = request.form.get("user_id")
    user_info = MONGO_DB.users.find_one({"_id":ObjectId(user_id)})
    
    friends = user_info.get("friend_list")
    
    RET["code"] = 0
    RET["msg"] = "好友列表查询"
    RET["data"] = friends
    
    return jsonify(RET)