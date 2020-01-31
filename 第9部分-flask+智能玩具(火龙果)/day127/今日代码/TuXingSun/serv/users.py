from flask import Blueprint,request,jsonify
from settings import MONGO_DB
from settings import RET
from bson import ObjectId

users = Blueprint("users",__name__)

@users.route("/login",methods=["POST"])
def login():
    login_form = request.form.to_dict()
    user_info = MONGO_DB.users.find_one(login_form,{"pwd":0})
    if not user_info:
        RET["code"] = 1
        RET["msg"] = "用户名密码错误"
        RET["data"] = []
        return jsonify(RET)
    
    user_info["_id"] = str(user_info.get("_id"))
    RET["code"] = 0
    RET["msg"] = "登陆成功"
    RET["data"] = user_info
    
    return jsonify(RET)

@users.route("/reg",methods=["POST"])
def reg():
    reg_form = request.form.to_dict()
    reg_form["avatar"] ="mama.jpg" if reg_form.get("gender") == "1" else "baba.jpg"
    reg_form["bind_toys"] = []
    reg_form["friend_list"] = []
    
    user_res = MONGO_DB.users.insert_one(reg_form)
    user_id = user_res.inserted_id

    RET["code"] = 0
    RET["msg"] = "注册成功"
    RET["data"] = {"user_id":str(user_id)}
    
    return jsonify(RET)


@users.route("/auto_login", methods=["POST"])
def auto_login():
    login_form = request.form.to_dict()
    print(login_form)
    login_form["_id"] = ObjectId(login_form.get("_id"))
    user_info = MONGO_DB.users.find_one(login_form, {"pwd": 0})
    user_info["_id"] = str(user_info.get("_id"))
    RET["code"] = 0
    RET["msg"] = "登陆成功"
    RET["data"] = user_info
    
    return jsonify(RET)


