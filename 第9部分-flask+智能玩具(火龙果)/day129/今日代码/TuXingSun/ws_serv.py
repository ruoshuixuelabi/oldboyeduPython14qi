from flask import Flask,request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket
from baidu_aip import speech
import json

ws = Flask(__name__)

user_socket_dict = {}

@ws.route("/toy/<toy_id>")
def toy(toy_id):
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    if user_socket:
        user_socket_dict[toy_id] = user_socket
    print(user_socket_dict)
    while 1:
        msg = user_socket.receive()
        # b'{to_user:"toy123",from_user:"123123123",chat:"11111.mp3","user_type":toy}'
        msg_dict = json.loads(msg)
        if msg_dict.get("user_type") == "toy":
            xxtx = speech.get_remark(msg_dict.get("to_user"),msg_dict.get("from_user"))
            msg_dict["chat"] = xxtx
        usocket = user_socket_dict.get(msg_dict.get("to_user"))
        usocket.send(json.dumps(msg_dict))
        
        
    
@ws.route("/app/<app_id>")
def app(app_id):
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    if user_socket:
        user_socket_dict[app_id] = user_socket
    print(user_socket_dict)

    while 1:
        msg = user_socket.receive()
        msg_dict = json.loads(msg)
        print(msg_dict)
        xxtx = speech.get_remark(msg_dict.get("to_user"),msg_dict.get("from_user"))
        usocket = user_socket_dict.get(msg_dict.get("to_user"))
        msg_dict["chat"] = xxtx
        
        usocket.send(json.dumps(msg_dict))
        
        

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9528),ws,handler_class=WebSocketHandler)
    http_serv.serve_forever()