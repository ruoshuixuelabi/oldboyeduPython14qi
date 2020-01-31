from flask import Blueprint,request,jsonify,send_file
from settings import MONGO_DB
from settings import RET
from settings import VOICE_PATH
from bson import ObjectId
import os

devices = Blueprint("devices",__name__)

@devices.route("/validate",methods=["POST"])
def validate():
    qrcode = request.form.get("qrcode")
    res = MONGO_DB.devices.find_one({"device_key":qrcode})
    if not res:
        RET["code"] = 2
        RET["msg"] = "二维码扫描错误，请扫描玩具二维码"
        RET["data"] = {}
        return jsonify(RET)
    else:
        toys = MONGO_DB.toys.find_one({"device_key":qrcode},{"friend_list":0})
        if toys:
            toys["_id"] = str(toys.get("_id"))
            RET["code"] = 1
            RET["msg"] = "添加好友流程"
            RET["data"] = toys
            return jsonify(RET)
            
        RET["code"] = 0
        RET["msg"] = "设备存在进入绑定流程"
        RET["data"] = {"device_key":qrcode}
        return jsonify(RET)


@devices.route("/bind_toy",methods=["POST"])
def bind_toy():
    bind_form = request.form.to_dict()
    bind_form["friend_list"]=[]
    bind_form["avatar"] = "toy.jpg"
    bind_form["bind_user"] = user_id = bind_form.pop("user_id")
    
    user_info = MONGO_DB.users.find_one({"_id":ObjectId(user_id)})
    
    chat = MONGO_DB.chats.insert_one({"user_list":[],"chat_list":[]})
    
    t2u_friend = {
        "friend_id":user_id,
        "friend_name":user_info.get("nickname"),
        "friend_avatar":user_info.get("avatar"),
        "friend_remark":bind_form.pop("remark"),
        "friend_chat":str(chat.inserted_id),
        "friend_type":"app"
    }

    bind_form["friend_list"].append(t2u_friend)
    
    toy = MONGO_DB.toys.insert_one(bind_form)
    toy_id = str(toy.inserted_id)
    
    u2t_friend={
        "friend_id":toy_id,
        "friend_name":bind_form.get("babyname"),
        "friend_avatar":bind_form.get("avatar"),
        "friend_remark":bind_form.get("toyname"),
        "friend_chat":str(chat.inserted_id),
        "friend_type": "toy"
    }
    
    user_info["bind_toys"].append(toy_id)
    user_info["friend_list"].append(u2t_friend)
    
    MONGO_DB.users.update_one({"_id":ObjectId(user_id)},{"$set":user_info})
    MONGO_DB.chats.update_one({"_id":chat.inserted_id},{"$set":{"user_list":[user_id,toy_id]}})
    
    RET["code"] = 0
    RET["msg"] = "绑定玩具成功"
    RET["data"] = {}
    
    return jsonify(RET)
    
    
@devices.route("/toy_list",methods=["POST"])
def toy_list():
    user_id = request.form.get("user_id")
    user_info = MONGO_DB.users.find_one({"_id":ObjectId(user_id)})
    bind_toy = user_info.get("bind_toys") # type:list
    
    for index,toy_id in enumerate(bind_toy):
        bind_toy[index] = ObjectId(toy_id) #[ObjectId(toy_id),ObjectId(toy_id)]
    
    toys = list(MONGO_DB.toys.find({"_id":{"$in":bind_toy}}))
    
    for index,toy_info in enumerate(toys):
        toys[index]["_id"] = str(toy_info.get("_id"))
    
    RET["code"] = 0
    RET["msg"] = "绑定玩具列表"
    RET["data"] = toys
    
    return jsonify(RET)
    
    
@devices.route("/toy_info",methods=["POST"])
def toy_info():
    toy_id = request.form.get("toy_id")
    toy = MONGO_DB.toys.find_one({"_id":ObjectId(toy_id)})
    toy["_id"] = str(toy.get("_id"))
    
    RET["code"] = 0
    RET["msg"] = "查询玩具"
    RET["data"] = toy
    
    return jsonify(RET)


@devices.route("/toy_login",methods=["POST"])
def toy_login():
    device_key = request.form.get("device_key")
    
    is_device = MONGO_DB.devices.find_one({"device_key":device_key})
    if is_device:
        is_bind = MONGO_DB.toys.find_one({"device_key":device_key})
        if is_bind:
            return jsonify({"music":"success.mp3","msg_type":"voices","toy_id":str(is_bind.get("_id"))})
        
        return jsonify({"music":"Nobind.mp3","msg_type":"voices"})
    
    return jsonify({"music":"Nolic.mp3","msg_type":"voices"})

    