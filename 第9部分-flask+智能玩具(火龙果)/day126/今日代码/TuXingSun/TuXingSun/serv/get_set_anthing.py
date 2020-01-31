from flask import Blueprint,request,send_file,jsonify
from settings import MONGO_DB,RET
from settings import MUSIC_PATH
from settings import IMAGE_PATH
from settings import VOICE_PATH
from settings import CHAT_PATH
import os

gsanthing = Blueprint("gsanthing",__name__)

@gsanthing.route("/get_audio/<filename>")
def get_audio(filename):
    file_path = os.path.join(MUSIC_PATH,filename)
    return send_file(file_path)

@gsanthing.route("/get_image/<filename>")
def get_image(filename):
    file_path = os.path.join(IMAGE_PATH,filename)
    return send_file(file_path)

@gsanthing.route("/get_voice/<filename>")
def get_voice(filename):
    file_path = os.path.join(VOICE_PATH,filename)
    return send_file(file_path)

@gsanthing.route("/get_chat/<filename>")
def get_chat(filename):
    file_path = os.path.join(CHAT_PATH,filename)
    return send_file(file_path)


@gsanthing.route("/app_upload",methods=["POST"])
def app_upload():
    to_user = request.form.get("to_user")
    from_user = request.form.get("from_user")
    user_list = [to_user,from_user]
    
    chat_window = MONGO_DB.chats.find_one({"user_list":{"$all":user_list}})
    
    file = request.files.get("reco")
    file_path = os.path.join(CHAT_PATH,file.filename)
    file.save(file_path)
    os.system(f"ffmpeg -i {file_path} {file_path}.mp3")
    
    chat_window["chat_list"].append({
        "sender":from_user,
        "recv":to_user,
        "content":f"{file.filename}.mp3"
    })
    
    MONGO_DB.chats.update_one({"user_list":{"$all":user_list}},{"$set":chat_window})
    

    RET["code"] = 0
    RET["msg"] = "上传语音消息"
    RET["data"] = {"file":f"{file.filename}.mp3"}
    
    return jsonify(RET)


@gsanthing.route("/toy_uploader", methods=["POST"])
def toy_uploader():
    file_name = request.form.get("file_name")
    file = request.files.get("record")
    file_path = os.path.join(CHAT_PATH, file_name)
    file.save(file_path)

    to_user = request.form.get("to_user")
    from_user = request.form.get("from_user")
    
    user_list = [to_user,from_user]
    
    
    chat_info = {
        "sender":from_user,
        "recv":to_user,
        "content":file_name
    }
    
    MONGO_DB.chats.update_one({"user_list":{"$all":user_list}},{"$push":{"chat_list":chat_info}})
    
    return jsonify({"file":file_name})