from flask import Blueprint, request, jsonify, send_file
from settings import MONGO_DB
from settings import RET
from settings import VOICE_PATH
from bson import ObjectId
import os

friend = Blueprint("friend", __name__)


@friend.route("/friend_list", methods=["POST"])
def friend_list():
    user_id = request.form.get("user_id")
    user_info = MONGO_DB.users.find_one({"_id": ObjectId(user_id)})
    
    friends = user_info.get("friend_list")
    
    RET["code"] = 0
    RET["msg"] = "好友列表查询"
    RET["data"] = friends
    
    return jsonify(RET)


@friend.route("/add_req", methods=["POST"])
def add_req():
    req_info = request.form.to_dict()
    print(req_info)
    if req_info.get("type") == "app":
        user_info = MONGO_DB.users.find_one({"_id": ObjectId(req_info.get("user_id"))})
    else:
        user_info = MONGO_DB.toys.find_one({"_id": ObjectId(req_info.get("user_id"))})
    
    req_info["avatar"] = user_info.get("avatar")
    req_info["name"] = user_info.get("nickname") if user_info.get("nickname") else user_info.get("babyname")
    
    MONGO_DB.request.insert_one(req_info)
    
    RET["code"] = 0
    RET["msg"] = "添加请求成功"
    RET["data"] = {}
    
    return jsonify(RET)


@friend.route("/req_list", methods=["POST"])
def req_list():
    user_id = request.form.get("user_id")
    user_info = MONGO_DB.users.find_one({"_id": ObjectId(user_id)})
    bind_toy = user_info.get("bind_toys")
    
    req_liebiao = list(MONGO_DB.request.find({"toy_id": {"$in": bind_toy}}))
    
    for index, req in enumerate(req_liebiao):
        req_liebiao[index]["_id"] = str(req.get("_id"))
    
    RET["code"] = 0
    RET["msg"] = "请求列表"
    RET["data"] = req_liebiao
    
    return jsonify(RET)


@friend.route("/acc_req", methods=["POST"])
def acc_req():
    req_id = request.form.get("req_id")
    remark = request.form.get("remark")
    req_info = MONGO_DB.request.find_one({"_id": ObjectId(req_id)})
    toy_id = req_info.get("toy_id")
    
    user_id = req_info.get("user_id")
    if req_info.get("type") == "app":
        user_info = MONGO_DB.users.find_one({"_id": ObjectId(user_id)})
    else:
        user_info = MONGO_DB.toys.find_one({"_id": ObjectId(user_id)})
    
    chat_window = MONGO_DB.chats.insert_one({"user_list": [user_id, toy_id], "chat_list": []})

    toy_info = MONGO_DB.toys.find_one({"_id": ObjectId(toy_id)})

    u_add_t = {
        "friend_id": str(toy_info.get("_id")),
        "friend_name": toy_info.get("babyname"),
        "friend_avatar": toy_info.get("avatar"),
        "friend_remark": req_info.get("remark"),
        "friend_chat": str(chat_window.inserted_id),
        "friend_type": "toy"
    }
    
    user_info["friend_list"].append(u_add_t)
    
    if req_info.get("type") == "app":
        MONGO_DB.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_info})
    else:
        MONGO_DB.toys.update_one({"_id": ObjectId(user_id)}, {"$set": user_info})

    t_add_u = {
        "friend_id": str(user_info.get("_id")),
        "friend_name": user_info.get("nickname") if user_info.get("nickname") else user_info.get("babyname"),
        "friend_avatar": user_info.get("avatar"),
        "friend_remark": remark,
        "friend_chat": str(chat_window.inserted_id),
        "friend_type": "app" if user_info.get("nickname") else "toy"
    }
    
    toy_info["friend_list"].append(t_add_u)
    
    MONGO_DB.toys.update_one({"_id": ObjectId(toy_id)}, {"$set": toy_info})

    MONGO_DB.request.update_one({"_id": ObjectId(req_id)}, {"$set": {"status": 1}})
    
    RET["code"] = 0
    RET["msg"] = "添加好友成功"
    RET["data"] = {}
    
    return jsonify(RET)


@friend.route("/ref_req", methods=["POST"])
def ref_req():
    req_id = request.form.get("req_id")
    MONGO_DB.request.update_one({"_id": ObjectId(req_id)}, {"$set": {"status": 2}})
    
    RET["code"] = 0
    RET["msg"] = "拒绝请求"
    RET["data"] = {}
    
    return jsonify(RET)
