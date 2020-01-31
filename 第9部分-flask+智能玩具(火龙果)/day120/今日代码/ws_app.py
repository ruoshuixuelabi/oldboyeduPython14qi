from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

from flask import Flask,request

app = Flask(__name__)

@app.route("/ws")
def ws():
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    while 1:
        user_msg = user_socket.receive()
        print(user_msg)
        user_socket.send(user_msg)
    


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9527),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()
    